from dataclasses import dataclass, field


@dataclass
class Level:
    name: str
    level: str
    level_matrix: list[list[str]] = field(init=False, repr=False)

    def __post_init__(self):
        self.level_matrix = [list(row) for row in self.level.strip().split()]

    def __repr__(self) -> str:
        return "\n".join(["".join(row) for row in self.level_matrix])


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
