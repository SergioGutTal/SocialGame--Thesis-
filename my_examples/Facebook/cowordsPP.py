import os
import simplejson as json
import urllib
import urllib2
import webbrowser
import nltk
from cgi import escape
import sqlite3


conn = sqlite3.connect('./commentsPPJune')
c = conn.cursor()


##ANALYZE THEMESSAGES PART
HTML_TEMPLATE = '../../web_code/wp_cumulus/tagcloud_template.html'
OUT_FILE = './facebook.tag_cloudPPJune.html'
MIN_FREQUENCY = 50
MIN_FONT_SIZE = 3
MAX_FONT_SIZE = 20

comments = c.execute('select * from comments')
comments = c.fetchall()
messages = []
for m in comments:
    messages.append(m[2].lower())
#print messages         

# Compute frequency distribution for the terms
fdist = nltk.FreqDist([term for c in messages for term in c.split()])

total_palabras=0
for (term, freq) in fdist.items():
    total_palabras+=freq
print 'NUMERO DE PALABRAS-->', total_palabras   
print 'NUMERO DE MENSAJES-->', len(messages)

# Customize a list of stop words as needed

stop_words = nltk.corpus.stopwords.words('spanish')
stop_words += ['&', '.', '?', '!']

# Create output for the WP-Cumulus tag cloud and sort terms by freq along the way

raw_output = sorted([[escape(term), '', freq] for (term, freq) in fdist.items()
                    if freq > MIN_FREQUENCY and term not in stop_words],
                    key=lambda x: x[2])

# Implementation adapted from 
# http://help.com/post/383276-anyone-knows-the-formula-for-font-s

min_freq = raw_output[0][2]
max_freq = raw_output[-1][2]


def weightTermByFreq(f):
    return (f - min_freq) * (MAX_FONT_SIZE - MIN_FONT_SIZE) / (max_freq
            - min_freq) + MIN_FONT_SIZE


weighted_output = [[i[0], i[1], weightTermByFreq(i[2])] for i in raw_output]
for word in raw_output:
    index = len(raw_output)-raw_output.index(word)
    print index, ': ', word[0], '-->',word[2]
print len(raw_output)   
# Substitute the JSON data structure into the template

html_page = open(HTML_TEMPLATE).read() % (json.dumps(weighted_output), )

f = open(OUT_FILE, 'w')
f.write(html_page)
f.close()

print 'Date file written to: %s' % f.name

# Open up the web page in your browser

webbrowser.open('file://' + os.path.join(os.getcwd(), OUT_FILE))
