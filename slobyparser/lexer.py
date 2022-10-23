
# this project
from slobyparser.tokens.tokens_type import Literals, Keywords, Operators, Identifiers
from slobyparser.exceptions import SlobyException


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

        # tokens
        self.literal = Literals()
        self.keywords = Keywords()
        self.operators = Operators()
        self.identifiers = Identifiers()

        self.token_types = [self.literal, self.keywords, self.operators, self.identifiers]

    def advance(self):

        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def find_token_type(self, token):
        for token_type in self.token_types:
            if token in token_type.ITEMS:
                print(f"{token=}: {token_type.__class__.__name__}")
                return token
            else:
                break

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in '\t':
                self.advance()
            if self.find_token_type(self.current_char):
                tokens.append(self.current_char)
                self.advance()
            else:
                raise SlobyException("Invalid")
