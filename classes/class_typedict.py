from typing import TypedDict, List


class Level(TypedDict):
    name: str
    level: List[List[str]]


def create_level(name: str, level: str) -> Level:
    level_matrix = [list(row) for row in level.strip().split()]
    return Level(name=name, level=level_matrix)


def print_level(level: Level) -> None:
    print("\n".join("".join(row) for row in level["level"]))


level_one = create_level(
    name="empty level",
    level="""
#############
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#############""",
)
print(level_one["name"])
print_level(level_one)
print(type(level_one))
