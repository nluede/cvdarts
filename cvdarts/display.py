import cv2


def display_with_information(processed_image):
    """
    Displays a processed image with all additional information (like dartboard level, darts axis etc.) in a
    seperate window.

    :param processed_image: The processed image which wraps the image itself and all additional information
    :type processed_image: ProcessedImage
    :return: None
    :rtype: None
    """
    if processed_image.image is not None:
        image_to_display = processed_image.image

        line = processed_image.darts_axis
        x = processed_image.bounding_box.x
        y = processed_image.bounding_box.y
        w = processed_image.bounding_box.w
        h = processed_image.bounding_box.h
        # draw darts axis
        if line is not None:
            image_to_display = cv2.line(image_to_display, (int(x + line[0]), y),
                                        (int(x + line[len(line) - 1]), y + h), (0, 255, 0), 3)
            # intersection dart with dart board
            x_value = int(processed_image.bounding_box.x +
                          processed_image.darts_axis[len(processed_image.darts_axis) - 1])

            image_to_display = cv2.line(image_to_display,
                                        (x_value, processed_image.darts_board_offset + 70),
                                        (x_value, processed_image.darts_board_offset - 20),
                                        (0, 0, 255),
                                        1)
            image_to_display = cv2.line(image_to_display,
                                        (x_value, processed_image.darts_board_offset + 30),
                                        (x_value, processed_image.darts_board_offset + 70),
                                        (0, 0, 255),
                                        10)
        # draw dart board level
        image_to_display = cv2.line(image_to_display,
                                    (0, processed_image.darts_board_offset),
                                    (processed_image.image_width, processed_image.darts_board_offset),
                                    (255, 0, 0),
                                    5)
        # draw bounding box
        image_to_display = cv2.rectangle(image_to_display, (x, y), (x + w, y + h), (0, 255, 0), 1)

        # show image
        cv2.imshow('device_' + str(processed_image.device_number), image_to_display)
        cv2.waitKey(1)

