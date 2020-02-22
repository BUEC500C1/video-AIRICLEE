import tweepy #https://github.com/tweepy/tweepy  
import twitterAPIKey


def getTwitsFeed():

	#Twitter API credentials
	consumer_key = twitterAPIKey.consumer_key
	consumer_secret = twitterAPIKey.consumer_secret
	access_key = twitterAPIKey.access_key
	access_secret = twitterAPIKey.access_secret


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