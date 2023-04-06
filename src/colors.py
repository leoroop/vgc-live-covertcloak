import numpy as np

# SWORD AND SHIELD DEFINITIONS

white_min = np.array([0, 0, 210])          # White tone HP Box
white_max = np.array([179, 85, 255])       # White tone HP Box

grey_min = np.array([0, 0, 0])              # Grey tone HP Bar
grey_max = np.array([179, 255, 170])        # Grey tone HP Bar

grey2_min = np.array([0, 0, 64])            #Grey tone Change screen
grey2_max = np.array([179, 65, 134])        #Grey tone Change screen

green_min = np.array([35, 160, 169])        # Green tone HP Bar
green_max = np.array([72, 255, 255])        # Green tone HP Bar

dynamax_min = np.array([0,127,215])         # Red tone HP dinamax box
dynamax_max = np.array([179,255,255])       # Red tone HP dinamax box

black_min = np.array([0,0,0])               # Black tone ingame boxes
black_max = np.array([179,255,50])          # Black tone ingame boxes


# NEW COLORS FOR SCARLET AND VIOLET

yellow_min = np.array([22, 93, 230])
yellow_max = np.array([45, 255, 255]) 