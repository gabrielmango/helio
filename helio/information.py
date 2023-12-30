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

    def __start(self, value: str, number: int):
        self.value = value
        self.number = number
        self.__normalize()
        return self.__valid_info()

    def __normalize(self): 
        if isinstance(self.value, str):
            self.valid = unidecode(self.value.lower())
    
    def __valid_len(self):
        if len(self.value) <= self.number:
            return True
        return False
    
    def __valid_info(self):
        while not self.__valid_len():
            self.__prompt()
            self.value = input('USER: ')
            self.__normalize()
        return self.value

    def __prompt(self):
        print(
            f"HELIO: Sorry, '{self.value}' "
            f"must have a maximum of {self.number} characters."
        )
        print(
            f"HELIO: It has {len(self.value)} characters. "
            "Please enter a new one: "
        )

    @staticmethod
    def get(mensage: str, size):
        print(f'\nHELIO: {mensage}, please.')
        validador = Validator()
        info = input('USER: ')
        return validador.__start(info, size)
