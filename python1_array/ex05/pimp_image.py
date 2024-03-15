import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.array) -> np.array:
    """Inverts the color of the image received

    Args:
        array (np.array): array of image to modify

    Returns:
        np.array: modified image array
    """
    # This will add 255 - the value of each colors in each dimensions (RGB)
    invertedArray = np.copy(array)
    invertedArray[:, :, :3] = 255 - invertedArray[:, :, :3]

    plt.imshow(invertedArray)
    plt.title("Inverted")
    plt.axis('off')
    plt.show()
    return invertedArray


def ft_red(array: np.array) -> np.array:
    """Turn red the colors of the image received

    Args:
        array (np.array): array of image to modify

    Returns:
        np.array: modified image array
    """
    # This mask will turn to 0 G and B values in all dimensions
    # Multiply the array by 0 will turn G and B values to 0,
    # Red is not touched because it's multiplied by 1
    redMask = np.array([1, 0, 0])
    redArray = np.copy(array)
    redArray = redArray * redMask

    plt.imshow(redArray)
    plt.title("Red")
    plt.axis('off')
    plt.show()
    return redArray


def ft_green(array: np.array) -> np.array:
    """Turn green the colors of the image received

    Args:
        array (np.array): array of image to modify

    Returns:
        np.array: modified image array
    """
    # Here we'll extract green only from the original array by creating
    # an empty array filled of 0
    # and get the green dimension of the original array to overwrite the 0 ones
    greenArray = np.zeros_like(array)
    greenArray[:, :, 1] = array[:, :, 1]

    plt.imshow(greenArray)
    plt.title("Green")
    plt.axis('off')
    plt.show()
    return greenArray


def ft_blue(array: np.array) -> np.array:
    """Turn blue the colors of the image received

    Args:
        array (np.array): array of image to modify

    Returns:
        np.array: modified image array
    """
    # Here we'll extract blue only from the original array by creating
    # an empty array filled of 0
    # and get the blue dimension of the original array to overwrite the 0 ones
    blueArray = np.zeros_like(array)
    blueArray[:, :, 2] = array[:, :, 2]

    plt.imshow(blueArray)
    plt.title("Blue")
    plt.axis('off')
    plt.show()
    return blueArray


def ft_grey(array: np.array) -> np.array:
    """Turn grey the colors of the image received

    Args:
        array (np.array): array of image to modify

    Returns:
        np.array: modified image array
    """
    redMask = array[:, :, 0] / 3
    greenMask = array[:, :, 1] / 3
    blueMask = array[:, :, 2] / 3
    greyMask = redMask + greenMask + blueMask

    # Overlay all masks in a 3 dimension and transform floats to int
    # that image can be translated with plt
    greyImage = np \
        .stack([greyMask, greyMask, greyMask], axis=2) \
        .astype(np.uint8)

    plt.imshow(greyImage)
    plt.title("Grey")
    plt.axis('off')
    plt.show()
    return greyImage
