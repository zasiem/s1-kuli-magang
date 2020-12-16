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

count = 5

for index, text_query in enumerate(text_queries) :
    try:
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.search,q=text_query).items(count)
        
        # Pulling information from tweets iterable object
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
        
        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        tweets_df = pd.DataFrame(tweets_list)
        print(tweets_df)

        tweets_df.to_csv("File Startup {}.csv".format(index+1))
        
    except BaseException as e:
        print('failed on_status,',str(e))