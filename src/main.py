import json

import numpy as np

from src.processors.game_processor import GameProcessor

from utils import *

def main():

    with open('resources/colors.json', 'r', encoding='utf-8') as file:
        colors = json.load(file)

    yellow_min = np.array([colors['yellow']['h_min'], colors['yellow']['s_min'], colors['yellow']['v_min']])
    yellow_max = np.array([colors['yellow']['h_max'], colors['yellow']['s_max'], colors['yellow']['v_max']])

    covers = {
        "moves": cv2.imread("covers/cover_moves.jpg", cv2.IMREAD_UNCHANGED),
    }


    device = choose_capturecard()
    device = 0
    capture = cv2.VideoCapture(device)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT , 1080)

    covers = {
        "moves": cv2.imread("covers/cover_moves.jpg"),
        "target": cv2.imread("covers/cover_target.jpg"),
        "changepkmn": cv2.imread("covers/cover_change.jpg")
    }

    # frame = cv2.imread("screens/target.png")

    success, frame = capture.read()

    gp = GameProcessor(frame)

    while True:
        # STILL FRAMES TO EASILY CALCULATE MARKERS POSITIONS
        
        # frame = cv2.imread("screens/moves.png")
        # frame = cv2.imread("screens/target.png")
        # frame = cv2.imread("screens/battle_menu.png")
        # frame = cv2.imread("screens/change.png")
        # frame = cv2.imread("screens/teampreview.png")
        # frame = cv2.imread("screens/pkmninfo.png")

        success, frame = capture.read()

        blurred_frame = cv2.GaussianBlur(frame, (7, 7), 1)  # Apply blur
        hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)  # Conversion to HSV colors
        mask_yellow = cv2.inRange(hsv_frame, yellow_min, yellow_max)

        clean = frame.copy()
        # process(frame, covers)

        gp.apply_moves_markers(frame)
        gp.move_selection_screen_is_active(mask_yellow)
        # gp.apply_targets_markers(frame)
        # gp.apply_battlemenuoptions_markers(frame)
        # gp.apply_changes_markers(frame)
        # gp.apply_teampreview_markers(frame)
        # gp.apply_pkmninfo_markers(mask_yellow)

        # show_markers(clean)
        cv2.imshow("Cleanfeed", clean)
        # cv2.imshow("HSV", hsv_frame)
        # cv2.imshow("Yellow Mask", mask_yellow)
        if gp.move_selection_screen_is_active(mask_yellow):
            frame[300:700, 735:1260] = covers["moves"]


        cv2.imshow("VGC Hide Info (Beta)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()