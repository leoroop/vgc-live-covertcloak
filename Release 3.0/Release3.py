import device
import cv2
import numpy as np

def SeleccionarCapturadora(recuento):

    mensaje = "Select a camera (0 to " + str(recuento) + "): "
    try:
        valor = int(input(mensaje))
        # select = int(select)
    except Exception:
        print("It's not a number!")
        return SeleccionarCapturadora(recuento)

    if valor > recuento:
        print("Invalid number! Retry!")
        return SeleccionarCapturadora(recuento)

    return valor

def main():
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

    # Select a camera
    NumeroCapturadora = SeleccionarCapturadora(recuento)

    return NumeroCapturadora


capture = cv2.VideoCapture(main())
capture.set(3, 1280)
capture.set(4, 720)

# Definir colores
rojo_min = np.array([170, 190, 140])        # Promedio del rango mínimo de color rojo con 3 capturadoras diferentes
rojo_max = np.array([179, 230, 213])        # Promedio del rango maximo de color rojo con 3 capturadoras diferentes
rojo2_min = np.array([0, 160, 190])         # TEAM BOX Red color
rojo2_max = np.array([10, 190, 255])        # TEAM BOX Red color
rojo3_min = np.array([174, 160, 190])       # TEAM BOX Red color
rojo3_max = np.array([179, 190, 255])       # TEAM BOX Red color
azul_min = np.array([105, 188, 188])        # TEAM BOX Blue color
azul_max = np.array([110, 255, 255])        # TEAM BOX Blue color
blanco_min = np.array([0, 0, 210])          # Blanco generico
blanco_max = np.array([179, 85, 255])       # Blanco generico
negro_min = np.array([0, 0, 0])             # Negro generico
negro_max = np.array([179, 255, 50])        # Negro generico


# Funcion para detectar punto control

def checkpoint(x):
    contornos, hierarchy = cv2.findContours(x, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contornos:
        area = cv2.contourArea(cnt)
        if area > 30:
            # cv2.drawContours(frame, cnt, -1, (255, 0, 0), 3)
            return True
        else:
            return False


# Bucle de ejecucion del programa

while True:

    # Leer la capturadora
    success, frame = capture.read()
    clean = frame.copy()

    # Transformación y manipulación del frame
    FrameBlur = cv2.GaussianBlur(frame, (7, 7), 1)                   # Difuminar el Frame
    FrameHSV = cv2.cvtColor(FrameBlur, cv2.COLOR_BGR2HSV)            # Conversión de color del Frame a gama de color HSV

    # Crear mascara de color
    maskWhite = cv2.inRange(FrameHSV, blanco_min, blanco_max)        # White tone detection mask  - for ALL
    maskBlack = cv2.inRange(FrameHSV, negro_min,  negro_max)         # Black tone detection mask  - for ALL
    maskRed = cv2.inRange(FrameHSV, rojo_min,   rojo_max)            # Red tone 2 detection mask  - for CHANGE SCREEN
    maskRed2 = cv2.inRange(FrameHSV, rojo2_min,  rojo2_max)          # Red tone detection mask    - for TEAM BOX
    maskRed3 = cv2.inRange(FrameHSV, rojo3_min, rojo3_max)           # Red tone detection mask    - for TEAM BOX
    maskBlue = cv2.inRange(FrameHSV, azul_min,   azul_max)           # Blue tone detection mask   - for TEAM BOX

    # Definir puntos de deteccion
    P1 = maskRed[15:30, 1220:1240]           # CHANGE SCREEN Canvas coordinates for Red    Checkpoint 1
    P2 = maskRed[15:30, 1130:1150]           # CHANGE SCREEN Canvas coordinates for Red    Checkpoint 2
    P3 = maskWhite[535:570, 1200:1235]       # CHANGE SCREEN Canvas coordinates for white  Checkpoint 3
    P4 = maskWhite[535:570, 1240:1265]       # CHANGE SCREEN Canvas coordinates for White  Checkpoint 4

    P10 = maskBlack[485:490, 1180:1210]      # MOVE SELECT   Canvas coordinates for Black  Checkpoint 1
    P11 = maskBlack[555:560, 1180:1210]      # MOVE SELECT   Canvas coordinates for Black  Checkpoint 2
    P12 = maskBlack[625:630, 1180:1210]      # MOVE SELECT   Canvas coordinates for Black  Checkpoint 3
    P13 = maskBlack[695:700, 1180:1210]      # MOVE SELECT   Canvas coordinates for Black  Checkpoint 4
    P14 = maskWhite[365:375, 1260:1270]      # MOVE SELECT   Canvas coordinates for White  Checkpoint 5

    P20 = maskBlack[323:330, 466:475]        # TARGET SLOT   Canvas coordinates for Black  Checkpoint 1
    P21 = maskBlack[323:330, 770:780]        # TARGET SLOT   Canvas coordinates for Black  Checkpoint 2
    P22 = maskBlack[468:475, 466:475]        # TARGET SLOT   Canvas coordinates for Black  Checkpoint 3
    P23 = maskBlack[468:475, 770:780]        # TARGET SLOT   Canvas coordinates for Black  Checkpoint 4
    P24 = maskWhite[65:70, 1250:1260]        # TARGET SLOT   Canvas coordinates for White  Checkpoint 5
    P25 = maskWhite[65:70, 910:920]          # TARGET SLOT   Canvas coordinates for White  Checkpoint 6

    P30 = maskBlue[100:110, 215:230]         # MY TEAM BOX   Canvas coordinates for Blue   Checkpoint 1
    P31 = maskBlue[100:110, 450:465]         # MY TEAM BOX   Canvas coordinates for Blue   Checkpoint 2
    P32 = maskWhite[375:385, 420:430]        # MY TEAM BOX   Canvas coordinates for White  Checkpoint 3

    P40 = maskRed2[140:150, 80:90]           # PICKING PKM   Canvas coordinates for Red1   Checkpoint 1
    P41 = maskRed2[140:150, 320:330]         # PICKING PKM   Canvas coordinates for Red1   Checkpoint 2
    P42 = maskRed3[140:150, 80:90]           # PICKING PKM   Canvas coordinates for Red2   Checkpoint 1
    P43 = maskRed3[140:150, 320:330]         # PICKING PKM   Canvas coordinates for Red2   Checkpoint 2

    P50 = maskWhite[75:85, 10:20]            # INFO SCREEN   Canvas coordinates for White  Checkpoint 1
    P51 = maskWhite[175:185, 10:20]          # INFO SCREEN   Canvas coordinates for White  Checkpoint 2
    P52 = maskBlack[640:650, 10:20]          # INFO SCREEN   Canvas coordinates for Black  Checkpoint 3
    P53 = maskBlack[640:650, 195:205]        # INFO SCREEN   Canvas coordinates for Black  Checkpoint 4
    P54 = maskBlack[700:710, 635:645]        # INFO SCREEN   Canvas coordinates for Black  Checkpoint 5

    Ptest = maskWhite[0:10, 0:10]

# LLAMADA DE FUNCIONES

    # HIDE CHANGE POKEMON SCREEN

    if checkpoint(P1) and checkpoint(P2) and checkpoint(P3) and checkpoint(P4) is True:

        img = cv2.imread("Recursos/change.png", cv2.IMREAD_UNCHANGED)  # Custom image import with RGB-A (4 Channels)
        imgResized = cv2.resize(img, (1280, 555))                     # Resize "img" to fit the area to hide (RGB-A)
        maskAlpha = imgResized[:, :, 3]                               # Generate alpha mask of "imgResized"
        maskAlphaInv = cv2.bitwise_not(maskAlpha)                     # Generate the inverse of the "maskAlpha"
        imgRGB = imgResized[:, :, 0:3]                                # Convert "imgResized" RGB-A to RGB (3 Channels)

        Recorte = frame[45:600, 0:1280]                                      # Crop the frame to fit the area to hide
        CapaInferior = cv2.bitwise_and(Recorte, Recorte, mask=maskAlphaInv)  # Apply "maskAlphaInv" to "Recorte"
        CapaSuperior = cv2.bitwise_and(imgRGB, imgRGB, mask=maskAlpha)       # Apply "maskAlpha" to "imgRGB"
        dst = cv2.add(CapaInferior, CapaSuperior)                            # Add "Capainferior" + "CapaSuperior"
        frame[45:600, 0:1280] = dst                                          # Draw "dst" in the frame area to hide

    # HIDE MOVE SELECT

    if checkpoint(P10) and checkpoint(P11) and checkpoint(P12) and checkpoint(P13) and checkpoint(P14) is True:

        img = cv2.imread("Recursos/moves.png", cv2.IMREAD_UNCHANGED)  # Custom image import with RGB-A (4 Channels)
        imgResized = cv2.resize(img, (630, 310))                      # Resize "img" to fit the area to hide (RGB-A)
        maskAlpha = imgResized[:, :, 3]                               # Generate alpha mask of "imgResized"
        maskAlphaInv = cv2.bitwise_not(maskAlpha)                     # Generate the inverse of the "maskAlpha"
        imgRGB = imgResized[:, :, 0:3]                                # Convert "imgResized" RGB-A to RGB (3 Channels)

        Recorte = frame[410:720, 650:1280]                                   # Crop the frame to fit the area to hide
        CapaInferior = cv2.bitwise_and(Recorte, Recorte, mask=maskAlphaInv)  # Apply "maskAlphaInv" to "Recorte"
        CapaSuperior = cv2.bitwise_and(imgRGB, imgRGB, mask=maskAlpha)       # Apply "maskAlpha" to "imgRGB"
        dst = cv2.add(CapaInferior, CapaSuperior)                            # Add "Capainferior" + "CapaSuperior"
        frame[410:720, 650:1280] = dst                                       # Draw "dst" in the frame area to hide

    # HIDE TARGET SLOT

    if checkpoint(P20) and checkpoint(P21) and checkpoint(P22) and checkpoint(P23) and \
            (checkpoint(P24) or checkpoint(P25)) is True:

        img = cv2.imread("Recursos/target.png", cv2.IMREAD_UNCHANGED)  # Custom image import with RGB-A (4 Channels)
        imgResized = cv2.resize(img, (630, 275))                      # Resize "img" to fit the area to hide (RGB-A)
        maskAlpha = imgResized[:, :, 3]                               # Generate alpha mask of "imgResized"
        maskAlphaInv = cv2.bitwise_not(maskAlpha)                     # Generate the inverse of the "maskAlpha"
        imgRGB = imgResized[:, :, 0:3]                                # Convert "imgResized" RGB-A to RGB (3 Channels)

        Recorte = frame[225:500, 305:935]                                    # Crop the frame to fit the area to hide
        CapaInferior = cv2.bitwise_and(Recorte, Recorte, mask=maskAlphaInv)  # Apply "maskAlphaInv" to "Recorte"
        CapaSuperior = cv2.bitwise_and(imgRGB, imgRGB, mask=maskAlpha)       # Apply "maskAlpha" to "imgRGB"
        dst = cv2.add(CapaInferior, CapaSuperior)                            # Add "Capainferior" + "CapaSuperior"
        frame[225:500, 305:935] = dst                                        # Draw "dst" in the frame area to hide

    # HIDE MY TEAM BOX

    if checkpoint(P30) and checkpoint(P31) and checkpoint(P32) is True:

        img = cv2.imread("Recursos/team.png", cv2.IMREAD_UNCHANGED)  # Custom image import with RGB-A (4 Channels)
        imgResized = cv2.resize(img, (70, 481))                       # Resize "img" to fit the area to hide (RGB-A)
        maskAlpha = imgResized[:, :, 3]                               # Generate alpha mask of "imgResized"
        maskAlphaInv = cv2.bitwise_not(maskAlpha)                     # Generate the inverse of the "maskAlpha"
        imgRGB = imgResized[:, :, 0:3]                                # Convert "imgResized" RGB-A to RGB (3 Channels)

        Recorte = frame[123:604, 410:480]                                    # Crop the frame to fit the area to hide
        CapaInferior = cv2.bitwise_and(Recorte, Recorte, mask=maskAlphaInv)  # Apply "maskAlphaInv" to "Recorte"
        CapaSuperior = cv2.bitwise_and(imgRGB, imgRGB, mask=maskAlpha)       # Apply "maskAlpha" to "imgRGB"
        dst = cv2.add(CapaInferior, CapaSuperior)                            # Add "Capainferior" + "CapaSuperior"
        frame[123:604, 410:480] = dst                                        # Draw "dst" in the frame area to hide

    # HIDE POKEMON PICKING

    if (checkpoint(P40) and checkpoint(P41)) or (checkpoint(P42) and checkpoint(P43)) is True:

        img = cv2.imread("Recursos/picking.png", cv2.IMREAD_UNCHANGED)  # Custom image import with RGB-A (4 Channels)
        imgResized = cv2.resize(img, (740, 580))                      # Resize "img" to fit the area to hide (RGB-A)
        maskAlpha = imgResized[:, :, 3]                               # Generate alpha mask of "imgResized"
        maskAlphaInv = cv2.bitwise_not(maskAlpha)                     # Generate the inverse of the "maskAlpha"
        imgRGB = imgResized[:, :, 0:3]                                # Convert "imgResized" RGB-A to RGB (3 Channels)

        Recorte = frame[20:600, 380:1120]                                    # Crop the frame to fit the area to hide
        CapaInferior = cv2.bitwise_and(Recorte, Recorte, mask=maskAlphaInv)  # Apply "maskAlphaInv" to "Recorte"
        CapaSuperior = cv2.bitwise_and(imgRGB, imgRGB, mask=maskAlpha)       # Apply "maskAlpha" to "imgRGB"
        dst = cv2.add(CapaInferior, CapaSuperior)                            # Add "Capainferior" + "CapaSuperior"
        frame[20:600, 380:1120] = dst                                        # Draw "dst" in the frame area to hide

    # HIDE INFO BATTLE STATUS (STATS, FIELD, WEATHER)

    if checkpoint(P50) and checkpoint(P51) and checkpoint(P52) and checkpoint(P53) and checkpoint(P54) is True:
        img = cv2.imread("Recursos/info.png", cv2.IMREAD_UNCHANGED)  # Custom image import with RGB-A (4 Channels)
        imgResized = cv2.resize(img, (1280, 555))                     # Resize "img" to fit the area to hide (RGB-A)
        maskAlpha = imgResized[:, :, 3]                               # Generate alpha mask of "imgResized"
        maskAlphaInv = cv2.bitwise_not(maskAlpha)                     # Generate the inverse of the "maskAlpha"
        imgRGB = imgResized[:, :, 0:3]                                # Convert "imgResized" RGB-A to RGB (3 Channels)

        Recorte = frame[45:600, 0:1280]                                      # Crop the frame to fit the area to hide
        CapaInferior = cv2.bitwise_and(Recorte, Recorte, mask=maskAlphaInv)  # Apply "maskAlphaInv" to "Recorte"
        CapaSuperior = cv2.bitwise_and(imgRGB, imgRGB, mask=maskAlpha)       # Apply "maskAlpha" to "imgRGB"
        dst = cv2.add(CapaInferior, CapaSuperior)                            # Add "Capainferior" + "CapaSuperior"
        frame[45:600, 0:1280] = dst                                          # Draw "dst" in the frame area to hide

# Mostrar ventanas


    cv2.imshow("frame", frame)              # SHOW HIDE VGC INFO window
    # cv2.imshow("clean", clean)              # SHOW CLEANFEED window

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
