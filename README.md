# snips_twitter
Dependencies: tweepy, snips

In order to use this code, you need to have a twitter dev account set up and place your own consumer key/secret and app key/secret in the corresponding fields in the snipsDefaults file.

The run method in both scripts expects an mqtt message object containing a parsed intent from Snips.  See my snips_listener for additional examples.

Sample use code:
import readTweet as rt
rt.run(understoodIntent)
