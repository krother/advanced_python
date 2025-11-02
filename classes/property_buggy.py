"""
the program contains 3 bugs
"""
class Game:

    name = "Pac using OpenCV"

    level: list[str] = (
        "######"
        "#....#"
        "#....#"
        "#....#"
        "######"        
    )

    @property
    def remaining_dots(self) -> int:
        return sum(
            [row.count(".") for row in self.level]
        )

    @property
    def finished(self):
        return self.remaining_dots > 0
    
    @classmethod
    def get_name(cls):
        return cls.name
    
    @staticmethod
    def version():
        return "1.0"


game = Game()

print(game.get_name())
print("version", game.version)
print("dots remaining:", game.remaining_dots)
print("finished:", game.finished)
