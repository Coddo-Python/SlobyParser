# third-party
import sys

# this project
from slobyparser.tokens.tokens_type import Literals, Keywords, Operators, Identifiers
from slobyparser.exceptions import SlobyException


class Lexer:
    __slots__ = ("text", "pos", "current_char", "literal", "keywords", "operators", "identifiers", "token_types")  # :)
    def __init__(self, text: str = None):
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


    def get_token(self, token):
        for token_type in self.token_types:
            if token_type.find_me(token):
                print(f"{token=}: {token_type.__class__.__name__}")
                return token
            else:
                break

    def find_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in '\t':
                self.advance()
            if self.get_token(self.current_char):
                tokens.append(self.current_char)
                self.advance()
            else:
                raise SlobyException("Invalid")

        return tokens


def run(text):
    lexer = Lexer(text)
    tokens = lexer.find_tokens()

    return tokens