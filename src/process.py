import cv2

from colors import *



def process(frame, covers):
    
    # Transform and manipulate frame
    blurred_frame = cv2.GaussianBlur(frame, (7,7),1)            # Apply blur
    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)  # Conversion to HSV colors

    mask_yellow = cv2.inRange(hsv_frame, yellow_min, yellow_max)

    process_moves(frame, mask_yellow, covers["moves"])
    process_targets(frame, mask_yellow, covers["target"])
    process_changepokemon(frame, mask_yellow, covers["changepkmn"])


def process_moves(frame, mask, cover):
    move_min_pixels = 200
    move_1 = mask[445:465, 940:960]
    move_2 = mask[520:540, 940:960]
    move_3 = mask[595:615, 940:960]
    move_4 = mask[670:690, 940:960]

    if( 
        checkpoint(move_1, move_min_pixels) == True or
        checkpoint(move_2, move_min_pixels) == True or 
        checkpoint(move_3, move_min_pixels) == True or 
        checkpoint(move_4, move_min_pixels) == True 
    ):
        # cv2.rectangle(frame, (750,300),(1260,700),(255,0,255),cv2.LINE_4)
        frame[300:700, 750:1260] = cover


def process_targets(frame, mask, cover):
    target_min_pixels = 4500
    target_top_left = mask[95:320, 435:635]
    target_top_right = mask[95:320, 650:850]
    target_bottom_left = mask[375:600, 435:635]
    target_bottom_right = mask[375:600, 650:850]

    if(
        checkpoint(target_top_left, target_min_pixels) == True or
        checkpoint(target_top_right, target_min_pixels) == True or
        checkpoint(target_bottom_left, target_min_pixels) == True or
        checkpoint(target_bottom_right, target_min_pixels) == True
    ):
        # cv2.rectangle(frame, (420,25),(865,620),(255,0,255),cv2.LINE_4)
        frame[25:620, 420:865] = cover


def process_changepokemon(frame, mask, cover):
    pokemon_1 = mask[115:125, 337:347]
    pokemon_2 = mask[198:208, 337:347]
    pokemon_3 = mask[282:292, 337:347]
    pokemon_4 = mask[366:376, 337:347]

    if(
        checkpoint(pokemon_1) == True or
        checkpoint(pokemon_2) == True or
        checkpoint(pokemon_3) == True or
        checkpoint(pokemon_4) == True
    ):
        # cv2.rectangle(frame, (30,70),(1260,620),(255,0,255),cv2.LINE_4)
        frame[70:620, 30:1260] = cover


# Check if enough colored pixels are in the selected area
def checkpoint(masked_area, min_pixels=30):
    pixels = cv2.countNonZero(masked_area)
    return pixels > min_pixels


# NOTE: DON'T USE THIS FUNCTION, THIS IS A PLACEHOLDER NOT TO LOSE SWOSHI MASKS
# I'LL ADD A SWOSHI-MODE IN THE FUTURE AND FIX THIS
def swoshi_masks():
    #Detectar color sobre el hsv_frame y crear una máscara con cada color
    maskWhite = cv2.inRange(hsv_frame, blanco_min, blanco_max)           # White tone detection mask - for HP BOX and CHANGE SCREEN
    maskDinamax = cv2.inRange(hsv_frame, dinamax_min, dinamax_max)       # Red tone detection mask   - for HP BOX
    maskGrey2 = cv2.inRange(hsv_frame, gris2_min, gris2_max)             # Grey tone detection mask  - for CHANGE SCREEN
    maskGreen = cv2.inRange(hsv_frame, verde_min, verde_max)             # Green tone detection mask - for HP BAR
    maskGrey = cv2.inRange(hsv_frame, gris_min, gris_max)                # Grey tone detection mask  - for HP BAR
    maskBlack = cv2.inRange(hsv_frame, negro_min, negro_max)             # Black tone detection mask - for MOVES

    return maskWhite, maskDinamax, maskGrey2, maskGreen, maskGrey, maskBlack