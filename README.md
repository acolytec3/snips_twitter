## Intro
A Snips skill for reading the latest tweet from any given user that you specify.

## Setup
Run the below command before deploying this skill to your Snips device.  This will install necessary dependencies that the setup script for the skill can't accommodate.

```sudo apt-get -y install libxml2-dev libxslt-dev```



## readTweet
In the Snips console, you have to specify the twitter handle of anyone you want Snips to read from as a value for the User slot.  Note, the value should match the actual twitter handle of the user.  Use synonyms to add ASR friendly variants that Snips will understand.

## Roadmap
1. Read multiple tweets
