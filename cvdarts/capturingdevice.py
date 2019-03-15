import cv2
import numpy as np

# Threshold for the image difference of two frames. Value between 0 and 255. 0 means that there needs to be no
# difference between two successive frames (which is obviously a bad idea), 255 is the biggest possible difference.
IMAGE_DIFFERENCE_THRESHOLD = 100


def get_capture_device(device_number, image_width, image_height):
    capture_device = cv2.VideoCapture(device_number)
    capture_device.set(cv2.CAP_PROP_FRAME_WIDTH, image_width)
    capture_device.set(cv2.CAP_PROP_FRAME_HEIGHT, image_height)
    return capture_device


class CapturingDevice(object):
    """
    Capturing device superclass
    """


class WebCamCapturingDevice(CapturingDevice):
    """
    WebcamCapturingDevice represents a device for capturing the darts visually (i.e. a web cam). It captures frames
    when the captured image changes. The latest captured image can be fetched from the device.
    """

    def __init__(self, device_number, image_width=1280, image_height=720):
        self.image_width = image_width
        self.image_height = image_height
        self.device_number = device_number
        self.capture_device = get_capture_device(device_number, image_width, image_height)
        self.previous_frame = []
        self.recorded_frame = []

    def release(self):
        self.capture_device.release()

    def has_new_frame(self):
        return self.recorded_frame != []

    def get_latest_frame(self):
        recent_frame = self.recorded_frame
        self.recorded_frame = []
        return recent_frame

    def process_image(self):
        _, frame = self.capture_device.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = self.get_difference(frame)

        white_pixels = np.sum(diff > IMAGE_DIFFERENCE_THRESHOLD)

        sixty_percent_of_all_pixels = (self.image_width * self.image_height) * 0.6
        minimum_changed_pixels_threshold = 10
        if minimum_changed_pixels_threshold < white_pixels < sixty_percent_of_all_pixels:
            self.recorded_frame = diff

        self.previous_frame = frame

    def get_difference(self, frame):
        has_previous_frame = len(self.previous_frame) > 0
        if has_previous_frame:
            return cv2.subtract(self.previous_frame, frame)
        else:
            return frame


class MockCapturingDevice(CapturingDevice):
    """
    MockCapturingDevice can be used if no webcams are available. This capturing device provides images from the hard
    drive in a given rhythm.
    The provided images simulate three darts thrown every 5 seconds.
    """

    def __init__(self, device_number):
        self.device_number = device_number
        self.previous_frame = []
        self.recorded_frame = []
        self.access_counter = 0
        self.frame = 0

    def release(self):
        pass

    def has_new_frame(self):
        if self.access_counter % 4 == 0:
            self.next_image()
            return True
        return False

    def get_latest_frame(self):
        recent_frame = self.recorded_frame
        self.recorded_frame = []
        return recent_frame

    def process_image(self):
        self.access_counter += 1

    def next_image(self):
        image_path = 'sampledata/' + str(self.frame) + '.jpg'

        if len(self.previous_frame) == 0:
            self.previous_frame = cv2.imread(image_path, 1)
            return

        last_image = self.previous_frame
        self.previous_frame = cv2.imread(image_path, 1)
        self.recorded_frame = cv2.subtract(last_image, self.previous_frame)
        self.frame += 1

