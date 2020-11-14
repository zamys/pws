import keys
import tweepy
import datetime
import time
import jsonpickle

time_start = time.time()
#Authenticatie
key = keys.GetKeys()
auth = tweepy.OAuthHandler(key.consumer, key.consumer_secret)
auth.set_access_token(key.access_token, key.access_token_secret)
api = tweepy.API(auth)

#Hoeveel tweets worden opgeslagen per run
date_today = datetime.datetime.now() #datum van vandaag
tweets_per_query = 100 #Meer mag niet van twitter
tweets_max = 500 #Hoeveel tweets er totaal worden opgeslagen
file_name = 'tweets-'+ date_today.strftime('%d-%m-%y') +'.txt'
since_id = None
max_id = -1
tweet_count = 0
print("Download begint nu...")

#Scraper gaat zoeken naar:
search_query = "#COVID19"
with open(file_name,'w') as f:
    print("Tweets met " + search_query + " worden gedownload.")
    while(tweet_count<tweets_max):
        try:
            if(max_id<=0):
                if(not since_id):
                    tweets_new = api.search(q=search_query,count=tweets_per_query,lang="en",tweet_mode='extended')

                else:
                    tweets_new = api.search(q=search_query,count=tweets_per_query,lang="en",tweet_mode='extended',since_id=since_id)
            else:
                if(not since_id):
                    tweets_new = api.search(q=search_query,count=tweets_per_query,lang="en",tweet_mode='extended',max_id=str(max_id-1))
                else:
                    tweets_new = api.search(q=search_query,count=tweets_per_query,lang="en",tweet_mode='extended',max_id=str(max_id-1),since_id=since_id)

            #Als er geen nieuwe tweets zijn binnen gekomen:
            if(not tweets_new):
                print("Geen nieuwe tweets gevonden")
                break
            
            for tweet in tweets_new:
                f.write(jsonpickle.encode(tweet._json,unpicklable=False)+'\n')
                tweet_count += len(tweets_new)
                print("{0} tweets zijn gedownload".format(tweet_count))
                max_id = tweets_new[-1].id

        except tweepy.TweepError as err:
            print("Foutmelding: "+str(err))
            break

time_end = time.time()
time_elapsed = time_end-time_start

print("{0} tweets zijn gedownload en zijn opgeslagen in {1}".format(tweet_count,file_name))
print("Het heeft {0} seconden geduurd".format(time_elapsed))