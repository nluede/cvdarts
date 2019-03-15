from cvdarts.capturingdevice import MockCapturingDevice, WebCamCapturingDevice
from cvdarts.throwwatcher import ThrowWatcher

if __name__ == '__main__':
    # Mock device list. Use if no web cam is present.
    # device_list = [MockCapturingDevice(0), MockCapturingDevice(1)]

    # Mock device list. Use if no web cam is present.
    device_list = [WebCamCapturingDevice(0), WebCamCapturingDevice(1)]

    watcher = ThrowWatcher(device_list)

    print(watcher.is_new_dart_recognized())
