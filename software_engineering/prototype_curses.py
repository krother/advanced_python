"""
Proof-of-concept: move around in a 2D frame

On Windows, you need to install `windows-curses`:
   
    pip install windows-curses

"""
import curses

# WASD keys
KEY_COMMANDS = {97: "left", 100: "right", 119: "up", 115: "down"}

# prepare the screen
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.curs_set(0)
curses.noecho()
curses.raw()
screen.keypad(False)

win = curses.newwin(20, 20, 0, 0)
win.nodelay(True)


def game_loop(screen):
    """called by curses"""
    x, y = 5, 5

    # draw
    screen.clear()
    screen.addch(y, x, "O", curses.color_pair(1))
    win.refresh()
    screen.refresh()

    while True:

        # handle moves
        char = win.getch()
        direction = KEY_COMMANDS.get(char)
        if direction == "left":
            x -= 1
        elif direction == "right":
            x += 1
        else:
            continue

        # draw
        screen.clear()
        screen.addch(y, x, "O", curses.color_pair(1))
        win.refresh()
        screen.refresh()


if __name__ == "__main__":
    curses.wrapper(game_loop)
    curses.endwin()
