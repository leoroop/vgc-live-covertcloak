from utils import *
import numpy as np
import json


def show_preview(sample_image="sample1"):
    simg = cv2.imread(f'samples/{sample_image}.jpg', cv2.IMREAD_UNCHANGED)
    simg_resized = cv2.resize(simg, (480, 270))
    separator = cv2.imread('samples/separator.jpg', cv2.IMREAD_UNCHANGED)
    title = cv2.imread('samples/title.jpg', cv2.IMREAD_UNCHANGED)

    while True:
        success, frame = capture.read()
        frame_resized = cv2.resize(frame, (480, 270))

        horizontal = np.concatenate((frame_resized, separator, simg_resized), axis=1)
        vertical = np.concatenate((title, horizontal), axis=0)

        w_name = f"Colors Auto-Calibrator"
        cv2.namedWindow(w_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(w_name, 966, 334)
        cv2.moveWindow(w_name, 40, 30)
        cv2.imshow(w_name, vertical)  # SHOW MASK window

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.destroyAllWindows()
            break


def calibrate_point(coord, h_tolerance=30, s_tolerance=30, v_tolerance=30, pixels=30):

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

    success, frame = capture.read()

    FrameBlur = cv2.GaussianBlur(frame, (7, 7), 1)
    FrameHSV = cv2.cvtColor(FrameBlur, cv2.COLOR_BGR2HSV)

    for value in values:
        while True:
            lower = np.array([values["h_min"], values["s_min"], values["v_min"]])
            upper = np.array([values["h_max"], values["s_max"], values["v_max"]])

            # print(lower, upper)

            mask = cv2.inRange(FrameHSV, lower, upper)
            my_point = mask[coord[0]:coord[1], coord[2]:coord[3]]

            if checkpoint(my_point, pixels):
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

    # lower = np.array([values["h_min"], values["s_min"], values["v_min"]])
    # upper = np.array([values["h_max"], values["s_max"], values["v_max"]])
    # mask = cv2.inRange(FrameHSV, lower, upper)
    # resized1 = cv2.resize(mask, (1280, 720), interpolation=cv2.INTER_AREA)
    # cv2.imshow("Covert Cloak", resized1)
    #
    # cv2.waitKey(0)

    return values


green_point = (895, 925, 1620, 1650)    # 15
yellow_point = (1078, 1080, 10, 1910)   # 30
white_point = (240, 250, 1345, 1545)    # 80

device = choose_capturecard()

capture = cv2.VideoCapture(device, cv2.CAP_DSHOW)
capture.set(3, 1920)
capture.set(4, 1080)

show_preview()

print("Calibration started. Please wait...")
colors = {'green': calibrate_point(green_point, h_tolerance=10, s_tolerance=50, v_tolerance=50, pixels=800),
          'yellow': calibrate_point(yellow_point, h_tolerance=10, s_tolerance=80, v_tolerance=80, pixels=3700),
          'white': calibrate_point(white_point, h_tolerance=80, s_tolerance=149, v_tolerance=80, pixels=1900)}

capture.release()

with open('colors.json', 'w+', encoding='utf-8') as file:
    json.dump(colors, file, indent=4)

print()
input('Finished!! Press enter to exit')
