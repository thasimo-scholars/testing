import os
import time
from github import Github as Github

access_token = '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'
g = Github(access_token)

repo_name = 'thasimo-scholars/testing'
file_path = 'watched file'
output_file_path = 'output'


def check_word_in_file(repo, file_path, word):
    file_contents = repo.get_contents(file_path)
    file_text = file_contents.decoded_content.decode('utf-8')
    return word.lower() in file_text.lower()

def update_file(repo, file_path, message):
    file_contents = repo.get_contents(file_path)
    repo.update_file(file_contents.path, f"Update: {message}", message, file_contents.sha)

def print_to_github(repo, output_file_path, message):
    output_file_contents = repo.get_contents(output_file_path)
    existing_output = output_file_contents.decoded_content.decode('utf-8')
    new_output = existing_output + message + '\n'
    update_file(repo, output_file_path, new_output)

def clear_output_file(repo, output_file_path):
    update_file(repo, output_file_path, '')

def main():
    repo = g.get_repo(repo_name)
    output_start_time = time.time()

    while True:
        file_contents = repo.get_contents(file_path)
        file_text = file_contents.decoded_content.decode('utf-8')

        if check_word_in_file(repo, file_path, 'T'):
            print_to_github(repo, output_file_path, "It is true")
            print("It is true")
            time.sleep(5)
        elif check_word_in_file(repo, file_path, 'Q'):
            print_to_github(repo, output_file_path, "Quit was selected. Confirm with 'Q' within 1 minute to delete the script.")
            print("quit was selected")
            time.sleep(3*60)

            if check_word_in_file(repo, file_path, 'Q'):
                print_to_github(repo, output_file_path, "Confirmation received. Deleting the script...")
                print("bye")
                script_path = os.path.abspath(__file__)
                os.remove(script_path)
                break
        elif check_word_in_file(repo, file_path, 'S'):
            print_to_github(repo, output_file_path, "Pausing the script for 20 minutes.")
            print("Pausing the script for 20 minutes")
            time.sleep(20 * 60)  # Pause for 20 minutes
        else:
            print_to_github(repo, output_file_path, "You inputted something else.")
            print("you inputted something else")
            time.sleep(60)

        # Check if 30 seconds have passed and clear the output file
        if time.time() - output_start_time >= 30:
            clear_output_file(repo, output_file_path)
            output_start_time = time.time()

if __name__ == "__main__":
    main()
