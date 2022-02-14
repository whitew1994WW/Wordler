import random
import unittest
from Wordler.Wordle import Wordle
from Wordler.models.NaiveWordler import NaiveWordler
from Wordler.evaluate_worlder_algorithm import evaluate_wordler

class TestNaiveWordler(unittest.TestCase):
    def test_wordler(self):
        wordle_game = Wordle(set_answer_to="hello")
        wordler = NaiveWordler()
        guess = wordler.get_first_word()
        for i in range(6):
            score = wordle_game.guess(guess)
            if not isinstance(score, str):
                guess = wordler.get_next_word(score)
            else:
                break

    def test_evaluate_wordler(self):
        random.seed(1)
        score1, score2 = evaluate_wordler(NaiveWordler())
        print(score1, score2)





if __name__ == '__main__':
    unittest.main()
