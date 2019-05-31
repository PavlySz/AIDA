import os
import time

def create_file(file_path):
    with open(file_path, 'w') as f:
        f.write("")


def open_file(file_path):
    try:
        os.startfile(file_path)
        print(f"{file_path} opened!")

    except FileNotFoundError:
        print(f"File {file_path} is not found!")
        print("Creating file...")
        create_file(file_path)
        print("Opening file...")
        open_file(file_path)

def open_program(program):
    try:
        os.system(f"start {program}.exe")
        print(f"{program} opened!")

    except Exception as e:
        print(str(e))

def close_program(program):
    try:
        os.system(f'TASKKILL /F /IM {program}.exe')
        print(f"{program} closed!")

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    file_path = 'C:/Users/paul/Desktop/x.txt'
    program = 'cmd'

    open_file(file_path)

    # open_program(program)
    # time.sleep(3)
    # close_program(program)