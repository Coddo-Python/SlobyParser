from slobyparser.types.token_types import token_value, token_type
import sys


class Token:
    __slots__ = ("type", "value", "token_position", "curr_pos", "end_pos", "start_pos")
    def __init__(self, type_: token_type = "", value: token_value = None):
        self.type = type_
        self.value = value

        self.token_position = self.TokenPosition()

        self.curr_pos = self.token_position.get_curr_position()

        self.end_pos = self.token_position.get_end_position()
        self.start_pos = self.token_position.get_start_position()

    class TokenPosition:
        def get_curr_position(self) -> str:
            pass

        def get_end_position(self) -> str:
            pass

        def get_start_position(self) -> str:
            pass


    def __str__(self):
        """Str representation of the object(readability)"""
        if not self.value:
            return f'{self.type}'

        return f'{self.type}:{self.value}'

    def __repr__(self):
        """str representation of the object, it contain information about the object(information)"""
        return f'Token(type_:{self.type}, value={self.value})'

    def __eq__(self, other):
        return self.value and self.type == other.value and other.type


if __name__ == '__main__':
    print(sys.getsizeof(Token))

