import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI
    BMI can be calculated with the formula: weight / (height * height)

    Args:
        height (list[int  |  float]): list of height
        weight (list[int  |  float]): list of weight

    Returns:
        list[int | float]: list of BMI for each given height & weight
    """
    try:
        try:
            infos = np.array([weight, height])
        except ValueError:
            assert False, "lists must have the same size"

        assert infos.dtype == 'float64', \
            "lists must contain only int and float elements"

        for item in np.nditer(infos):
            assert item > 0, "numbers in lists must be greater than 0"

    except AssertionError as error:
        print("AssertionError:", error)
        exit()

    bmiList = []
    it = np.nditer(infos[0], flags=['f_index'])
    for item in it:
        bmiList.append(item / (infos[1][it.index] ** 2))

    return bmiList


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Show limit on list

    Args:
        bmi (list[int  |  float]): list of BMI to check
        limit (int): limit to use for the list

    Returns:
        list[bool]: list of boolean values
            iterate in bmi that is greater than limit
    """
    try:
        arrBmi = np.array([bmi])
        assert arrBmi.dtype == 'float64', \
            "lists must contain only int and float elements"
    except AssertionError as error:
        print("AssertionError", error)

    limitList = []
    for item in np.nditer(arrBmi):
        limitList.append(True) \
            if item > float(limit) \
            else limitList.append(False)

    return limitList
