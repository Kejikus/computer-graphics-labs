import cv2
import numpy as np
from dataclasses import dataclass
import base64
from .common import readb64


@dataclass
class Task2Results:
    first_diff_min: int
    first_diff_max: int
    second_diff_min: int
    second_diff_max: int


def task_2(input_file: str) -> (list, Task2Results):

    img = readb64(input_file, cv2.COLOR_RGB2BGR)

    first_diff = np.diff(img)
    second_diff = np.diff(first_diff)

    return [], Task2Results(np.min(first_diff),
                            np.max(first_diff),
                            np.min(second_diff),
                            np.max(second_diff))


def task_2_2(arr: list) -> list:

    arr = np.array(arr)
    first_diff = np.diff(arr)
    second_diff = np.diff(first_diff)

    return [[], Task2Results(np.min(first_diff),
                             np.max(first_diff),
                             np.min(second_diff),
                             np.max(second_diff))]


if __name__ == "__main__":
    step_value = 100

    imagefile = "images\\test.jpg"

    image_file = open(imagefile, "rb")
    encoded_string = base64.b64encode(image_file.read())
    task_2(encoded_string)
    # print(task_2_2([[12, 2, 3], [4, 5, 6], [10, 11, 77]]))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
