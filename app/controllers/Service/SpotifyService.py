import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID="2b5da941f2bd45be90335c85663ce744"
CLIENT_SECRET="4401ec7039cd4d1396f4c74f88756e88"
client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret=CLIENT_SECRET)

class SpotifyService:
  sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)