from load_image import ft_load

import matplotlib.pyplot as plt
import numpy as np


def transpose(arrImage: np.array) -> np.array:
    """Rotate a square image on the left

    Args:
        arrImage (np.array): array of the image to rotate

    Returns:
        np.array: array of the rotated image
    """
    try:
        # To transpose we have to take a 2D Array, let's remove the third dimension
        arrImage = arrImage[:, :, 0]
        arrTransposed = np.copy(arrImage)

        # Here we'll use indexes of our dimensions to move each elements on
        # the position that we want
        # The first one at the top left of the image will go at the bottom left ...
        width = 0
        height = 0
        for x in arrImage:
            for y in x:
                arrTransposed[height][width] = y
                height += 1

            height = 0
            width += 1
    except TypeError as typeError:
        print("TypeError:", typeError)
        exit()

    return arrTransposed


def main():
    """Load the image to rotate and call function to rotate it
    Print informations as shape and content of arrays
    Show image
    """
    arrImage = ft_load("animal.jpeg")
    print("The shape of image is:", np.shape(arrImage))
    print(arrImage)
    arrTransposedImage = transpose(arrImage)
    print("New shape after Transpose:", np.shape(arrTransposedImage))
    print(arrTransposedImage)

    plt.imshow(arrTransposedImage, cmap="grey")
    plt.show()


if __name__ == "__main__":
    main()
