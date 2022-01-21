import numpy as np
import cv2
from mss import mss
from PIL import Image
import threading

mon = {'left': 0, 'top': 0, 'width': 1366, 'height': 768}
mon2 = {'left': 100, 'top': 100, 'width': 1066, 'height': 568}


with mss() as sct:
    while True:
        screenShot = sct.grab(mon)
        screenShot2 = sct.grab(mon2)
        img = Image.frombytes(
            'RGB', 
            (screenShot.width, screenShot.height), 
            screenShot.rgb, 
        )
        img2 = Image.frombytes(
            'RGB', 
            (screenShot2.width, screenShot2.height), 
            screenShot2.rgb, 
        )
        cv2.imshow('test', np.array(img))
        cv2.imshow('test2', np.array(img2))
        if cv2.waitKey(33) & 0xFF in (
            ord('q'), 
            27, 
        ):
            break