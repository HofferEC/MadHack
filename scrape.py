import requests
from bs4 import BeautifulSoup
import re
import random


def get_line(keyword):
    page = requests.get(
        "https://search.azlyrics.com/search.php?q=" + keyword + "&w=songs&p=1"
    )
    soup = BeautifulSoup(page.text, "html.parser")
    song_list = soup.find_all("a")

    valid_songs = []
    for song in song_list:
        if "https://www.azlyrics.com/lyrics/" in song.get("href"):
            valid_songs.append(song.get("href"))

    random.shuffle(valid_songs)
    for song in valid_songs:
        new_page = requests.get(song)
        new_soup = BeautifulSoup(new_page.text, "html.parser")
        lyrics = new_soup.find_all("div")[21]
        filtered_lyrics = lyrics.text.replace("<\br>", "")
        filtered_lyrics_lines = filtered_lyrics.split("\n")

        for value in filtered_lyrics_lines:
            if value.split(" ")[-1] == keyword:
                return value


