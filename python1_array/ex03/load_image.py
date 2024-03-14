from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Get image pixel informations as array, only RGB supported

    Args:
        path (str): path of image to load

    Returns:
        np.array: array of pixels in RGB line by line horizontaly
    """
    try:
        try:
            image = Image.open(path, 'r')
        except FileNotFoundError:
            assert False, "image not found"
        except IsADirectoryError:
            assert False, "is it really a dir?"
        except Image.UnidentifiedImageError:
            assert False, "an error occured while opening the image"

        assert image.mode == 'RGB', "image must be coded in RGB"
    except AssertionError as error:
        print("AssertionError:", error)
        exit()

    arrImage = np.array(image)
    print("The shape of image is:", np.shape(arrImage))
    return arrImage
