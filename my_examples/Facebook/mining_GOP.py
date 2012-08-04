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

conn = sqlite3.connect('./commentsGOP')
c = conn.cursor()
access_token = 'AAAC5toaTpLgBALJo800KmAC8dvoZAhaokKvW3npEaad9815PVGASahuyYIIZA0G894vADU7HRCrtLHVKLqsZAVoHgIwusnpUbNmUjW2kgZDZD'

#We call Facebook and save the comments with all their data
try:
    posts = fb_call('123192635089/feed', args={'access_token': access_token, 'limit': 100})
except urllib2.HTTPError, error:
    print "ERROR: ", error.read()
       
print len(posts['data'])

#Array with the messages of the comments
comments = []
comment_name = []
for post in posts['data']:
    call=post['id']
    call+='/comments'
    try:
        comments_temp = fb_call(call, args={'access_token': access_token, 'limit': 25})
        for comment in comments_temp['data']:
            comments.append(comment['message'])
            c.execute('insert into comments values (?,?,?)', (comment['created_time'],comment['from']['id'],comment['message']))
            conn.commit()
    except urllib2.HTTPError, error:
        print "ERROR: ", error.read()    
    print post['id'], len(comments_temp['data']), post['created_time']
print len(comments)
