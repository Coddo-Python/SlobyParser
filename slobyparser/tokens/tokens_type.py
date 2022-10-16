# third party
import keyword
from typing import Literal
# this project
from slobyparser.token import Token


class Keywords(Token):
    """
    They are used to define the syntax and structure of the Python language.
    """
    ITEMS = keyword.kwlist


class Identifiers(Token):
    """
    1.Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _
    2.An identifier cannot start with a digit. 1variable is invalid, but variable1 is a valid name.
    3.Keywords cannot be used as identifiers.
    4.We cannot use special symbols like !, @, #, $, % etc. in our identifier.
    5.An identifier can be of any length.
    """



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