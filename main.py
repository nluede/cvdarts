from cvdarts.capturingdevice import MockCapturingDevice, WebCamCapturingDevice
from cvdarts.darts_detector import DartsDetector
from cvdarts.gameloop import GameLoop

if __name__ == '__main__':

    mode = "cam"

    if mode == "mock":
        # Mock device list. Use if no web cam is present.
        device_list = [MockCapturingDevice(0), MockCapturingDevice(1)]
    else:
        # Mock device list. Use if one or more web cams are available.
        device_list = [WebCamCapturingDevice(1)]
        # device_list = [WebCamCapturingDevice(2), WebCamCapturingDevice(3)]

    game_loop = GameLoop(device_list)
    game_loop.run()
