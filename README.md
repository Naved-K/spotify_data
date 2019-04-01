For this python project, I have exported 3 csv's based off arbitrary data pulled through the Spotify API.
I imported Spotipy, a Python library for the Spotify API to help code this, and used pandas to create dataframes for the CSV files.

For the first dataset, I search for songs in the year 2018. Spotify limits the search by 50 songs, so I run this code twice to get the requested 100. The dataset returns songs with their name, the artist name, and their popularity. 

For the second dataset, I search for artists who have "Lil" in their name. The dataset shows the popularity difference between each artist with "Lil" in their name.

For the third dataset, I search for tracks that have the word "Hello" in it. Then the other column shows whether the song is explicit or not. 

Hope you enjoy my short project!

Naved