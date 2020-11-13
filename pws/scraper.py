import keys
import tweepy

key = keys.GetKeys()
auth = tweepy.OAuthHandler(key.consumer, key.consumer_secret)
auth.set_access_token(key.access_token, key.access_token_secret)

api = tweepy.API(auth)