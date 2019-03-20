import argparse

from cvdarts.capturingdevice import MockCapturingDevice, WebCamCapturingDevice
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


if __name__ == '__main__':

    parse_args()
    print(args)

    if args.config:
        for device_id in args.device_ids:
            WebCamCapturingDevice(device_id, configure=True)

    devices = []
    for device_id in args.device_ids:
        devices.append(WebCamCapturingDevice(device_id))

    if args.testdata:
        devices = [MockCapturingDevice(0)]

    game_loop = GameLoop(devices)
    game_loop.run()
