from typing import Annotated
from pydantic import BaseModel, BeforeValidator, ValidationError


def parse_level(level: str) -> list[list[str]]:
    return [list(row) for row in level.strip().split()]


class Level(BaseModel):
    name: str
    level: Annotated[list[list[str]], BeforeValidator(parse_level)]

    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self.level)

    class Config:
        extra = "forbid"  # Disallow unknown fields


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
#############""", # type: ignore
)

print(level_one)
