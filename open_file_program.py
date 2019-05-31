import os
import time

class OpenFileProgram():
        def create_file(self, file_path):
                with open(file_path, 'w') as f:
                        f.write("")


        def open_file(self, file_path):
                try:
                        os.startfile(file_path)
                        print("{file_path} opened!".format(file_path=file_path))

                except FileNotFoundError:
                        print("File {file_path} is not found!".format(file_path=file_path))
                        print("Creating file...")
                        self.create_file(file_path)
                        print("Opening file...")
                        self.open_file(file_path)

        def open_program(self, program):
                try:
                        os.system("start {program}.exe".format(program=program))
                        print("{program} opened!".format(program=program))

                except Exception as e:
                        print(str(e))

        def close_program(self, program):
                try:
                        os.system('TASKKILL /F /IM {program}.exe'.format(program=program))
                        print("{program} closed!".format(program=program))

                except Exception as e:
                        print(str(e))

if __name__ == '__main__':
        file_path = 'C:/Users/XPS/Desktop/x.txt'
        program = 'notepad'

        OP = OpenFileProgram()

        OP.open_file(file_path)

        OP.open_program(program)

        time.sleep(3)

        OP.close_program(program)