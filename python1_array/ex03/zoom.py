from load_image import ft_load

import matplotlib.pyplot as plt
import numpy as np


def zoom(arrImage: np.array) -> np.array:
    """Zoom on image by given an numpy array of existed image

    Args:
        arrImage (np.array): array of image

    Returns:
        np.array: array of zoomed image
    """
    try:
        # Slice the array of the image by using Y and X axis
        arrZoomedImage = arrImage[100:500, 450:850, 0:1]
        print("New shape after slicing:", np.shape(arrZoomedImage))
    except TypeError as typeError:
        print("TypeError:", typeError)
        exit()

    return arrZoomedImage


def main():
    """Call ft_load function to get array of image and zoom and it,
    Print both returns arrays
    """
    arrImage = ft_load("animal.jpeg")
    print(arrImage)
    arrZoomedImage = zoom(arrImage)
    print(arrZoomedImage)

    plt.imshow(arrZoomedImage, cmap="grey")
    plt.show()


if __name__ == "__main__":
    main()
