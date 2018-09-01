#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import tweepy
from tweepy import OAuthHandler

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}

def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()

def readTweet(hermes, intentMessage):
	drumpf = api.user_timeline(id=intentMessage.slots.User[0].slot_value.value.value,tweet_mode='extended',count=10)
	for status in drumpf:
		if status.retweeted==False:
			print(status.full_text)
		break
	return status._json['user']['name'] + ' said ' + status.full_text

def readTweet_callback(hermes, intentMessage):
	message = readTweet(hermes, intentMessage)
	hermes.publish_end_session(intentMessage.session_id, message)


if __name__ == "__main__":
	config = read_configuration_file(CONFIG_INI)

	auth = OAuthHandler(config['secret']['consumerkey'],config['secret']['consumersecret'])
	auth.set_access_token(config['secret']['appkey'],config['secret']['appsecret'])
	api = tweepy.API(auth)

	with Hermes("localhost:1883") as h:
		h.subscribe_intent("readTweet",readTweet_callback).start()


