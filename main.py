import os
from flask import Flask, session, request, redirect, render_template, url_for
from flask_session import Session
import spotipy
import ssl
import io
from colorthief import ColorThief
from urllib.request import urlopen
import numpy


ssl._create_default_https_context = ssl._create_unverified_context
os.environ['SPOTIPY_CLIENT_ID'] = 'SPOTIFY CLIENT ID HERE'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'SPOTIFY CLIENT SECRET HERE'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:5000'


app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)


@app.route('/')
def index():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-read-currently-playing user-modify-playback-state user-read-playback-state', cache_handler=cache_handler, show_dialog=False)

    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/')

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url()
        return render_template('sign_in.html', auth_url=auth_url)

    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return render_template('home.html', name = spotify.me()["display_name"])


@app.route('/signout')
def signout():
    session.pop("token_info", None)
    return redirect('/')


@app.route('/gradient', methods = ['GET', 'POST'])
def gradient():

    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, scope='user-read-currently-playing user-modify-playback-state user-read-playback-state')
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    try:

        if request.method == 'POST':

            if request.form['submit'] == '⏮':
                spotify.previous_track()
                return redirect('/gradient')

            if request.form['submit'] == '⏯':
                if (spotify.current_playback()["actions"]["disallows"] == {'resuming': True}):
                    spotify.pause_playback()
                    return redirect('/gradient')
                else:
                    spotify.start_playback()
                    return redirect('/gradient')

            if request.form['submit'] == '⏭':
                spotify.next_track()
                return redirect('/gradient')

        for file in os.listdir(os.getcwd()):
            if file.startswith('img'):
                os.remove(file)

        t = spotify.current_user_playing_track()["item"]["name"]
        if (len(t) > 35):
            track =(t[0:35]+'...')
        else:
            track = spotify.current_user_playing_track()["item"]["name"]

        artist = spotify.current_user_playing_track()["item"]["artists"][0]["name"]
        image = spotify.current_user_playing_track()["item"]["album"]["images"][0]["url"]

        fd = urlopen(image)
        f = io.BytesIO(fd.read())
        color_thief = ColorThief(f)
        pallet = color_thief.get_palette(quality=1)
        ar = []
        for i in range (4):
            ar.append((int(pallet[i][0]) + int(pallet[i][1]) + int(pallet[i][2]))/3)
        s = numpy.array(ar)
        sort = numpy.argsort(s)
        a = pallet[sort[0]]
        b = pallet[sort[1]]
        c = pallet[sort[2]]
        d = pallet[sort[3]]
        if (sum(ar) < 350):
            txt = '#FFFFFF'
        else:
            txt = '#000000'

        dr = int(spotify.current_user_playing_track()["item"]["duration_ms"])
        pg = int(spotify.current_user_playing_track()["progress_ms"])
        time = (dr-pg)/1000

        if (spotify.current_playback()["actions"]["disallows"] == {'pausing': True}):
            time = 'none'

    except TypeError or UnboundLocalError:
        track = "Your Player Is Idle"
        artist = "Please Refresh After Playing"
        image = url_for('static', filename='idle.jpeg')
        txt = '#FFFFFF'
        a = '(238, 119, 82)'
        b = '(231, 60, 126)'
        c = '(35, 166, 213)'
        d = '(35, 213, 171)'
        time = 'none'
    
    except spotipy.exceptions.SpotifyException:
        return render_template('prem.html')

    return render_template('gradient.html', track = track, artist = artist, image=image, a=a, b=b, c=c, d=d, txt=txt, time=time)


@app.route('/turntable', methods=['GET', 'POST'])
def turntable():

    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, scope='user-read-currently-playing user-modify-playback-state user-read-playback-state')
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    try:

        if request.method == 'POST':

            if request.form['submit'] == '⏮':
                spotify.previous_track()
                return redirect('/turntable')

            if request.form['submit'] == '⏯':
                if (spotify.current_playback()["actions"]["disallows"] == {'resuming': True}):
                    spotify.pause_playback()
                    return redirect('/turntable')
                else:
                    spotify.start_playback()
                    return redirect('/turntable')

            if request.form['submit'] == '⏭':
                spotify.next_track()
                return redirect('/turntable')

        for file in os.listdir(os.getcwd()):
            if file.startswith('img'):
                os.remove(file)

        t = spotify.current_user_playing_track()["item"]["name"]
        if (len(t) > 12):
            track =(t[0:12]+'...')
        else:
            track = spotify.current_user_playing_track()["item"]["name"]

        artist = spotify.current_user_playing_track()["item"]["artists"][0]["name"]
        image = spotify.current_user_playing_track()["item"]["album"]["images"][0]["url"]

        dr = int(spotify.current_user_playing_track()["item"]["duration_ms"])
        pg = int(spotify.current_user_playing_track()["progress_ms"])
        time = (dr-pg)/1000
        animation = '2s'

        if (spotify.current_playback()["actions"]["disallows"] == {'pausing': True}):
            time = 'none'
            animation = 'none'

    except TypeError or UnboundLocalError:
        track = "Your Player Is Idle"
        artist = "Please Refresh After Playing"
        image = 'https://upload.wikimedia.org/wikipedia/commons/a/a8/Ski_trail_rating_symbol_black_circle.png'
        time = 'none'
        animation = 'none'
    
    except spotipy.exceptions.SpotifyException:
        return render_template('prem.html')

    return render_template('turntable.html', image=image, time=time, record = url_for('static', filename='record.png'), track=track, logo=url_for('static', filename='logo.png'), needle = url_for('static', filename='needle.png'), rod = url_for('static', filename='rod.png'), animation=animation)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)