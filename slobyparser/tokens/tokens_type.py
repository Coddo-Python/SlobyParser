# third party
import keyword
# this project
import string
from slobyparser.token import Token


class Keywords(Token):
    """
    They are used to define the syntax and structure of the Python language.
    """
    ITEMS = keyword.kwlist

    @staticmethod
    def find_me(text) -> bool:
        if text in Keywords.ITEMS:
            return True
        return False


class Identifiers(Token):
    """
    1.Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _
    2.An identifier cannot start with a digit. 1variable is invalid, but variable1 is a valid name.
    3.Keywords cannot be used as identifiers.
    4.We cannot use special symbols like !, @, #, $, % etc. in our identifier.
    5.An identifier can be of any length.
    """

    # ITEMS = [can't get it]

    @staticmethod
    def find_me(text) -> bool:
        if text.is_identifier():
            return True
        return False


class Literals(Token):
    """
    1.Strings
    2.Numeric
    3.Boolean
    4.Collection
    5.Special
    """




class Operators(Token):
    """
    Operators are used to perform operations on variables and values.
    """
    ITEMS = ["+", "-", "*", "/", "%", "**", "//"]

    @staticmethod
    def find_me(text) -> bool:
        if text in Operators.ITEMS:
            return True
        return False


class Punctuators(Token):
    """
    A punctuator is a token that has syntactic and semantic meaning to the compiler, but the exact significance depends on the context
    """

    ITEMS = string.punctuation

    @staticmethod
    def find_me(text) -> bool:
        if text in Punctuators.ITEMS:
            return True
        return False