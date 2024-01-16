"""
Proof-of-concept: move around on a 2D grid

Install dependencies:

    pip install opencv-python
"""
import numpy as np
import cv2


# constants measured in pixel
SCREEN_SIZE_X, SCREEN_SIZE_Y = 640, 640
TILE_SIZE = 64



def read_image(filename):
    """returns an image twice as big"""
    img = cv2.imread(filename)
    return np.kron(img, np.ones((2, 2, 1), dtype=img.dtype))


player_img = read_image("tiles/deep_elf_high_priest.png")

def draw(x, y):
    """draws the player image on the screen"""
    frame = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)
    xpos, ypos = x * TILE_SIZE, y * TILE_SIZE
    frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = player_img
    cv2.imshow("frame", frame)


# starting position of the player in dungeon
x, y = 4, 4

exit_pressed = False

while not exit_pressed:
    draw(x, y)

    # handle keyboard input
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "d":
        x += 1
    elif key == "a":
        x -= 1
    elif key == "q":
        exit_pressed = True

cv2.destroyAllWindows()
