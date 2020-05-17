#This bot will access my Twitter account and like some tweets based on a specific keyword that I will pass as a parameter
#Created by WilliamOtieno

import tweepy
import time

#Access the Consumer api keys after creating an account in the Tweeter developers website

#arguments are (API key, API scret key) in the consumer api keys
auth = tweepy.OAuthHandler("T5dE0zyEkof0kCraAR8mXYO72", "TAF5dld2SqCgnCiE6f12vaOZKdRMLxE8fyFkt9l4Ypaua3z4cs")

 #arguments are (access token, access token secret) from the access token and access token secret  keys
auth.set_access_token("935912368231546882-Zzv3tISnLzeusZc7huwU36nD9ftGtWH", "O4TpDDyZRGVJezNbtoF5x2zjaEZNZS8bSsKdCBghIzwst")

#Access the API and set rate limits to True to avoid being banned
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

#Keyword to use when searchinng for tweets to be liked
search = '100DaysOfCode'
numTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(numTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
