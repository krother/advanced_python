
# Tennis

**🎯 Write a class `TennisGame` that determines the score of a round of tennis..**

* The score should be calculated by the method `get_score()` as a string
* The referee calls either `point('player1')` or `point('player2')`.

Use the following structure:

    class TennisGame:

        def __init__(self):
            self.score = {'player1': 0, 'player2': 0}

        def point(self, player):
            """called with 'player1' or 'player2'"""
            self.scores[player] += 1

        def get_score(self):
            ...

## Rules

1. The first player with at least four points and two points more than the opponent wins. The score is then *"Win Player 1"* or *"Win Player 2"*.
2. The current score in tennis is somewhat peculiar: points from 0 to 3 are described with *"love", "fifteen", "thirty" and "forty"*.
3. If both players have at least three points, the score with equal points is *"deuce"*.
4. If both players have at least three points, the score will be *"Advantage Player 1"* or *"Advantage Player 2"* depending on which player has more points.


*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
