import re

class Tokenizer:
    def tokenize(self, program):
        regex = re.compile(r'\s*([-+*/\(\)\[\]]|[A-Za-z]+|[0-9]+)\s*')
        tokens = regex.findall(program)
        return [int(tok) if tok.isdigit() else tok for tok in tokens]
