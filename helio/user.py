class User:
    def __init__(
        self, information: str, maximum_lenght: int = 30, validate: bool = True
    ) -> None:
        self.information = information
        self.maximum_lenght = maximum_lenght
        self.validate = validate
