from lex_token import *

class Lex:
    current_line = 0
    file_name = ""
    token = Token

    def __init__(self, file_name):
        self.file_name = file_name

    def next_token(self):
        return Token("program", "keyword", 1)