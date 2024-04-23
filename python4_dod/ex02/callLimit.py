# First function to take the limit value in parameter
def callLimit(limit: int):
    """Function to use as decorator to limit call of a function

    Args:
        limit (int): limit to execute function
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer, "
                        f"received \'{limit}\' {type(limit)}")

    count = 0

    # Second function to take the function to check in parameter
    def callLimiter(function):
        """Function to take the function to execute in parameter"""
        # Wrapper function to expends the behavior of the function
        # Here used to know how many times the function has been executed
        # and executes it or not
        def limit_function(*args: any, **kwds: any):
            """Wrapper to limit the execution count of the function"""
            nonlocal count

            if count >= limit:
                print("Error:", function, "call too many times")
                return

            count += 1
            return function(*args, *kwds)

        return limit_function
    return callLimiter
