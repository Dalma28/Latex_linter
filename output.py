"Here a new file is created and all the edited content is written in the new file"


class Output:
    '''Here we write all the output in a new file'''
    def __init__(self,content,file) :
        self.content = content
        file_created= file.replace(".tex", "_edited.tex")
        self.new_file = open(file_created, "w")


    def edited_file(self):
        '''The function that writes the outcomes'''
        for line in self.content :
            self.new_file.writelines(line)
        self.new_file.close()
        