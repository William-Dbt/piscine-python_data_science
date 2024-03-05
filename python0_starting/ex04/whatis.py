import sys

# This function print the number given in parameter is even or not
def printEvenStatus(number: int):
	print("I'm Even.") if int(number) % 2 == 0 else print("I'm odd.")

# We first check the len of the argv thanks to sys library, if it's equal to 1 => no arguments given
# Next, if the condition (len(argv) == 2) is false, then throw AssertionError thanks to assert it means that we haven't enough arguments
# Next, we'll check if the cast in int of the argv[1] is possible, if not, throw error, it means that the argument is not a number
# Then, call printEvenStatus function to print the status of the number
try:
	if (len(sys.argv) == 1):
		exit()

	assert len(sys.argv) == 2, "more than one argument is provided"
	try:
		printEvenStatus(int(sys.argv[1]))
	except ValueError:
		assert False, "argument is not an integer"
except AssertionError as error:
	print("AssertionError:", str(error))
