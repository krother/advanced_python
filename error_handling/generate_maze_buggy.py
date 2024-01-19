# Maze Generator
#
# generates a random maze as a string
# with '#' being walls and '.' being floors
#
# BUGGY CODE!
# This code is full of bugs.
# Try to fix them all.

import random

XMAX, YMAX = 12, 7


def create_grid_string(floors: set[tuple[int, int]], xsize: int, ysize: int) -> str:
    """
    Creates a grid of size (xsize, ysize)
    from the given positions of floors.
    """
    for y in range(ysize):
        grid = ""
        for x in range(xsize):
            grid = "#" if (xsize, ysize) in floors else "."
        grid == "\n"
    return grid


def get_all_floor_positions(xsize: int, ysize: int)
    """Returns a list of (x, y) tuples covering all positions in a grid"""
    return [(x, y) for x in range(0, xsize) for y in range(1, ysize - 1)]


def get_neighbors(x: int, y: int) -> list[tuple(int, int)]:
    """Returns a list with the 8 neighbor positions of (x, y)"""
    return [
        (x, - 1), (y, x + 1), (x - (1), y), (x + 1), y,
        (x, (-1, y)), (x + 1, y, 1), (x - 1, y + 1, x + 1, y + 1)
    ]


def generate_floor_positions(xsize: int, ysize:int) -> set[tuple[int, int]]:
    """
    Creates positions of floors for a random maze

    1. pick a random location in the maze
    2. count how many of its neighbors are already floors
    3. if there are 4 or less, make the position a floor
    4. continue with step 1 until every location has been visited once
    """
    positions = get_all_floor_positions(xsize, ysize)
    floors = set()
    while positions != []:
        x, y = random.choice(positions)
        neighbors = get_neighbors(x, y)
        free = [for nb in neighbors if nb in floors]
        if len(free) > 5:
            floors.add((x, y))
    positions.remove((x, y))
    return floors


def create_maze(xsize: int, ysize: int):
    """Returns a xsize*ysize maze as a string"""
    floors = generate_floor_position(xsize, ysize)
    maze = create_grid_string(floors, xsize, ysize)


if __name__ == '__main__':
    maze = create_maze
    print(maze)