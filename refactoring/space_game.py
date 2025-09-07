"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""

TEXT = {
    "OPENING_MESSAGE": """
-------------------------------------------------------------------------------

    You and your trusted spaceship set out to look for
    fame, wisdom, and adventure. The stars are waiting for you.
""",
    "EARTH_DESCRIPTION": "\nYou are on Earth. Beautiful is better than ugly.",
    "CENTAURI_DESCRIPTION": "\nYou are on Alpha Centauri. All creatures are welcome here.",
    "HYPERDRIVE_SHOPPING_QUESTION": """There is a brand new hyperdrive with a built-in GPU for sale.
    
Would you like to buy one [yes/no]""",
    "HYPERDRIVE_TOO_EXPENSIVE": """
You cannot afford it. The GPU is too expensive.""",
    "SIRIUS_DESCRIPTION": """
You are on Sirius. The system is full of media companies and content delivery networks.""",
    "SIRIUS_QUIZ_QUESTION": """You manage to get a place in *Stellar* - the greatest quiz show in the universe.
Here is your question:

    Which star do you find on the shoulder of Orion?

[1] Altair
[2] Betelgeuse
[3] Aldebaran
[4] Andromeda
""",
    "SIRIUS_QUIZ_CORRECT": """
*Correct!!!* You win a ton or credits.
""",
    "SIRIUS_QUIZ_INCORRECT": """
Sorry, this was the wrong answer. Don't take it too sirius.
Better luck next time.
""",
    "ORION_DESCRIPTION": """
You are on Orion. An icy world inhabited by furry sentients.""",
    "ORION_HIRE_COPILOT_QUESTION": """A tech-savvy native admires your spaceship.
They promise to join as a copilot if you can answer a question:

    What is the answer to question of life, the universe and everything?
    
What do you answer?""",
    "COPILOT_QUESTION_CORRECT": """
Your new copilot jumps on board and immediately starts
configuring new docker containers.
""",
    "COPILOT_QUESTION_INCORRECT": """
Sorry, that's not it. Try again later.
""",
    "BLACK_HOLE_DESCRIPTION": """
You are close to Black Hole #0997. Maybe coming here was a really stupid idea.
Do you want to examine the black hole closer? [yes/no]
""",
    "BLACK_HOLE_CRUNCHED": """
The black hole condenses your spaceship into a grain of dust.

    THE END
""",
    "BLACK_HOLE_COPILOT_SAVES_YOU": """
On the rim of the black hole your copilot blurts out:

    Turn left!

You ignite the next-gen hyperdrive, creating a time-space anomaly.
You travel through other dimensions and experience wonders beyond description.
""",
    "END_CREDITS": """
    THE END
""",
}


def travel():

    print(TEXT["OPENING_MESSAGE"])

    planet = "earth"
    engines = False
    copilot = False
    credits = False
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
        if planet == "earth":
            destinations = ["centauri", "sirius"]
            print(TEXT["EARTH_DESCRIPTION"])

        if planet == "centauri":
            print(TEXT["CENTAURI_DESCRIPTION"])
            destinations = ["earth", "orion"]

            if not engines:
                print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
                if input() == "yes":
                    if credits:
                        engines = True
                    else:
                        print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])

        if planet == "sirius":
            print(TEXT["SIRIUS_DESCRIPTION"])
            destinations = ["orion", "earth", "black_hole"]

            if not credits:
                print(TEXT["SIRIUS_QUIZ_QUESTION"])
                answer = input()
                if answer == "2":
                    print(TEXT["SIRIUS_QUIZ_CORRECT"])
                    credits = True
                else:
                    print(TEXT["SIRIUS_QUIZ_INCORRECT"])

        if planet == "orion":
            destinations = ["centauri", "sirius"]
            if not copilot:
                print(TEXT["ORION_DESCRIPTION"])
                print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
                if input() == "42":
                    print(TEXT["COPILOT_QUESTION_CORRECT"])
                    copilot = True
                else:
                    print(TEXT["COPILOT_QUESTION_INCORRECT"])
            else:
                print(TEXT["ORION_DESCRIPTION"])

        if planet == "black_hole":
            print(TEXT["BLACK_HOLE_DESCRIPTION"])
            destinations = ["sirius"]
            if input() == "yes":
                if engines and copilot:
                    print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
                    game_end = True
                else:
                    print(TEXT["BLACK_HOLE_CRUNCHED"])
                    return

        if not game_end:
            # select next planet
            print("\nWhere do you want to travel?")
            position = 1
            for d in destinations:
                print(f"[{position}] {d}")
                position += 1

            choice = input()
            planet = destinations[int(choice) - 1]

    print(TEXT["END_CREDITS"])


if __name__ == "__main__":
    travel()
