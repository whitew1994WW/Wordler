"""
Most Basic Wordler

Always reuses previous green and yellow letters.
Always tries yellow letters in different locations.
Never reuses grey letters.
"""

from Wordler.Wordle import Wordle
import random
import copy


class NaiveWordler:
    def __init__(self):
        random.seed(1)
        self.reset_wordler()

    def get_first_word(self):
        random.shuffle(self.possible_words)
        self.word_history.append(self.possible_words[0])
        return self.possible_words[0]

    def get_next_word(self, result):
        previous_word = self.word_history[-1]
        for idx in range(5):
            character = previous_word[idx]
            char_colour = result[idx]
            remaining_words = []

            for word in self.possible_words:
                if char_colour == "GREY":
                    if character not in word:
                        remaining_words.append(word)
                elif char_colour == "GREEN":
                    if word[idx] == character:
                        remaining_words.append(word)
                elif char_colour == "AMBER":
                    if character in word:
                        remaining_words.append(word)
            self.possible_words = copy.copy(remaining_words)
        self.word_history.append(self.possible_words[0])
        return self.possible_words[0]

    def reset_wordler(self):
        self.word_history = []
        possible_guesses, possible_solutions = Wordle.load_word_list()
        self.possible_words = list(possible_guesses.keys()) + list(possible_solutions.keys())






