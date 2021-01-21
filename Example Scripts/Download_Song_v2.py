'''
Downloads a song given a Hash and Album_ID as input
Example Hash:285e799e87cbd2828ae5e1247aa1d601
        Album ID: 40641376

Requirements:
requests
tqdm 
json

'''


import requests
import re
import json
import sys
from tqdm import tqdm

def get_data(songHash, songalbumid, saveData = True):    
    baseURL = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19107732973609967178_1607543233092&mid=1&'
    queryURL = baseURL + 'hash=' + songHash + '&album_id=' + songalbumid

    response = requests.get(queryURL)
    data = (response.text).partition("jQuery19107732973609967178_1607543233092(")[2]
    data = data[:-2]
    data = json.loads(data)

    if saveData:
        fname = data["data"]['audio_name'] + '.json'
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4) 

    return data


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

if __name__ == '__main__':
    songHash = input('hash:')
    songalbumid = input('album ID:')

    data = get_data(songHash, songalbumid)


    fname = data["data"]['audio_name'] + '.mp3'
    downloadUrl = data['data']['play_url']
    download_file(downloadUrl,fname)
