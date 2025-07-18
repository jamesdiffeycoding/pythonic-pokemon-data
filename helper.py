import os

def log_main_file():
    filename = os.path.basename(__file__)
    print(f"{f'\nFile running: {filename}'.ljust(150, '~')}")
