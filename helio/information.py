class Sequence:

    @staticmethod
    def create_name(text):
        abbreviation = [letter[0] for letter in text[3:].split('_')]
        return f'sq_{text[3:].replace("_", "")}_coseq' + ''.join(abbreviation)