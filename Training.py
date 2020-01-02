import os
import copy
import json

from Tweetloader import *
from nltk.corpus import stopwords

from Preprocessing import *
from Agent import *
from Filter import *






if __name__=='__main__':
    # Training
    
    stemmer = PorterStemmer()
    cached_stopwords = stopwords.words(LANG)
    # ngrams = get_ngram_func(input('N (n-grams): '))
    ngrams = [get_trigrams_in_line]
    data_raw = get_labelled_examples()
    raw_sentences = list(data_raw.keys())
    agent_id = input('Agent id: ')
    word_vec = get_word_vec(stemmer, cached_stopwords, ngrams)
    A = Agent(agent_id, len(word_vec), 1)
    word_states = []
    targets = []

    print('Filling training-batch')
    for key in raw_sentences:
        word_states.append(get_value_vec_for_text(key, word_vec, stemmer, cached_stopwords, ngrams)[0])
        targets.append(data_raw[key])
    """
    with open(os.path.join(os.getcwd(), 'Data', 'trainingdata.json'), 'w') as file:
        json.dump((word_states, targets), file)
    """
    
    print('Training started')
    A.train_on_batch((np.array(word_states), np.array(targets)))