import cv2
import device

def choose_capturecard():
    print("OpenCV version: " + cv2.__version__)

    # Get camera list
    device_list = device.getDeviceList()
    etiqueta = 0

    for name in device_list:
        print(str(etiqueta) + ': ' + name)
        etiqueta += 1

    recuento = etiqueta - 1

    if recuento < 0:
        print("No device is connected")
        return

    message = "Select a camera (0 to " + str(recuento) + "): "
    try:
        capture_number = int(input(message))
    except Exception:
        print("It's not a number!")
        print()
        return choose_capturecard()

    if (capture_number > recuento) or capture_number < 0:
        print("Invalid number! Retry!")
        print()
        return choose_capturecard()

    return capture_number