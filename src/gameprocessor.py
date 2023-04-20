import cv2

class GameProcessor():
    def __init__(start_frame):
        self.frame_height = start_frame.shape[0]
        self.frame_width = start_frame.shape[1]

        self.moves_x = int(width * 0.734375) # 940 / 1280
        self.move1_y = int(height * 0.618056) # 445 / 720
        self.move2_y = int(height * 0.722222) # 520 / 720
        self.move3_y = int(height * 0.826389) # 595 / 720
        self.move4_y = int(height * 0.930556) # 670 / 720

        self.moves_x_offset = int(width / 64)
        self.moves_y_offset = int(height / 36)

        self.red_color = (0,0,255) # red
        self.line_style = cv2.LINE_4