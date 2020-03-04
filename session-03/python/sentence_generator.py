# imports the random generator
from math import floor
from random import random


nouns1 = ["elephant", "rabbit", "shrimp", "tiger", "turtle" ];
nouns2 = [ "clementine", "orange", "kiwi", "durian"];
adjs = [ "orange", "soft", "shrimpy"];

def pick_random_word(words):
	"""Given a list of words, returns a word randomly selected from it.""" 
	r = random()

	# gets a random number between 0 and the number
	# of words in the list, and converts it to an integer.
	random_index = int(floor(r*len(words))) 
	
	# get a word from the list using this random number
	random_word = words[random_index]

	# outputs a random word
	return random_word;


def make_sentence():
	"""Takes each list and picks a word at random, compiles and prints a sentence."""			

	random_noun1 = pick_random_word(nouns1);
	random_noun2  = pick_random_word(nouns2);
	random_adj = pick_random_word(adjs);

	sentence = "{} is a {} {}"
	print(sentence.format(random_noun1, random_adj, random_noun2))


# run make_sentence()
make_sentence()

