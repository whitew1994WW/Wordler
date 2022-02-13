import unittest
from Wordler import Wordle


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.wordle_class = Wordle.Wordle()

    def test_load_word_list(self):
        self.assertTrue(len(self.wordle_class.valid_guesses) > 5000)

    def test_random_five_letter_word(self):
        word_1 = self.wordle_class.random_five_letter_word()
        word_2 = self.wordle_class.random_five_letter_word()
        self.assertNotEqual(word_2, word_1)

    def test_guess(self):
        # Test input catching
        try:
            self.wordle_class.guess('who')
            self.fail()
        except IOError:
            pass

        try:
            self.wordle_class.guess('zzzzo')
            self.fail()
        except IOError:
            pass

        try:
            self.wordle_class.guess(5)
            self.fail()
        except IOError:
            pass

        # Test running out of guesses
        for i in list(range(7)):
            resp = self.wordle_class.guess('helio')
        self.assertFalse(resp)

        # Test winning
        self.wordle_class = Wordle.Wordle(set_answer_to='helio')
        resp = self.wordle_class.guess('helio')
        self.assertTrue(isinstance(resp, str))

    def test_hard_mode(self):
        self.wordle_class = Wordle.Wordle(set_answer_to='hello', hard_mode=True)
        resp = self.wordle_class.guess('storm')
        resp = self.wordle_class.guess('sprig')
        self.assertFalse(resp)
        resp = self.wordle_class.guess('horny')
        resp = self.wordle_class.guess('phone')
        self.assertFalse(resp)

