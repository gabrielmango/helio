from unidecode import unidecode


class User:
    def __init__(
        self, information: str = '', limit: int = 30, validate: bool = True
    ) -> None:
        self.information = information
        self.limit = limit
        self.validate = validate

    def normalize(self) -> str:
        if self.information:
            self.information = unidecode(self.information.lower())

    def is_valid_information(self) -> bool:
        if len(self.information) <= self.limit:
            return True
        return False