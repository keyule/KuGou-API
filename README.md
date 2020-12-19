# KuGou API
Just some documentation on KuGou's API and some scripts  
This would help people outside of China, and not get hit with 'Area not Supported'

## Example Scripts:

* Download Song
* Play Song

## Search Song

#### URL
```
http://msearchcdn.kugou.com/api/v3/search/song?
```
#### Params
##### Required
Field | Description
------------ | -------------
plat | plat=0 is required
keyword | What you want to search for
##### Optional
Field | Description
------------ | -------------
tagtype | 全部(Show All), DJ, 现场, 广场舞, 伴奏, 铃声 
tag_aggr | 1 to show aggregates of each tag type
highlight | highlights the title eg: em,br
pagesize | pagesize
page | page
  
Others that I have no idea does what: *showtype, sver, correct, api_ver, version, tag, with_res_tag*

#### Example
Searching for 安静 all versions. Return 1 result
```
http://msearchcdn.kugou.com/api/v3/search/song?&plat=0&keyword=安静&tagtype=全部&pagesize=1
```
<details><summary>Response:</summary>
  
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
        "tab": "",
        "info": [{
            "othername_original": "",
            "pay_type_320": 0,
            "m4afilesize": 1372372,
            "price_sq": 0,
            "isoriginal": 1,
            "filesize": 5349921,
            "source": "",
            "bitrate": 128,
            "topic": "",
            "trans_param": {
                "cid": -1,
                "pay_block_tpl": 1,
                "musicpack_advance": 0,
                "display_rate": 0,
                "display": 0,
                "cpy_attr0": 0
            },
            "price": 0,
            "Accompany": 1,
            "old_cpy": 1,
            "songname_original": "安静",
            "singername": "周杰伦",
            "pay_type": 0,
            "sourceid": 0,
            "topic_url": "",
            "fail_process_320": 0,
            "pkg_price": 0,
            "feetype": 0,
            "filename": "周杰伦 - 安静",
            "price_320": 0,
            "songname": "安静",
            "group": [],
            "hash": "45f763d7beb1fd000af890eb6c70b9a2",
            "mvhash": "3b87ec9136e850f977d0ac9d1c626b59",
            "rp_type": "audio",
            "privilege": 0,
            "album_audio_id": 38166666,
            "rp_publish": 1,
            "album_id": "1589936",
            "ownercount": 23,
            "fold_type": 0,
            "audio_id": 2565477,
            "pkg_price_sq": 0,
            "320filesize": 13371558,
            "isnew": 0,
            "duration": 334,
            "pkg_price_320": 0,
            "srctype": 1,
            "fail_process_sq": 0,
            "sqfilesize": 37912735,
            "fail_process": 0,
            "320hash": "e97cde7c3528b50dc5b869ddc2e0f5de",
            "extname": "mp3",
            "sqhash": "06bdeb695f0645ebf19e99fec5d001a4",
            "pay_type_sq": 0,
            "320privilege": 0,
            "sqprivilege": 0,
            "album_name": "他&他 好男真情歌",
            "othername": ""
        }],
        "correctiontype": 0,
        "timestamp": 1608359604,
        "allowerr": 0,
        "total": 461,
        "istag": 0,
        "istagresult": 0,
        "forcecorrection": 0,
        "correctiontip": ""
    },
    "errcode": 0
}
  ```

</details>

## Get Song Data

#### URL
```
https://wwwapi.kugou.com/yy/index.php?r=play/getdata
```
#### Params
##### Required
Field | Description
------------ | -------------
callback | jQuery19107732973609967178_1607543233092 *required no idea what it is*
mid | =1 *can be almost any number*
hash | hash of the song
album_id | album ID of the song

##### Optional
Others: *platid, dfid, _*

#### Example
Getting Details of 安静 from our search earlier
```
https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19107732973609967178_1607543233092&mid=1&hash=45f763d7beb1fd000af890eb6c70b9a2&album_id=1589936
```
<details><summary>Response:</summary>
  
  ```javascript
jQuery19107732973609967178_1607543233092({
    "status": 1,
    "err_code": 0,
    "data": {
        "hash": "45f763d7beb1fd000af890eb6c70b9a2",
        "timelength": 334000,
        "filesize": 5349921,
        "audio_name": "\u5468\u6770\u4f26 - \u5b89\u9759",
        "have_album": 1,
        "album_name": "\u4ed6&\u4ed6 \u597d\u7537\u771f\u60c5\u6b4c",
        "album_id": "1589936",
        "img": "http:\/\/imge.kugou.com\/stdmusic\/20200909\/20200909110347808587.jpg",
        "have_mv": 1,
        "video_id": "756685",
        "author_name": "\u5468\u6770\u4f26",
        "song_name": "\u5b89\u9759",
        "lyrics": "\ufeff[id:$00000000]\r\n[ar:\u5468\u6770\u4f26]\r\n[ti:\u5b89\u9759]\r\n[by:]\r\n[hash:45f763d7beb1fd000af890eb6c70b9a2]\r\n[al:]\r\n[sign:]\r\n[qq:]\r\n[total:334488]\r\n[offset:0]\r\n[00:00.78]\u5468\u6770\u4f26 - \u5b89\u9759\r\n[00:02.36]\u4f5c\u8bcd\uff1a\u5468\u6770\u4f26\r\n[00:03.89]\u4f5c\u66f2\uff1a\u5468\u6770\u4f26\r\n[00:27.91]\u53ea\u5269\u4e0b\u94a2\u7434\u966a\u6211\u5f39\u4e86\u4e00\u5929\r\n[00:33.19]\u7761\u7740\u7684\u5927\u63d0\u7434\r\n[00:36.54]\u5b89\u9759\u7684\u65e7\u65e7\u7684\r\n[00:41.22]\u6211\u60f3\u4f60\u5df2\u8868\u73b0\u7684\u975e\u5e38\u660e\u767d\r\n[00:46.45]\u6211\u61c2\u6211\u4e5f\u77e5\u9053\r\n[00:49.80]\u4f60\u6ca1\u6709\u820d\u4e0d\u5f97\r\n[00:54.67]\u4f60\u8bf4\u4f60\u4e5f\u4f1a\u96be\u8fc7\u6211\u4e0d\u76f8\u4fe1\r\n[01:01.17]\u7275\u7740\u4f60\u966a\u7740\u6211\u4e5f\u53ea\u662f\u66fe\u7ecf\r\n[01:07.12]\u5e0c\u671b\u4ed6\u662f\u771f\u7684\u6bd4\u6211\u8fd8\u8981\u7231\u4f60\r\n[01:13.68]\u6211\u624d\u4f1a\u903c\u81ea\u5df1\u79bb\u5f00\r\n[01:21.50]\u4f60\u8981\u6211\u8bf4\u591a\u96be\u582a\r\n[01:24.75]\u6211\u6839\u672c\u4e0d\u60f3\u5206\u5f00\r\n[01:28.05]\u4e3a\u4ec0\u4e48\u8fd8\u8981\u6211\u7528\u5fae\u7b11\u6765\u5e26\u8fc7\r\n[01:34.85]\u6211\u6ca1\u6709\u8fd9\u79cd\u5929\u5206\r\n[01:38.00]\u5305\u5bb9\u4f60\u4e5f\u63a5\u53d7\u4ed6\r\n[01:41.40]\u4e0d\u7528\u62c5\u5fc3\u7684\u592a\u591a\r\n[01:44.76]\u6211\u4f1a\u4e00\u76f4\u597d\u597d\u8fc7\r\n[01:48.05]\u4f60\u5df2\u7ecf\u8fdc\u8fdc\u79bb\u5f00\r\n[01:51.45]\u6211\u4e5f\u4f1a\u6162\u6162\u8d70\u5f00\r\n[01:54.70]\u4e3a\u4ec0\u4e48\u6211\u8fde\u5206\u5f00\u90fd\u8fc1\u5c31\u7740\u4f60\r\n[02:01.51]\u6211\u771f\u7684\u6ca1\u6709\u5929\u5206\r\n[02:04.76]\u5b89\u9759\u7684\u6ca1\u8fd9\u4e48\u5feb\r\n[02:08.32]\u6211\u4f1a\u5b66\u7740\u653e\u5f03\u4f60\r\n[02:11.53]\u662f\u56e0\u4e3a\u6211\u592a\u7231\u4f60\r\n[02:28.22]\u53ea\u5269\u4e0b\u94a2\u7434\u966a\u6211\u5f39\u4e86\u4e00\u5929\r\n[02:33.50]\u7761\u7740\u7684\u5927\u63d0\u7434\r\n[02:36.85]\u5b89\u9759\u7684\u65e7\u65e7\u7684\r\n[02:41.57]\u6211\u60f3\u4f60\u5df2\u8868\u73b0\u7684\u975e\u5e38\u660e\u767d\r\n[02:46.80]\u6211\u61c2\u6211\u4e5f\u77e5\u9053\r\n[02:50.25]\u4f60\u6ca1\u6709\u820d\u4e0d\u5f97\r\n[02:54.92]\u4f60\u8bf4\u4f60\u4e5f\u4f1a\u96be\u8fc7\u6211\u4e0d\u76f8\u4fe1\r\n[03:01.46]\u7275\u7740\u4f60\u966a\u7740\u6211\u4e5f\u53ea\u662f\u66fe\u7ecf\r\n[03:07.61]\u5e0c\u671b\u4ed6\u662f\u771f\u7684\u6bd4\u6211\u8fd8\u8981\u7231\u4f60\r\n[03:14.20]\u6211\u624d\u4f1a\u903c\u81ea\u5df1\u79bb\u5f00\r\n[03:22.07]\u4f60\u8981\u6211\u8bf4\u591a\u96be\u582a\r\n[03:25.17]\u6211\u6839\u672c\u4e0d\u60f3\u5206\u5f00\r\n[03:28.52]\u4e3a\u4ec0\u4e48\u8fd8\u8981\u6211\u7528\u5fae\u7b11\u6765\u5e26\u8fc7\r\n[03:35.49]\u6211\u6ca1\u6709\u8fd9\u79cd\u5929\u5206\r\n[03:38.68]\u5305\u5bb9\u4f60\u4e5f\u63a5\u53d7\u4ed6\r\n[03:41.87]\u4e0d\u7528\u62c5\u5fc3\u7684\u592a\u591a\r\n[03:45.17]\u6211\u4f1a\u4e00\u76f4\u597d\u597d\u8fc7\r\n[03:48.78]\u4f60\u5df2\u7ecf\u8fdc\u8fdc\u79bb\u5f00\r\n[03:51.88]\u6211\u4e5f\u4f1a\u6162\u6162\u8d70\u5f00\r\n[03:55.23]\u4e3a\u4ec0\u4e48\u6211\u8fde\u5206\u5f00\u90fd\u8fc1\u5c31\u7740\u4f60\r\n[04:01.99]\u6211\u771f\u7684\u6ca1\u6709\u5929\u5206\r\n[04:05.18]\u5b89\u9759\u7684\u6ca1\u8fd9\u4e48\u5feb\r\n[04:08.58]\u6211\u4f1a\u5b66\u7740\u653e\u5f03\u4f60\r\n[04:11.83]\u662f\u56e0\u4e3a\u6211\u592a\u7231\u4f60\r\n[04:19.63]\u4f60\u8981\u6211\u8bf4\u591a\u96be\u582a\r\n[04:23.03]\u6211\u6839\u672c\u4e0d\u60f3\u5206\u5f00\r\n[04:26.33]\u4e3a\u4ec0\u4e48\u8fd8\u8981\u6211\u7528\u5fae\u7b11\u6765\u5e26\u8fc7\r\n[04:32.88]\u6211\u6ca1\u6709\u8fd9\u79cd\u5929\u5206\r\n[04:36.08]\u5305\u5bb9\u4f60\u4e5f\u63a5\u53d7\u4ed6\r\n[04:39.38]\u4e0d\u7528\u62c5\u5fc3\u7684\u592a\u591a\r\n[04:42.68]\u6211\u4f1a\u4e00\u76f4\u597d\u597d\u8fc7\r\n[04:46.44]\u4f60\u5df2\u7ecf\u8fdc\u8fdc\u79bb\u5f00\r\n[04:49.74]\u6211\u4e5f\u4f1a\u6162\u6162\u8d70\u5f00\r\n[04:53.03]\u4e3a\u4ec0\u4e48\u6211\u8fde\u5206\u5f00\u90fd\u8fc1\u5c31\u7740\u4f60\r\n[04:59.89]\u6211\u771f\u7684\u6ca1\u6709\u5929\u5206\r\n[05:03.08]\u5b89\u9759\u7684\u6ca1\u8fd9\u4e48\u5feb\r\n[05:06.43]\u6211\u4f1a\u5b66\u7740\u653e\u5f03\u4f60\r\n[05:09.78]\u662f\u56e0\u4e3a\u6211\u592a\u7231\u4f60\r\n",
        "author_id": "3520",
        "privilege": 0,
        "privilege2": "0",
        "play_url": "https:\/\/webfs.yun.kugou.com\/202012191434\/6625f5f431060e56dbb8c8c8971398fc\/G076\/M04\/1B\/11\/LJQEAFguljqAeB6KAFGiITyQqts281.mp3",
        "authors": [{
            "author_id": "3520",
            "author_name": "\u5468\u6770\u4f26",
            "is_publish": "1",
            "sizable_avatar": "http:\/\/singerimg.kugou.com\/uploadpic\/softhead\/{size}\/20180515\/20180515002522714.jpg",
            "avatar": "http:\/\/singerimg.kugou.com\/uploadpic\/softhead\/400\/20180515\/20180515002522714.jpg"
        }],
        "is_free_part": 0,
        "bitrate": 128,
        "recommend_album_id": "1589936",
        "audio_id": "2565477",
        "has_privilege": true,
        "play_backup_url": "https:\/\/webfs.cloud.kugou.com\/202012191434\/33c012b1159c61c095b8e7ce28415e7e\/G076\/M04\/1B\/11\/LJQEAFguljqAeB6KAFGiITyQqts281.mp3"
    }
});
  ```
</details>