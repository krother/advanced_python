Tennis
======

**🎯 Write a class ``TennisGame`` that determines the score of a round of tennis.**

Use the following structure:

.. code:: python3

   class TennisGame:

       def __init__(self):
           self.score = {
               'player1': 0,
               'player2': 0,
           }

       def point(self, player: str) -> None:
           """called with 'player1' or 'player2' to record points"""
           self.scores[player] += 1

       def get_score(self) -> str:
           """calculates the score"""
           ...


.. topic:: Rules

   1. The first player with at least four points and two points more than the opponent wins.
   2. The score is then *"Win Player 1"* or *"Win Player 2"*.
   3. The current score in tennis is somewhat peculiar: points from 0 to 3 are described with *"love", "fifteen", "thirty" and "forty"*.
   4. If both players have at least three points, the score with equal points is *"deuce"*.
   5. If both players have at least three points, the score will be *"Advantage Player 1"* or *"Advantage Player 2"* depending on which player has more points.

*Translated with*\ `www.DeepL.com <www.DeepL.com/Translator>`__
