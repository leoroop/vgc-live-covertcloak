import cv2

def show_markers(frame):
    moves_markers(frame)
    target_markers(frame)

    teampreview_markers(frame)
    
    # changepokemon_markers(frame)
    # hp_markers(frame)


def moves_markers(frame):
    height = frame.shape[0]
    width = frame.shape[1]

    moves_x = int(width * 0.734375) # 940 / 1280
    move1_y = int(height * 0.618056) # 445 / 720
    move2_y = int(height * 0.722222) # 520 / 720
    move3_y = int(height * 0.826389) # 595 / 720
    move4_y = int(height * 0.930556) # 670 / 720

    color = (0,0,255) # red
    line_style = cv2.LINE_4

    #TODO: calcolare offset correttamente
    cv2.rectangle(frame, (moves_x, move1_y), (moves_x + 20, move1_y + 20), color, line_style)
    cv2.rectangle(frame, (moves_x, move2_y), (moves_x + 20, move2_y + 20), color, line_style)
    cv2.rectangle(frame, (moves_x, move3_y), (moves_x + 20, move3_y + 20), color, line_style)
    cv2.rectangle(frame, (moves_x, move4_y), (moves_x + 20, move4_y + 20), color, line_style)


def target_markers(frame):
    height = frame.shape[0]
    width = frame.shape[1]
    
    color = (255, 0,0) # blue
    line_style = cv2.LINE_4

    # TODO: Calcolare i coefficienti veri
    target_left = int(width * 0.734375) # 435 / 1280
    target_right = int(width * 0.734375) # 650 / 1280

    target_top = int(height * 0.618056) # 95 / 720
    target_bottom = int(height * 0.618056) # 375 / 720
    
    #TODO: calcolare offset
    cv2.rectangle(frame, (target_left, target_top), (635,320), color, line_style)
    cv2.rectangle(frame, (target_right, target_top), (850,320), color, line_style)
    cv2.rectangle(frame, (target_left, target_bottom), (635,600), color, line_style)
    cv2.rectangle(frame, (target_right, target_bottom), (850,600), color, line_style)


def teampreview_markers(frame):
    height = frame.shape[0]
    width = frame.shape[1]

    cv2.rectangle(frame, (105,100),(540,170),(0, 255, 0),cv2.LINE_4)
    cv2.rectangle(frame, (105,178),(540,248),(0, 255, 0),cv2.LINE_4)
    cv2.rectangle(frame, (105,256),(540,326),(0, 255, 0),cv2.LINE_4)
    cv2.rectangle(frame, (105,333),(540,403),(0, 255, 0),cv2.LINE_4)
    cv2.rectangle(frame, (105,410),(540,480),(0, 255, 0),cv2.LINE_4)
    cv2.rectangle(frame, (105,489),(540,559),(0, 255, 0),cv2.LINE_4)
    cv2.rectangle(frame, (110,567),(535,627),(0, 255, 0),cv2.LINE_4)


#TODO: Old system markers, have to update them

def changepokemon_markers(frame):
    height = frame.shape[0]
    width = frame.shape[1]

    cv2.rectangle(frame, (337,115),(347,125),(255, 0, 255),cv2.FILLED)
    cv2.rectangle(frame, (337,198),(347,208),(255, 0, 255),cv2.FILLED)
    cv2.rectangle(frame, (337,282),(347,292),(255, 0, 255),cv2.FILLED)
    cv2.rectangle(frame, (337,366),(347,376),(255, 0, 255),cv2.FILLED)


def hp_markers():
    #TODO: Da sistemare
    height = frame.shape[0]
    width = frame.shape[1]

    # LEFT
    cv2.rectangle(frame, (5,620),(12,650),(0,0,255),cv2.FILLED)
    cv2.rectangle(frame, (290,620),(305,650),(0,0,255),cv2.FILLED)

    # RIGHT
    cv2.rectangle(frame, (340,640),(345,680),(0,0,255),cv2.FILLED)
    cv2.rectangle(frame, (620,640),(630,680),(0,0,255),cv2.FILLED)