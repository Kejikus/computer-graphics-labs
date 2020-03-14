import cv2
import numpy as np
from matplotlib import pyplot as plt
import io
from common import readb64_v2, writeb64


def task_10(input_image: str, debug=False):
    # img = readb64(input_image, cv2.COLOR_RGB2BGR)
    img = readb64_v2(input_image, 0)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    spectrum = np.log(np.abs(fshift))

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(spectrum, cmap='gray')
    plt.title('Spectrum'), plt.xticks([]), plt.yticks([])

    if debug:
        plt.show()

    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes,  format='png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read())

    plt.close()

    return pic_hash


if __name__ == "__main__":
    import base64
    import cv2

    image_file_name = "algorithms\\images\\test2.jpg"

    image_file = open(image_file_name, "rb")
    encoded_string = base64.b64encode(image_file.read())

    task_10(encoded_string, True)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
