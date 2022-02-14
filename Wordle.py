import csv
import random


class Wordle:
    _valid_guesses_filename = "../data/valid_guesses.csv"
    _valid_solutions_filename = "../data/valid_solutions.csv"
    valid_guesses = {}
    valid_solutions = {}

    def __init__(self, hard_mode=False, set_answer_to=''):
        self.guess_history = {}
        self.guess_score_history = {}
        self.greyed_letters = []
        self.hard_mode = hard_mode
        self.valid_guesses, self.valid_solutions = Wordle.load_word_list()
        if set_answer_to:
            self._answer = set_answer_to
            self._guesses_left = 6
        else:
            self.reset_wordle()

    @staticmethod
    def load_word_list():
        with open(Wordle._valid_guesses_filename) as infile:
            reader = csv.reader(infile)
            valid_guesses = {rows[0]: 0 for rows in reader}

        with open(Wordle._valid_solutions_filename) as infile:
            reader = csv.reader(infile)
            valid_solutions = {rows[0]: 0 for rows in reader}
        return valid_guesses, valid_solutions

    def guess(self, current_guess):
        # Check word is the correct format
        if not isinstance(current_guess, str):
            raise IOError("Word MUST be in string format")

        if not len(current_guess) == 5:
            raise IOError("Input word MUST be 5 letters long")

        if self._guesses_left == 0:
            print("You have run out of guesses! Pick a new word")
            return False

        if current_guess not in self.valid_guesses.keys() and \
                current_guess not in self.valid_solutions.keys():
            raise IOError("Input word must be in word list")

        if self._guesses_left == 6:
            pass
        elif not self.check_valid_hard_mode_word(current_guess):
            print("You are playing HARD MODE! You must include previous AMBER or GREEN words")
            return False

        # Score each letter in the word
        guess_score = {}
        for idx in range(5):
            guess_score[idx] = 'GREY'
            if current_guess[idx] in self._answer:
                guess_score[idx] = 'AMBER'
            else:
                self.greyed_letters.append(current_guess[idx])

            if current_guess[idx] == self._answer[idx]:
                guess_score[idx] = 'GREEN'

        # Update guess history
        self.guess_score_history[7 - self._guesses_left] = guess_score
        self.guess_history[7 - self._guesses_left] = current_guess

        # Check win conditions
        if self.check_word_guessed():
            old_answer = self._answer
            self.reset_wordle()
            return f"Well done you have correctly guessed the word as {old_answer}!! \nThere is now a new word for you to guess..."

        self._guesses_left -= 1

        return guess_score

    def random_five_letter_word(self):
        random_word = random.choice(list(self.valid_solutions))
        return random_word

    def check_word_guessed(self):
        current_guess_score = self.guess_score_history[7 - self._guesses_left]
        for score in list(current_guess_score.values()):
            if score != 'GREEN':
                return False
        return True

    def reset_wordle(self):
        self._answer = self.random_five_letter_word()
        self._guesses_left = 6
        self.guess_history = {}
        self.greyed_letters = []

    def get_used_words(self):
        return

    def check_valid_hard_mode_word(self, current_guess):
        if self.hard_mode:
            previous_guess = self.guess_history[6 - self._guesses_left]
            previous_guess_score = self.guess_score_history[6 - self._guesses_left]
            for idx in list(range(5)):
                if previous_guess_score[idx] == 'AMBER':
                    if previous_guess[idx] not in current_guess:
                        return False
                elif previous_guess_score[idx] == 'GREEN':
                    if previous_guess[idx] != current_guess[idx]:
                        return False
        return True
