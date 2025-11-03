"""
prototype of a pac game
"""

import os
import cv2
from typing import Final, Literal

import numpy as np

Direction = Literal["up", "down", "left", "right"]

WINDOW_TITLE = "Pac"
TILE_FILE = os.path.split(__file__)[0] + "/tiles.png"

# constants measured in pixels
SCREEN_SIZE_X, SCREEN_SIZE_Y = 640, 640
TILE_SIZE = 32

# map keyboard keys to move commands
MOVES = {
    "a": "left",
    "d": "right",
    "w": "up",
    "s": "down",
}


def read_images():
    """
    Reads an image with tiles and extracts slices for game elements
    """
    img = cv2.imread(TILE_FILE)
    if img is None:
        raise IOError(f"Image not found: '{TILE_FILE}'")
    # img = np.kron(img, np.ones((2, 2, 1), dtype=img.dtype))  # double image size
    tiles = {
        "wall": img[0:32, 0:32],
        "floor": img[32:64, 0:32],
        "dot": img[64:96, 0:32],
        "player": img[96:128, 0:32],
        "ghost_green": img[128:160, 96:128],
        "ghost_blue": img[160:192, 96:128],
        "ghost_red": img[192:224, 96:128],
        "ghost_pink": img[224:256, 96:128],
    }
    return tiles


def draw_tile(
    frame: np.ndarray, x: int, y: int, tile: str, xbase: int = 0, ybase: int = 0
):
    """convert grid position to screen position in pixels and draw tile"""
    xpos = xbase + x * TILE_SIZE
    ypos = ybase + y * TILE_SIZE
    frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = tile_images[tile]


def draw():
    frame = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)  # empty screen
    draw_tile(frame=frame, x=x, y=y, tile="player")
    draw_tile(frame=frame, x=1, y=2, tile="wall")
    draw_tile(frame=frame, x=2, y=2, tile="dot")
    draw_tile(frame=frame, x=3, y=2, tile="floor")
    draw_tile(frame=frame, x=4, y=2, tile="ghost_green")
    draw_tile(frame=frame, x=5, y=2, tile="ghost_blue")
    draw_tile(frame=frame, x=6, y=2, tile="ghost_red")
    draw_tile(frame=frame, x=7, y=2, tile="ghost_pink")
    cv2.imshow(WINDOW_TITLE, frame)  # display complete image


def move_player(direction: Direction):
    """Things that happen when the player walks on stuff"""
    global x
    global y
    if direction == "right":
        x += 1
    elif direction == "left":
        x -= 1


def handle_keyboard():
    """keys are mapped to move commands"""
    global game_status
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "q":
        game_status = "exited"
    return MOVES.get(key)


game_status: str = "running"
x: int = 1
y: int = 1
tile_images: Final[dict[str, np.ndarray]] = read_images()


def main():
    queued_move = None
    moves = []
    while game_status == "running":
        draw()
        queued_move = handle_keyboard()
        move_player(queued_move)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
