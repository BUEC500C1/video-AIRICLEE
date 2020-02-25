import tweepy #https://github.com/tweepy/tweepy  
import twitterAPIKey
import json


def getTwitsFeed():

	#Twitter API credentials
	consumer_key = twitterAPIKey.consumer_key
	consumer_secret = twitterAPIKey.consumer_secret
	access_key = twitterAPIKey.access_key
	access_secret = twitterAPIKey.access_secret

	dataset = []
	if(len(consumer_key ) == 0 or len(consumer_secret) == 0 or len(access_key) == 0 or len(access_secret) == 0):
		with open('./test01.json','r') as load_f:
		    dataset = json.load(load_f)
		    # print(load_dict)
	return dataset

	# Authentification
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	# key word to look for twitter
	query = twitterAPIKey.query 


	language = "en"

	# user_timeline function
	results = api.search(q=query, lang=language)


	list_tweet = []
	for tweet in results:
	    list_tweet.append(tweet.text)
	return list_tweet