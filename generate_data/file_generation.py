


#_____________ Delete big letters and punctuation ________________

import re, string
def no_punctuation(my_string):
	regex = re.compile('[%s]' % re.escape(string.punctuation))
	return (regex.sub('', my_string)).lower()


#_____________ Generate latin text ________________


import lorem   #https://pypi.python.org/pypi/lorem

def generate_latin_files(number, size) : 
	for i in range(number) : 
		filename = "file"+str(i)+"_size"+str(size)+".txt"
		p = lorem.paragraph()
		f=open(filename, 'w')
		f.write(no_punctuation(p))
		if size =="2":
			p2 = lorem.paragraph()
			f.write(no_punctuation(p2))
		f.close()


#_____________Generate english/french text  ________________

#Source for the code : https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6

import numpy as np


def make_pairs(corpus):
	for i in range(len(corpus)-1):
		yield (corpus[i], corpus[i+1])


#Generate multiple words
def my_words_generator(n_words, corpus): 
        
	pairs = make_pairs(corpus)


	word_dict = {}

	for word_1, word_2 in pairs:
	    if word_1 in word_dict.keys():
	        word_dict[word_1].append(word_2)
	    else:
	        word_dict[word_1] = [word_2]
	 
	first_word = np.random.choice(corpus)

	while first_word.islower():
	    first_word = np.random.choice(corpus)

	chain = [first_word]

	for i in range(n_words):
	    chain.append(np.random.choice(word_dict[chain[-1]]))

	res = ' '.join(chain)

	return res 

def generate_files(number, corpus, size) : 
	for i in range(number) : 
		filename = "file"+str(i)+"_size"+str(size)+".txt"
		if size=="1":
			nb_words = 50
		if size=="2":
			nb_words = 100
		p = no_punctuation(my_words_generator(nb_words, corpus))
		f=open(filename, 'w')
		f.write(p)
		f.close()




#_____________ Script ________________


#! /usr/bin/env python3
# coding: utf-8

import sys

if __name__ == "__main__":
	if sys.argv[1] == "latin": 
		generate_latin_files(3, sys.argv[2])
	if sys.argv[1] == "french":
		data = open('french.txt', encoding='utf8').read()   
		corpus = data.split()
		generate_files(3, corpus, sys.argv[2])
	if sys.argv[1] =="english":
		data = open('english.txt', encoding='utf8').read()   #Trump speech
		corpus = data.split()
		generate_files(3, corpus, sys.argv[2])
