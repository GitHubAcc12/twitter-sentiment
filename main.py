import os
import copy
import json
import matplotlib.pyplot as plt

from Tweetloader import *
from nltk.corpus import stopwords

from Preprocessing import *
from Agent import *
from Filter import *
from utils import *


if __name__=='__main__':
    tweetloader = Tweetloader()
    stemmer = PorterStemmer()
    cached_stopwords = stopwords.words(LANG)
    classification_strings = {0:'negative', 1:'positive'}
    
    ngrams = [get_unigrams_in_line, get_bigrams_in_line] # get_ngram_func(input('N (n-grams): '))
    word_vec = get_word_vec(stemmer, cached_stopwords, ngrams)
    agent_id = '1_3_7_layers_steam'
    A = Agent(agent_id)
    print('Enter "!end" to kill the process')
    while True:
        query = input('Search for tweets containing: ')
        if query == '!end':
            break
        resulting_tweets = tweetloader.search_tweets(query)['statuses']
        pos = 0
        neg = 0
        for tweet in resulting_tweets:
            print(tweet['text'])
            vec = get_value_vec_for_text(tweet['text'], word_vec, stemmer, cached_stopwords, ngrams)
            classification = A.classify(vec)
            if classification > .6:
                pos += 1
            elif classification < .4:
                neg += 1
            print(f'Classification: {classification}')
        
    labels =['Positive', 'Negative']
    sizes = [37, 63]
    colors = ['green', 'red']
    plt.pie(sizes, labels=labels, colors=colors)
    plt.title('Sentiment analyzed for tweets containint: Trump')
    plt.axis('equal')
    plt.show()