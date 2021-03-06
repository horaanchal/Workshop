#Using twitter Search API

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '949971570948100097-DSQg6ySE1pKZljDGa30eaIGI2wbH9Qw'
ACCESS_SECRET = 'DIhfH3l0Sax8uuxa8MhlZPke1Qxc6r2eT7YWvvEU6jw72'
CONSUMER_KEY = 'qOnfdMIOKju3dTi78pi3B2iGb'
CONSUMER_SECRET = 'tnsNac26XPvO6YLJY1qaddiOSIJx7EteAztjzdCbMA9Pxe8PVH'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

#Initiating the connection to Twitter REST API
twitter = Twitter(auth=oauth)

#Search for 10 latest english tweets about "#nlproc"
search_result = twitter.search.tweets(q='#nlproc', result_type='recent', lang = 'en', count = 10)

print(search_result)
