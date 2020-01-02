
import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import random


class Tweetloader:

    def __init__(self):

        # Tokens need to be replaced with valid ones
        ACCESS_TOKEN = '3169980851-FwVdy8u0vVphYmZ32qdLRFKdQuAZPwE7Jl6Bbtd'
        ACCESS_SECRET = 'gIallicC5EMtOBk81UvDmrBUxJM7m8AvfqcfGpU3NRyC9'
        CONSUMER_KEY = 'x0s9tOEtJDteMCFvD8cZCb8cK'
        CONSUMER_SECRET = 'lUXRUZDnFSnk4vp0zzhrF2gPRQcMF8hOPvsrxQMlrBW3pfrMtq'
        self.queries = ['facebook', 'apple', 'google', 'amazon', 'trump', 'right', 'left', \
         'zuckerberg', 'cook', 'page', 'bezos', 'world', 'cup', 'exam', 'france', 'england', \
         'america', 'maga', 'europe', 'chocolate', 'summer', 'hot', 'haha', 'purge', 'lol', \
         '4th of july', '4thjuly', 'uber', 'trade war', 'intel', 'migrants', 'wall', 'parenthood', \
         '6yo', '5yo', '4yo', 'ice', 'icecream', 'cream', 'breakfast']
        oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        self.twitter = Twitter(auth=oauth)

    def search_tweets(self, query=''):
        if query == '':
            query = random.choice(self.queries)
        return self.twitter.search.tweets(q=query, lang='en', count=100)