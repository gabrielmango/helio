"""Module defines the main function for Helio."""
import os
from pprint import pprint

from user import User

ENTITY_SIZE = 30


def main():
    """Helio's main function."""
    # Start the apresentation of Helio
    print("HELIO: Hello! My name is Helio.")
    print(
        "HELIO: I am a tool designed to help professionals "
        "who work with relational databases."
        "\nHELIO: Lets start!\n"
    )

    # Create dict for all script SQL information
    sql_information = {}
    user = User()

    # Getting schema name
    user.get_infomation(
        input("HELIO: Enter the project schema name: \nUSER: "), ENTITY_SIZE
    )
    sql_information["schema"] = user.information

    pprint(sql_information)


if __name__ == "__main__":
    os.system("cls")
    main()
