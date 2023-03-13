from os import path
from lex_token import *

class Lex:
    current_line = 0
    data = ""
    token = LexToken

    def __init__(self, file_name):
        self.__file_is_valid(file_name)
        self.__open__and_read_file(file_name)

    def next_token(self):
        return LexToken("program", "keyword", 1)
    
    def __file_is_valid(self, file_name):
        file_type = file_name.split(".")[1]
        if (file_type != "cpy"):
            raise Exception("File type is invalid. Only .cpy files are allowed.")
        
        if (path.exists(file_name) == False):
            raise Exception("File not found. Please check the given path and try again!")
    
    def __open__and_read_file(self, file_name):
        file = open(file_name, "r")
        self.data = file.read()

    def __handle_number():
        buffer = ""

