#imports
import json

#Twitter API Keys

class GetKeys:
    
    def __init__(self):
        with open('pws/keys.json') as keys:
            key = json.load(keys)
        self.consumer = key['consumer']
        self.consumer_secret = key['consumer_secret']
        self.access_token = key['access_token']
        self.access_token_secret = key['access_token_secret']

