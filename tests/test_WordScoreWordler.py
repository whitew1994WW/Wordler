import unittest
from Wordler.models.WordScoreWordler import WordScoreWordler
from Wordler.evaluate_worlder_algorithm import evaluate_wordler
import random


class TestWordScoreWordler(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_learn_ranking(self):
        wordler = WordScoreWordler(train=True)

    def test_evaluate_wordler(self):
        random.seed(1)
        score1, score2 = evaluate_wordler(WordScoreWordler())
        print(score1, score2)


if __name__ == '__main__':
    unittest.main()
