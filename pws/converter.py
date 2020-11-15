import json
import csv
import tkinter as tk
from tkinter import filedialog

#CSV file wordt aangemaakt als hij niet bestaat
#Als er een CSV file is dan wordt er data aan toegevoegd
file = open('tweets.csv','a',encoding='utf-8') #encoding moet utf-8 zijn vanwege emoji's en dergelijken
csv_writer = csv.writer(file)
headers = ['tekst','retweets','volgers','plaats','datum','id_str']
csv_writer.writerow(headers)

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

tweets = []
for line in open(file_path, 'r'):
    tweets.append(json.loads(line))
    
print(str(len(tweets))+" tweets")
line_amount = 0
for tweet in tweets:
    try:
        csv_writer.writerow([
            tweet['full_text'],
            tweet['retweet_count'],
            tweet['user']['followers_count'],
            tweet['place'],
            tweet['created_at'],
            str(tweet['id_str'])
        ])
        line_amount+-1
    except Exception as err:
        print(err)


