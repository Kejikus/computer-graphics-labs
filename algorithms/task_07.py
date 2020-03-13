import cv2
import numpy as np
from matplotlib import pyplot as plt
import io

from common import readb64, writeb64


def Laplacian(img, small_kernel):

    kernel = np.zeros((3, 3))
    kernel[:] = small_kernel

    dst = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    c = -1
    cv2.filter2D(src=img, dst=dst, ddepth=c, kernel=kernel)
    return dst


def task_7(input_image: str, debug=False) -> list:
    '''
        For a given image, it builds a brightness histogram, performs an equalization conversion, and builds a brightness histogram for the resulting image
        Parameters:
        -----------
        input_image: Base64 string, containing input image

        debug: Shows image if `True`
        Returns:
        --------
        list with list with images'''

    import base64

    img = readb64(input_image, cv2.COLOR_RGB2BGR)
    # img = readb64(input_image, cv2.COLOR_BGR2GRAY)

    kernel_1 = \
        [[1, 1, 1],
         [1, -8, 1],
         [1, 1, 1]]

    kernel_2 = \
        [[0, 1, 0],
         [1, -4, 1],
         [0, 1, 0]]

    lapl_1 = Laplacian(img, kernel_1)
    lapl_2 = Laplacian(img, kernel_2)

    # laplacian = cv2.Laplacian(img, cv2.CV_8U)

    if debug:
        cv2.imshow('original image', img)
        cv2.imshow('laplacian 1', lapl_1)
        cv2.imshow('laplacian 2', lapl_2)

    return [[writeb64(lapl_1), writeb64(lapl_2)]]


if __name__ == "__main__":
    import base64
    import cv2

    image_file_name = "algorithms\\images\\test1.jpg"

    image_file = open(image_file_name, "rb")
    encoded_string = base64.b64encode(image_file.read())

    task_7(encoded_string, True)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
