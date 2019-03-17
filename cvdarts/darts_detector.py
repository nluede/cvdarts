def get_new_images(device_list):
    """
    Checks all devices for new images. If all devices have new images, a list with all new images gets returned.
    Otherwise an empty list gets returned.

    :param device_list: All the devices which should be considered for the darts detection.
    :type device_list: list of CapturingDevice
    :return: the captured images of all devices
    :rtype: list of UMat
    """
    # check for each capturing device if there are new frames available to process
    new_images_available = list(map(lambda x: x.has_new_frame(), device_list))
    # when there are new images for all capturing devices
    if all(new_images_available):
        return list(map(lambda x: x.fetch_latest_frame(), device_list))
    else:
        return []


class DartsDetector(object):
    """
    Detects changes on the dart board
    """
    pass
