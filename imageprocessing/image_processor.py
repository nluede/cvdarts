import cv2
import numpy as np
from skimage.measure import LineModelND

from imageprocessing.data import ProcessedImage, BoundingBox


def erode(image):
    """
    :param image: Image input that needs to be eroded
    :type image: ProcessedImage
    :return: The eroded image
    :rtype: UMat
    """
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((4, 4), np.uint8)
    img_erosion = cv2.erode(image.image, kernel, iterations=1)
    _, eroded_image = cv2.threshold(img_erosion, 30, 255, cv2.THRESH_BINARY)
    return eroded_image


def segment(processed_image):
    """
    Determines a bounding box for the part of the image that changed.

    :param processed_image: The image that is processed this iteration
    :type processed_image: ProcessedImage
    :return: A bounding box which surrounds the area of interest (e.g. the dart)
    :rtype: BoundingBox
    """
    # Get binary image by applying a threshold
    image = cv2.cvtColor(processed_image.image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(image, 30, 255, cv2.THRESH_BINARY)

    # applying morphological operation to join detached segments
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))
    threshed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, rect_kernel)

    # Find contours
    contours, hierarchy = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) <= 0:
        return BoundingBox(0, 0, 0, 0)

    best_contour = find_best_contour(contours)

    x, y, w, h = cv2.boundingRect(best_contour)
    if y+h < processed_image.darts_board_offset:
        h = processed_image.darts_board_offset - y
    return BoundingBox(x, y, w, h)


def find_best_contour(contours):
    # find the contour with the biggest area
    best_contour = contours[0]
    best_area = cv2.contourArea(best_contour)
    for cnt in contours:
        if cv2.contourArea(cnt) > best_area:
            best_contour = cnt
            best_area = cv2.contourArea(cnt)
    return best_contour


def find_darts_axis(processed_image):
    """
    Applies a total least squares estimator to the image that is processed this iteration. The function evaluates the
    image data and takes the bounding box into consideration.
    For the estimation, the x-axis is vertical to processed_image.image (from top to bottom). The y-axis is horizontal
    (from left to right). The represented line follows through the shaft of the dart.

    :param processed_image: image that is processed.
    :type processed_image: ProcessedImage
    :return: An array of y-coordinates. array is as long as the bounding box is high.
    :rtype: [int]
    """
    if processed_image.has_bounding_box():
        x = processed_image.bounding_box.x
        y = processed_image.bounding_box.y
        w = processed_image.bounding_box.w
        h = processed_image.bounding_box.h
        segmented_image = processed_image.image[y: y + h, x: x + w]

        #find points that are white
        data = np.argwhere(segmented_image == 255)
        if len(data) < 2:
            return None

        #estimate least squares
        model = LineModelND()
        model.estimate(data)

        top_y = np.arange(0-y, h)

        try:
            return model.predict_y(top_y)
        except ValueError:  # Can occur when axis is parallel to dartboard
            return None

    return None
