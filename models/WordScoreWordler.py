"""
More advanced model that still restricts the word choice to the possible remaining words, but uses a learning stage
to order each word by the liklihood that it will lead to a win.
"""
from Wordler.models.AbstractWordler import AbstractWordler
from Wordler.Wordle import Wordle
from Wordler.models.NaiveWordler import NaiveWordler
import random
import json


class WordScoreWordler(AbstractWordler):

    word_rankings_filename = "../data/word_rankings.json"

    def __init__(self, train=False):
        self.word_history = []
        self.possible_words = {}
        self.train = train
        if train:
            self.learn_ranking()
        self.load_ranking()
        super().__init__()

    def learn_ranking(self):
        possible_guesses, possible_solutions = Wordle.load_word_list()
        self.possible_words = {**possible_guesses, **possible_solutions}
        wordler = NaiveWordler()
        for idx in range(10000):
            wordle = Wordle()
            wordler.reset_wordler()
            guesses = []
            guess = wordler.get_first_word()
            guesses.append(guess)
            for i in range(6):
                score = wordle.guess(guess)
                if isinstance(score, str):
                    self.increase_scores(guesses)
                    wordle.reset_wordle()
                    break
                elif i == 5:
                    self.decrease_scores(guesses)
                else:
                    guess = wordler.get_next_word(score)
                    guesses.append(guess)
        self.save_ranking()

    def save_ranking(self):
        with open(self.word_rankings_filename, 'w') as file:
            json.dump(self.possible_words, file)

    def load_ranking(self):
        with open(self.word_rankings_filename, 'r') as file:
            self.possible_words = json.load(file)
        self.possible_words = {k: v for k, v in sorted(self.possible_words.items(), reverse=True, key=lambda item: item[1])}

    def increase_scores(self, guesses):
        for guess in guesses:
            self.possible_words[guess] += 1

    def decrease_scores(self, guesses):
        for guess in guesses:
            self.possible_words[guess] -= 1

    def get_first_word(self):
        self.word_history.append(list(self.possible_words.keys())[0])
        return list(self.possible_words.keys())[0]

    def get_next_word(self, result):
        previous_word = self.word_history[-1]
        for idx in range(5):
            character = previous_word[idx]
            char_colour = result[idx]

            for word in list(self.possible_words.keys()):
                if char_colour == "GREY":
                    if character in word:
                        del self.possible_words[word]
                elif char_colour == "GREEN":
                    if not word[idx] == character:
                        del self.possible_words[word]
                elif char_colour == "AMBER":
                    if character not in word:
                        del self.possible_words[word]

        first_word = list(self.possible_words.keys())[0]
        self.word_history.append(first_word)
        return first_word

    def reset_wordler(self):
        self.word_history = []
        if not self.train:
            self.load_ranking()
