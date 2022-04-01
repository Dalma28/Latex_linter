
class InputClass:

    def __init__(self,file):
        self.file_content= []
        self.file= file


    def reading_file(self):
        '''Reading the file and extracting the content.'''
        self.textfile = open(self.file, 'r')
        self.file_content = self.textfile.readlines()
        self.textfile.close()