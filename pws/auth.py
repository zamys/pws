#imports
import tweepy

#De twitter developer API keys
consumer_key = "zX3J8KUpxwz0l1lZxO8x6vIPm"
consumer_secret = "WiCpmd4m570VZrCnGHP0ZuzL9lOgvVhq6X1LoHTrAbqQ0MDvAv"
access_token = "4105761881-MyTNEZDLTREIDqikaaoi4zXQAJBeLwBit1N1iX5"
access_token_secret = "Po4ooOCNV9KSI6HiA03oCNrgBNWHbgeL6S7jChBQBRFUd"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

