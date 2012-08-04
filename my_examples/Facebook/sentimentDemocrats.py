# -*- coding: utf-8 -*-

import os
import simplejson as json
import urllib
import urllib2
import webbrowser
import nltk
from cgi import escape
import sqlite3
import AlchemyAPI


conn = sqlite3.connect('./commentsDemocrats')
c = conn.cursor()


##ANALYZE THEMESSAGES PART
HTML_TEMPLATE = '../../web_code/wp_cumulus/tagcloud_template.html'
javascript_template = '../../web_code/wp_cumulus/javascript_template.js'
OUT_FILE2 = '../../web_code/wp_cumulus/JavaScript-1.js'
OUT_FILE = './facebook.tag_sentiment_cloudDemocrats.html'
MIN_FREQUENCY = 40
MIN_FONT_SIZE = 3
MAX_FONT_SIZE = 20

comments = c.execute('select * from comments')
comments = c.fetchall()
messages = []
#Pasamos los mensajes a minœsculas
for m in comments:
    messages.append(m[2].lower())

# Compute frequency distribution for the terms
# Contamos la frecuencia de las palabras en los mensajes. Genera una lista con palabra:repeticiones
fdist = nltk.FreqDist([term for c in messages for term in c.split()])
          

# Customize a list of stop words as needed
# Realizamos el filtrado de palabras, simbolos, etc.
stop_words = nltk.corpus.stopwords.words('english')
stop_words += ['&', '.', '?', '!']

# Create output for the WP-Cumulus tag cloud and sort terms by freq along the way
# Ordenamos por frecuencia y creamos la salida para la nube de "terminos WP-Cumulus" (
raw_output = sorted([[escape(term), '', freq] for (term, freq) in fdist.items()
                    if freq > MIN_FREQUENCY and term not in stop_words],
                    key=lambda x: x[2]) #para decir que ordene por el tercer parametro de cada palabra en la lista, es decir, la frecuencia
for i in raw_output:
    if '\'' not in i[0]:
        i[1]='http://www.wolframalpha.com/input/?i='+i[0]
    else:
        i[1]='http://www.wolframalpha.com/'
        
# Implementation adapted from 
# http://help.com/post/383276-anyone-knows-the-formula-for-font-s

min_freq = raw_output[0][2]
max_freq = raw_output[-1][2] #con el -1 cogemos la ultima palabra (ciclico)

def weightTermByFreq(f):
    return (f - min_freq) * (MAX_FONT_SIZE - MIN_FONT_SIZE) / (max_freq
            - min_freq) + MIN_FONT_SIZE


weighted_output = [[i[0], i[1], weightTermByFreq(i[2])] for i in raw_output]
for word in raw_output:
    index = len(raw_output)-raw_output.index(word)
    print index, ': ', word[0], '-->',word[2]
print len(raw_output)  

# Creamos el objeto AlchemyAPI y cargamos el APIkey del disco.
alchemyObj = AlchemyAPI.AlchemyAPI()
alchemyObj.loadAPIKey("AlchemyAPI_key.txt")

# Creamos un array con las palabras y los rellenamos de palabras
word_list = {}
# En ocurrences guaradremos las correspondencias entre palabras y mensajes donde aparecen. En el primer valor del array la palabra y en el segundo el id de los mensajes donde aparece concatenados
for word in weighted_output:
    word_list[word[0]]=[]
print word_list    

# Recorremos los mensajes buscando las palabras 
for message in messages:
    for word in weighted_output:
        if word[0] in message:
            #print sentiment.index(word[0]), word_list.index(word[0]), sentiment[sentiment.index(word[0])], messages.index(message)
            word_list[word[0]].append(messages.index(message))
for e in word_list['jobs']:
    print e,')',messages[int(e)], '\n'
            
#ÊGuardamos en sentiment[] la palabra a buscar junto con los resultados obtenidos de todas las consultas para obtener el sentimiento de los mensajes
sentiment=[]
json_output = {
                "children": [],
                "data": {
                         "$dim": 1,
                         "$color": "#001eff"},   
                "name": 'SENTIMIENTO DE LAS PALABRAS',
                "id": 'WORDS',
                }

words_looking_for = word_list.keys();
for word_looking_for in words_looking_for:
    for message_number in word_list[word_looking_for]:
        print message_number, word_looking_for, '---->', messages[message_number]
    json_output['children'].append({
                        "children": [ 
                                #print messages[int(message_number)], word_looking_for
                                #result=alchemyObj.TextGetTargetedSentiment(messages[int(message_number)], word_looking_for); PONER LUEGO
                                #sentiment[ocurrences.index(ocurrence)]+=str(result)
                        ],
                        "data": {
                                 "$dim": 1,
                                 "$color": "#001eff"},   
                        "name": word_looking_for,
                        "id": word_looking_for,      
    })

for child in json_output['children']:
    for message_number in word_list[child['id']]:
        if message_number<160:
            child['children'].append(
                                     {"id": message_number, "name": messages[int(message_number)][0:60],
                                      "data": {
                                               "$dim": 1,
                                               "$color": "#001eff"
                                               #ROJO#FF0000
                                               #VERDE#00FF00
                                               }
                                      })
                                                 
for posts in json_output['children']:
    for post in posts['children']:
        try:
            #post_sentiment = 0
            post_sentiment = alchemyObj.TextGetTextSentiment(messages[int(post['id'])])
            post_sentiment=post_sentiment[post_sentiment.find('<score>')+7:post_sentiment.find('</score>')]
            post_sentiment=float(post_sentiment)
        except:
            print 'Error llamando a ALCHEMY_API', messages[int(post['id'])], posts['id']
            post_sentiment = 0
            post['data']['$color']='#FFA500'
        if post_sentiment>0:
            post['data']['$color']='#00FF00'
            print 'POSITIVE', post_sentiment
        elif post_sentiment<0:
            post['data']['$color']='#FF0000' 
            print 'NEGATIVE', post_sentiment      
                
#print json_output['id']    
javascript_file = open(javascript_template).read() % (json.dumps(json_output, indent=4), )
f2 = open(OUT_FILE2, 'w')
#f2 = open('../../web_code/wp_cumulus/JavaScript-'+word_looking_for+'.js', 'w')
f2.write(javascript_file)
f2.close()
print 'Date file written to: %s' % f2.name

# Substitute the JSON data structure into the templates
html_page = open(HTML_TEMPLATE).read() % (json.dumps(weighted_output), )

f = open(OUT_FILE, 'w')
f.write(html_page)
f.close()

print 'Date file written to: %s' % f.name

# Open up the web page in your browser

webbrowser.open('file://' + os.path.join(os.getcwd(), OUT_FILE))
