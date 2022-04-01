"Here a new file is created and all the edited content is written in the new file"


class OutputClass:

    def __init__(self,content,file) :
        self.content = content
        file_created= file.replace(".tex", "_edited.tex")
        self.new_file = open(file_created, "w")


    def edited_file(self):
        for line in self.content :
            self.new_file.writelines(line)
        self.new_file.close()