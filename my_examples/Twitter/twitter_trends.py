'''
Created on Jan 26, 2012

@author: drazic_1
'''
#example 1.5 Mining the Social Web
import twitter
import json
from time import mktime




#@TheDemocrats
#@GOP

twitter_api = twitter.Twitter(domain="api.twitter.com", api_version='1')
WORLD_WOE_ID = 23424950 # The Yahoo! Where On Earth ID for the entire world
world_trends = twitter_api.trends._(WORLD_WOE_ID) # get back a callable
for trend in world_trends()[0]['trends']:
    print trend['name']
    
search_results = []
for page in range(1,6):
    search_results.append(twitter_api.search(q="Chacon", page=page))
#print json.dumps(search_results, sort_keys=True, indent=1)
#print search_results[0]['results']
dates = []
for jiji in search_results[0]['results']:
    dates.append(jiji['created_at'])
    print jiji['created_at']
    print mktime(jiji['created_at'])

print dates[1]-dates[0] 
    
#print json.dumps(search_results[0]['results'], sort_keys=True, indent=1)
    