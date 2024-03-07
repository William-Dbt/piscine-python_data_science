import sys


NESTED_MORSE = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    " ": "/ "
}


def encodeStrToMorse(string: str):
    """Make a translationTable from previous declared dict
and use it to translate our string in Morse Code"""

    string = string.upper()
    translationTable = str.maketrans(NESTED_MORSE)
    print(string.translate(translationTable))


def main():
    """Check for errors as number of arguments and string format
then call encoreStrToMorse function to translate the given string"""

    try:
        assert len(sys.argv) == 2, "only one string is expected"
        text = sys.argv[1]
        splitedText = [word for word in text.split() if word.isalnum()]
        assert text.split() == splitedText, "the arguments are bad"
    except AssertionError as error:
        print("AssertionError:", error)
        exit()

    encodeStrToMorse(text)


if __name__ == "__main__":
    main()
