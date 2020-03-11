import cv2
# import os
import numpy as np
# from dataclasses import dataclass
import base64
from PIL import Image
import io

def readb64(base64_string, format):
    imgdata = base64.b64decode(base64_string)
    pimg = Image.open(io.BytesIO(imgdata))

    return cv2.cvtColor(np.array(pimg), format)

def readb64_v2(base64_string, format):
    nparr = np.fromstring(base64.b64decode(base64_string), np.uint8)
    return cv2.imdecode(nparr, format)

def writeb64(img):
    retval, buffer = cv2.imencode('.jpg', img)
    return base64.b64encode(buffer)