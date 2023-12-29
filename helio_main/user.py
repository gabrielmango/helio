"""
Module to handle user information with validation.

This module defines a User class that can be used to manage user information,
including normalization and validation.
"""
from unidecode import unidecode


class User:
    """Class to handle user information with validation."""

    def __init__(
        self, information: str = '', limit: int = 0, validate: bool = True
    ) -> None:
        """Initialize User instance."""
        self.information = information
        self.limit = limit
        self.validate = validate

    def normalize(self) -> str:
        """Normalize information by removing accents and lowercase."""
        if self.information:
            self.information = unidecode(self.information.lower())

    def is_valid_information(self) -> bool:
        """Check if the user information is valid based on the specified limit."""
        if len(self.information) <= self.limit:
            return True
        return False

    def validate_information(self):
        """Validate user information, prompting for new input if necessary."""
        while self.validate and not self.is_valid_information():
            self.prompt_for_new_input()

    def prompt_for_new_input(self) -> None:
        """Prompt the user for new input if the current information is invalid."""
        print(
            f'Sorry, the sequence ({self.information}) '
            'must have a maximum of 30 characters.'
        )
        print(
            f'It has {len(self.information)} characters.'
            'Please enter a sequence '
            f'(up to {self.limit} characters): '
        )
        self.information = input()
        self.normalize()

    def get_infomation(self, value: str, number: int) -> None:
        """Set user information and limit, normalize, and validate."""
        self.information = value
        self.limit = number
        self.normalize()
        self.validate_information()
