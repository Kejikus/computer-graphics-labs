from dataclasses import dataclass

import cv2
from .common import readb64, writeb64


@dataclass
class CropRect:
    x: int
    y: int
    w: int
    h: int


def getInversedImage(img):
    return 255 - img % 255


def getMonochannelImage(input_file):
    return readb64(input_file, cv2.COLOR_BGR2GRAY)


def rotate(img):
    return cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)


def thresholding(img, threshold):
    ret, thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO)
    return thresh


def crop(img, rectangle: CropRect):
    y = rectangle.y
    x = rectangle.x
    w = rectangle.w
    h = rectangle.h

    crop_img = img[y:y+h, x:x+w]
    return crop_img


def task_3(input_file: str, threshold: int, rectangle: CropRect, *_, debug=False) -> list:

    img = readb64(input_file, cv2.COLOR_RGB2BGR)

    img_inverse = getInversedImage(img)

    img_gray = getMonochannelImage(input_file)

    img_rotate_90_counterclockwise = rotate(img)

    thresh = thresholding(img, threshold)

    crop_img = crop(img, rectangle)

    if debug:
        cv2.imshow('original', img)
        cv2.imshow('inversed', img_inverse)
        cv2.imshow('gray', img_gray)
        cv2.imshow('rotate', img_rotate_90_counterclockwise)
        cv2.imshow('thresh', thresh)
        cv2.imshow("cropped", crop_img)

    return [[writeb64(img_inverse),
             writeb64(img_gray),
             writeb64(img_rotate_90_counterclockwise),
             writeb64(thresh),
             writeb64(crop_img)]]
