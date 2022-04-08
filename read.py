'''Here is where the input file gets read'''


def read_file(file):
    '''The function that read the input file and send the content further'''
    file_content = []
    with open(file,"r") as textfile:
        file_content = textfile.readlines()
        textfile.close()
    return file_content
