import os
import copy
import json

from Tweetloader import *
from nltk.corpus import stopwords

from Preprocessing import *
from Filter import *
from Agent import *



if __name__=='__main__':
    # Testing
    eps = 0.1
    stemmer = PorterStemmer()
    cached_stopwords = stopwords.words(LANG)
    # ngrams = get_ngram_func(input('N (n-grams): '))
    ngrams = [get_trigrams_in_line]
    word_vec = get_word_vec(stemmer, cached_stopwords, ngrams)
    data_raw = get_labelled_examples(directory='data/testdata', only_words=True)
    raw_sentences = list(data_raw.keys())
    agent_id = input('Agent id: ')
    A = Agent(agent_id, len(word_vec), 1)

    wrong = 0
    for key in raw_sentences:
        classification = A.classify(get_value_vec_for_text(key, word_vec, stemmer, cached_stopwords, ngrams))
        if abs(classification - data_raw[key]) > 0.1:
            wrong += 1
        print(f'Class: {data_raw[key]}, Classification: {classification}')
    print(f'Error rate: {wrong/len(list(data_raw.keys()))}')