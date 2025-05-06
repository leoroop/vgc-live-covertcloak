import cv2
from pygrabber.dshow_graph import FilterGraph


class Utils:
    @classmethod
    def choose_capturecard(cls):
        print("OpenCV version: " + cv2.__version__)

        # Get camera list
        graph = FilterGraph()
        device_list = graph.get_input_devices()
        label = 0

        for name in device_list:
            print(str(label) + ': ' + name)
            label += 1

        recuento = label - 1

        if recuento < 0:
            print("No device is connected")
            return

        message = "Select a camera (0 to " + str(recuento) + "): "
        try:
            capture_number = int(input(message))
        except Exception:
            print("It's not a number!")
            print()
            return cls.choose_capturecard()

        if (capture_number > recuento) or capture_number < 0:
            print("Invalid number! Retry!")
            print()
            return cls.choose_capturecard()

        return capture_number

    @staticmethod
    def get_marker_area(x_offset, y_offset) -> int:
        base = x_offset
        height = y_offset
        return base * height