import sys

# This function print the wheter the number given in parameter is ever or not
def printEvenStatus(number: int):
	print("I'm Even.") if int(number) % 2 == 0 else print("I'm odd.")

# We first check the len of the argv thanks to sys library, if it's equal to 1 => no arguments given
# Next, if the condition (len(argv) == 2) is false, then throw AssertionError thankt to assert
# Next, we'll check if the cast in int of the argv[1] is possible, if not, throw error
# Then, call isEven function to print the status of the number
try:
	if (len(sys.argv) == 1):
		exit()

	assert len(sys.argv) == 2, "more than one argument is provided"
	try:
		printEvenStatus(int(sys.argv[1]))
	except ValueError:
		assert False, "argument is not an integer"
except AssertionError as error:
	print("AssertionError: " + str(error))
