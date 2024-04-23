def square(x: int | float) -> int | float:
    """Calculate square of variable"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Calculate pow of variable"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Function used as door to reach 'function argument'

    Args:
        x (int | float): first variable to use
        function (_type_): function to call on x

    Returns:
        object: return the function inner() that calls 'function'
    """
    error = ""
    def errorFunc() -> str:
        nonlocal error

        return error

    if not isinstance(x, int | float):
        error = "TypeError: Variable value must be an int of a float."
        return errorFunc

    if not function:
        error = "TypeError: Function must be a callable function."
        return errorFunc

    # Initiate the first value of x that will be used for further calls
    # of inner() function
    # once it's declared as nonlocal variable, it's used as global variable
    # to keep the last result in memory
    count = x

    def inner() -> float:
        """Function used as reminder of x each times it passed through
        the fuctions

        Returns:
            float: result of 'function'
        """
        nonlocal count

        try:
            count = function(count)
        except TypeError:
            print("TypeError: Something may went wrong with the result,",
                  "please check the function used")
            pass

        return count

    return inner


my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
