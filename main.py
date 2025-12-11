import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

CLIENT_ID =  os.getenv("CLIENT_ID")        # regenerate this!
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

# Scrape Billboard
response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Authenticate Spotify
oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="https://127.0.0.1:8888/callback",
    scope="playlist-modify-private",
    cache_path="token.txt",
    show_dialog=True
)

sp = spotipy.Spotify(auth_manager=oauth)

user = sp.current_user()["id"]

# Search each song
song_uris = []
for song in song_names:
    result = sp.search(q=song, type="track")

    if result["tracks"]["items"]:
        song_uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    else:
        print(f"Song '{song}' not found on Spotify")

# Create playlist
playlist_name = f"Billboard Hot 100 - {date}"
playlist = sp.user_playlist_create(
    user=user,
    name=playlist_name,
    description=f"Top Billboard 100 songs from {date}",
    public=False
)

# Add songs
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"Playlist created: {playlist['external_urls']['spotify']}")
