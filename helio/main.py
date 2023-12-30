"""Module defines the main function for Helio."""
import os
from pprint import pprint

from information import Sequence, Validator
from user import User

ENTITY_SIZE = 30
TABLE_NAME_SIZE = 24
COMMENT = 255


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

    # Getting schema name
    sql_information['schema'] = Validator('Enter the project schema name', ENTITY_SIZE).start()

    # Getting schema name
    sql_information['table'] = Validator('Enter the table name', TABLE_NAME_SIZE).start()



    # # Getting sequence of the main table
    # user.get_infomation(Sequence.main(sql_information["main_table"]), ENTITY_SIZE)
    # sql_information["main_sequence"] = user.information

    pprint(sql_information)


if __name__ == "__main__":
    os.system("cls")
    main()
