"""
Space Travel Game

A simple text adventure written for Python tutorials.
"""

from text import TEXT
from planets import Planet, planets


def travel():

    print(TEXT["OPENING_MESSAGE"])

    planet : Planet = planets["earth"]
    engines, copilot, credits = False, False, False
    game_end = False

    while not game_end:

        # display inventory
        print("-" * 79)
        inventory = "\nYou have: "
        inventory += "plenty of credits, " if credits else ""
        inventory += "a hyperdrive, " if engines else ""
        inventory += "a skilled copilot, " if copilot else ""
        if inventory.endswith(", "):
            print(inventory.strip(", "))

        #
        # interaction with planets
        #
        print(planet.description)

        # TODO: move puzzles to separate functions
        if planet.name == "centauri":
            if not engines:
                print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
                if input() == "yes":
                    if credits:
                        engines = True
                    else:
                        print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])

        elif planet.name == "sirius":
            if not credits:
                print(TEXT["SIRIUS_QUIZ_QUESTION"])
                answer = input()
                if answer == "2":
                    print(TEXT["SIRIUS_QUIZ_CORRECT"])
                    credits = True
                else:
                    print(TEXT["SIRIUS_QUIZ_INCORRECT"])

        elif planet.name == "orion":
            if not copilot:
                print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
                if input() == "42":
                    print(TEXT["COPILOT_QUESTION_CORRECT"])
                    copilot = True
                else:
                    print(TEXT["COPILOT_QUESTION_INCORRECT"])

        elif planet.name == "black_hole":
            if input() == "yes":
                if engines and copilot:
                    print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
                    game_end = True
                else:
                    print(TEXT["BLACK_HOLE_CRUNCHED"])
                    return

        if not game_end:
            print("\nWhere do you want to travel?")
            position = 1
            for d in planet.connections:
                print(f"[{position}] {d.name}")
                position += 1
            # TODO: use Planet.show_connections instead

            choice = input()
            # TODO: add input validation
            # if is_choice_valid(choice):
            planet = planet.connections[int(choice) - 1]

    print(TEXT["END_CREDITS"])


if __name__ == "__main__":
    travel()
