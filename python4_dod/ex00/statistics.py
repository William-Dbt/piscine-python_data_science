class ListOperations:
    def mean(self, listValues: list):
        """Calculate the mean of the list"""
        return sum(listValues) / len(listValues)

    def median(self, listValues: list):
        """Calculate the median of the list"""
        sortedList = sorted(listValues)
        listLen = len(sortedList)
        # list is odd (take the middle value of the list)
        if listLen % 2 == 1:
            return sortedList[int(listLen / 2)]

        # list is even, take the two middle values and take the mean of them
        medianValue = (sortedList[int(listLen / 2) - 1]
                       + sortedList[int(listLen / 2)]) / 2
        if medianValue % 1 == 0:
            return int(medianValue)

        return medianValue

    def quartile(self, listValues: list):
        """Calculate the quartile of the list"""
        sortedList = sorted(listValues)
        listLen = len(sortedList)
        firstQuartileList = sortedList[:int(listLen / 2)]
        # Check if list is odd, if it is,
        # take the index of the median value + 1
        # if not, just take the middle index
        # by doing that, we avoid a bug with even lists
        # where the index of the median is jumped by one
        if listLen % 2 == 1:
            thirdQuartileList = sortedList[int(listLen / 2) + 1:]
        else:
            thirdQuartileList = sortedList[int(listLen / 2):]

        return [float(self.median(self, firstQuartileList)),
                float(self.median(self, thirdQuartileList))]

    def std(self, listValues: list):
        """Calculate the standard deviation of the list
        https://fr.wikipedia.org/wiki/%C3%89cart_type for more details"""
        mean = self.mean(self, listValues)
        meanDeviationValues = [abs(item - mean) ** 2 for item in listValues]
        return (sum(meanDeviationValues) / len(listValues)) ** 0.5

    def var(self, listValues: list):
        """Calculate variance of the list"""
        mean = self.mean(self, listValues)
        meanDeviationValues = [abs(item - mean) ** 2 for item in listValues]
        return (sum(meanDeviationValues) / len(listValues))

    def switchOP(self, operation: str, listValues: list):
        """Function that act as match case statement
        flake8 don't allow to use it so I took an alternative

        Args:
            operation (str): operation's name to do on the list
            listValues (list): list to be processed
        """
        operationFunc = getattr(self, str(operation))
        if operationFunc:
            print(operation, ": ", end='')
            return operationFunc(self, listValues)


# args[0] means first list, args[1] means kwargs list
def isListsOk(*args: any) -> bool:
    """Iterate through the list to know if any arg is a int or a float

    Returns:
        bool: True if list is Ok, false otherwise
    """
    if not len(args[0]):
        return False

    argsList = [item for item in args[0] if isinstance(item, int | float)]
    if argsList != list(args[0]):
        return False

    return True


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Function to calculate the mean, median, qurtile, standard deviation
    and variance"""
    for key, value in kwargs.items():
        if not isListsOk(args, kwargs):
            print("ERROR")
            continue

        try:
            print(ListOperations.switchOP(ListOperations, value, list(args)))
        except AttributeError:
            pass
