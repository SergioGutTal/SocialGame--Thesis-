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

conn = sqlite3.connect('./commentsPSOEApril')
c = conn.cursor()
access_token = 'AAAC5toaTpLgBACOv6ZAYJPZCGDn7dXcM83hNq2ZANdvTRp71vEjUBbSe1RuVh8Oz7Bx5KQOweHjb4k9BiC1yK0ZBbgpACnZCFPZCmTZBIzQjAZDZD'

#We call Facebook and save the comments with all their data
try:
    posts = fb_call('189318235003/posts', args={'access_token': access_token, 'since': '01 April 2012', 'until': '01 May 2012', 'limit': 100})
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
    print post['id'], len(comments_temp['data'])
print len(comments)
