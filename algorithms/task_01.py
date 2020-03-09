import cv2
from dataclasses import dataclass

from .common import writeb64, readb64


@dataclass
class Task1Results:
    width: float
    height: float
    channels: int


def task_1(input_image: str, threshold: int, *_, debug: bool = False) -> (list, Task1Results):
    """
    Task 1 - ...
    :param input_image: Base64 string, containing input image
    :param threshold:
    :param debug: Debug argument - show OpenCV windows with images
    :return:
    """

    cvimg = readb64(input_image, cv2.COLOR_RGB2BGR)
    tmp = readb64(input_image, cv2.cv2.COLOR_BGR2HSV)
    result = readb64(input_image, cv2.COLOR_RGB2BGR)

    for x in range(cvimg.shape[0]):
        for y in range(cvimg.shape[1]):
            if (tmp[x, y][0] < threshold-2) or (tmp[x, y][0] > threshold+2):
                result[x, y] = [0, 0, 0]

    if debug:
        cv2.imshow('original', cvimg)
        cv2.imshow('threshold', result)

    return [writeb64(result)], Task1Results(cvimg.shape[0],
                                            cvimg.shape[1],
                                            cvimg.shape[2])
