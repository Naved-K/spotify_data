#!/usr/bin/python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

cid ="d3771655f20b47bd83c1e71dd2187b6b" 
secret = "f7be4d6c13734e7588c8941a29354e1c"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []
popularity = []

for i in range(0,2):
    track_results = sp.search(q='year:2018', type='track', limit=50)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        popularity.append(t['popularity'])
df_tracks = pd.DataFrame({'artist_name':artist_name,'track_name':track_name,'popularity':popularity})
df_tracks.to_csv('data.csv')

lil_artists = []
lil_popularity = []

for i in range(0,2):
    lil_results = sp.search(q='lil', type='artist', limit=50, offset = 1,market = 'US')
    for i, t in enumerate(lil_results['artists']['items']):
        lil_artists.append(t['name'])
        lil_popularity.append(t['popularity'])
df2 = pd.DataFrame({'lil_artists':lil_artists, 'lil_popularity':lil_popularity})
df2.to_csv('data2.csv')

song_name = []
song_explicit = []
for i in range(0,2):
    hello_songs = sp.search(q="hello", type='track', limit=50, offset = 1)
    for i, t in enumerate(hello_songs['tracks']['items']):
        song_name.append(t['name'])
        if song_explicit.append(t['explicit']) == "FALSE" :
            song_explicit.append("No")
        else:
            song_explicit.append("Yes")

df3 = pd.DataFrame({'explicit':song_explicit,'song_name':song_name})
df3.to_csv('data3.csv')


    