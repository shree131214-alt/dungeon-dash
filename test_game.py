import unittest
from unittest.mock import patch

from main import play_round


class PlayRoundTests(unittest.TestCase):
    @patch("main.random.choice", return_value="spell")
    @patch("builtins.input", return_value="1")
    def test_sword_beats_spell(self, _input, _choice):
        self.assertEqual(play_round(), 1)

    @patch("main.random.choice", return_value="sword")
    @patch("builtins.input", return_value="1")
    def test_matching_moves_draw(self, _input, _choice):
        self.assertEqual(play_round(), 0)

    @patch("main.random.choice", return_value="sword")
    @patch("builtins.input", return_value="2")
    def test_shield_beats_sword(self, _input, _choice):
        self.assertEqual(play_round(), 1)

    @patch("main.random.choice", return_value="spell")
    @patch("builtins.input", side_effect=["x", "2"])
    def test_invalid_input_is_retried(self, _input, _choice):
        self.assertEqual(play_round(), -1)


if __name__ == "__main__":
    unittest.main()
