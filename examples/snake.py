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
    "a": (-1, 0),
    "d": (1, 0),
    "w": (0, -1),
    "s": (0, 1),
}

RAINBOW = [
    (0, 0, 255),
    (0, 128, 255),
    (0, 255, 255),
    (0, 255, 0),
    (255, 0, 0),
    (255, 0, 255),
]


def ticker(speed: int):
    counter = speed
    while True:
        for _ in range(counter):
            yield False
        yield True


Color = tuple[int, int, int]

class Food(BaseModel):
    position: tuple[int, int]
    color: Color


class Snake(BaseModel):
    tail: list[tuple[int, int]] = []
    colors: list[Color]
    direction: str = (1, 0)

    @property
    def head(self):
        return self.tail[0]

    def move(self, food):
        x, y = self.head
        dx, dy = self.direction
        new_head = x + dx, y + dy
        self.tail.insert(0, new_head)
        if new_head != food.position:
            self.tail.pop()
        else:
            self.colors.insert(0, food.color)

    def collides(self):
        return (
            self.head in self.tail[1:]
            or self.head[0] < 0
            or self.head[1] < 0
            or self.head[0] == COLS
            or self.head[1] == ROWS
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

frame_tick = ticker(FRAME_SPEED)
move_tick = ticker(MOVE_SPEED)

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
