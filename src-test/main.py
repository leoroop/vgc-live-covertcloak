from utils import *
from colors import *


def checkpoint(masked_area, min_pixels=30):
    pixels = cv2.countNonZero(masked_area)
    return pixels > min_pixels


covers = {
    "command": cv2.imread("covers/command.png"),
    "target": cv2.imread("covers/target.png"),
    "change": cv2.imread("covers/change.png"),
    "pick": cv2.imread("covers/pick.png")
}

device = choose_capturecard()
capture = cv2.VideoCapture(device, cv2.CAP_DSHOW)
capture.set(3, 1920)
capture.set(4, 1080)

pick_cnt = 0
command_cnt = 0
target_cnt = 0
change_cnt = 0

hide_color = [72, 41, 155]

buffer = []
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
        buffer[0][130:860, 80:1700] = covers['pick']
        pick_cnt = 10
    else:
        if pick_cnt:
            buffer[0][130:860, 80:1700] = covers['pick']
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
        buffer[0][580:1080, 1110:1920] = covers['command']
        command_cnt = 10
    else:
        if command_cnt:
            buffer[0][580:1080, 1110:1920] = covers['command']
            command_cnt -= 1

    # check if choosing target screen
    target_top_left = mask_yellow[155:195, 660:665]
    target_top_right = mask_yellow[155:195, 981:986]
    target_bot_left = mask_yellow[860:885, 660:665]
    target_bot_right = mask_yellow[860:885, 981:986]
    not_target_top = mask_yellow[140:260, 615:620]
    not_target_bot = mask_yellow[560:680, 615:620]
    not_target_left = mask_yellow[870:920, 370:380]

    if (
        (
            checkpoint(target_top_left, 115) is True or
            checkpoint(target_top_right, 115) is True or
            checkpoint(target_bot_left, 115) is True or
            checkpoint(target_bot_right, 115) is True
        ) and
            checkpoint(not_target_top, 30) is False and
            checkpoint(not_target_bot, 30) is False and
            checkpoint(not_target_left, 300) is False
    ):
        buffer[0][20:1050, 615:1325] = covers['target']
        target_cnt = 10
    else:
        if target_cnt:
            buffer[0][20:1050, 615:1325] = covers['target']
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
        buffer[0][100:1000, 40:1840] = covers["change"]
        change_cnt = 10
    else:
        if change_cnt:
            buffer[0][100:1000, 40:1840] = covers["change"]
            change_cnt -= 1

    # team preview_markers(frame)
    resized1 = cv2.resize(clean, (1280, 720), interpolation=cv2.INTER_AREA)
    cv2.imshow("clean", resized1)

    if len(buffer) >= 5:
        resized2 = cv2.resize(buffer[0], (1280, 720), interpolation=cv2.INTER_AREA)
        cv2.imshow("hide", resized2)
        del buffer[0]

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
