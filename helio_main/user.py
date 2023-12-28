from unidecode import unidecode


class User:
    def __init__(
        self, information: str = '', limit: int = 0, validate: bool = True
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

    def validate_information(self):
        while self.validate and not self.is_valid_information():
            self.prompt_for_new_input()

    def prompt_for_new_input(self) -> None:
        print(
            f'Sorry, the sequence ({self.information}) '
            'must have a maximum of 30 characters.'
        )
        print(f'It has {len(self.information)} characters.')
        self.information = self.normalize_input(
            input(
                f'Please enter a sequence '
                f'(up to {self.maximum_lenght} characters): '
            )
        )

    def get_infomation(self, value: str, number: int):
        self.information = value
        self.limit = number
        self.normalize()
        self.validate_information()
