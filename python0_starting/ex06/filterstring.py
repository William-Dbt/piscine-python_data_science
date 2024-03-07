import sys
from ft_filter import ft_filter


def main():
    """Errors managment:
    - Arguments not equals to 2
    - Second argument isn't an integer
    - First argument contains special chars

Call ft_filter function with lambda function as function to send
in parameters, it'll check the len of each words of the list"""

    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        try:
            wordLen = int(sys.argv[2])
            text = str(sys.argv[1])
        except ValueError:
            assert False, "the arguments are bad"

        splitedText = [word for word in text.split() if word.isalnum()]
        assert \
            text.split() == splitedText, \
            "the string may not contains special chars"

    except AssertionError as error:
        print("AssertionError:", error)
        exit()

    print(
        list(ft_filter(lambda word: len(word) > wordLen, splitedText))
    )


if __name__ == "__main__":
    main()
