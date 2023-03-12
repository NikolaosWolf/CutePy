class Token:
    def __init__(self, recognized_string, family, line):
        self.recognized_string = recognized_string
        self.family = family
        self.line = line

    def __str__(self):
        return f"{self.recognized_string} - {self.family} - {self.line}"
    