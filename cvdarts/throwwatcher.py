import cv2
import time
from time import sleep


def is_frame_at_framerate(frame_rate, time_elapsed):
    return time_elapsed > 1. / frame_rate


class ThrowWatcher:
    """
    ThrowWatcher checks all capturing devices for changes in the image. It gets the image from the device at a pretty
    slow  framerate and checks for differences in the images. When the difference in the images exceeds a certain
    threshold, a dart is recognized.

     Attributes: deviceNumber (int): The identifier of the device (webcam) for this DartThrowWatcher.
    """

    def __init__(self, device_list):
        self.device_list = device_list
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
        for device in self.device_list:
            device.release()

        cv2.destroyAllWindows()

    def capture_images(self):
        for device in self.device_list:
            device.process_image()

    def process_captured_images(self):
        new_images_available = list(map(lambda x: x.has_new_frame(), self.device_list))
        if all(new_images_available):
            for device in self.device_list:
                latest_frame = device.get_latest_frame()
                if latest_frame != []:
                    cv2.imshow('device_' + str(device.device_number), latest_frame)
                    cv2.waitKey(1)
