<!-- README.md -->
<h1 align="center">🎵 Billboard → Spotify Playlist</h1>

<p align="center">
  This project is a Python automation tool that takes any date in the format YYYY-MM-DD, scrapes the Billboard Hot 100 chart for that day, and automatically creates a private Spotify playlist with the available songs. It uses web scraping to collect track names from Billboard.com, then connects to the Spotify Web API via Spotipy to search for each song and add it to a newly created playlist in the user’s account. The result is a fast and seamless way to recreate nostalgic or historical music charts as Spotify playlists with a single command.
</p>

---

## ✨ Quick overview
- Enter a date (YYYY-MM-DD).  
- Script scrapes the Billboard Hot 100 for that date.  
- Searches Spotify for each track, creates a private playlist, and adds the found songs.  
- Perfect for nostalgia trips and making curated throwback playlists.

---

## 🚀 Quick start

```bash
# clone
git clone https://github.com/deepthi-sree123/billboard-spotify-playlist.git
cd billboard-spotify-playlist

# install
pip install requests beautifulsoup4 spotipy

# run
python main.py
