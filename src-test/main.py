from utils import *
import numpy as np
import json

device = choose_capturecard()

number_of_windows = choose_number_of_windows()

with open('colors.json', 'r', encoding='utf-8') as file:
    colors = json.load(file)

green_min = np.array([colors['green']['h_min'], colors['green']['s_min'], colors['green']['v_min']])
green_max = np.array([colors['green']['h_max'], colors['green']['s_max'], colors['green']['v_max']])
white_min = np.array([colors['white']['h_min'], colors['white']['s_min'], colors['white']['v_min']])
white_max = np.array([colors['white']['h_max'], colors['white']['s_max'], colors['white']['v_max']])
yellow_min = np.array([colors['yellow']['h_min'], colors['yellow']['s_min'], colors['yellow']['v_min']])
yellow_max = np.array([colors['yellow']['h_max'], colors['yellow']['s_max'], colors['yellow']['v_max']])

covers = {
    "command": cv2.imread("covers/command.png", cv2.IMREAD_UNCHANGED),
    "target": cv2.imread("covers/target.png", cv2.IMREAD_UNCHANGED),
    "change": cv2.imread("covers/change.png", cv2.IMREAD_UNCHANGED),
    "pick": cv2.imread("covers/pick.png", cv2.IMREAD_UNCHANGED)
}

pick_cnt = 0
command_cnt = 0
target_cnt = 0
change_cnt = 0

hide_color = [72, 41, 155]

buffer = []

capture = cv2.VideoCapture(device, cv2.CAP_DSHOW)
capture.set(3, 1920)
capture.set(4, 1080)
while True:
    success, frame = capture.read()
    clean = frame.copy()

    buffer.append(frame)

    blurred_frame = cv2.GaussianBlur(frame, (7, 7), 1)  # Apply blur
    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)  # Conversion to HSV colors

    mask_green = cv2.inRange(hsv_frame, green_min, green_max)
    mask_white = cv2.inRange(hsv_frame, white_min, white_max)
    mask_yellow = cv2.inRange(hsv_frame, yellow_min, yellow_max)

    # check if pick screen
    piked_right = mask_green[895:925, 1630:1650]
    piked_left = mask_green[895:925, 660:680]
    team_right = mask_white[240:250, 1345:1520]
    team_left = mask_white[240:250, 385:560]

    if (
        (
            checkpoint(piked_right, 250) is True or
            checkpoint(piked_left, 250) is True
        ) and (
            checkpoint(team_right, 1600) is True or
            checkpoint(team_left, 1600) is True
        )
    ):
        buffer[0] = overlay_frame(buffer[0], covers['pick'])
        pick_cnt = 10
    else:
        if pick_cnt:
            buffer[0] = overlay_frame(buffer[0], covers['pick'])
            pick_cnt -= 1

    # check if input command screen
    command_top = mask_yellow[415:440, 1874:1877]
    command_bot = mask_yellow[510:535, 1874:1877]
    not_command_top = mask_yellow[415:440, 1890:1893]
    not_command_bot = mask_yellow[510:535, 1890:1893]

    if (
        checkpoint(command_top, 60) is True and
        checkpoint(command_bot, 60) is True and
        checkpoint(not_command_top, 60) is False and
        checkpoint(not_command_bot, 60) is False
    ):
        buffer[0] = overlay_frame(buffer[0], covers['command'])
        command_cnt = 5
    else:
        if command_cnt:
            buffer[0] = overlay_frame(buffer[0], covers['command'])
            command_cnt -= 1

    # check if target screen
    target_top = mask_yellow[0:1, 10:1910]
    target_bot = mask_yellow[1079:1080, 10:1910]
    target_button_left = mask_white[1030:1046, 1774:1776]
    target_button_right = mask_white[1030:1046, 1793:1795]

    if (
        checkpoint(target_top, 1500) and
        checkpoint(target_bot, 1500) and
        checkpoint(target_button_left, 25) and
        checkpoint(target_button_right, 25)
    ):
        buffer[0] = overlay_frame(buffer[0], covers['target'])
        target_cnt = 8
    else:
        if target_cnt:
            buffer[0] = overlay_frame(buffer[0], covers['target'])
            target_cnt -= 1

    # check if change Pokémon screen
    change1 = mask_white[400:402, 1421:1423]
    change2 = mask_white[486:488, 1421:1423]
    change3 = mask_white[572:574, 1421:1423]
    change4 = mask_white[658:660, 1421:1423]
    not_change1 = mask_white[385:415, 1490:1495]
    not_change2 = mask_white[471:501, 1490:1495]
    not_change3 = mask_white[557:587, 1490:1495]
    not_change4 = mask_white[643:673, 1490:1495]

    if (
        checkpoint(change1, 2) is True and
        checkpoint(change2, 2) is True and
        checkpoint(change3, 2) is True and
        checkpoint(change4, 2) is True and
        checkpoint(not_change1, 20) is False and
        checkpoint(not_change2, 20) is False and
        checkpoint(not_change3, 20) is False and
        checkpoint(not_change4, 20) is False
    ):
        buffer[0] = overlay_frame(buffer[0], covers['change'])
        change_cnt = 10
    else:
        if change_cnt:
            buffer[0] = overlay_frame(buffer[0], covers['change'])
            change_cnt -= 1

    if number_of_windows == 2:
        # team preview_markers(frame)
        resized1 = cv2.resize(clean, (1280, 720), interpolation=cv2.INTER_AREA)
        cv2.imshow("Cleanfeed", resized1)

    if len(buffer) >= 5:
        resized2 = cv2.resize(buffer[0], (1280, 720), interpolation=cv2.INTER_AREA)
        cv2.imshow("VGC Live Covert Cloak", resized2)
        del buffer[0]

    if cv2.waitKey(1) & 0xFF == 27:
        break


capture.release()
cv2.destroyAllWindows()
