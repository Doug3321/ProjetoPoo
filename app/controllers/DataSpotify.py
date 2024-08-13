<<<<<<< HEAD
#pip install spotipy
=======
#!pip install spotipy
>>>>>>> 76a9b900c6c00a30769d7b742d7da06ea621a6dc
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID="2b5da941f2bd45be90335c85663ce744"
CLIENT_SECRET="4401ec7039cd4d1396f4c74f88756e88"
<<<<<<< HEAD
client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
busca = sp.search(q='barão', type='album', limit=1)
dic = busca['albums']['items'][0]

print(dic['name'])
print(dic['id'])
print(dic['artists'])
=======
client_credentials_manager = SpotifyClientCredentials(cliente_id = CLENT_ID, client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
>>>>>>> 76a9b900c6c00a30769d7b742d7da06ea621a6dc
