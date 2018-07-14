# snips_twitter
Dependencies: tweepy, snips

#readTwitter intent
In the Snips console, you have to specify the twitter handle of anyone you want Snips to read from as a value for the User slot.  Note, the value should match the actual twitter handle of the user.  Use synonyms to add ASR friendly variants that Snips will understand.

#trendingTopics
This intent makes use of Twitter's trending topics API so only locations found in the current location slot will work.  The companion python script translates those location names into the "where on earth ID" code that Twitter uses to actually identify the region to pull trending topics for.  As currently designed, you do have to specify region so say something like "Tell me whats trending worldwide" to get the top trending results across all of Twitter.  
In order to use this code, you need to have a twitter dev account set up and place your own consumer key/secret and app key/secret in the corresponding fields in the snipsDefaults file.

#General Comments on the companion scripts
The run method in both scripts expects an mqtt message object containing a parsed intent from Snips.  See my snips_listener for additional examples.
Both scripts return a speech friendly message that can be passed to Snips to reply back via TTS.  It's up to your snips handler to repost this message to the /hermes/tts/say message in Snips to make sure Snips actually reads the data back from Twitter.


Sample use code:
import readTweet as rt
rt.run(understoodIntent)
