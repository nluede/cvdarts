class ProcessedImage(object):
    def __init__(self, image, image_width, image_height, device_number):
        self.image = image
        self.image_width = image_width
        self.image_height = image_height
        self.device_number = device_number
        self.darts_board_offset = 0
        self.bounding_box = None
        self.darts_axis = None

    def set_bounding_box(self, bounding_box):
        self.bounding_box = bounding_box

    def set_darts_axis(self, darts_axis):
        self.darts_axis = darts_axis

    def set_darts_board_offset(self, darts_board_offset):
        self.darts_board_offset = darts_board_offset

    def has_bounding_box(self):
        return self.bounding_box is not None


class BoundingBox(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
