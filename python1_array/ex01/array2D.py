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

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
