import tweepy #https://github.com/tweepy/tweepy
import twitter
import json
import os
import io  
from PIL import Image, ImageFont, ImageDraw
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


def transTwits2Image(list_tweet):

	# transform text to image
	i = 0
	for tweet in list_tweet:
		text = tweet
		im = Image.new('RGB',(1080,720),(255,255,255))  
		dr = ImageDraw.Draw(im)  

		ttf='/usr/share/fonts/truetype/myfonts/puhui.ttf'
		font=ImageFont.truetype(ttf, 12)

		dr.text((10, 5), text, font=font, fill="#000000")
		# im.show()  
		im.save("images/t%d.png"%i)
		i = i + 1;


def transImage2Video(usrName):

	with open('videos.txt', 'w') as f:
	    for i in range(12):
	        command = "ffmpeg -loglevel quiet -y -ss 0 -t 3 -f lavfi -i color=c=0x000000:s=830x794:r=30  " \
	                  "-i /home/lighao/EC500/assignment_3/images/t" + str(i+1) \
	                  + ".png -filter_complex \"[1:v]scale=830:794[v1];[0:v][v1]overlay=0:0[outv]\"  " \
	                  "-map [outv] -c:v libx264 /home/lighao/EC500/assignment_3/video" \
	                  + str(i+1) + ".mp4 -y"
	        p = os.popen(command)
	        p.close()
	        f.write("file video" + str(i+1) + ".mp4" + '\n')
	    f.close()
	cd = "ffmpeg -loglevel quiet -y -f concat -i videos.txt -c copy OutputVideo" + "test" + usrName + ".mp4"
	pp = os.popen(cd)
	pp.close()


def getResult(usrName):
	list_tweet = getTwitsFeed()
	transTwits2Image(list_tweet)
	transImage2Video(usrName)

if __name__ == '__main__':
	getResult()
