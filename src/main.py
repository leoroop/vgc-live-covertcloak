from src.processors.game_processor import GameProcessor

from utils import *

def main():

    #TODO: implementare moves processor e targets processor
    #TODO: implementare calcolo marker no moves
    
    # device = choose_capturecard()
    device = 0
    capture = cv2.VideoCapture(device)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT , 1080)

    covers = {
        "moves": cv2.imread("covers/cover_moves.jpg"),
        "target": cv2.imread("covers/cover_target.jpg"),
        "changepkmn": cv2.imread("covers/cover_change.jpg")
    }

    frame = cv2.imread("screens/target.png")

    # success, frame = capture.read()

    gp = GameProcessor(frame)

    while True:
        # STILL FRAMES TO EASILY CALCULATE MARKERS POSITIONS
        
        # frame = cv2.imread("screens/moves.png")
        # frame = cv2.imread("screens/target.png")
        # frame = cv2.imread("screens/battle_menu.png")
        # frame = cv2.imread("screens/change.png")

        frame = cv2.imread("screens/teampreview.png")
        # success, frame = capture.read()

        clean = frame.copy()
        # process(frame, covers)

        # gp.apply_moves_markers(frame)
        # gp.apply_targets_markers(frame)
        # gp.apply_battlemenuoptions_markers(frame)
        # gp.apply_changes_markers(frame)
        gp.apply_teampreview_markers(frame)

        # show_markers(clean)

        cv2.imshow("VGC Hide Info (Beta)", frame)
        # cv2.imshow("Cleanfeed", clean)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()