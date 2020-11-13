#imports
import tweepy
import json

#Twitter API Keys
with open('pws/keys.json') as keys:
    key = json.load(keys)
consumer_key = key['consumer']
consumer_secret = key['consumer_secret']
access_token = key['access_token']
access_token_secret = key['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)