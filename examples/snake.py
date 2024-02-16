"""
Snake

Install dependencies:

    pip install opencv-python pydantic

(c) 2024 Dr. Kristian Rother
"""
import numpy as np
import cv2
from itertools import cycle
from random import randint
from pydantic import BaseModel

ROWS, COLS = 14, 20
TILE_SIZE = 32
SCREEN_SIZE_X = COLS * TILE_SIZE
SCREEN_SIZE_Y = ROWS * TILE_SIZE

FRAME_SPEED = 10
MOVE_SPEED = 100

MOVES = {
    "a": (-1, 0),  # left
    "d": (1, 0),   # right
    "w": (0, -1),  # up
    "s": (0, 1),   # down
}

RAINBOW = [
    (0, 0, 255),  # BGR - blue, green red
    (0, 128, 255),
    (0, 255, 255),
    (0, 255, 0),
    (255, 0, 0),
    (255, 0, 255),
]


Color = tuple[int, int, int]
Position = tuple[int, int]


class Food(BaseModel):
    position: Position
    color: Color


class Snake(BaseModel):
    tail: list[Position] = []  # the tail is a queue
    colors: list[Color] = []
    direction: Position = (1, 0)

    @property   # decorator: allows us to use .head like an attribute
    def head(self):
        return self.tail[0]

    def move(self, food):
        x, y = self.head           # calls the function automatically
        dx, dy = self.direction    # unpack a tuple into two variables
        new_head = x + dx, y + dy  # create a new position tuple
        self.tail.insert(0, new_head)
        if new_head != food.position:
            self.tail.pop()
        else:
            self.colors.insert(0, food.color)

    def collides(self):
        x, y = self.head
        return (
            self.head in self.tail[1:]
            or x < 0
            or y < 0
            or x == COLS
            or y == ROWS
        )


def draw(snake, food):
    frame = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)
    for (fx, fy), col in zip(snake.tail, snake.colors):
        frame[
            fy * TILE_SIZE : (fy + 1) * TILE_SIZE - 1,
            fx * TILE_SIZE : (fx + 1) * TILE_SIZE - 1,
            :,
        ] = col
    fx, fy = food.position
    frame[
        fy * TILE_SIZE : (fy + 1) * TILE_SIZE, fx * TILE_SIZE : (fx + 1) * TILE_SIZE, :
    ] = food.color
    cv2.imshow("Snake", frame)


color_gen = cycle(RAINBOW)

snake = Snake(tail=[(5, 5)], colors=[(255, 0, 255)])
food = Food(position=(10, 5), color=next(color_gen))

frame_tick = cycle([True] + [False] * FRAME_SPEED)
move_tick = cycle([True] + [False] * MOVE_SPEED)

while not snake.collides():
    # draw everything
    if next(frame_tick):
        draw(snake, food)

    # handle keyboard input
    key = chr(cv2.waitKey(1) & 0xFF)
    if key in MOVES:
        snake.direction = MOVES[key]
    elif key == "q":
        break

    if next(move_tick):
        snake.move(food)

    if snake.head == food.position:
        food = Food(
            position=(randint(1, COLS - 1), randint(1, ROWS - 1)),
            color=next(color_gen)
        )

cv2.destroyAllWindows()
