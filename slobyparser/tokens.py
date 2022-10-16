from slobyparser.common.t_names import T_NAMES


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __str__(self):
        """Str representation of the object(readability)"""
        if not self.value:
            return f'{self.type}'
        return f'{self.type}:{self.value}'

    def __repr__(self):
        """str representation of the object, it contain information about the object(information)"""
        pass
