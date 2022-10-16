from slobyparser.types.token_types import token_value, token_type


class Token(str):
    __slots__ = ("type", "value")
    def __init__(self, type_: token_type = "", value: token_value = None):
        self.type = type_
        self.value = value

    def __str__(self):
        """Str representation of the object(readability)"""
        if not self.value:
            return f'{self.type}'
        return f'{self.type}:{self.value}'

    def __repr__(self):
        """str representation of the object, it contain information about the object(information)"""
        return f'Token(type_:{self.type}, value={self.value})'
