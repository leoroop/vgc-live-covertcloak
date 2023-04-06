import cv2
import numpy as np

from markers import *
from process import process

from utils import *

def main():
    
    device = choose_capturecard()
    capture = cv2.VideoCapture(device)
    capture.set(3, 1280)
    capture.set(4, 720)

    covers = {
        "moves": cv2.imread("../covers/cover_moves.jpg"),
        "target": cv2.imread("../covers/cover_target.jpg"),
        "changepkmn": cv2.imread("../covers/cover_change.jpg")
    }

    while True:
        # STILL FRAMES TO EASILY CALCULATE MARKERS POSITIONS
        
        # frame = cv2.imread("../screens/no_move.png")
        # frame = cv2.imread("../screens/moves.png")
        # frame = cv2.imread("../screens/target.png")
        # frame = cv2.imread("../screens/change.png")
        # frame = cv2.imread("../screens/teampreview.png")
        success, frame = capture.read()
        
        clean = frame.copy()        
        process(frame, covers)
        
        # show_markers(clean)

        cv2.imshow("VGC Hide Info (Beta)", frame)
        cv2.imshow("Cleanfeed", clean)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()