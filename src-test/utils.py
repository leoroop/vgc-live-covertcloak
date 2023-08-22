import cv2
from pygrabber.dshow_graph import FilterGraph

def choose_capturecard():
    print("OpenCV version: " + cv2.__version__)

    # Get camera list
    graph = FilterGraph()
    device_list = graph.get_input_devices()
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


def choose_number_of_windows():
    print()
    print('1: Show only "Covert Cloak" window')
    print('2: Show "Cleanfeed" and "Covert Cloak" windows')
    try:
        valor = int(input('Choose number of windows (1 or 2): '))
    except Exception:
        print("It's not a number!")
        return choose_number_of_windows()

    if valor < 1 or valor > 3:
        print("Invalid number! Retry!")
        return choose_number_of_windows()

    return valor


def overlay_frame(frame, overlay):
    overlay_mask = overlay[:, :, 3]
    overlay = cv2.bitwise_and(overlay, overlay, mask=overlay_mask)
    overlay = overlay[:, :, 0:3]

    frame_mask = cv2.bitwise_not(overlay_mask)
    frame = cv2.bitwise_and(frame, frame, mask=frame_mask)

    img = cv2.add(frame, overlay)

    return img


def checkpoint(masked_area, min_pixels=30):
    pixels = cv2.countNonZero(masked_area)
    return pixels > min_pixels
