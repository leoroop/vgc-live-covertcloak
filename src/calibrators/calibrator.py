import json
from typing import Tuple

import cv2
import numpy as np


class Calibrator:

    def __init__(self, capture, desktop_width, desktop_height):
        self.capture = capture
        self.desktop_width = desktop_width
        self.desktop_height = desktop_height


        self.green_point = (895, 925, 1620, 1650)    # 15
        self.yellow_point = (1078, 1080, 10, 1910)   # 30
        self.white_point = (240, 250, 1345, 1545)    # 80

    def perform_calibration(self):
        self.__show_preview()

        print("Calibration started. Please wait...")
        colors = {'green': self.__calibrate_point(self.green_point, h_tolerance=10, s_tolerance=50, v_tolerance=50, pixels=800),
                  'yellow': self.__calibrate_point(self.yellow_point, h_tolerance=10, s_tolerance=80, v_tolerance=80, pixels=3700),
                  'white': self.__calibrate_point(self.white_point, h_tolerance=80, s_tolerance=149, v_tolerance=80, pixels=1900)}

        # self.capture.release()

        with open('resources/colors.json', 'w+', encoding='utf-8') as file:
            json.dump(colors, file, indent=4)

        print()
        input('Finished!! Press enter to exit')


    @staticmethod
    def __checkpoint(masked_area, min_pixels=30):
        pixels = cv2.countNonZero(masked_area)
        return pixels > min_pixels

    def __show_preview(self, sample_image="sample1"):
        s_img = cv2.imread(f'resources/samples/{sample_image}.jpg', cv2.IMREAD_UNCHANGED)
        s_img_resized = cv2.resize(s_img, (1280, 784))

        while True:
            cv2.imshow("Instructions", s_img_resized)

            success, frame = self.capture.read()
            w_name = f"Colors Auto-Calibrator"
            cv2.imshow(w_name, frame)  # SHOW MASK window

            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.destroyAllWindows()
                break


    def __calibrate_point(
            self,
            coord: Tuple[int, int, int, int],
            h_tolerance: int = 30,
            s_tolerance: int = 30,
            v_tolerance: int = 30,
            pixels: int =30
    ):

        values = {
            "v_max": 255,
            "v_min": 0,
            "s_max": 255,
            "s_min": 0,
            "h_max": 179,
            "h_min": 0
        }

        tolerance = {
            "v_max": v_tolerance,
            "v_min": -v_tolerance,
            "s_max": s_tolerance,
            "s_min": -s_tolerance,
            "h_max": h_tolerance,
            "h_min": -h_tolerance
        }

        success, frame = self.capture.read()

        blurred_frame = cv2.GaussianBlur(frame, (7, 7), 1)
        hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

        for value in values:
            while True:
                lower = np.array([values["h_min"], values["s_min"], values["v_min"]])
                upper = np.array([values["h_max"], values["s_max"], values["v_max"]])

                mask = cv2.inRange(hsv_frame, lower, upper)
                my_point = mask[coord[0]:coord[1], coord[2]:coord[3]]

                if self.__checkpoint(my_point, pixels):
                    if "max" in value:
                        values[value] -= 1
                    else:
                        values[value] += 1
                else:
                    values[value] = values[value] + tolerance[value]
                    if values[value] > 255:
                        values[value] = 255
                    if values[value] < 0:
                        values[value] = 0
                    break

                resized1 = cv2.resize(mask, (1280, 720), interpolation=cv2.INTER_AREA)
                cv2.imshow("Let the script cook", resized1)

                if cv2.waitKey(1) & 0xFF == 27:
                    break

            cv2.destroyAllWindows()
        return values