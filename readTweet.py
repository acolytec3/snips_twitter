import tweepy
from tweepy import OAuthHandler
import snipsDefaults as snips

def run(msg):
	auth = OAuthHandler(snips.consumerkey,snips.consumersecret)
	auth.set_access_token(snips.appkey,snips.appsecret)
	api = tweepy.API(auth)
	data = parse_slots(msg)
	drumpf = api.user_timeline(id=data['User'],tweet_mode='extended',count=10)
	for status in drumpf:
		if status.retweeted==False:
			print(status.full_text)
		break
	return status._json['user']['name'] + 'said ' + status.full_text

def parse_slots(data):
	return dict((slot['slotName'], slot['value']['value']) for slot in data['slots'])