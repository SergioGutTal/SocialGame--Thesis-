import os
import simplejson as json
import urllib
import urllib2
import webbrowser
import nltk
from cgi import escape
import sqlite3


musician = False
movie = False
university = False
tvshow = False
book = False
politician = False
actor = False
athlete = False

conn = sqlite3.connect('./friendslikes')
c = conn.cursor()

likes = c.execute('select * from likes')
likes = c.fetchall()
my_likes = c.execute('select * from my_likes')
my_likes = c.fetchall()

likes_dictionary = {}
for like in likes:    
    if likes_dictionary.has_key(like[1]):
        likes_dictionary[like[1]][2]+=1
    else:
        likes_dictionary[like[1]] = [like[3],like[0],1,like[1]] 

likes_ordered = sorted(likes_dictionary.values(), key=lambda like: like[2], reverse=True)

toplikes = []
for b in likes_ordered:
    if 'Musician/band' in b[1] and musician is False:
        musician = True
        toplikes.append([b[1],b[0],b[2],b[3]])
    elif 'Athlete' in b[1] and athlete is False:
        athlete = True
        toplikes.append([b[1],b[0],b[2],b[3]])
    elif 'Movie' in b[1] and movie is False:
        if 'DORY' not in b[0] and 'princesa' not in b[0]:
            movie = True
            toplikes.append([b[1],b[0],b[2],b[3]])
    elif 'Actor/director' in b[1] and actor is False:
        if 'Tambien' not in b[0]:
            actor = True
            toplikes.append([b[1],b[0],b[2],b[3]])
    elif 'Book' in b[1]and book is False:
        book = True
        toplikes.append([b[1],b[0],b[2],b[3]])
    elif 'Tv show' in b[1] and tvshow is False:
        tvshow = True
        toplikes.append([b[1],b[0],b[2],b[3]])
    elif 'University' in b[1] and university is False:
        university = True
        toplikes.append([b[1],b[0],b[2],b[3]])
    elif 'Politician' in b[1] and politician is False:
        politician = True
        toplikes.append([b[1],b[0],b[2],b[3]])                        

for tl in toplikes:
    print tl
    
for my_like in my_likes:
    for tl in toplikes:
        if tl[3] in my_like[1]:
            print my_like