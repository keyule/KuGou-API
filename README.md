#KuGou API
Just some documentation on KuGou's API and some scripts  
This would help people outside of China, and not get hit with 'Area not Supported'

## Example Scripts:

* Download Song
* Play Song

## Search Song

##### URL
```
http://msearchcdn.kugou.com/api/v3/search/song?
```
##### Params
###### Required
Field | Description
------------ | -------------
plat | plat=0 is required
keyword | What you want to search for
###### Optional
Field | Description
------------ | -------------
tagtype | 全部(Show All), DJ, 现场, 广场舞, 伴奏, 铃声 
tag_aggr | 1 to show aggregates of each tag type
highlight | highlights the title eg: em,br
pagesize | pagesize
page | page
Others that I have no idea does what: showtype, sver, correct, api_ver, version, tag, with_res_tag

##### Example
Searching for 安静 but only live versions. Return first 5 results
```
http://msearchcdn.kugou.com/api/v3/search/song?&plat=0&keyword=安静&tagtype=现场&pagesize=5
```
<details>
  <summary>Response</summary>
```javascript
{
    "status": 1,
    "error": "",
    "data": {
        "aggregation": [{
            "key": "DJ",
            "count": 0
        }, {
            "key": "现场",
            "count": 0
        }, {
            "key": "广场舞",
            "count": 0
        }, {
            "key": "伴奏",
            "count": 0
        }, {
            "key": "铃声",
            "count": 0
        }],
        "tab": "现场",
        "info": [{
            "othername_original": "2017地表最强演唱会台北站",
            "pay_type_320": 0,
            "m4afilesize": 1395353,
            "price_sq": 0,
            "isoriginal": 0,
            "filesize": 5446149,
            "source": "",
            "bitrate": 128,
            "topic": "",
            "trans_param": {
                "cid": -1,
                "pay_block_tpl": 1,
                "musicpack_advance": 0,
                "display_rate": 1,
                "display": 32,
                "cpy_attr0": 0
            },
            "price": 0,
            "Accompany": 1,
            "old_cpy": 1,
            "songname_original": "不该+解脱+黑色幽默+安静+如果你也听说+稻香+渴了",
            "singername": "周杰伦、张惠妹",
            "pay_type": 0,
            "sourceid": 0,
            "topic_url": "",
            "fail_process_320": 0,
            "pkg_price": 0,
            "feetype": 0,
            "filename": "周杰伦、张惠妹 - 不该+解脱+黑色幽默+安静+如果你也听说+稻香+渴了 (2017地表最强演唱会台北站)",
            "price_320": 0,
            "songname": "不该+解脱+黑色幽默+安静+如果你也听说+稻香+渴了 (2017地表最强演唱会台北站)",
            "group": [],
            "hash": "f75c0b440acbb11cc5849bf68902c295",
            "mvhash": "4154539a8a0bc26793c0fe579c802a4c",
            "rp_type": "audio",
            "privilege": 0,
            "album_audio_id": 123951555,
            "rp_publish": 1,
            "album_id": "",
            "ownercount": 30,
            "fold_type": 0,
            "audio_id": 47478040,
            "pkg_price_sq": 0,
            "320filesize": 0,
            "isnew": 0,
            "duration": 340,
            "pkg_price_320": 0,
            "srctype": 1,
            "fail_process_sq": 0,
            "sqfilesize": 0,
            "fail_process": 0,
            "320hash": "",
            "extname": "mp3",
            "sqhash": "",
            "pay_type_sq": 0,
            "320privilege": 0,
            "sqprivilege": 0,
            "album_name": "",
            "othername": ""
        }],
        "correctiontype": 0,
        "timestamp": 1608357835,
        "allowerr": 0,
        "total": 59,
        "istag": 0,
        "istagresult": 0,
        "forcecorrection": 0,
        "correctiontip": ""
    },
    "errcode": 0
}

```
</details>