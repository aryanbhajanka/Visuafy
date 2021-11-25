#Visuafy a Spotify visualiser by Aryan Bhajanka

from os import name
from flask import Flask, request, url_for, session, redirect, render_template
from flask.helpers import get_template_attribute
import spotipy
from spotipy.exceptions import SpotifyException
from spotipy.oauth2 import SpotifyOAuth, SpotifyOauthError

app = Flask(__name__, static_folder='static')
app.secret_key = "7490017841visuafy7490017841"
app.config['SESSION_COOKIE_NAME'] = 'spotify-user-read-currently-playing'
scope = "user-read-currently-playing"

@app.route('/', methods =["GET", "POST"])
def login():
    if request.method == "POST":
       session['token'] = request.form.get("oauth")
       return redirect (url_for('select_theme', _external = True))
    return render_template("token.html")

@app.route('/colours')
def colours():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        return render_template ("index.html", name = song_name, artist = song_artist, image = artist_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/moonlight')
def moon():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        return render_template ("city.html", name = song_name, artist = song_artist, image = artist_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/leo_the_cat')
def leo_the_cat():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        return render_template ("leo_the_cat.html", name = song_name, artist = song_artist, image = artist_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/ship')
def lofi_ship():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        return render_template ("ship.html", name = song_name, artist = song_artist, image = artist_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/homework')
def homework():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        return render_template ("homework.html", name = song_name, artist = song_artist, image = artist_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/by_the_window')
def by_the_window():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        return render_template ("by_the_window.html", name = song_name, artist = song_artist, image = artist_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/on_the_road')
def on_the_road():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        return render_template ("on_the_road.html", name = song_name, artist = song_artist, image = artist_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/comfy_night')
def comfy_night():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        return render_template ("comfy_night.html", name = song_name, artist = song_artist, image = artist_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/custom_image', methods =["GET", "POST"])
def custom_image():
    if request.method == "POST":
       session['image_address'] = request.form.get("imagead")
       return redirect (url_for('custom_theme', _external = True))
    return render_template("custom_image.html")

@app.route('/custom_theme')
def custom_theme():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        custom_image = session['image_address']
        return render_template ("custom_theme.html", name = song_name, artist = song_artist, image = artist_image, custom_image = custom_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/la')
def la():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        return render_template ("la.html", name = song_name, artist = song_artist, image = artist_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/nyc')
def nyc():
    try:
        token = session['token']
        spotify = spotipy.Spotify(token)
        current_song =  spotify.currently_playing(market="ES")
        song_item = current_song.get("item")
        song_name = (song_item['name'])
        song_artist = (song_item['artists'][0]['name'])
        image_result = spotify.search(q='artist:'+song_artist, type='artist')
        items = image_result['artists']['items']
        artist = items[0]
        artist_image = (artist['images'][0]['url'])
        return render_template ("nyc.html", name = song_name, artist = song_artist, image = artist_image)
    except AttributeError:
        return render_template ('none.html')
    except SpotifyException:
        return redirect (url_for('login', _external = True))
    except NameError:
        return redirect (url_for('login', _external = True))

@app.route('/info')
def info():
    return render_template ("info.html")

@app.route('/select_theme')
def select_theme():
    return render_template ("select_theme.html")

@app.route('/help')
def help():
    return render_template ("help.html")

@app.route('/credits')
def credits():
    return render_template ("credits.html")

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "28b4cc3000d54dcd86e32d2d59719787",
        client_secret = "119bd035eea54111aa915b747ab2e204",
        redirect_uri = url_for('redirectpage', _external = True),
        scope = "user-read-currently-playing")

if __name__ == '__main__':
    app.run()