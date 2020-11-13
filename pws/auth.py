#imports
import tweepy

#De twitter developer API keys
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

