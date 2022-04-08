'''Rules file'''


import json


class Rules:
    '''Here is the all the used rules'''
    def __init__(self, content):
        self.lines_container = content
        with open("rules.json", "r") as myjsonfile:
            jsondata = myjsonfile.read()
            self.obj = json.loads(jsondata)
            myjsonfile.close()


    def new_line(self):
        '''A new line is added after every sentence.'''
        json_name = "newline"
        try:
            if self.obj[json_name] is True:
                line_index = 0
                for line in self.lines_container:
                    line_index += 1
                    letter_index = 0
                    if line.find("%") != -1:
                        continue
                    else:
                        for character in line:
                            letter_index += 1
                            if character == "." or character == "!" or character == "?":
                                try:
                                    if line[letter_index] == " ":
                                        line = line[:letter_index +1] + "\n" + line[letter_index+1:]
                                        letter_index += 1
                                    elif line[letter_index].isupper():
                                        line =line[:letter_index] + "\n" + line[letter_index:]
                                        letter_index+=1
                                except IndexError:
                                    continue
                        self.lines_container[line_index-1] = line
            elif self.obj[json_name] is not False:
                print("json file has been edited wrongly. Please read README file.")
        except KeyError:
            print("json file has been edited wrongly. Please read README file.")


    def format_comment(self):
        '''A space is added after every comment mark.'''
        json_name = "format_comments"
        try:
            if self.obj[json_name] is True:
                line_index = 0
                for line in self.lines_container:
                    line_index += 1
                    letter_index = 0
                    for character in line:
                        letter_index += 1
                        if character == "%":
                            try:
                                if line[letter_index] != " ":
                                    line = line[:letter_index] + " " + line[letter_index:]
                                    letter_index += 1
                            except IndexError:
                                continue
                    self.lines_container[line_index-1] = line
            elif self.obj[json_name] is not False:
                print("json file has been edited wrongly. Please read README file.")
        except KeyError:
            print("json file has been edited wrongly. Please read README file.")


    def blank_lines(self):
        '''Configurable number of blank lines is added after specefic latex environments.'''
        try:
            config_list = self.obj["blanklines"]
            num_of_blanklines = config_list[1].get("number_of_lines")
            if config_list[0].get("use") is True:
                sign_list = ["\chapter","\section","\subsection","\subsubsection"]
                line_index = 0
                for line in self.lines_container:
                    line_index +=1
                    for sign in sign_list:
                        if line.startswith(sign):
                            line = "\n" *num_of_blanklines + line
                            self.lines_container[line_index - 1] = line
            elif config_list[0].get("use") is not False:
                print("json file has been edited wrongly. Please read README file.")
        except KeyError:
            print("json file has been edited wrongly. Comment formating option is deactivated.")
            print("Please read README file to reactivate it.")


    def tab_adding(self):
        "A tab between a (begin) and an (end) environment that imrove the structure of the file"
        try:
            if self.obj["adding_tabs"] is True:
                line_index = 0
                edited_index = 0
                for line in self.lines_container:
                    line_index += 1
                    words = line.split()
                    try:
                        found = words[0].find("begin{")
                        excludable = line.find("begin{document}")
                        if excludable != -1:
                            continue
                        elif found != -1:
                            edited_index += 1
                            firs_word= words[0]
                            start_index = firs_word.index("{")
                            end_index = firs_word.index("}")
                            sig_word= firs_word[start_index:end_index+1]
                            sign = "\end" +sig_word
                            while_index = line_index -1
                            while self.lines_container[while_index +1].find(sign) == -1:
                                self.lines_container[while_index+1] = "\t" + self.lines_container[while_index +1]
                                while_index += 1
                                if while_index == len(self.lines_container)-1:
                                    break
                    except (ValueError, IndexError):
                        continue
            elif self.obj["adding_tabs"] is not False:
                print("json file has been edited wrongly. Please read README file.")
        except KeyError:
            print("json file has been edited wrongly. Please read README file.")
