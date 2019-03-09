import cv2
import numpy as np
import time
from time import sleep

# Threshold for the image difference of two frames. Value between 0 and 255. 0 means that there needs to be no
# difference between two successive frames (which is obviously a bad idea), 255 is the biggest possible difference.
IMAGE_DIFFERENCE_THRESHOLD = 100


def get_capture_device(device_number, image_width, image_height):
    capture_device = cv2.VideoCapture(device_number)
    capture_device.set(cv2.CAP_PROP_FRAME_WIDTH, image_width)
    capture_device.set(cv2.CAP_PROP_FRAME_HEIGHT, image_height)
    return capture_device


def is_frame_at_framerate(frame_rate, time_elapsed):
    return time_elapsed > 1. / frame_rate


class DartThrownWatcher:
    """
    DartsThrowWatcher checks all webcams for changes in the image. It gets the image from the webcam at a pretty slow
    framerate and checks for differences in the images. When the difference in the images exceeds a certain
    threshold, a dart is recognized.

     Attributes: deviceNumber (int): The identifier of the device (webcam) for this DartThrowWatcher.
    """

    def __init__(self, webcam_device_ids):
        self.device_list = []
        for device_id in webcam_device_ids:
            self.device_list.append(DartsCapturingDevice(device_id))
        self.capturing = True

    def is_new_dart_recognized(self):
        frame_rate = 2
        prev = 0

        while self.capturing:
            time_elapsed = time.time() - prev
            # TODO find a way to free cpu time (non-blocking) and remove sleep
            sleep(0.1)
            if is_frame_at_framerate(frame_rate, time_elapsed):
                prev = time.time()

                self.capture_images()
                self.process_captured_images()

        # When everything done, release the capture
        self.left_capture_device.release()
        self.right_capture_device.release()

        cv2.destroyAllWindows()

    def capture_images(self):
        for device in self.device_list:
            device.process_image()

    def process_captured_images(self):
        new_images_available = list(map(lambda x: x.has_new_frame(), self.device_list))
        if all(new_images_available):
            for device in self.device_list:
                f = device.get_latest_frame()
                cv2.imshow('device_' + str(device.device_number), f)
                cv2.waitKey(1)


class DartsCapturingDevice:
    """
    DartsCapturingDevice represents a device for capturing the darts visually (i.e. a web cam). It captures frames
    when the captured image changes. The latest captured image can be fetched from the device.
    """

    def __init__(self, device_number, image_width=1280, image_height=720):
        self.image_width = image_width
        self.image_height = image_height
        self.device_number = device_number
        self.capture_device = get_capture_device(device_number, image_width, image_height)
        self.previousFrame = []
        self.recordedFrame = []

    def release(self):
        self.capture_device.release()

    def has_new_frame(self):
        return self.recordedFrame != []

    def get_latest_frame(self):
        recent_frame = self.recordedFrame
        self.recordedFrame = []
        return recent_frame

    def process_image(self):
        _, frame = self.capture_device.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = self.get_difference(frame)

        white_pixels = np.sum(diff > IMAGE_DIFFERENCE_THRESHOLD)

        sixty_percent_of_all_pixels = (self.image_width * self.image_height) * 0.6
        minimum_changed_pixels_threshold = 10
        if minimum_changed_pixels_threshold < white_pixels < sixty_percent_of_all_pixels:
            self.recordedFrame = diff

        self.previousFrame = frame

    def get_difference(self, frame):
        has_previous_frame = len(self.previousFrame) > 0
        if has_previous_frame:
            return cv2.subtract(self.previousFrame, frame)
        else:
            return frame
