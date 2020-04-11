#This bot will access my Twitter account and like some tweets based on a specific keyword that I will pass as a parameter
#Created by WilliamOtieno

import tweepy
import time

#Access the Consumer api keys after creating an account in the Tweeter developers website

#arguments are (API key, API scret key) in the consumer api keys
auth = tweepy.OAuthHandler("ID3RfiTfCHHuwhkD2ZX9c97jD", "n2DhdVocJ25YIHDRDLZF0aMsv5r0iwyQmGXT00pIZsU3xYMtem") 

 #arguments are (access token, access token secret) from the access token and access token secret  keys
auth.set_access_token("935912368231546882-9vWa4Y5uq2WBZutsdRXVBLXCZnjkYKw", "eQBLAQ3yqk9upjDKYqoCngl9gvltUayzvjT0RqCL3olYJ")

#Access the API and set rate limits to True to avoid being banned 
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

#Keyword to use when searchinng for tweets to be liked 
search = 'Python'
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
