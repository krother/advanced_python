"""
Breakout

Install dependencies:

    pip install opencv-python pydantic

(c) 2024 Dr. Kristian Rother
"""
import numpy as np
import cv2
import random
from pydantic import BaseModel

BR_ROWS, ROWS, COLS = 5, 20, 12
TILE_SIZE_Y, TILE_SIZE_X = 32, 64
SCREEN_SIZE_X, SCREEN_SIZE_Y = COLS * TILE_SIZE_X, ROWS * TILE_SIZE_Y

FRAME_SPEED = 10
MOVE_SPEED = 3


def ticker(speed: int):
    counter = speed
    while True:
        for _ in range(counter):
            yield False
        yield True


class Ball(BaseModel):
    x: int
    y: int
    dx: int = 0
    dy: int = 0
    size: int = 16
    docked: bool = True

    def start(self):
        if self.docked:
            self.dx = -2
            self.dy = -2
            self.docked = False

    def move(self, paddle, bricks, background):
        self.x += self.dx
        self.y += self.dy
        self.check_border()
        self.hit_paddle(paddle)
        self.hit_brick(bricks, background)

    def check_border(self):
        if self.y <= 0:
            self.y = 0
            self.dy = -self.dy
        if self.x <= 0:
            self.x = 0
            self.dx = -self.dx
        if self.x >= SCREEN_SIZE_X - 16:
            self.x = SCREEN_SIZE_X - 16
            self.dx = -self.dx

    def hit_paddle(self, paddle):
        if (
            self.y == paddle.y - 16
            and self.x >= paddle.x - 16
            and self.x < paddle.x + paddle.width
        ):
            self.dy = random.choice([-1, -2])
            self.dx = self.dx // abs(self.dx) * random.choice([1, 2, 3])

    def hit_brick(self, bricks, background):
        xx, yy = self.x // TILE_SIZE_X, self.y // TILE_SIZE_Y
        if xx < COLS and yy < BR_ROWS and bricks[yy, xx] == 1:
            self.dx *= random.choice([-1, 1])
            self.dy *= -1
            bricks[yy, xx] = 0
            background[
                yy * TILE_SIZE_Y : (yy + 1) * TILE_SIZE_Y,
                xx * TILE_SIZE_X : (xx + 1) * TILE_SIZE_X,
                :,
            ] = 0


class Paddle(BaseModel):
    x: int
    y: int
    width: int
    height: int = 16
    speed: int

    def move(self, ball, dx):
        self.x += dx
        if ball.docked:
            ball.x += dx

    def right(self, ball):
        if self.x < SCREEN_SIZE_X - self.width - self.speed:
            self.move(ball, self.speed)

    def left(self, ball):
        if self.x >= self.speed:
            self.move(ball, -self.speed)


def draw(background, paddle, ball):
    frame = background.copy()
    frame[
        paddle.y : paddle.y + paddle.height, paddle.x : paddle.x + paddle.width, :
    ] = 128
    frame[ball.y : ball.y + ball.size, ball.x : ball.x + ball.size, :] = 255
    cv2.imshow("Breakout", frame)


bricks = np.ones((BR_ROWS, COLS), dtype=np.uint8)
background = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)

# draw the bricks
background[TILE_SIZE_Y * 0 : TILE_SIZE_Y * 1, :] = (0, 0, 255)
background[TILE_SIZE_Y * 1 : TILE_SIZE_Y * 2, :] = (0, 128, 255)
background[TILE_SIZE_Y * 2 : TILE_SIZE_Y * 3, :] = (0, 255, 255)
background[TILE_SIZE_Y * 3 : TILE_SIZE_Y * 4, :] = (0, 255, 0)
background[TILE_SIZE_Y * 4 : TILE_SIZE_Y * 5, :] = (255, 0, 0)

ball = Ball(x=425, y=600 - 16)
paddle = Paddle(x=400, y=600, width=100, speed=16)

frame_tick = ticker(FRAME_SPEED)
move_tick = ticker(MOVE_SPEED)

while bricks.sum() > 0 and ball.y < SCREEN_SIZE_Y:
    # draw everything
    if next(frame_tick):
        draw(background, paddle, ball)

    # handle keyboard input
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "a":
        paddle.left(ball)
    elif key == "d":
        paddle.right(ball)
    elif key == " ":
        ball.start()
    elif key == "q":
        break

    if next(move_tick) and not ball.docked:
        ball.move(paddle, bricks, background)

cv2.destroyAllWindows()
