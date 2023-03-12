from lex import *

parser = Lex("this-is-a-test-file.cpy")

print(parser.next_token().__str__())
