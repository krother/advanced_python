class Level:

    def __init__(self, name: str, level: str):
        self.name = name
        self.level = [list(row) for row in level.strip().split()]

    def __repr__(self) -> str:
        return "\n".join(["".join(row) for row in self.level])


level_one = Level(
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
print(level_one)
