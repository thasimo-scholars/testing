def show_message_box(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)

show_message_box("Title", "This is a message.")
