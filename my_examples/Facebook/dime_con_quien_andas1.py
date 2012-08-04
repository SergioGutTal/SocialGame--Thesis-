import os
import simplejson as json
import urllib
import urllib2
import webbrowser
import nltk
from cgi import escape
import sqlite3


def fb_call(call, args=None):
    return json.loads(urllib2.urlopen("https://graph.facebook.com/" + call +
                                      '?' + urllib.urlencode(args)).read())

conn = sqlite3.connect('./friendslikes')
c = conn.cursor()
access_token = 'AAAC5toaTpLgBACOv6ZAYJPZCGDn7dXcM83hNq2ZANdvTRp71vEjUBbSe1RuVh8Oz7Bx5KQOweHjb4k9BiC1yK0ZBbgpACnZCFPZCmTZBIzQjAZDZD'

#We call Facebook and save the friends with all their data
try:
    friends = fb_call('702354702/friends', args={'access_token': access_token, 'limit': 150})
except urllib2.HTTPError, error:
    print "ERROR: ", error.read()
       
print len(friends['data'])

i=0 
likes=[]
for friend in friends['data']:
    raw_data = fb_call(friend['id']+'/likes', args={'access_token': access_token})
    likes.append([friend['id'], raw_data['data']])
    i+=1
    print i 

i=0  
for users in likes: 
    #users[0] tiene el id del usuario
    for like in users[1]:  
    #users[1]  tiene los likes en bruto 
        c.execute('insert into likes values (?,?,?,?)', (like['category'],like['id'],users[0],like['name']))
        conn.commit()
    i+=1
    print i
    
#We call Facebook and save my likes with all their data
try:
    my_likes = fb_call('me/likes', args={'access_token': access_token})
except urllib2.HTTPError, error:
    print "ERROR: ", error.read()  
    
for my_like in my_likes['data']:
    c.execute('insert into my_likes values (?,?,?)', (my_like['category'],my_like['id'],my_like['name']))
    conn.commit()
    print my_like
    