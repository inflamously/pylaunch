class VariableError(Exception):
    def __init__(self, key, value="", message="Variable Error"):
        self.key = key
        self.value = value
        self.message = message
        super()\
            .__init__(message)

    def __str__(self):
        return f'({self.key}, {self.value}) -> {self.message}'


class InvalidVariableSymbol(VariableError):
    def __init__(self, key):
        super().__init__(key, message="Parsed key contains no or invalid variable symbol.")


class EmptyVariable(VariableError):
    def __init__(self, key):
        super().__init__(key, message="Key does not define proper variable (example): $NAME$")