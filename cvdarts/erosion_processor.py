import cv2
import numpy as np


def erode(captured_input):
    """

    :param captured_input: Image input that needs to be eroded
    :type captured_input: UMat
    :return: The eroded image
    :rtype: UMat
    """
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((4, 4), np.uint8)
    img_erosion = cv2.erode(captured_input, kernel, iterations=3)
    _, captured_input = cv2.threshold(img_erosion, 30, 255, cv2.THRESH_BINARY)
    return captured_input
