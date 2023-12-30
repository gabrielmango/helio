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

    def check_info(self):
        """Checks the lenght of input."""
        while not len(self.value) <= self.number:
            self.prompt_erro()
