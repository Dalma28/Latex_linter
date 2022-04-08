'''Please start the program here'''

import argparse
from read import read_file
from rules_file import Rules
from output import Output


def _main_():
    '''Here is the main function'''
    parser = argparse.ArgumentParser(description='The name of the file')
    parser.add_argument('file_name', type=str, help='Enter the name of the latex file you want to edit')
    args = parser.parse_args()
    file_name = args.file_name
    if file_name.endswith(".tex") is False:
        print("The file format is unacceptable. Please insert a tex file")
    else:
        try:
            input_file = read_file(file_name)
            user_object = Rules(input_file)
            user_object.new_line()
            user_object.format_comment()
            user_object.blank_lines()
            user_object.tab_adding()
            result = Output(user_object.lines_container,file_name)
            result.edited_file()
        except FileNotFoundError:
            print("The file cannot be found.")


if __name__ == '__main__':
    _main_()
