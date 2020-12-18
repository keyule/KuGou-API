'''
Plays a song given a URL as input
Example URL: https://www.kugou.com/song/#hash=FBD3B28DD04462E3A681A9BC5E9D37C0&album_id=20795407

Requirements:
requests
tqdm 
vlc
json
'''

import requests
import re
import json
import sys
import vlc
import time
from time import sleep
from tqdm import tqdm

def get_data(url):    
    baseURL = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19107732973609967178_1607543233092&mid=1&'

    songHash = url.partition("song/#")[2]
    queryURL = baseURL + songHash

    response = requests.get(queryURL)
    data = (response.text).partition("jQuery19107732973609967178_1607543233092(")[2]
    data = data[:-2]
    return json.loads(data)

def play_song(url):
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
    player=instance.media_player_new()
    media=instance.media_new(url)
    player.set_media(media)
    player.play()
    time.sleep(5)
    while player.is_playing():
        sleep(1)
    print('Finish')


if __name__ == '__main__':
    raw_url = input('song URL:')
    data = get_data(raw_url)

    fname = data["data"]['audio_name'] + '.mp3'
    downloadUrl = data['data']['play_url']

    print(f"playing {fname}... Ctrl+C to stop")
    play_song(downloadUrl)
