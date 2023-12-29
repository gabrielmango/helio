'''
Module: helio

This module defines the main function for Helio, a tool designed to assist
professionals working with relational databases, facilitating the creation
of SQL scripts to carry out migrations in backend projects.

Functions:
- main(): Helio's main function that initiates the tool.

Constants:
- ENTITY_SIZE: The size limit for collecting information from the user.

Dependencies:
- user.User: representing a user with methods for collecting information.
'''
import os
from pprint import pprint

from helio_main.user import User

ENTITY_SIZE = 30


def main():
    '''Helio's main function.'''

    # Start the apresentation of Helio
    print('HELIO: Hello! My name is Helio.')
    print(
        'HELIO: I am a tool designed to help professionals '
        'who work with relational databases.'
        '\nHELIO: Lets start!\n'
    )

    # Create dict for all script SQL information
    sql_information = {}
    user = User()

    # Getting schema name
    user.get_infomation(
        input('HELIO: Enter the project schema name: \nUSER: '), ENTITY_SIZE
    )
    sql_information['schema'] = user.information

    pprint(sql_information)


if __name__ == '__main__':
    os.system('cls')
    main()
