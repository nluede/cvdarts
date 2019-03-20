from cvdarts.capturingdevice import MockCapturingDevice, WebCamCapturingDevice
from cvdarts.gameloop import GameLoop

if __name__ == '__main__':

    mode = "mock"

    if mode == "mock":
        # Mock device list. Use if no web cam is present.
        device_list = [MockCapturingDevice(0), MockCapturingDevice(1)]
    else:
        # Mock device list. Use if one or more web cams are available.
        # device_list = [WebCamCapturingDevice(1)]
        device = WebCamCapturingDevice(2)
        capturing_device = WebCamCapturingDevice(3)
        device_list = [device, capturing_device]

    game_loop = GameLoop(device_list)
    game_loop.run()
