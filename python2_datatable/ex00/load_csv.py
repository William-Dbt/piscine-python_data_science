import pandas as pnd


def load(path: str) -> pnd.DataFrame:
    """Generate a pandas array from datas of csv file

    Args:
        path (str): csv file to read

    Returns:
        pnd.DataFrame: DataFrame of csv file
    """
    try:
        dataTable = pnd.read_csv(path)
    except FileNotFoundError as error:
        print(FileNotFoundError.__name__, error)
        return None
    except IsADirectoryError as error:
        print(IsADirectoryError.__name__, error)
        return None
    except pnd.errors.ParserError as error:
        print("An error occured while parsing the file:", error)
        return None
    except ValueError as error:
        print(ValueError.__name__, error)
        return None

    print(f"Loading dataset of dimensions {dataTable.shape}")
    return dataTable
