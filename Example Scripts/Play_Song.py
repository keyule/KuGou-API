#!/usr/bin/env python3

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

def download_file(url,fname):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open(fname, 'wb') as file, tqdm(
            desc=fname,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

    print('Download Complete')
    return

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
    #download_file(downloadUrl,fname)
    print(f"playing {fname}... Ctrl+C to stop")
    play_song(downloadUrl)
