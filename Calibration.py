import device
import numpy as np
import cv2


def choose_capturecard():
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


def checkpoint(my_frame, value):
    contornos, hierarchy = cv2.findContours(my_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contornos:
        area = cv2.contourArea(cnt)
        if area > value:
            # cv2.drawContours(frame, cnt, -1, (255, 0, 0), 3)
            return True
        else:
            return False


def show_preview(sample_image):
    simg = cv2.imread('Recursos/SampleImages/' + sample_image + '.jpg', cv2.IMREAD_UNCHANGED)
    simg_resized = cv2.resize(simg, (480, 270))
    separator = cv2.imread('Recursos/SampleImages/separator.jpg', cv2.IMREAD_UNCHANGED)
    title = cv2.imread('Recursos/SampleImages/title.jpg', cv2.IMREAD_UNCHANGED)

    while True:
        success, frame = capture.read()
        frame_resized = cv2.resize(frame, (480, 270))

        horizontal = np.concatenate((frame_resized, separator, simg_resized), axis=1)
        vertical = np.concatenate((title, horizontal), axis=0)

        cv2.namedWindow('Calibrating: ' + sample_image + ' screen', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Calibrating: ' + sample_image + ' screen', 966, 334)
        cv2.moveWindow('Calibrating: ' + sample_image + ' screen', 40, 30)
        cv2.imshow('Calibrating: ' + sample_image + ' screen', vertical)  # SHOW MASK window

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.destroyAllWindows()
            break


def calibrate_points(*points):

    Hmin = 0
    Hmax = 179
    Smin = 0
    Smax = 255
    Vmin = 0
    Vmax = 255

    start = 0

    while True:

        success, frame = capture.read()

        FrameBlur = cv2.GaussianBlur(frame, (7, 7), 1)  # Difuminar el Frame
        FrameHSV = cv2.cvtColor(FrameBlur, cv2.COLOR_BGR2HSV)  # Conversión de color del Frame a gama de color HSV

        lower = np.array([Hmin, Smin, Vmin])
        upper = np.array([Hmax, Smax, Vmax])

        mask = cv2.inRange(FrameHSV, lower, upper)

        for a in points:
            my_point = mask[a[0]:a[1], a[2]:a[3]]
            if checkpoint(my_point, 30) is True:
                pass
            else:
                start += 1
                break

        if start == 0:
            Vmax -= 1
            print('Vmax: ' + str(Vmax))

        elif start == 1:
            Vmax += 30
            if Vmax > 255:
                Vmax = 255
            print('Final Vmax: ' + str(Vmax))
            start += 1

        elif start == 2:
            Vmin += 1
            print('Vmin: ' + str(Vmin))

        elif start == 3:
            Vmin -= 30
            if Vmin < 0:
                Vmin = 0
            print('Final Vmin: ' + str(Vmin))
            start += 1

        elif start == 4:
            Smax -= 1
            print('Smax: ' + str(Smax))

        elif start == 5:
            Smax += 30
            if Smax > 255:
                Smax = 255
            print('Final Smax: ' + str(Smax))
            start += 1

        elif start == 6:
            Smin += 1
            print('Smin: ' + str(Smin))

        elif start == 7:
            Smin -= 30
            if Smin < 0:
                Smin = 0
            print('Final Smin: ' + str(Smin))
            start += 1

        elif start == 8:
            Hmax -= 1
            print('Hmax: ' + str(Hmax))

        elif start == 9:
            Hmax += 30
            if Hmax > 179:
                Hmax = 179
            print('Final Hmax: ' + str(Hmax))
            start += 1

        elif start == 10:
            Hmin += 1
            print('Hmin: ' + str(Hmin))

        elif start == 11:
            Hmin -= 30
            if Hmin < 0:
                Hmin = 0
            print('Final Hmin: ' + str(Hmin))
            start += 1

        cv2.namedWindow('Calculating...', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Calculating...', 480, 270)
        cv2.moveWindow('Calculating...', 40, 30)
        cv2.imshow('Calculating...', mask)  # SHOW MASK window

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            capture.release()
            break

        if start == 12:
            print('Hmin: ' + str(Hmin) + ' Smin: ' + str(Smin) + ' Vmin: ' + str(Vmin))
            print('Hmax: ' + str(Hmax) + ' Smax: ' + str(Smax) + ' Vmax: ' + str(Vmax))

            cv2.destroyAllWindows()
            lista = (Hmin, Hmax, Smin, Smax, Vmin, Vmax)

            return lista


def savedata(file_name, mylist):
    coma = ','
    myvalues = map(str, mylist)
    final = coma.join(myvalues)
    with open('Recursos/' + file_name + '.txt', "w+") as file:
        file.write(final)


# DECLARACION DE VARIABLES
P11 = (140, 150, 80, 90)      # PICKING SCREEN Canvas coordinates for Red - Checkpoint A
P12 = (140, 150, 320, 330)    # PICKING SCREEN Canvas coordinates for Red - Checkpoint A

P21 = (15, 30, 1220, 1240)    # CHANGE SCREEN Canvas coordinates for Red - Checkpoint B
P22 = (15, 30, 1130, 1150)    # CHANGE SCREEN Canvas coordinates for Red - Checkpoint B

P81 = (100, 110, 215, 230)    # MY TEAM BOX SCREEN Canvas coordinates for Blue - Checkpoint H
P82 = (100, 110, 450, 465)    # MY TEAM BOX SCREEN Canvas coordinates for Blue - Checkpoint H


# PROGRAMA
capture = cv2.VideoCapture(choose_capturecard(), cv2.CAP_DSHOW)
capture.set(3, 1280)
capture.set(4, 720)

# Picking Screen - Red Calibration
show_preview('Picking')
result = calibrate_points(P11, P12)
savedata('Picking-Red', result)

# Team Screen - Blue Calibration
show_preview('team')
result = calibrate_points(P81, P82)
savedata('Team-Blue', result)

# Change Screen - Red Calibration
show_preview('Change')
result = calibrate_points(P21, P22)
savedata('Change-Red', result)

capture.release()

print()
input('Finished!! Press enter to exit')
