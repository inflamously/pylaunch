class VariableError(Exception):
    def __init__(self, key, value="", message="Variable error"):
        self.key = key
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'({self.key}, {self.value}) -> {self.message}'


class ProviderError(Exception):


    def __init__(self, config = None, name = "", message = "Provider error"):
        self.config = config
        self.name = name
        self.message = message
        super().__init__(message)


    def __str__(self):
        return f'({self.config, self.name}) -> {self.message}'


class ParserError(Exception):
    def __init__(self, message="Parser error"):
        super().__init__(message)

    def __str__(self):
        return f'() -> {self.message}'


class InvalidVariableSymbol(VariableError):
    def __init__(self, key):
        super().__init__(key, message="Parsed key contains no or invalid variable symbol.")


class EmptyVariable(VariableError):
    def __init__(self, key):
        super().__init__(key, message="Key does not define proper variable (example): $NAME$")


class EmptyVariableDictionary(ParserError):
    def __init__(self):
        super().__init__(message="No assignable variables were passed for processing.")


class NoScriptProviderDefined(ProviderError):
    def __init__(self, config):
        super().__init__(config, message="No script provider found in config.")


class ConfigVariableNotFound(VariableError):
    def __init__(self, key):
        super().__init__(key, message="Variable not found in loaded configuration file.")


class InvalidProviderNameProvided(ProviderError):
    def __init__(self, name, message="Invalid provider name."):
        super().__init__(name=name, message=message)


class NamedProviderNotImplemented(ProviderError):
    def __init__(self, name, message="No valid provider found for name."):
        super().__init__(name=name, message=message)