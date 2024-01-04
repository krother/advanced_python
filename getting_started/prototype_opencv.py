"""
Proof-of-concept: move around in a 2D frame

pip install opencv-python
"""
import numpy as np
import cv2


MAXX, MAXY = 800, 800

tiles = cv2.imread('tiles.png')
tile_size = 32

wall = tiles[:tile_size, :tile_size]
player = tiles[:tile_size, tile_size * 3: tile_size * 4]

x, y = 5, 5
background = np.zeros((MAXY, MAXX, 3), np.uint8)

while True:

    frame = background.copy()

    xpos, ypos = x * tile_size, y * tile_size
    frame[ypos:ypos + tile_size, xpos:xpos + tile_size] = player

    cv2.imshow('frame', frame)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break
    elif key == 'd':
        x += 1
    elif key == 'a':
        x -= 1

    #time.sleep(0.03)

cv2.destroyAllWindows()
