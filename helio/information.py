"""Manipulates text sequences to generate a new formatted sequence."""

from unidecode import unidecode


class Sequence:
    """Class for manipulating and formatting text sequences."""  # noqa: D203

    @staticmethod
    def main(text):
        """Generates a formatted sequence from the input text."""
        abbreviation = [letter[0] for letter in text[3:].split("_")]
        return f'sq_{text[3:].replace("_", "")}_coseq' + "".join(abbreviation)


class Validator:
    """Class for valida the input information."""  # noqa: D203

    def __init__(self, message: str = "", number: int = 1) -> None:
        """Starts the class when instantiating."""
        self.message = message
        self.number = number
        self.value = None

    def start(self, info: str = None) -> str:
        """Start validation of the input information."""
        if info:
            self.value = self.normalize(info)
        else:
            self.prompt_init()

        self.check_info()
        return self.value

    def normalize(self, text: str) -> str:
        """Normalize the input, removing accentuation and spaces."""
        if self.number > 100:
            return unidecode(str(text.capitalize()))
        return unidecode(str(text.replace(" ", "").lower()))

    def prompt_erro(self) -> None:
        """Prompt to user when input no valid."""
        print(
            f"HELIO: Sorry, '{self.value}' "
            f"must have a maximum of {self.number} characters."
        )
        print(
            f"HELIO: It has {len(self.value)} characters. " "Please enter a new one: "
        )
        self.value = self.normalize(input("USER: "))

    def prompt_init(self) -> None:
        """Prompt to user make the input of information."""
        print(f"\nHELIO: {self.message}, please.")
        self.value = self.normalize(input("USER: "))

    def check_info(self) -> None:
        """Checks the lenght of input."""
        while not len(self.value) <= self.number:
            self.prompt_erro()


class ColumnInformation:
    def __init__(self, name_size, comment_size) -> None:
        self.name_size = name_size
        self.comment_size = comment_size

    def get(self) -> list[dict]:
        columns = []
        while True:
            columns.append(self.get_info())
            if not self.question():
                break
        return columns

    def get_info(self) -> dict:
        return {
            "name": Validator("Enter column name", self.name_size).start(),
            "type": Validator("Enter column type", self.name_size).start().upper(),
            "required": Validator("Enter column NULL/NOT NULL", self.comment_size)
            .start()
            .upper(),
            "commet": Validator("Enter column commet", self.comment_size).start(),
        }

    def question(self) -> bool:
        print("HELIO: Do you want to add a new column? [y/n]")
        response = input("USER: ")

        if response == "y":
            return True
        return False
