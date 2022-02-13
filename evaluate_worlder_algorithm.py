from Wordler.Wordle import Wordle
import random


def evaluate_wordler(wordler, hard_mode=False):
    valid_guesses, valid_solutions = Wordle.load_word_list()
    valid_solutions = list(valid_solutions.keys())
    random.shuffle(valid_solutions)
    guess_scores = []
    failures = 0
    for solution in valid_solutions:
        wordle = Wordle(set_answer_to=solution, hard_mode=hard_mode)
        wordler.reset_wordler()
        guess = wordler.get_first_word()
        for i in range(6):
            score = wordle.guess(guess)
            if guess == solution:
                guess_scores.append(i+1)
                wordle.reset_wordle()
                break
            elif i == 5:
                failures += 1
            else:
                guess = wordler.get_next_word(score)

    success_rate = (len(valid_solutions) - failures) / len(valid_solutions)
    average_score = sum(guess_scores) / (len(valid_solutions) - failures)
    return success_rate, average_score




