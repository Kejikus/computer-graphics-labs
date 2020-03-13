import cv2
from matplotlib import pyplot as plt
import io
from scipy.stats import norm, expon, cauchy

from .common import readb64_v2, writeb64


def getHistogram(img, Mx, sigma):

    count, bins, ignored = plt.hist(img.flatten(), 256, density=True)

    plt.plot(bins, norm.pdf(bins, Mx, sigma), linewidth=3, color='r')
    plt.plot(bins, expon.pdf(bins, Mx, sigma), linewidth=3, color='y')
    plt.plot(bins, cauchy.pdf(bins, Mx, sigma), linewidth=3, color='g')

    plt.legend(('нормальное распределение', 'экспотенциальное распределение',
                'Распределение Коши'),  loc='upper left')

    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes,  format='png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read())

    plt.close()

    return pic_hash


def task_6(input_image: str, Mx: int, sigma: int, debug=False) -> list:
    '''
        For a given image, it builds a brightness histogram, performs an equalization conversion, and builds a brightness histogram for the resulting image
        Parameters:
        -----------
        input_image: Base64 string, containing input image

        Mx: Mathematical expectation

        sigma: dispersion

        debug: Shows image if `True`
        Returns:
        --------
        list with list with two histogramms and equalized image'''

    import base64

    img = readb64_v2(input_image, 0)

    pic_hash = getHistogram(img, Mx, sigma)

    plt = readb64_v2(pic_hash, cv2.COLOR_RGB2BGR)

    if debug:
        cv2.imshow('original image', img)
        cv2.imshow('histogram', plt)

    return [[writeb64(plt)]]


if __name__ == "__main__":
    import base64
    import cv2

    image_file_name = "algorithms\\images\\test.jpg"

    image_file = open(image_file_name, "rb")
    encoded_string = base64.b64encode(image_file.read())

    task_6(encoded_string, 10, 10, True)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
