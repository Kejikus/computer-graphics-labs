import cv2
import numpy as np
from matplotlib import pyplot as plt
import io
from math import sin, e
import base64

from common import readb64_v2, writeb64


def task_9(debug=False):

    min, max = 1, 100
    a = 0.2
    b = 2

    x_coords = range(min, max)

    F1 = np.fft.fft([np.exp(-a**2*x**2) for x in x_coords])

    F2 = np.fft.fft([1/(1+b**2 * x**2) for x in x_coords])

    F3 = np.fft.fft([sin(a*x)/(1+b*x**2) for x in x_coords])

    fig, axs = plt.subplots(3, 2)
    axs[0, 0].plot(x_coords, F1.real)
    axs[0, 1].plot(x_coords, F1.imag)

    axs[1, 0].plot(x_coords, F2.real)
    axs[1, 1].plot(x_coords, F2.imag)

    axs[2, 0].plot(x_coords, F3.real)
    axs[2, 1].plot(x_coords, F3.imag)

    if debug:
        plt.show()

    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes,  format='png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read())

    plt.close()

    return pic_hash


if __name__ == "__main__":
    task_9(True)
