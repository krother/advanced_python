"""
Proof-of-concept: move around on a 2D grid

Install dependencies:

    pip install numpy opencv-python
"""
import numpy as np
import cv2


# constants measured in pixel
SCREEN_SIZE_X, SCREEN_SIZE_Y = 800, 800
TILE_SIZE = 32

# load image and extract square tiles from it
tiles = cv2.imread('tiles.png')
wall = tiles[:TILE_SIZE, :TILE_SIZE]
player = tiles[:TILE_SIZE, TILE_SIZE * 3: TILE_SIZE * 4]

# define boundaries of the 2D grid
min_x, max_x = 0, SCREEN_SIZE_X // TILE_SIZE
min_y, max_y = 0, SCREEN_SIZE_Y // TILE_SIZE

# NumPy array used as background (BGR color channels)
background = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)

# starting position of the player
x, y = 5, 5

while True:

    # draw
    frame = background.copy()
    xpos, ypos = x * TILE_SIZE, y * TILE_SIZE
    frame[ypos:ypos + TILE_SIZE, xpos:xpos + TILE_SIZE] = player
    cv2.imshow('frame', frame)

    # handle keyboard input
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break
    elif key == 'd':
        x += 1
    elif key == 'a':
        x -= 1

cv2.destroyAllWindows()
