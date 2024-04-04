
# from flask import Flask, request, redirect
# import requests
# import json
# import urllib.parse

# app = Flask(__name__)

# # Spotify API credentials
# CLIENT_ID = 'daeea42af07e4702905904f246591317'
# CLIENT_SECRET = '3ef2f6e66658400490e6add0739a9a3b'
# REDIRECT_URI = 'http://localhost:5000/callback'
# ENCODED_REDIRECT_URI = urllib.parse.quote(REDIRECT_URI, safe='')

# @app.route('/')
# def index():
#     return '<a href="/login">Login with Spotify</a>'

# @app.route('/login')
# def login():
#     # Redirect user to Spotify login page
#     return redirect('https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope=user-top-read'.format(CLIENT_ID, REDIRECT_URI))

# @app.route('/callback')
# def callback():
#     # Exchange the code for an access token
#     code = request.args.get('code')
#     token_response = requests.post('https://accounts.spotify.com/api/token', data={
#         'grant_type': 'authorization_code',
#         'code': code,
#         'redirect_uri': REDIRECT_URI,
#         'client_id': CLIENT_ID,
#         'client_secret': CLIENT_SECRET
#     })

#     access_token = token_response.json().get('access_token')

#     if access_token:
#         # Fetch user's top tracks
#         headers = {'Authorization': 'Bearer ' + access_token}
#         top_tracks_response = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers)
#         top_tracks = top_tracks_response.json()

#         return json.dumps(top_tracks)
#     else:
#         return 'Failed to retrieve access token'

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, redirect
import requests
import json
import urllib.parse

app = Flask(__name__)

# Spotify API credentials
CLIENT_ID = 'daeea42af07e4702905904f246591317'
CLIENT_SECRET = '3ef2f6e66658400490e6add0739a9a3b'
REDIRECT_URI = 'http://localhost:5000'
ENCODED_REDIRECT_URI = urllib.parse.quote(REDIRECT_URI, safe='')

@app.route('/')
def index():
    return '<a href="/login">Login with Spotify</a>'

@app.route('/login')
def login():
    # Redirect user to Spotify login page with encoded redirect URI
    return redirect('https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope=user-top-read'.format(CLIENT_ID, ENCODED_REDIRECT_URI))

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
        # Fetch user's top tracks
        headers = {'Authorization': 'Bearer ' + access_token}
        top_tracks_response = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers)
        top_tracks = top_tracks_response.json()

        return json.dumps(top_tracks)
    else:
        return 'Failed to retrieve access token'

if __name__ == '__main__':
    app.run(debug=True)

