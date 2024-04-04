from flask import Flask, request, redirect, render_template
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Spotify API credentials
CLIENT_ID = 'daeea42af07e4702905904f246591317'
CLIENT_SECRET = '3ef2f6e66658400490e6add0739a9a3b'
REDIRECT_URI = 'http://localhost:5000/callback'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    # Redirect user to Spotify login page
    return redirect('https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope=user-top-read'.format(CLIENT_ID, REDIRECT_URI))

@app.route('/callback')
def callback():
    # Exchange the code for an access token
    code = request.args.get('code')
    token_response = requests.post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    })

    access_token = token_response.json().get('access_token')

    if access_token:
        # Fetch user's top artists
        headers = {'Authorization': 'Bearer ' + access_token}
        top_artists_response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers)
        top_artists = top_artists_response.json()

        # Pass top artists data to myArtists.html template
        return render_template('myArtists.html', top_artists=top_artists)
    else:
        return 'Failed to retrieve access token'

if __name__ == '__main__':
    app.run(debug=True)
