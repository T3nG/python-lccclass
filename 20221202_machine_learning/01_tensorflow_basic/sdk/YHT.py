import math
import cv2
import numpy as np


def circle(radius):
    return math.pi*(radius**2)


class YHTCv():
    host = 'cosmowhale.asuscomm.com'

    @staticmethod
    def read(filePath):
        # IMREAD_UNCHANGED 不改顏色, 保留透明度等
        img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        return img

    @staticmethod
    def resize(image, width, height):
        resized_img = cv2.resize(image, (width, height), cv2.INTER_LINEAR)
        return resized_img

