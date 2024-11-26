import unittest
from TennisGame import TennisGame

class TestTennisGame(unittest.TestCase):
    def setUp(self):
        self.game = TennisGame("Player 1", "Player 2")

    def test_initial_score(self):
        self.assertEqual(self.game.get_score(), "Love all")

    def test_player_one_scores(self):
        self.game.player_one_scores()
        self.assertEqual(self.game.get_score(), "Fifteen,Love")

    def test_player_two_scores(self):
        self.game.player_two_scores()
        self.assertEqual(self.game.get_score(), "Love,Fifteen")

    def test_deuce(self):
        for _ in range(3):
            self.game.player_one_scores()
            self.game.player_two_scores()
        self.assertEqual(self.game.get_score(), "Deuce")

    def test_advantage(self):
        for _ in range(3):
            self.game.player_one_scores()
            self.game.player_two_scores()
        self.game.player_one_scores()
        self.assertEqual(self.game.get_score(), "Advantage Player 1")

    def test_winner(self):
        for _ in range(4):
            self.game.player_one_scores()
        self.assertEqual(self.game.get_score(), "Player 1 wins")

if __name__ == "__main__":
    unittest.main()
