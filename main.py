import argparse

from cvdarts.capturingdevice import MockCapturingDevice, WebCamCapturingDevice
from cvdarts.configuration_repository import create_config, put_config_for_device, find_config_for_device
from cvdarts.dartboard import Board
from cvdarts.gameloop import GameLoop


def parse_args():
    global args
    parser = argparse.ArgumentParser(description="""
        Detect darts on a dart board using web cam. Run this command with the ids of the web cam as arguments. The ids \n
        are starting with 0 and increment with the numbers of web cams that are connected to your computer.
        Use the --config option to configure the web cams before detecting darts.
    """)
    parser.add_argument('device_ids', metavar='N', type=int, nargs='+',
                        help='Device ids for the devices that should be used')
    parser.add_argument('--config', '-c', help='sum the integers (default: find the max)', action="store_true")
    parser.add_argument('--testdata', '-t', help='Use testdata instead of webcams', action="store_true")
    args = parser.parse_args()


def initialize_real_devices():
    for device_id in args.device_ids:
        config_of_device = find_config_for_device(device_id)
        dartboard_level_from_config = 0
        if config_of_device is not None:
            dartboard_level_from_config = config_of_device[1]
        devices.append(WebCamCapturingDevice(device_id, dartboard_level_from_config))


def configure_devices():
    for device in devices:
        config_of_device = find_config_for_device(device.device_number)
        level_loaded_from_config = 0
        if config_of_device is not None:
            level_loaded_from_config = config_of_device[1]
        dartboard_level = device.configure(level_loaded_from_config)
        put_config_for_device(device.device_number, dartboard_level)


if __name__ == '__main__':

    b = Board()
    b.print()

    parse_args()
    devices = []
    create_config()

    if args.testdata:
        devices = [MockCapturingDevice(0)]
    else:
        initialize_real_devices()
        if args.config:
            configure_devices()
        else:
            game_loop = GameLoop(devices)
            game_loop.run()
