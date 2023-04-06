import cv2

def show_markers(frame):
    moves_markers(frame)
    target_markers(frame)

    teampreview_markers(frame)
    
    changepokemon_markers(frame)
    # hp_markers(frame)


def moves_markers(frame):
    cv2.rectangle(frame, (940,445),(960,465),(0,0,255),cv2.LINE_4)
    cv2.rectangle(frame, (940,520),(960,540),(0,0,255),cv2.LINE_4)
    cv2.rectangle(frame, (940,595),(960,615),(0,0,255),cv2.LINE_4)
    cv2.rectangle(frame, (940,670),(960,690),(0,0,255),cv2.LINE_4)


def target_markers(frame):
    # Selezione target
    cv2.rectangle(frame, (435,95),(635,320),(255, 0,0),cv2.LINE_4)
    cv2.rectangle(frame, (650,95),(850,320),(255, 0,0),cv2.LINE_4)
    cv2.rectangle(frame, (435,375),(635,600),(255, 0,0),cv2.LINE_4)
    cv2.rectangle(frame, (650,375),(850,600),(255, 0,0),cv2.LINE_4)


def teampreview_markers(frame):
    #TODO: make this!
    pass


#TODO: Old system markers, have to update them

def changepokemon_markers(frame):
    # Cambio pokemon
    cv2.rectangle(frame, (337,115),(347,125),(255, 0, 255),cv2.FILLED)
    cv2.rectangle(frame, (337,198),(347,208),(255, 0, 255),cv2.FILLED)
    cv2.rectangle(frame, (337,282),(347,292),(255, 0, 255),cv2.FILLED)
    cv2.rectangle(frame, (337,366),(347,376),(255, 0, 255),cv2.FILLED)


def hp_markers():
    #TODO: Da sistemare

    # LEFT
    cv2.rectangle(frame, (5,620),(12,650),(0,0,255),cv2.FILLED)
    cv2.rectangle(frame, (290,620),(305,650),(0,0,255),cv2.FILLED)

    # RIGHT
    cv2.rectangle(frame, (340,640),(345,680),(0,0,255),cv2.FILLED)
    cv2.rectangle(frame, (620,640),(630,680),(0,0,255),cv2.FILLED)