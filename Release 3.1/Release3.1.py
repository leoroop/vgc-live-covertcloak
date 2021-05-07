# Added color calibration
# Added choose number of windows
# Added choose overlay size
# Added hide black screen
# Improved capture quality (directshow)

import device
import numpy as np
import cv2


def choose_capturecard():
    # print OpenCV version
    print("OpenCV version: " + cv2.__version__)

    # Get camera list
    device_list = device.getDeviceList()
    etiqueta = 0

    for name in device_list:
        print(str(etiqueta) + ': ' + name)
        etiqueta += 1

    recuento = etiqueta - 1

    if recuento < 0:
        print("No device is connected")
        return

    mensaje = "Select a camera (0 to " + str(recuento) + "): "
    try:
        capture_number = int(input(mensaje))
    except Exception:
        print("It's not a number!")
        print()
        return choose_capturecard()

    if (capture_number > recuento) or capture_number < 0:
        print("Invalid number! Retry!")
        print()
        return choose_capturecard()

    return capture_number


def choose_number_of_windows():
    print()
    print('1: Show only HideInfo window')
    print('2: Show Cleanfeed and HideInfo windows')
    try:
        valor = int(input('Choose number of windows (1 or 2): '))
    except Exception:
        print("It's not a number!")
        return choose_number_of_windows()

    if valor < 1 or valor > 3:
        print("Invalid number! Retry!")
        return choose_number_of_windows()

    return valor


def choose_overlay_size():
    print()
    print('1: Cropped overlay (Legacy Release3)')
    print('2: Full screen overlay')
    try:
        valor = int(input('Choose overlay size (1 or 2): '))

    except Exception:
        print("It's not a number!")
        return choose_overlay_size()

    if valor < 1 or valor > 3:
        print("Invalid number! Retry!")
        return choose_overlay_size()

    return valor


def checkpoint(myframe, value):
    contornos, hierarchy = cv2.findContours(myframe, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contornos:
        area = cv2.contourArea(cnt)
        if area > value:
            # cv2.drawContours(frame, cnt, -1, (255, 0, 0), 3)
            return True
        else:
            return False


def overlay_frame(imagen, overlay, y0, y1, x0, x1):
    myimg = cv2.imread("Recursos/" + overlay + '.png',
                       cv2.IMREAD_UNCHANGED)  # Custom image import with RGB-A (4 Channels)
    my_img_resized = cv2.resize(myimg, ((x1 - x0), (y1 - y0)))  # Resize "img" to fit the area to hide (RGB-A)
    my_mask_alpha = my_img_resized[:, :, 3]  # Generate alpha mask of "my_img_resized"
    my_mask_alpha_inv = cv2.bitwise_not(my_mask_alpha)  # Generate the inverse of the "my_mask_alpha"
    my_img_rgb = my_img_resized[:, :, 0:3]  # Convert "my_img_resized" RGB-A to RGB (3 Channels)

    my_recorte = imagen[y0:y1, x0:x1]  # Crop the frame to fit the area to hide
    my_capa_inferior = cv2.bitwise_and(my_recorte, my_recorte, mask=my_mask_alpha_inv)  # Apply "alpha inv" to "recorte"
    my_capa_superior = cv2.bitwise_and(my_img_rgb, my_img_rgb, mask=my_mask_alpha)  # Apply "mask alpha" to "img rgb"
    my_dst = cv2.add(my_capa_inferior, my_capa_superior)  # Add "my_capa_inferior" + "my_capa_superior"
    imagen[y0:y1, x0:x1] = my_dst  # Draw "my_dst" in the frame area to hide

    return imagen


def get_color(text_file):

    lista = []
    with open('Recursos/' + text_file + '.txt', "r") as file:
        data = file.read()
    data = data.split(',')
    for a in data:
        lista.append(int(a))

    return tuple(lista)


# DEFINICION DE VARIABLES
# Alpha
alpha_value = 0

# Colores
color = get_color('0White')
general_white_min = np.array([color[0], color[2], color[4]])
general_white_max = np.array([color[1], color[3], color[5]])

color = get_color('0Black')
general_black_min = np.array([color[0], color[2], color[4]])
general_black_max = np.array([color[1], color[3], color[5]])

color = get_color('Change-Red')
change_red_min = np.array([color[0], color[2], color[4]])
change_red_max = np.array([color[1], color[3], color[5]])

color = get_color('Picking-Red')
picking_red_min = np.array([color[0], color[2], color[4]])
picking_red_max = np.array([color[1], color[3], color[5]])

color = get_color('Team-Blue')
team_blue_min = np.array([color[0], color[2], color[4]])
team_blue_max = np.array([color[1], color[3], color[5]])


# PROGRAMA
capture = cv2.VideoCapture(choose_capturecard(), cv2.CAP_DSHOW)
capture.set(3, 1280)
capture.set(4, 720)

number_of_windows = choose_number_of_windows()

overlay_size = choose_overlay_size()

while True:

    # Leer la capturadora
    success, frame = capture.read()
    clean = frame.copy()

    # Transformación y manipulación del frame
    FrameBlur = cv2.GaussianBlur(frame, (7, 7), 1)  # Difuminar el Frame
    FrameHSV = cv2.cvtColor(FrameBlur, cv2.COLOR_BGR2HSV)  # Conversión de color del Frame a gama de color HSV

    # Crear mascara de color
    mask_general_white = cv2.inRange(FrameHSV, general_white_min, general_white_max)
    mask_general_black = cv2.inRange(FrameHSV, general_black_min, general_black_max)
    mask_change_red = cv2.inRange(FrameHSV, change_red_min, change_red_max)
    mask_pinking_red = cv2.inRange(FrameHSV, picking_red_min, picking_red_max)
    mask_team_blue = cv2.inRange(FrameHSV, team_blue_min, team_blue_max)

    # # Definir puntos de deteccion
    P1 = mask_change_red[15:30, 1220:1240]  # CHANGE SCREEN
    P2 = mask_change_red[15:30, 1130:1150]  # CHANGE SCREEN
    P3 = mask_general_white[535:570, 1200:1235]  # CHANGE SCREEN
    P4 = mask_general_white[535:570, 1240:1265]  # CHANGE SCREEN

    P10 = mask_general_black[485:490, 1180:1210]  # MOVE SELECT
    P11 = mask_general_black[555:560, 1180:1210]  # MOVE SELECT
    P12 = mask_general_black[625:630, 1180:1210]  # MOVE SELECT
    P13 = mask_general_black[695:700, 1180:1210]  # MOVE SELECT
    P14 = mask_general_white[365:375, 1260:1270]  # MOVE SELECT

    P20 = mask_general_black[323:330, 466:475]  # TARGET SLOT
    P21 = mask_general_black[323:330, 770:780]  # TARGET SLOT
    P22 = mask_general_black[468:475, 466:475]  # TARGET SLOT
    P23 = mask_general_black[468:475, 770:780]  # TARGET SLOT
    P24 = mask_general_white[65:70, 1250:1260]  # TARGET SLOT
    P25 = mask_general_white[65:70, 910:920]    # TARGET SLOT

    P30 = mask_team_blue[100:110, 215:230]   # MY TEAM BOX
    P31 = mask_team_blue[100:110, 450:465]   # MY TEAM BOX
    P32 = mask_general_white[375:385, 420:430]  # MY TEAM BOX

    P40 = mask_pinking_red[140:150, 80:90]    # PICKING PKM
    P41 = mask_pinking_red[140:150, 320:330]  # PICKING PKM

    P50 = mask_general_white[75:85, 10:20]      # INFO SCREEN
    P51 = mask_general_white[175:185, 10:20]    # INFO SCREEN
    P52 = mask_general_black[640:650, 10:20]    # INFO SCREEN
    P53 = mask_general_black[640:650, 195:205]  # INFO SCREEN
    P54 = mask_general_black[700:710, 635:645]  # INFO SCREEN

    P99 = mask_general_black[60:660, 340:940]  # BLACK SCREEN BETWEEN TRAINER CARD AND GAME

    if overlay_size == 1:
        # HIDE CHANGE POKEMON SCREEN
        if checkpoint(P1, 30) and checkpoint(P2, 30) and checkpoint(P3, 30) and checkpoint(P4, 30) is True:
            overlay_frame(frame, 'LegacyOverlay/change', 45, 600, 0, 1280)

        # HIDE MOVE SELECT
        elif checkpoint(P10, 30) and checkpoint(P11, 30) and checkpoint(P12, 30) and checkpoint(P13, 30) and checkpoint(
                P14, 30) is True:
            overlay_frame(frame, 'LegacyOverlay/moves', 410, 720, 650, 1280)

        # HIDE TARGET SLOT
        elif checkpoint(P20, 30) and checkpoint(P21, 30) and checkpoint(P22, 30) and checkpoint(P23, 30) and (
                checkpoint(P24, 30) or checkpoint(P25, 30)) is True:
            overlay_frame(frame, 'LegacyOverlay/target', 225, 500, 305, 935)

        # HIDE MY TEAM BOX
        elif checkpoint(P30, 30) and checkpoint(P31, 30) and checkpoint(P32, 30) is True:
            overlay_frame(frame, 'LegacyOverlay/team', 123, 604, 410, 480)

        # HIDE POKEMON PICKING
        elif (checkpoint(P40, 30) and checkpoint(P41, 30)) is True:
            overlay_frame(frame, 'LegacyOverlay/picking', 20, 600, 380, 1120)

        # HIDE INFO BATTLE STATUS (STATS, FIELD, WEATHER)
        elif checkpoint(P50, 30) and checkpoint(P51, 30) and checkpoint(P52, 30) and checkpoint(P53, 30) and checkpoint(
                P54, 30) is True:
            overlay_frame(frame, 'LegacyOverlay/info', 45, 600, 0, 1280)

    elif overlay_size == 2:
        # HIDE CHANGE POKEMON SCREEN
        if checkpoint(P1, 30) and checkpoint(P2, 30) and checkpoint(P3, 30) and checkpoint(P4, 30) is True:
            overlay_frame(frame, 'FullscreenOverlay/change', 0, 720, 0, 1280)

        # HIDE MOVE SELECT
        elif checkpoint(P10, 30) and checkpoint(P11, 30) and checkpoint(P12, 30) and checkpoint(P13, 30) and checkpoint(
                P14, 30) is True:
            overlay_frame(frame, 'FullscreenOverlay/moves', 0, 720, 0, 1280)

        # HIDE TARGET SLOT
        elif checkpoint(P20, 30) and checkpoint(P21, 30) and checkpoint(P22, 30) and checkpoint(P23, 30) and (
                checkpoint(P24, 30) or checkpoint(P25, 30)) is True:
            overlay_frame(frame, 'FullscreenOverlay/target', 0, 720, 0, 1280)

        # HIDE MY TEAM BOX
        elif checkpoint(P30, 30) and checkpoint(P31, 30) and checkpoint(P32, 30) is True:
            overlay_frame(frame, 'FullscreenOverlay/team', 0, 720, 0, 1280)

        # HIDE POKEMON PICKING
        elif (checkpoint(P40, 30) and checkpoint(P41, 30)) is True:
            overlay_frame(frame, 'FullscreenOverlay/picking', 0, 720, 0, 1280)

        # HIDE INFO BATTLE STATUS (STATS, FIELD, WEATHER)
        elif checkpoint(P50, 30) and checkpoint(P51, 30) and checkpoint(P52, 30) and checkpoint(P53, 30) and checkpoint(
                P54, 30) is True:
            overlay_frame(frame, 'FullscreenOverlay/info', 0, 720, 0, 1280)

    # FADE LOGO IN ANY BLACK SCREEN
    if checkpoint(P99, 90000) is True:
        img = cv2.imread("Recursos/logo/logo.png", cv2.IMREAD_UNCHANGED)  # Custom image import with RGB-A (4 Channels)
        imgResized = cv2.resize(img, (1280, 720))  # Resize "img" to fit the area to hide (RGB-A)
        maskAlpha = imgResized[:, :, 3]  # Generate alpha mask of "imgResized"
        maskAlphaInv = cv2.bitwise_not(maskAlpha)  # Generate the inverse of the "maskAlpha"
        imgRGB = imgResized[:, :, 0:3]  # Convert "imgResized" RGB-A to RGB (3 Channels)

        Recorte = frame[0:720, 0:1280]  # Crop the frame to fit the area to hide
        CapaInferior = cv2.bitwise_and(Recorte, Recorte, mask=maskAlphaInv)  # Apply "maskAlphaInv" to "Recorte"
        CapaSuperior = cv2.bitwise_and(imgRGB, imgRGB, mask=maskAlpha)  # Apply "maskAlpha" to "imgRGB"
        dst = cv2.addWeighted(CapaInferior, 1, CapaSuperior, alpha_value, 0)
        frame[0:720, 0:1280] = dst  # Draw "dst" in the frame area to hide
        if alpha_value + 0.033 > 1:
            alpha_value = 1
        else:
            alpha_value = alpha_value + 0.033
    else:
        alpha_value = 0

    # Mostrar ventanas
    if number_of_windows == 2:
        cv2.imshow("HideInfo", frame)  # SHOW HIDE VGC INFO window
        cv2.imshow("Cleanfeed", clean)  # SHOW CLEANFEED window
    elif number_of_windows == 1:
        cv2.imshow("HideInfo", frame)  # SHOW HIDE VGC INFO window

    if cv2.waitKey(1) & 0xFF == ord('q'):
        capture.release()
        cv2.destroyAllWindows()
        break
