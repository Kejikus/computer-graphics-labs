from dataclasses import dataclass
import numpy as np

import cv2
from .common import readb64, writeb64

def getStepConversion(img, threshold):
    _, thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return thresh

def getLogConversion(input_image, scale_multiplier):
    img = readb64(input_image, cv2.COLOR_BGR2GRAY)
    return scale_multiplier * np.log(1 + np.asmatrix(img))

def getPowerConversion(img, scale_multiplier, gamma):
    return scale_multiplier * img**gamma

def getInversedImage(img):
    return 255 -1 -img


def task_4(input_image: str, threshold: int, scale_multiplier_for_log: int, scale_multiplier_for_power: int, gammma: float, debug=False) -> list:
    '''
        Performs brightness conversions: gradation, logarithmic, power, and color inversion
        Parameters
        ----------
        input_image: Base64 string, containing input image
        
        threshold: ... 
        
        scale_multiplier_for_log: ...
        
        scale_multiplier_for_power: ...
        
        gamma: ...
        Returns:
        --------
        list with list of output images in Base64 string format
        '''

    img = readb64(input_image, cv2.COLOR_RGB2BGR)

    img_step_conversion = getStepConversion(img, threshold)
    img_log_conversion = getLogConversion(input_image, scale_multiplier_for_log)
    img_power_conversion = getPowerConversion(img, scale_multiplier_for_power, gammma)
    img_inverse_conversion = getInversedImage(img)

    if debug:
        cv2.imshow('original', img)
        cv2.imshow('step conversion', img_step_conversion)
        cv2.imshow('log conversion', img_log_conversion)
        cv2.imshow('power conversion', img_power_conversion)
        cv2.imshow('inverse conversion', img_inverse_conversion)

    return [[writeb64(img_step_conversion),
             writeb64(img_log_conversion),
             writeb64(img_power_conversion),
             writeb64(img_inverse_conversion)]]
    
    
if __name__ == "__main__":
    import base64
    import cv2

    step_value = 100

    imagefile = "images\\test2.jpg"

    image_file = open(imagefile, "rb")
    encoded_string = base64.b64encode(image_file.read())

    task_4(encoded_string, 125, 100, 50, 2, True)

    cv2.waitKey(0)
    cv2.destroyAllWindows()