import base64
import os
import os.path
import simplejson as json
import urllib
import urllib2
import socket
import sys
import sqlite3

from flask import Flask, request, redirect, render_template

#FBAPI_APP_ID = os.environ.get('FACEBOOK_APP_ID')
conn = sqlite3.connect('./static/tokens')
c = conn.cursor()


def oauth_login_url(preserve_path=True, next_url=None):
    fb_login_uri = ("https://www.facebook.com/dialog/oauth"
                    "?client_id=%s&redirect_uri=%s" %
                    (app.config['FBAPI_APP_ID'], get_home()))

    if app.config['FBAPI_SCOPE']:
        fb_login_uri += "&scope=%s" % ",".join(app.config['FBAPI_SCOPE'])
    return fb_login_uri


def getLoginUri():
    return fb_login_uri


def simple_dict_serialisation(params):
    return "&".join(map(lambda k: "%s=%s" % (k, params[k]), params.keys()))


def base64_url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip('=')


def fbapi_get_string(path, domain=u'graph', params=None, access_token=None,
                     encode_func=urllib.urlencode):
    """Make an API call"""
    if not params:
        params = {}
    params[u'method'] = u'GET'
    if access_token:
        params[u'access_token'] = access_token

    for k, v in params.iteritems():
        if hasattr(v, 'encode'):
            params[k] = v.encode('utf-8')

    url = u'https://' + domain + u'.facebook.com' + path
    params_encoded = encode_func(params)
    url = url + params_encoded
    result = urllib2.urlopen(url).read()

    return result


def fbapi_auth(code):
    params = {'client_id': app.config['FBAPI_APP_ID'],
              'redirect_uri': get_home(),
              'client_secret': app.config['FBAPI_APP_SECRET'],
              'code': code}

    result = fbapi_get_string(path=u"/oauth/access_token?", params=params,
                              encode_func=simple_dict_serialisation)
    
    print 'User access_token received is: ', result
    pairs = result.split("&", 1)
    result_dict = {}
    for pair in pairs:
        (key, value) = pair.split("=")
        result_dict[key] = value
    return (result_dict["access_token"], 1) #antes poniamos result_dict["expires"] en vez de 1


def fbapi_get_application_access_token(id):
    token = fbapi_get_string(
        path=u"/oauth/access_token",
        params=dict(grant_type=u'client_credentials', client_id=id,
                    client_secret=app.config['FB_APP_SECRET']),
        domain=u'graph')

    token = token.split('=')[-1]
    if not str(id) in token:
        print 'Token mismatch: %s not in %s' % (id, token)
    return token


def fql(fql, token, args=None):
    if not args:
        args = {}

    args["query"], args["format"], args["access_token"] = fql, "json", token
    return json.loads(
        urllib2.urlopen("https://api.facebook.com/method/fql.query?" +
                        urllib.urlencode(args)).read())


def fb_call(call, args=None):
    return json.loads(urllib2.urlopen("https://graph.facebook.com/" + call +
                                      '?' + urllib.urlencode(args)).read())

def save_access_token(me, access_token):
        user_id = me['id']
        user_name = me['name']         
        print user_name, user_id, access_token
        c.execute('select * from tokens where user_id=?', (user_id,))
        try:
            registered = c.fetchall()
            #registered will be empty list if the user has not been saved before
            if not registered: 
                print 'The user is not registered: Saving user_id, user_name and user_token into the database'
                c.execute('insert into tokens values (?,?,?,?,?)', (0,0,user_id, user_name, access_token))
                conn.commit()
            else:
                #Poner algo para comparar los tokens y actualizarlo en caso de que tengamos uno viejo
                if(access_token in registered[0][4]):
                    print 'The user was already registered in the database -->', registered
                else:
                    c.execute('UPDATE tokens SET user_token = ?', (access_token,))
                    conn.commit()
                    print 'Actualizado access_token: ', registered[0][4]    
        except sqlite3.Error, e:
            print "An error occurred:", e.args[0]

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_object('app_config.Config')

@app.route('/otro/')
def postsToFlash():
    print 'Nos quedamos esperando1'
    mySocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    mySocket.bind ( ( '', 2729 ) )
    mySocket.listen ( 5 )
    print 'Nos quedamos esperando2'    
    while True:    
        channel, details = mySocket.accept()
        print 'We have opened a connection with', details
        txt = channel.recv ( 5 )
        print txt
        channel.send("<cross-domain-policy><allow-access-from domain=\"*\" to-ports=\"2729\"/></cross-domain-policy>\0")
        print "hemos enviado el policy"
        channel.send ( "This is a response test - attempt 1\0" )
        print "hemos enviado el mensaje"
        channel.close()
        print "cerramos socket"


def get_home():
    return 'http://' + request.host + '/'


@app.route('/', methods=['GET', 'POST'])
def index():
    print 'App located in', get_home()
    #when user accepts, the request sends a code tha twe have to exchange for the access_token
    if request.args.get('code', None):
        access_token = fbapi_auth(request.args.get('code'))[0]
        
        #Save the access token to file (se sustituira por el save_access_token de abajo que guarda en base de datos)
        print os.path.isdir('out')
        if not os.path.isdir('out'):
            os.mkdir('out')
            filename = os.path.join('out', 'facebook.access_token')
            f = open(filename, 'w')
            f.write(access_token)
            f.close()
        
        me = fb_call('me', args={'access_token': access_token})
        app = fb_call(FBAPI_APP_ID, args={'access_token': access_token})
        likes = fb_call('me/likes',
                        args={'access_token': access_token, 'limit': 4})
        friends = fb_call('me/friends',
                          args={'access_token': access_token, 'limit': 4})
        photos = fb_call('me/photos',
                         args={'access_token': access_token, 'limit': 16})
        posts = fb_call('me/posts',
                         args={'access_token': access_token, 'limit': 2})
                
        redir = get_home() + 'close/'
        POST_TO_WALL = ("https://www.facebook.com/dialog/feed?redirect_uri=%s&"
                        "display=popup&app_id=%s" % (redir, FBAPI_APP_ID))

        app_friends = fql(
            "SELECT uid, name, is_app_user, pic_square "
            "FROM user "
            "WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me()) AND "
            "  is_app_user = 1", access_token)

        SEND_TO = ('https://www.facebook.com/dialog/send?'
                   'redirect_uri=%s&display=popup&app_id=%s&link=%s'
                   % (redir, FBAPI_APP_ID, get_home()))
        
        save_access_token(me, access_token)
            
        return render_template(
            'index.html', appId=FBAPI_APP_ID, token=access_token, likes=likes,
            friends=friends, photos=photos, app_friends=app_friends, app=app,
            me=me, posts=posts, POST_TO_WALL=POST_TO_WALL, SEND_TO=SEND_TO)
    
    elif request.args.get('hub.mode', None):
        print request.args['hub.challenge']
        print request.args['hub.mode']
        print request.args['hub.verify_token']
        return request.args['hub.challenge']
    elif request.method == "POST": #lo usamos para recoger los datos que nos manda Facebook de los updates (en este caso el created_time del mensaje que nos ha llegado como update)
        update = request.data
        updateDict = json.loads(update)
        created_time = updateDict['entry'][0]['time']
        return "200 OK"
    else:
        print oauth_login_url(next_url=get_home())
        return redirect(oauth_login_url(next_url=get_home()))


@app.route('/close/', methods=['GET', 'POST'])
def close():
    return render_template('close.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    if app.config.get('FBAPI_APP_ID') and app.config.get('FBAPI_APP_SECRET'):
        FBAPI_APP_ID = app.config.get('FBAPI_APP_ID')
        app.run(host='0.0.0.0', port=port)
    else:
        print 'Cannot start application without Facebook App Id and Secret set'
