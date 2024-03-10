import sys


def showTextCharDetails(text: str):
    """
        Print de full details of the chars of the given string as:
            - Number of chars
            - How many upper letters
            - How many lower letters
            - How many punctuation marks
            - How many spaces
            - How many digits
    """
    strPonctuactions = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    print("The text contains", str(len(text)), "characters:")
    print((sum(1 for letter in text if letter.isupper())), "upper letters")
    print((sum(1 for letter in text if letter.islower())), "lower letters")
    print((sum(1 for letter in text if letter in strPonctuactions)),
          "punctuation marks")
    print((sum(1 for letter in text if letter.isspace())), "spaces")
    print((sum(1 for letter in text if letter.isdigit())), "digits")


def main():
    """
        - Check the number of arguments provided,
          if more than 1 send AssertionError

        - If none provided, ask for user the text to check by reading on stdin
          The subject asks to manage CTRL + D, it is done by checking EOFError
          when a string is empty

        - Send the text in showTextCharDetails() function
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as error:
        print("AssertionError:", str(error))
        exit()

    line = ""
    if len(sys.argv) == 1:
        print("What is the text to count?")
        for text in sys.stdin:
            line = text
            break
    else:
        line = sys.argv[1]

    showTextCharDetails(line)


if __name__ == "__main__":
    main()
