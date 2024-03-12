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
    arrFamily = np.array(family)
    print("My shape is:", np.shape(arrFamily))

    arrFamily = arrFamily[start:end]
    print("My new shape is:", np.shape(arrFamily))

    return arrFamily.tolist()
