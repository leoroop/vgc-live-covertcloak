import cv2

class GameProcessor():
    def __init__(self, start_frame):
        self.frame_height = start_frame.shape[0]
        self.frame_width = start_frame.shape[1]        

        self.red_color = (0,0,255)
        self.blue_color = (255, 0,0)
        self.line_style = cv2.LINE_4

        self.__calc_moves_positions();
        self.__calc_targets_positions();


    def __calc_moves_positions(self):
        self.moves_x = int(self.frame_width * 0.734375) # 940 / 1280
        self.move1_y = int(self.frame_height * 0.618056) # 445 / 720
        self.move2_y = int(self.frame_height * 0.722222) # 520 / 720
        self.move3_y = int(self.frame_height * 0.826389) # 595 / 720
        self.move4_y = int(self.frame_height * 0.930556) # 670 / 720

        self.moves_x_offset = int(self.frame_width / 64)
        self.moves_y_offset = int(self.frame_height / 36)


    def __calc_targets_positions(self):
        self.target_left = int(self.frame_width * 0.734375) # 435 / 1280
        self.target_right = int(self.frame_width * 0.734375) # 650 / 1280

        self.target_top = int(self.frame_height * 0.618056) # 95 / 720
        self.target_bottom = int(self.frame_height * 0.618056) # 375 / 720


    def apply_moves_markers(self, frame):
        cv2.rectangle(frame, (self.moves_x, self.move1_y), (self.moves_x + self.moves_x_offset, self.move1_y + self.moves_y_offset), self.color_red, self.line_style)
        cv2.rectangle(frame, (self.moves_x, self.move2_y), (self.moves_x + self.moves_x_offset, self.move2_y + self.moves_y_offset), self.color_red, self.line_style)
        cv2.rectangle(frame, (self.moves_x, self.move3_y), (self.moves_x + self.moves_x_offset, self.move3_y + self.moves_y_offset), self.color_red, self.line_style)
        cv2.rectangle(frame, (self.moves_x, self.move4_y), (self.moves_x + self.moves_x_offset, self.move4_y + self.moves_y_offset), self.color_red, self.line_style)