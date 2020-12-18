'''
Downloads a song given a URL as input
Example URL: https://www.kugou.com/song/#hash=FBD3B28DD04462E3A681A9BC5E9D37C0&album_id=20795407

Requirements:
requests
tqdm 
json

'''

import requests
import json
import sys
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

if __name__ == '__main__':
    raw_url = input('song URL:')
    data = get_data(raw_url)

    fname = data["data"]['audio_name'] + '.mp3'
    downloadUrl = data['data']['play_url']

    download_file(downloadUrl,fname)
