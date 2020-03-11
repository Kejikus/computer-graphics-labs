import cv2
import numpy as np
from matplotlib import pyplot as plt
import io

from .common import readb64_v2, writeb64


def getHistogram(img, legend):
    plt.hist(img.flatten(), 256, [0, 256],  color='b')
    plt.xlim([0, 256])
    plt.legend(legend,  loc='upper left')

    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes,  format='png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read())

    plt.close()

    return pic_hash


def task_5(input_image: str, debug=False) -> list:
    '''
        For a given image, it builds a brightness histogram, performs an equalization conversion, and builds a brightness histogram for the resulting image
        Parameters:
        -----------
        input_image: Base64 string, containing input image

        debug: Shows image if `True`
        Returns:
        --------
        list with list with two histogramms and equalized image'''

    import base64

    img = readb64_v2(input_image, 0)

    equ = cv2.equalizeHist(img)

    pic_hash = getHistogram(img, 'original')

    orig_plt = readb64_v2(pic_hash, cv2.COLOR_RGB2BGR)

    pic_hash = getHistogram(equ, 'equalized')

    equ_plt = readb64_v2(pic_hash, cv2.COLOR_RGB2BGR)

    if debug:
        cv2.imshow('original image', img)
        cv2.imshow('original histogram', orig_plt)
        cv2.imshow('equalized image', equ)
        cv2.imshow('equalized histogram', equ_plt)

    return [[writeb64(orig_plt),
             writeb64(equ),
             writeb64(equ_plt)]]


if __name__ == "__main__":
    import base64
    import cv2

    image_file_name = "algorithms\\images\\test2.jpg"

    image_file = open(image_file_name, "rb")
    encoded_string = base64.b64encode(image_file.read())

    task_5(encoded_string, True)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
