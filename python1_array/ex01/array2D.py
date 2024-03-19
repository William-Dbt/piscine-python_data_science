import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array, discover of the slicing method

    Args:
        family (list): list to slice
        start (int): start index
        end (int): end index

    Returns:
        list: sliced 2D array
    """
    try:
        arrFamily = np.array(family)
        assert arrFamily.dtype == 'float64' or arrFamily.dtype == 'int', \
            "lists must contain only int and float elements"

        print("My shape is:", np.shape(arrFamily))

        arrFamily = arrFamily[start:end]
        print("My new shape is:", np.shape(arrFamily))
    except AssertionError as error:
        print("AssertionError:", error)
        exit()
    except TypeError as error:
        print("TypeError:", error)
        exit()

    return arrFamily.tolist()
