"""
Tetris

Install dependencies:

    pip install opencv-python
"""
import numpy as np
import cv2
import random

ROWS, COLS = 17, 10
TILE_SIZE = 32
SCREEN_SIZE_X, SCREEN_SIZE_Y = COLS * TILE_SIZE, ROWS * TILE_SIZE

# box with three extra layers of wall for rotations and moves
box = np.ones((ROWS + 2, COLS + 4), dtype=np.uint8)
box[:-3, 3:-3] = 0

# definition of bricks
BRICKS = [
    """
.#.
###
...
""", """
.#.
##.
#..
""", """
.#.
.##
..#
""", """
.##
.#.
.#.
""", """
##.
.#.
.#.
""", """
##
##
""", """
..#.
..#.
..#.
..#.
""", """
#.
#.
"""
]
BRICKS = [
    (np.array([list(row) for row in b.strip().split()]) == "#").astype(np.uint8)
    for b in BRICKS
]


# create first brick
brick = random.choice(BRICKS)
x, y = 5, 0

timer = 150
box_full = False
while not box_full:

    # draw everything
    frame = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)
    box_cut = box[:-2, 2:-2]
    bb = np.kron(box_cut, np.ones((TILE_SIZE, TILE_SIZE), dtype=np.uint8)) * 192
    frame[:,:,0] = bb
    frame[:,:,1] = bb
    frame[:,:,2] = bb

    br = np.kron(brick, np.ones((TILE_SIZE, TILE_SIZE), dtype=np.uint8)) * 255
    frame[y*TILE_SIZE:y*TILE_SIZE+br.shape[0], (x-2)*TILE_SIZE:(x-2)*TILE_SIZE+br.shape[1],0] += br

    cv2.imshow("Tetris", frame)

    # handle keyboard input
    key = chr(cv2.waitKey(1) & 0xFF)
    newbrick = brick
    newx, newy = x, y
    if key == "d":
        newx += 1
    elif key == "a":
        newx -= 1
    elif key == "s":
        newy += 1
    elif key == "w":
        newbrick = brick.T[::-1]  # swap x & y, then mirror y
    elif key == "q":
        box_full = True

    # place brick in new position if it does not collide
    check = box.copy()
    check[newy:newy+newbrick.shape[0], newx:newx+newbrick.shape[1]] += newbrick
    if not (check == 2).any():
        brick = newbrick
        x, y = newx, newy

    timer -= 1
    if timer == 0:
        # brick drops automatically
        timer = 150
        y += 1
        check = box.copy()
        check[y:y+brick.shape[0], newx:newx+brick.shape[1]] += brick
        if (check == 2).any():
            # brick stops moving, place it in the box
            if y == 1:
                box_full = True
            y -= 1
            box[y:y+brick.shape[0], newx:newx+brick.shape[1]] += brick

            # remove rows
            for row in range(box.shape[0] - 3):
                if box[row].sum() == box.shape[1]:
                    box[1:row + 1] = box[:row]
                    box[0, 3:-3] = 0

            x, y = 4, 0
            brick = random.choice(BRICKS)

cv2.destroyAllWindows()
