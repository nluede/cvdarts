def has_new_images(device_list):
    """
    Checks all devices for new images. If all devices have new images, it returns true.

    :param device_list: All the devices which should be considered for the darts detection.
    :type device_list: list of CapturingDevice
    :return: returns if all devices have new input
    :rtype: bool
    """
    # check for each capturing device if there are new frames available to process
    new_images_available = list(map(lambda x: x.has_new_frame(), device_list))
    # when there are new images for all capturing devices
    return all(new_images_available)


class DartsDetector(object):
    """
    Detects changes on the dart board
    """
    pass
