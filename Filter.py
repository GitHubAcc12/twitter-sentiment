import numpy as np
import statistics

from nltk.corpus import stopwords

from Preprocessing import *


def get_words_and_frequency(stemmer, cached_stopwords, ngrams, directory='Data'):
    words = {}
    dir = os.path.join(os.getcwd(), directory)
    for ngram_func in ngrams:
        for filename in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, filename)):
                with open(os.path.join(dir, filename), 'r', encoding='utf-8') as file:
                    for line in file:
                        raw_input = line.split('\t')
                        grams = ngram_func(raw_input[0], stemmer, cached_stopwords)
                        for word in grams:
                            words.update({word:words.get(word, 0)+1})
    return words
    
def remove_lowest_words(words):
    keys = list(words.keys())
    for key in keys:
        if words[key] == 1: # TODO Grenze finden
            words.pop(key, None)
    
def get_word_vec(stemmer, cached_stopwords, ngrams):      
    filtered = get_words_and_frequency(stemmer, cached_stopwords, ngrams)
    remove_lowest_words(filtered)
    return list(filtered.keys())