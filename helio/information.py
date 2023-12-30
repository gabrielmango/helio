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
    """A class for collecting information about database columns."""  # noqa: D203

    def __init__(self, table_name: str, name_size: int = 30, comment_size: int = 255) -> None:
        """Starts the class when instantiating."""
        self.table_name = table_name
        self.name_size = name_size
        self.comment_size = comment_size

    def get(self) -> list[dict]:
        """Collects information about multiple columns and returns a list of dictionaries."""
        columns = []
        columns.append(self.create_first_column())
        while True:
            columns.append(self.get_info())
            if not self.question():
                break
        return columns

    def get_info(self) -> dict:
        """Collects information about a single column and returns a dictionary."""
        info = {
            "name": Validator("Enter column name", self.name_size).start(),
            "type": Validator("Enter column type", self.name_size).start().upper(),
            "required": Validator("Enter column NULL/NOT NULL", self.comment_size)
            .start()
            .upper(),
            "commet": Validator("Enter column commet", self.comment_size).start(),
        }
        return self.format_information(info)

    def format_information(self, info: dict) -> str:
        """Format column information to string."""
        return {
            "column": info["name"] + "   " + info["type"] + "    " + info["required"],
            "commet": info["commet"],
        }

    def question(self) -> bool:
        """Asks the user if they want to add a new column and returns a boolean."""
        print("HELIO: Do you want to add a new column? [y/n]")
        response = input("USER: ")

        if response == "y":
            return True
        return False
    
    def create_first_column(self):
        """Create the firts column for primary key."""
        column_name = f'co_seq_{self.table_name[3:]}'
        return {
            "column": f'{column_name}   BIGINT  NOT NULL    DEFAULT nextval(',
            "commet": 'Chave primaria sequencial da tabela que eh gerada pela sequence '
        }


class ContraintInformation:
    def __init__(self, table_name: str, name_size: int = 30, comment_size: int = 255) -> None:
        """Starts the class when instantiating."""
        self.table_name = table_name
        self.name_size = name_size
        self.comment_size = comment_size

    def get(self) -> list[dict]:
        """Collects information about a single constraint and returns a dictionary."""
        constraints = []
        constraints.append(self.create_pk_contraint())
        while True:
            if not self.question():
                break
            constraints.append(self.get_info())

        return constraints

    def get_info(self) -> str:
        """Get information of contraints."""
        info = {}

        info["name"] = Validator("Enter contraint name", self.name_size).start()

        print(
            "HELIO: The contraint types are PRIMARY KEY, FOREIGN KEY, CHECK and UNIQUE"
        )
        info["type"] = (
            Validator("Enter contraint type", self.comment_size).start().upper()
        )

        if info["type"] == "PRIMARY KEY" or info["type"] == "UNIQUE":
            info["description"] = '('
            info["description"] += Validator(
                "Enter the column name", self.name_size
            ).start()
            info["description"] += ')'
        elif info["type"] == "CHECK":
            info["description"] = '('
            info["description"] += Validator(
                "Enter the expression", self.name_size
            ).start()
            info["description"] += ')'
        elif info["type"] == "FOREIGN KEY":
            info["description"] = '('
            info["description"] += (
                Validator("Enter the column name", self.name_size).start()
                + ") REFERENCES "
            )
            info["description"] += (
                Validator("Enter the table name", self.name_size).start() + "("
            )
            info["description"] += (
                Validator(
                    "Enter the column name references table", self.name_size
                ).start()
                + ")"
            )

        return self.format_information(info)

    def format_information(self, info: dict) -> str:
        """Format column information to string."""
        return ''.join(
            [
                "CONSTRAINT  ",
                info["name"],
                "    ",
                info["type"],
                "    ",
                info["description"]
            ]
        )

    def question(self) -> bool:
        """Asks the user if they want to add a new column and returns a boolean."""
        print("HELIO: Do you want to add a new contraint? [y/n]")
        response = input("USER: ")

        if response == "y":
            return True
        return False

    def prompt_types(self):
        """Prompt constraints types to user."""
        print(
            "HELIO: The contraint types are PRIMARY KEY, FOREIGN KEY, CHECK and UNIQUE"
        )

    def create_pk_contraint(self):
        """Create the primary key."""
        contraint_name = 'pk_' + self.table_name[3:].replace("_", "")
        column_name = f'co_seq_{self.table_name[3:]}'
        return ''.join(
            [
                'CONSTRAINT  ',
                contraint_name,
                f'   PRIMARY KEY ({column_name})'
            ]
        )

