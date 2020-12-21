'''
Downloads the top 100 songs for that particular ranking list
Example: Ranking ID = 6666

Requirements:
requests
json

'''

import json
import requests

def get_volID(ranklistID):
    url = 'http://mobilecdnbj.kugou.com/api/v3/rank/vol?ranktype=2&plat=0&rankid=' + str(ranklistID) +'&with_res_tag=1'
    response = requests.get(url)
    data = response.text
    data = data.partition('START-->')[2]
    data = data.partition('<!--')[0]
    data = json.loads(data)
    return data['data']['info'][0]['vols'][0]['volid']

def print_list(ranklistID, volID):
    url = 'http://mobilecdnbj.kugou.com/api/v3/rank/song?version=9108&ranktype=2&plat=0&pagesize=100&area_code=1&page=1&volid='+ str(volID) + '&rankid=' + str(ranklistID) +'&with_res_tag=1'
    response = requests.get(url)
    data = response.text
    data = data.partition('START-->')[2]
    data = data.partition('<!--')[0]
    data = json.loads(data)
    ranking = 1
    for song in data['data']['info']:
        string = str(ranking) + '. ' + song['filename'] + ' | hash: ' + song['hash'] + ' | album_id: ' + song['album_id']
        print(string)
        ranking = ranking + 1

    return

if __name__ == '__main__':
    ranklistID = input('Ranking ID:')
    volID = get_volID(ranklistID)
    print_list(ranklistID, volID)