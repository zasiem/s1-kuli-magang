import tweepy
import pandas as pd

auth = tweepy.OAuthHandler('key', 'key')
auth.set_access_token('key', 'key')

api = tweepy.API(auth, wait_on_rate_limit=True)

text_queries = [
    'lang:id #StartUpEP1',
    'lang:id #StartUpEP2',
    'lang:id #StartUpEP3',
    'lang:id #StartUpEP4',
    'lang:id #StartUpEP5',
    'lang:id #StartUpEP6',
    'lang:id #StartUpEP7',
    'lang:id #StartUpEP8',
    'lang:id #StartUpEP9',
    'lang:id #StartUpEP10',
    'lang:id #StartUpEP11',
    'lang:id #StartUpEP12',
    'lang:id #StartUpEP13',
    'lang:id #StartUpEP14',
    'lang:id #StartUpEP15',
    'lang:id #StartUpEP16',
]

count = 100

import snscrape.modules.twitter as sntwitter

tweets_df = pd.DataFrame(columns = ["Date", "Tweet"])

for index, text_query in enumerate(text_queries) :

    tweets_df = pd.DataFrame(columns = ["Date", "Tweet"])

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(text_query + 'since:2020-10-16 until:2020-12-16').get_items()) :
        if i > count :
            break
        tweet_list = [tweet.date , tweet.content.encode('utf-8')]
        df_length = len(tweets_df)
        tweets_df.loc[df_length] = tweet_list

    tweets_df.to_csv("File Startup {}.csv".format(index+1))    