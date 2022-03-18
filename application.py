"Please start the program here"


from lin_rules import Rules
from output import output
import os

def main():
    file_name = input("Please type the name of the latex file that you want to edit: ")
    while file_name.endswith(".tex") is False:
        print("The file format is unacceptable. Please insert a tex file")
        file_name = input("Please type the name of the latex file that you want to edit: ")
    try:
        user_object = Rules(file_name)
        user_object.new_line()
        user_object.format_comment()
        user_object.blank_lines()
        user_object.tab_adding()
        result = output(user_object.lines_container,file_name)
        result.edited_file() 
    except FileNotFoundError:
        print("The file cannot be found, please move the file to the current folder and check that you typed the name right")
        main()

if __name__ == '__main__' : 
    main() 