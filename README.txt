# Can you make a Wordler?

Solving a *wordle* is impressive, but can your algorithm solve every wordle? Is it always possible?

This repo contains a Wordle simulator, a basic "Wordler" (an algorithm for playing wordle) and a function to evaluate
the wordler against the average number of guesses it takes and how often it wins the game.

If you have never heard of Wordle, then you are missing out. Go and play it here first to learn the rules:

https://www.nytimes.com/games/wordle/index.html

## Wordle Simulator

The Wordle simulator (Wordle.py) is built from the word lists used by wordle. To use this class as the game simply
create an instance and then use the guess function to submit your guess. The class will return a dictionary of scores
for each letter.

You can enable hard mode if you want, which means you have to use previous AMBER and GREEN scored letters.

## Naive Wordler

I have written a basic algorithm for solving wordle that starts with a list of potential words, and removes words for
each score. If a letter is GREY then it removes all words containing that letter. If a letter is GREEN then it only keeps
words containing letters in that place. If a letter is AMBER then it removes all words that do not contain that letter.

The wordler is evaluated using "evaluate_wordler_algorithm", which gives it two scores. An Average number of guesses for
won games and a success rate. This algorithm scored 0.54 for success rate  and 4.78 for the
average number of guesses. There is plenty of room for improvement, by choosing a better starting word, choosing from the list of possile words using
english language statistics etc.

## WordScoreWordler

This algorithm, is the same as Naive Wordler, except it ranks each word before guessing. During a training stage it plays
the wordle game 10000 times, and ranks each word based on how likely it is to succeed. For each guess it removes not possible words
like the naive wordler and then chooses the remaining word with the highest rank.

This algorithm scored 0.75 for success rate and 4.56 for the average number of guesses.


## Rules for building a Wordler:

If you want to build a wordler, then you will need to create a class that implements the following functions:

get_first_word()
get_next_word(score)
reset_wordler()

Get_next_word, takes in the score provided by Wordle.guess(guess).

You can use any external resources, and the wordlists provided by the Wordle class. You must combine the possible_guesses
and possible_solutions lists, as it is not fair to only use words in the solution list for guesses.



## External Resources

https://www.kaggle.com/bcruise/wordle-valid-words - For wordle words list
