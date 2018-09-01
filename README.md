# snips_twitter
Dependencies: tweepy, snips

Setting things up:
1) You must have an active Twitter developer account for this to work.  Once you do, set up a new app at apps.twitter.com.
2) Grab the consumer key/secret and access token/secret and place them in the corresponding variables in the config.ini file.

## readTweet
In the Snips console, you have to specify the twitter handle of anyone you want Snips to read from as a value for the User slot.  Note, the value should match the actual twitter handle of the user.  Use synonyms to add ASR friendly variants that Snips will understand.

## trendingTopics (not currently coded according to Snips App Server specifications)
This intent makes use of Twitter's trending topics API so only locations found in the current location slot will work.  The companion python script translates those location names into the "where on earth ID" code that Twitter uses to actually identify the region to pull trending topics for.  As currently designed, you do have to specify region so say something like "Tell me whats trending worldwide" to get the top trending results across all of Twitter.  
In order to use this code, you need to have a twitter dev account set up and place your own consumer key/secret and app key/secret in the corresponding fields in the snipsDefaults file.
