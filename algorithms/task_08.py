import cv2
import numpy as np
from matplotlib import pyplot as plt
import io

from common import readb64, writeb64


def imadjust(x, a, b, c, d, gamma=1):
    # Similar to imadjust in MATLAB.
    # Converts an image range from [a,b] to [c,d].
    # The Equation of a line can be used for this transformation:
    #   y=((d-c)/(b-a))*(x-a)+c
    # However, it is better to use a more generalized equation:
    #   y=((x-a)/(b-a))^gamma*(d-c)+c
    # If gamma is equal to 1, then the line equation is used.
    # When gamma is not equal to 1, then the transformation is not linear.

    y = (((x - a) / (b - a)) ** gamma) * (d - c) + c
    return y


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
    kernel = np.ones((5, 5), np.float32)/25
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])

    img = readb64(input_image, cv2.COLOR_RGB2BGR)
    # img = readb64(input_image, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(img, cv2.CV_8U)

    img_laplacian = img + laplacian

    sobel = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  # y

    sobel_filter = cv2.filter2D(sobel, -1, kernel)

    mul_img = img_laplacian * sobel_filter

    sum_img = img + mul_img

    # img = cv2.filter2D(img, -1, kernel_sharpening)

    arr = np.asarray(sum_img)
    grad_img = imadjust(arr, arr.min(), arr.max(), 0, 1)

    # Добавить опреации между преобразованиями и вывести промежуточные варианты

    if debug:
        cv2.imshow('original image', img)
        cv2.imshow('laplacian', laplacian)
        cv2.imshow('original image with laplacian', img_laplacian)
        cv2.imshow('sobel', sobel)
        cv2.imshow('sobel with middle filter', sobel_filter)
        cv2.imshow('mul laplacian and filtered sobel', mul_img)
        cv2.imshow('sum original img and res of mul', sum_img)
        cv2.imshow('gradient correction', grad_img)

    return [[writeb64(img)]]


if __name__ == "__main__":
    import base64
    import cv2

    image_file_name = "algorithms\\images\\test3.jpg"

    image_file = open(image_file_name, "rb")
    encoded_string = base64.b64encode(image_file.read())

    task_7(encoded_string, True)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
