from unidecode import unidecode


class User:
    def __init__(
        self, information: str = '', limit: int = 30, validate: bool = True
    ) -> None:
        self.information = information
        self.limit = limit
        self.validate = validate

    def normalize(self) -> str:
        if not self.information:
            return ''
        return unidecode(self.information.lower())