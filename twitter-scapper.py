import tweepy
import pandas as pd

auth = tweepy.OAuthHandler('key', 'key')
auth.set_access_token('key', 'key')

api = tweepy.API(auth, wait_on_rate_limit=True)

text_query = 'lang:id #StartUpEP1'
count = 100
try:
 # Creation of query method using parameters
 tweets = tweepy.Cursor(api.search,q=text_query).items(count)
 
 # Pulling information from tweets iterable object
 tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
 
 # Creation of dataframe from tweets list
 # Add or remove columns as you remove tweet information
 tweets_df = pd.DataFrame(tweets_list)
 print(tweets_df)

 tweets_df.to_csv("file1.csv")
 
except BaseException as e:
    print('failed on_status,',str(e))