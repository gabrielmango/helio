"""Module defines the main function for Helio."""
import os
from pprint import pprint

from information import ColumnInformation, Sequence, Validator

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
    sql_information["schema"] = Validator(
        "Enter the project schema name", ENTITY_SIZE
    ).start()

    # Getting table name
    sql_information["table"] = Validator(
        "Enter the table name", TABLE_NAME_SIZE
    ).start()

    # Getting table comment
    sql_information["table_comment"] = Validator(
        "Enter the table comment", COMMENT
    ).start()

    # Getting sequence
    sequence_name = Sequence.main(sql_information["table"])
    sql_information["sequence"] = Validator(number=ENTITY_SIZE).start(sequence_name)

    sql_information["columns"] = ColumnInformation().get()

    pprint(sql_information)


if __name__ == "__main__":
    os.system("cls")
    main()
