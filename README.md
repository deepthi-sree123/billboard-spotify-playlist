🎵 Billboard to Spotify Playlist

A Python script that takes any date (YYYY-MM-DD), scrapes the Billboard Hot 100 chart for that day, and automatically creates a private Spotify playlist with the available songs.

🚀 How It Works

Enter a date

Script scrapes Billboard for the top 100 songs

Authenticates with Spotify using Spotipy

Searches each song on Spotify

Creates a playlist in your account and adds the songs

🛠 Requirements

Python 3

requests

beautifulsoup4

spotipy

Install:

pip install requests beautifulsoup4 spotipy

🔐 Setup

Set your Spotify credentials as environment variables in PyCharm:

CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret


Redirect URI used:

https://127.0.0.1:8888/callback

▶ Run
python main.py

📌 Notes

Playlist is private

Some songs may not be available on Spotify
