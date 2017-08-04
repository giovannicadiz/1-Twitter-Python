from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = 'consumer_key here'
consumer_secret = 'consumer_secret here'
access_token = 'access_token here'
access_token_secret = 'access_token_secret here'

class MyListener(StreamListener):

	def on_data(self, data):
		print data
		return True
	
	def on_error(self, status):
		print status


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, MyListener())
twitterStream.filter(track = ["#hashtag here"]) 
