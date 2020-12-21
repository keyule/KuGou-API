# KuGou API
Just some documentation on KuGou's API and some scripts  
Most of the other stuff on github for KuGou are all for people inside China and dont work for people outside China  
Hopefully, this would help people outside of China, and not get hit with 'Area not Supported'  

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
tag_aggr | `1` to show aggregates of each tag type
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
  
  ```json
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
callback | `jQuery19107732973609967178_1607543233092` *required no idea what it is*
mid | `1` *can be almost any number*
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
  
  ```json
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

## Get list of Rankings

#### URL
```
http://mobilecdnbj.kugou.com/api/v3/rank/list
```
#### Params
##### Optional
Field | Description
------------ | -------------
withsong | `1` will show the top 3 songs

Others: *version, plat, showtype, parentid, apiver, area_code, with_res*

#### Example
Getting list of Rankings and show top 3 songs
```
http://mobilecdnbj.kugou.com/api/v3/rank/list?withsong=1
```
<details><summary>Response:</summary>

```json
{
    "status": 1,
    "error": "",
    "data": {
        "timestamp": 1608365895,
        "info": [{
            "rankid": 6666,
            "id": 1,
            "intro": "数据来源：酷狗\r\n排序方式：按歌曲搜索播放量的涨幅排序\r\n更新周期：每天",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20200914\/20200914155202513813.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190906\/20190906162522894877.jpg",
            "jump_title": "",
            "rankname": "酷狗飙升榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175722740417.png",
            "jump_url": "",
            "img_9": "",
            "classify": 1,
            "update_frequency": "每天",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190906\/20190906162520714932.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "铭志 - 他只是经过 (完整版)"
            }, {
                "songname": "刘若英 - 成全"
            }, {
                "songname": "黄品源、莫文蔚 - 那么爱你为什么"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20190214\/20190214100333414437.jpg",
            "ranktype": 2,
            "custom_type": 0,
            "issue": 354
        }, {
            "rankid": 8888,
            "id": 2,
            "intro": "数据来源：酷狗\r\n排序方式：按每日歌曲播放总量排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201203\/20201203150402833578.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122516438289.jpg",
            "jump_title": "",
            "rankname": "酷狗TOP500",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175730485341.png",
            "jump_url": "",
            "img_9": "",
            "classify": 1,
            "update_frequency": "每天",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122513972113.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "回小仙 - 醒不来的梦"
            }, {
                "songname": "是七叔呢 - 踏山河"
            }, {
                "songname": "IN-K、王忻辰 - 迷失幻境 (DJ版)"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019122517263545.jpg",
            "ranktype": 2,
            "custom_type": 0,
            "issue": 354
        }, {
            "rankid": 37361,
            "id": 227,
            "intro": "数据来源：浮浮雷达（千万用户的识曲选择，遛街刷抖必备）和酷狗听歌识曲。\r\n排序方式：过去7天识别最多的top100首歌曲，告诉你时下最热歌曲。\r\n更新周期：周一至周五每天",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201203\/20201203124801937215.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190808\/20190808200003312447.jpg",
            "jump_title": "",
            "rankname": "酷狗雷达榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175741530197.png",
            "jump_url": "",
            "img_9": "",
            "classify": 1,
            "update_frequency": "工作日",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190808\/20190808200002300015.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "是七叔呢 - 踏山河"
            }, {
                "songname": "花僮 - 浪子闲话 (加速版)(DJ名龙版)"
            }, {
                "songname": "是七叔呢 - 燕无歇 (DJ黑桃A版)"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20190808\/20190808200005885980.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 252
        }, {
            "rankid": 23784,
            "id": 65,
            "intro": "数据来源：酷狗网络类歌曲\r\n排序方式：按歌曲搜索播放一周总量排序\r\n更新周期：周一",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201203\/20201203150402833578.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122442518606.jpg",
            "jump_title": "",
            "rankname": "网络红歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175751510685.png",
            "jump_url": "",
            "img_9": "",
            "classify": 1,
            "update_frequency": "周一",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122440628627.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "回小仙 - 醒不来的梦"
            }, {
                "songname": "是七叔呢 - 踏山河"
            }, {
                "songname": "秋原依 - 错季"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019122444129869.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 49
        }, {
            "rankid": 24971,
            "id": 109,
            "intro": "数据来源：酷狗DJ类歌曲\r\n排序方式：按歌曲搜索播放一周总量排序\r\n更新周期：周三",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201105\/20201105152707626594.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122333384421.jpg",
            "jump_title": "",
            "rankname": "DJ热歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175759623740.png",
            "jump_url": "",
            "img_9": "",
            "classify": 1,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122331572959.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "花僮 - 浪子闲话 (DJ沈念(5)版)"
            }, {
                "songname": "IN-K、王忻辰 - 迷失幻境 (DJ版)"
            }, {
                "songname": "IN-K、王忻辰 - 落差 (DJ版)"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019122335144078.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 51
        }, {
            "rankid": 35811,
            "id": 215,
            "intro": "数据来源：酷狗\r\n排序方式：按会员专享歌曲播放总量排序\r\n更新周期：每周一",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20200909\/20200909135350181905.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190311\/20190311103835919973.png",
            "jump_title": "",
            "rankname": "会员专享热歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175807440272.png",
            "jump_url": "",
            "img_9": "",
            "classify": 1,
            "update_frequency": "周一",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190311\/20190311103833106637.png",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "周杰伦 - 稻香"
            }, {
                "songname": "Ava Max - Salt"
            }, {
                "songname": "刘德华 - 暗里着迷"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20190311\/20190311103837451504.png",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 41
        }, {
            "rankid": 31308,
            "id": 35,
            "intro": "数据来源：酷狗一个月内发行的华语新歌\r\n排序方式：按播放量、搜索量等维度排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201214\/20201214175701864670.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122308789982.jpg",
            "jump_title": "",
            "rankname": "华语新歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174155391977.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174154367599.jpg",
            "classify": 2,
            "update_frequency": "工作日",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122306857444.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "花僮 - 上仙"
            }, {
                "songname": "周深 - 和光同尘"
            }, {
                "songname": "白小白 - 爱我就别走了"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019122310609161.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 251
        }, {
            "rankid": 31310,
            "id": 36,
            "intro": "数据来源：酷狗一个月内发行的欧美新歌\r\n排序方式：按播放量、搜索量等维度排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201130\/20201130235604703264.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122240929645.jpg",
            "jump_title": "",
            "rankname": "欧美新歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174215666798.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174213704743.jpg",
            "classify": 2,
            "update_frequency": "工作日",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122238418415.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "VIZE、Alan Walker、Leony!、Edward Artemyev - Space Melody (Edward Artemyev)"
            }, {
                "songname": "Taylor Swift - willow (moonlit witch version)"
            }, {
                "songname": "Sam Smith - Have Yourself a Merry Little Christmas"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019122242395797.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 253
        }, {
            "rankid": 31311,
            "id": 67,
            "intro": "数据来源：酷狗一个月内发行的韩语新歌\r\n排序方式：按播放量、搜索量等维度排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201215\/20201215104605616172.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122158610214.jpg",
            "jump_title": "",
            "rankname": "韩国新歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174232828133.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174231152346.jpg",
            "classify": 2,
            "update_frequency": "工作日",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122156828017.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "太妍 - What Do I Call You"
            }, {
                "songname": "太妍 - To the moon"
            }, {
                "songname": "太妍 - Playlist"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019122200515578.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 253
        }, {
            "rankid": 31312,
            "id": 69,
            "intro": "数据来源：酷狗一个月内发行的日语新歌\r\n排序方式：按播放量、搜索量等维度排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201124\/20201124155112428866.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122121141047.jpg",
            "jump_title": "",
            "rankname": "日本新歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174248928394.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174246536761.jpg",
            "classify": 2,
            "update_frequency": "工作日",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122119973845.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "初音ミク、MiveMusic - 元气与幸运"
            }, {
                "songname": "AKB48 - 10年桜 (10年樱)"
            }, {
                "songname": "AKB48 - 前しか向かねえ (勇往直前)"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019122124188716.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 253
        }, {
            "rankid": 31313,
            "id": 39,
            "intro": "数据来源：酷狗半年内发行的粤语新歌\r\n排序方式：按播放量、搜索量等维度排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201214\/20201214202502980624.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122018837980.jpg",
            "jump_title": "",
            "rankname": "粤语新歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190910\/20190910102927369195.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190910\/20190910102926520806.jpg",
            "classify": 2,
            "update_frequency": "工作日",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019122016271749.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "刘德华 - 原谅我 (粤语版)"
            }, {
                "songname": "刘德华 - 孤雁"
            }, {
                "songname": "刘德华 - 爱永远存在"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019122021568840.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 251
        }, {
            "rankid": 33162,
            "id": 123,
            "intro": "数据来源：酷狗ACG类歌曲\r\n排序方式：按搜索播放一周总量排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201211\/20201211155601353392.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190911\/20190911195358567855.jpg",
            "jump_title": "",
            "rankname": "ACG新歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201019\/20201019153148570872.png",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190911\/20190911195400836023.jpg",
            "classify": 1,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190911\/20190911195356382314.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "洛天依 - 音乐之路"
            }, {
                "songname": "洛天依、言和 - 享受 想瘦"
            }, {
                "songname": "洛天依 - 高贵的野蛮人"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20190911\/20190911195359896034.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 51
        }, {
            "rankid": 21101,
            "id": 30,
            "intro": "数据来源：酷狗\r\n排序方式：根据酷狗用户的分享、转发、下载量综合排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201210\/20201210185004290362.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121858279252.jpg",
            "jump_title": "",
            "rankname": "酷狗分享榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175816902442.png",
            "jump_url": "",
            "img_9": "",
            "classify": 1,
            "update_frequency": "周二",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121855584689.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "青微工作室、奇然 - 破浪"
            }, {
                "songname": "王琪 - 可可托海的牧羊人"
            }, {
                "songname": "回小仙 - 醒不来的梦"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019121900772347.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 50
        }, {
            "rankid": 30972,
            "id": 167,
            "intro": "数据来源：腾讯原创音乐\r\n排序方式：按播放量、话题热度等维度排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201215\/20201215143735942739.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190624\/20190624154847939871.jpg",
            "jump_title": "",
            "rankname": "腾讯音乐人原创榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175825226653.png",
            "jump_url": "",
            "img_9": "",
            "classify": 1,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190624\/20190624153614300323.png",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "Bomb比尔 - 1022-比尔的歌"
            }, {
                "songname": "赵政豪 - 椰城邮信"
            }, {
                "songname": "JIHU、Sugar - Going Down"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20190624\/20190624154340922603.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 51
        }, {
            "rankid": 22603,
            "id": 42,
            "intro": "数据来源：5sing\r\n排序方式：根据5sing原创歌曲每周综合热度来排序\r\n更新周期：周一",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201104\/20201104175510980273.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121805248654.jpg",
            "jump_title": "",
            "rankname": "5sing音乐榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201010\/20201010114440874606.png",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200218\/20200218112936134809.jpg",
            "classify": 1,
            "update_frequency": "周一",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121803749516.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "伦桑、一棵小葱张晓涵 - 字正腔圆"
            }, {
                "songname": "叶洛洛 - 词牌名"
            }, {
                "songname": "萧忆情Alex - 姑娘安好"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019121807146762.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 50
        }, {
            "rankid": 33160,
            "id": 119,
            "intro": "数据来源：酷狗电音类别歌曲\r\n排序方式：按搜索播放一周总量排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201204\/20201204164651345673.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121747524588.jpg",
            "jump_title": "",
            "rankname": "电音热歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174449662435.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174447336807.jpg",
            "classify": 3,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121744206764.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "傅梦彤 - 潮汐 (Natural)"
            }, {
                "songname": "灼夭、小田音乐社 - 鲸落万物生"
            }, {
                "songname": "Phao、CM1X - Hai Phút Hơn"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019121749428993.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 51
        }, {
            "rankid": 21335,
            "id": 32,
            "intro": "数据来源：繁星\r\n排序方式：按繁星网友投票数排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201105\/20201105152707626594.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20180824\/20180824185745798417.png",
            "jump_title": "",
            "rankname": "繁星音乐榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174504223797.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174502141408.jpg",
            "classify": 3,
            "update_frequency": "每半个月",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20180824\/20180824185738518086.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "花僮 - 浪子闲话"
            }, {
                "songname": "王琪 - 可可托海的牧羊人"
            }, {
                "songname": "小阿枫 - 醉倾城"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20180824\/20180824185748528807.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 21
        }, {
            "rankid": 44412,
            "id": 265,
            "intro": "酷狗说唱榜，替你准备最优质最前沿的中文说唱音乐作品",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20200717\/20200717155004986560.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200708\/20200708214042268851.jpg",
            "jump_title": "",
            "rankname": "酷狗说唱榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200708\/20200708214043368250.png",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200708\/20200708214114341727.jpg",
            "classify": 3,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200708\/20200708214041363780.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "Lil Ghost小鬼 - 偏爱 (Live)"
            }, {
                "songname": "R1SE姚琛 - 不屑·NEVERMIND"
            }, {
                "songname": "Jac - 11"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20200708\/20200708214043722340.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 24
        }, {
            "rankid": 33161,
            "id": 79,
            "intro": "数据来源：酷狗国风类歌曲\r\n排序方式：按搜索播放一周总量排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201208\/20201208112606522316.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200908\/20200908194553602319.jpg",
            "jump_title": "",
            "rankname": "国风新歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201010\/20201010110127855584.png",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200908\/20200908194947749696.jpg",
            "classify": 2,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200908\/20200908194552887844.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "王一博 - 熹微"
            }, {
                "songname": "封茗囧菌、天涯未晚 - 风月迟迟来"
            }, {
                "songname": "花僮 - 不见人归来"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20200908\/20200908194555197108.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 51
        }, {
            "rankid": 46910,
            "id": 275,
            "intro": "数据来源：按综艺新歌热度综合排序\r\n排序方式：按播放量、搜索量等维度排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201213\/20201213120103596319.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201109\/20201109170516777658.png",
            "jump_title": "",
            "rankname": "综艺新歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201109\/20201109170519725585.png",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201109\/20201109170541307701.png",
            "classify": 2,
            "update_frequency": "周三更新",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201109\/20201109170514307375.png",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "李克勤、周深 - 爱情转移 (粤语版) (Live)"
            }, {
                "songname": "常石磊、王源 - 血腥爱情故事 (Live)"
            }, {
                "songname": "张信哲、太一 - 口是心非 (Live)"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20201109\/20201109170517558959.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 7
        }, {
            "rankid": 33163,
            "id": 77,
            "intro": "数据来源：酷狗影视类歌曲\r\n排序方式：按搜索播放一周总量排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201207\/20201207203010500213.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121701875027.jpg",
            "jump_title": "",
            "rankname": "影视金曲榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174854191515.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174852244391.jpg",
            "classify": 3,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121659616445.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "吴青峰 - 如果声音不记得【《如果声音不记得》电影主题曲】"
            }, {
                "songname": "张碧晨 - 骗【《如果声音不记得》电影插曲】"
            }, {
                "songname": "薛之谦 - 野心【《缉魂》电影推广曲】"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019121704873377.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 51
        }, {
            "rankid": 33166,
            "id": 193,
            "intro": "数据来源：酷狗欧美歌曲\r\n排序方式：按搜索播放一周总量排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20191211\/20191211153103312934.png",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121544655833.jpg",
            "jump_title": "",
            "rankname": "欧美金曲榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174931685280.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174929869298.jpg",
            "classify": 3,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121542609944.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "Ava Max - Salt"
            }, {
                "songname": "Sasha Sloan - Dancing With Your Ghost"
            }, {
                "songname": "Hawk Nelson - Sold Out"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019121546998825.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 51
        }, {
            "rankid": 33165,
            "id": 38,
            "intro": "数据来源：酷狗粤语歌曲\r\n排序方式：按搜索播放一周总量排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20200927\/20200927181659368520.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121611360472.jpg",
            "jump_title": "",
            "rankname": "粤语金曲榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174949759288.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909174947924578.jpg",
            "classify": 3,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121609698871.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "刘德华 - 暗里着迷"
            }, {
                "songname": "街道办GDC、欧阳耀莹 - 春娇与志明"
            }, {
                "songname": "陈慧娴 - 千千阙歌"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019121613673415.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 51
        }, {
            "rankid": 36107,
            "id": 217,
            "intro": "数据来源：酷狗小语种歌曲\r\n排序方式：按搜索播放一周总量排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20200310\/20200310170034956740.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190403\/20190403162618621048.jpg",
            "jump_title": "",
            "rankname": "小语种热歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175105662534.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175104364464.jpg",
            "classify": 3,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190403\/20190403162616176601.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "Phao、CM1X - Hai Phút Hơn"
            }, {
                "songname": "Elgit Doda - Larg"
            }, {
                "songname": "Rauf & Faik - Колыбельная"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20190403\/20190403162620781596.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 50
        }, {
            "rankid": 4681,
            "id": 10,
            "intro": "数据来源：美国Billboard\r\n排序方式：根据歌曲在美国的销量、电台播放量、流媒体下载量等指标进行排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20200909\/20200909132733952925.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121339813327.jpg",
            "jump_title": "",
            "rankname": "美国BillBoard榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175149284640.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175148246788.jpg",
            "classify": 4,
            "update_frequency": "周四",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121336278152.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "Mariah Carey - All I Want For Christmas Is You"
            }, {
                "songname": "24KGoldn、iann dior - Mood"
            }, {
                "songname": "Brenda Lee - Rockin' Around The Christmas Tree"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019121340103598.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 51
        }, {
            "rankid": 4680,
            "id": 12,
            "intro": "数据来源：英国Single Chart\r\n排序方式：根据歌曲在英国的一周销量进行排序\r\n更新周期：周一",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20200909\/20200909132733952925.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121316839345.jpg",
            "jump_title": "",
            "rankname": "英国单曲榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175205814368.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175204409709.jpg",
            "classify": 4,
            "update_frequency": "周一",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121314950680.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "Mariah Carey - All I Want For Christmas Is You"
            }, {
                "songname": "Wham! - Last Christmas (Single Version)"
            }, {
                "songname": "Ariana Grande - positions"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019121317188050.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 50
        }, {
            "rankid": 4673,
            "id": 8,
            "intro": "数据来源：日本Oricon\r\n排序方式：根据日本实体CD销量进行排序\r\n更新周期：周三",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201203\/20201203213920459874.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121248478803.jpg",
            "jump_title": "",
            "rankname": "日本公信榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175221447910.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20190909\/20190909175220462967.jpg",
            "classify": 4,
            "update_frequency": "周三",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20181019\/20181019121246308170.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "櫻坂46 - Nobody's fault (任何人都没错)"
            }, {
                "songname": "NiziU - Step and a step"
            }, {
                "songname": "LiSA - 炎"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019121251431378.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 50
        }, {
            "rankid": 38623,
            "id": 9,
            "intro": "数据来源：韩国Melon官网\r\n排序方式：根据Melon官方的周榜排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201123\/20201123133507923552.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20191021\/20191021201705225728.jpg",
            "jump_title": "",
            "rankname": "韩国Melon音乐榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20191021\/20191021201717772506.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20191021\/20191021201714155508.jpg",
            "classify": 4,
            "update_frequency": "周一",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20191021\/20191021201704859649.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "미란이、먼치맨、Khundi Panda、MUSHVENOM、JUSTHIS - VVS (Prod. GroovyRoom)"
            }, {
                "songname": "오승택、Giriboy、BIG Naughty - 내일이 오면 (Tomorrow)"
            }, {
                "songname": "BTS(防弹少年团) - Dynamite"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20181019\/20181019121225649566.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 50
        }, {
            "rankid": 42807,
            "id": 251,
            "intro": "数据来源：joox本地歌曲播放数据\r\n排序方式：按播放量、话题热度等维度排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201119\/20201119171503191308.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200320\/20200320185607939528.jpg",
            "jump_title": "",
            "rankname": "joox本地热歌榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200320\/20200320185610630505.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200320\/20200320185609894362.jpg",
            "classify": 4,
            "update_frequency": "周五",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200320\/20200320185606356366.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "陈奕迅 - 是但求其爱"
            }, {
                "songname": "容祖儿 - 东京人寿"
            }, {
                "songname": "林家谦 - 时光倒流一句话"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20200320\/20200320185608883318.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 46
        }, {
            "rankid": 42808,
            "id": 253,
            "intro": "数据来源：KKBOX数位音乐风云榜歌曲数据\r\n排序方式：按播放量、话题热度等维度排序",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201113\/20201113100455982158.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200320\/20200320190008242289.jpg",
            "jump_title": "",
            "rankname": "台湾KKBOX风云榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200320\/20200320190011360333.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200320\/20200320190010792757.jpg",
            "classify": 4,
            "update_frequency": "周五",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20200320\/20200320190007542793.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "陈昊森 - 刻在我心底的名字"
            }, {
                "songname": "陈零九 - 千年以后 (录音室版)"
            }, {
                "songname": "陈芳语、E-SO - 邮票"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20200320\/20200320190009931456.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 46
        }, {
            "rankid": 46868,
            "id": 273,
            "intro": "在日本最大的音乐频道「SPACE SHOWER TV」中被介绍的榜单。\r\n\r\nSPACE SHOWER TV设立于1989年，因通过MV和直播节目介绍了日本的众多艺人而备受好评。\r\n本榜单根据频道上的播放次数计算，为你展现日本音乐的流行趋势。\r\n每周三更新",
            "album_img_9": "http:\/\/imge.kugou.com\/stdmusic\/{size}\/20201116\/20201116160323251505.jpg",
            "banner7url": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201028\/20201028152646615355.jpg",
            "jump_title": "",
            "rankname": "日本SPACE SHOWER榜",
            "isvol": 1,
            "banner_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201028\/20201028160743576779.jpg",
            "jump_url": "",
            "img_9": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201028\/20201028160742765173.jpg",
            "classify": 4,
            "update_frequency": "周三更新",
            "imgurl": "http:\/\/imge.kugou.com\/mcommon\/{size}\/20201028\/20201028152644700630.jpg",
            "show_play_button": 0,
            "songinfo": [{
                "songname": "King Gnu - 千両役者"
            }, {
                "songname": "Sekai no Owari - silent"
            }, {
                "songname": "福山雅治 - 心音"
            }],
            "bannerurl": "http:\/\/imge.kugou.com\/mcommonbanner\/{size}\/20201028\/20201028152647239085.jpg",
            "ranktype": 1,
            "custom_type": 0,
            "issue": 8
        }],
        "total": 31
    },
    "errcode": 0
}
```
</details>

## Get Volume ID of Ranking List

#### URL
```
http://mobilecdnbj.kugou.com/api/v3/rank/vol
```
#### Params
##### Required
Field | Description
------------ | -------------
rankid | The rank's unique id

>**Note:** Rank ID can be obtained from the list of rankings above

##### Optional
Others: *ranktype, plat, with_rest_tag*

#### Example
Getting list of volume IDs for the DJ热歌榜 rankings
```
http://mobilecdnbj.kugou.com/api/v3/rank/vol?rankid=24971
```
<details><summary>Response:</summary>

```json
{
    "status": 1,
    "error": "",
    "data": {
        "timestamp": 1608366572,
        "info": [{
            "vols": [{
                "volid": 47843,
                "volname": "51期",
                "voltitle": "51期"
            }, {
                "volid": 47697,
                "volname": "50期",
                "voltitle": "50期"
            }, {
                "volid": 47571,
                "volname": "49期",
                "voltitle": "49期"
            }, {
                "volid": 47441,
                "volname": "48期",
                "voltitle": "48期"
            }, {
                "volid": 47323,
                "volname": "47期",
                "voltitle": "47期"
            }, {
                "volid": 47215,
                "volname": "46期",
                "voltitle": "46期"
            }, {
                "volid": 47106,
                "volname": "45期",
                "voltitle": "45期"
            }, {
                "volid": 46940,
                "volname": "44期",
                "voltitle": "44期"
            }, {
                "volid": 46806,
                "volname": "43期",
                "voltitle": "43期"
            }, {
                "volid": 46687,
                "volname": "42期",
                "voltitle": "42期"
            }, {
                "volid": 46570,
                "volname": "41期",
                "voltitle": "41期"
            }, {
                "volid": 46447,
                "volname": "40期",
                "voltitle": "40期"
            }, {
                "volid": 46324,
                "volname": "39期",
                "voltitle": "39期"
            }, {
                "volid": 46207,
                "volname": "38期",
                "voltitle": "38期"
            }, {
                "volid": 46089,
                "volname": "37期",
                "voltitle": "37期"
            }, {
                "volid": 45973,
                "volname": "36期",
                "voltitle": "36期"
            }, {
                "volid": 45855,
                "volname": "35期",
                "voltitle": "35期"
            }, {
                "volid": 45744,
                "volname": "34期",
                "voltitle": "34期"
            }, {
                "volid": 45603,
                "volname": "33期",
                "voltitle": "33期"
            }, {
                "volid": 45484,
                "volname": "32期",
                "voltitle": "32期"
            }, {
                "volid": 45363,
                "volname": "31期",
                "voltitle": "31期"
            }, {
                "volid": 45246,
                "volname": "30期",
                "voltitle": "30期"
            }, {
                "volid": 45125,
                "volname": "29期",
                "voltitle": "29期"
            }, {
                "volid": 44975,
                "volname": "28期",
                "voltitle": "28期"
            }, {
                "volid": 44851,
                "volname": "27期",
                "voltitle": "27期"
            }, {
                "volid": 44699,
                "volname": "26期",
                "voltitle": "26期"
            }, {
                "volid": 44562,
                "volname": "25期",
                "voltitle": "25期"
            }, {
                "volid": 44424,
                "volname": "24期",
                "voltitle": "24期"
            }, {
                "volid": 44289,
                "volname": "23期",
                "voltitle": "23期"
            }, {
                "volid": 44153,
                "volname": "22期",
                "voltitle": "22期"
            }, {
                "volid": 44021,
                "volname": "21期",
                "voltitle": "21期"
            }, {
                "volid": 43890,
                "volname": "20期",
                "voltitle": "20期"
            }, {
                "volid": 43760,
                "volname": "19期",
                "voltitle": "19期"
            }, {
                "volid": 43626,
                "volname": "18期",
                "voltitle": "18期"
            }, {
                "volid": 43492,
                "volname": "17期",
                "voltitle": "17期"
            }, {
                "volid": 43343,
                "volname": "16期",
                "voltitle": "16期"
            }, {
                "volid": 43208,
                "volname": "15期",
                "voltitle": "15期"
            }, {
                "volid": 43058,
                "volname": "14期",
                "voltitle": "14期"
            }, {
                "volid": 42924,
                "volname": "13期",
                "voltitle": "13期"
            }, {
                "volid": 42790,
                "volname": "12期",
                "voltitle": "12期"
            }, {
                "volid": 42677,
                "volname": "11期",
                "voltitle": "11期"
            }, {
                "volid": 40815,
                "volname": "10期",
                "voltitle": "10期"
            }, {
                "volid": 40679,
                "volname": "9期",
                "voltitle": "9期"
            }, {
                "volid": 40557,
                "volname": "8期",
                "voltitle": "8期"
            }, {
                "volid": 40446,
                "volname": "7期",
                "voltitle": "7期"
            }, {
                "volid": 40343,
                "volname": "6期",
                "voltitle": "6期"
            }, {
                "volid": 40246,
                "volname": "5期",
                "voltitle": "5期"
            }, {
                "volid": 40145,
                "volname": "4期",
                "voltitle": "4期"
            }, {
                "volid": 40052,
                "volname": "3期",
                "voltitle": "3期"
            }, {
                "volid": 39945,
                "volname": "2期",
                "voltitle": "2期"
            }, {
                "volid": 39812,
                "volname": "1期",
                "voltitle": "1期"
            }],
            "year": 2020
        }, {
            "vols": [{
                "volid": 39722,
                "volname": "53期",
                "voltitle": "53期"
            }, {
                "volid": 39592,
                "volname": "52期",
                "voltitle": "52期"
            }, {
                "volid": 39483,
                "volname": "51期",
                "voltitle": "51期"
            }, {
                "volid": 39379,
                "volname": "50期",
                "voltitle": "50期"
            }, {
                "volid": 39266,
                "volname": "49期",
                "voltitle": "49期"
            }, {
                "volid": 39129,
                "volname": "48期",
                "voltitle": "48期"
            }, {
                "volid": 39006,
                "volname": "47期",
                "voltitle": "47期"
            }, {
                "volid": 38891,
                "volname": "46期",
                "voltitle": "46期"
            }, {
                "volid": 38765,
                "volname": "45期",
                "voltitle": "45期"
            }, {
                "volid": 38648,
                "volname": "44期",
                "voltitle": "44期"
            }, {
                "volid": 38537,
                "volname": "43期",
                "voltitle": "43期"
            }, {
                "volid": 38430,
                "volname": "42期",
                "voltitle": "42期"
            }, {
                "volid": 38328,
                "volname": "41期",
                "voltitle": "41期"
            }, {
                "volid": 38218,
                "volname": "40期",
                "voltitle": "40期"
            }, {
                "volid": 38131,
                "volname": "39期",
                "voltitle": "39期"
            }, {
                "volid": 38042,
                "volname": "38期",
                "voltitle": "38期"
            }, {
                "volid": 37955,
                "volname": "37期",
                "voltitle": "37期"
            }, {
                "volid": 37877,
                "volname": "36期",
                "voltitle": "36期"
            }, {
                "volid": 37776,
                "volname": "35期",
                "voltitle": "35期"
            }, {
                "volid": 37692,
                "volname": "34期",
                "voltitle": "34期"
            }, {
                "volid": 37585,
                "volname": "33期",
                "voltitle": "33期"
            }, {
                "volid": 37492,
                "volname": "32期",
                "voltitle": "32期"
            }, {
                "volid": 37404,
                "volname": "31期",
                "voltitle": "31期"
            }, {
                "volid": 37322,
                "volname": "30期",
                "voltitle": "30期"
            }, {
                "volid": 37236,
                "volname": "29期",
                "voltitle": "29期"
            }, {
                "volid": 37154,
                "volname": "28期",
                "voltitle": "28期"
            }, {
                "volid": 37072,
                "volname": "27期",
                "voltitle": "27期"
            }, {
                "volid": 36993,
                "volname": "26期",
                "voltitle": "26期"
            }, {
                "volid": 36917,
                "volname": "25期",
                "voltitle": "25期"
            }, {
                "volid": 36840,
                "volname": "24期",
                "voltitle": "24期"
            }, {
                "volid": 36738,
                "volname": "23期",
                "voltitle": "23期"
            }, {
                "volid": 36654,
                "volname": "22期",
                "voltitle": "22期"
            }, {
                "volid": 36572,
                "volname": "21期",
                "voltitle": "21期"
            }, {
                "volid": 36495,
                "volname": "20期",
                "voltitle": "20期"
            }, {
                "volid": 36417,
                "volname": "19期",
                "voltitle": "19期"
            }, {
                "volid": 36344,
                "volname": "18期",
                "voltitle": "18期"
            }, {
                "volid": 36274,
                "volname": "17期",
                "voltitle": "17期"
            }, {
                "volid": 36184,
                "volname": "16期",
                "voltitle": "16期"
            }, {
                "volid": 36111,
                "volname": "15期",
                "voltitle": "15期"
            }, {
                "volid": 36048,
                "volname": "14期",
                "voltitle": "14期"
            }, {
                "volid": 35956,
                "volname": "13期",
                "voltitle": "13期"
            }, {
                "volid": 35945,
                "volname": "12期",
                "voltitle": "12期"
            }, {
                "volid": 35869,
                "volname": "11期",
                "voltitle": "11期"
            }, {
                "volid": 35785,
                "volname": "10期",
                "voltitle": "10期"
            }, {
                "volid": 35710,
                "volname": "9期",
                "voltitle": "9期"
            }, {
                "volid": 35637,
                "volname": "8期",
                "voltitle": "8期"
            }, {
                "volid": 35561,
                "volname": "7期",
                "voltitle": "7期"
            }, {
                "volid": 35488,
                "volname": "6期",
                "voltitle": "6期"
            }, {
                "volid": 35417,
                "volname": "5期",
                "voltitle": "5期"
            }, {
                "volid": 35341,
                "volname": "4期",
                "voltitle": "4期"
            }, {
                "volid": 35270,
                "volname": "3期",
                "voltitle": "3期"
            }, {
                "volid": 35184,
                "volname": "2期",
                "voltitle": "2期"
            }, {
                "volid": 35114,
                "volname": "1期",
                "voltitle": "1期"
            }],
            "year": 2019
        }]
    },
    "errcode": 0
}
```
</details>

## Get List of Songs for the Ranking

#### URL
```
http://mobilecdnbj.kugou.com/api/v3/rank/song?
```
#### Params
##### Required
Field | Description
------------ | -------------
rankid | The rank's unique ID
volid | The Volume's unique ID

>**Note:** Volume ID can be obtained from the above

##### Optional
Field | Description
------------ | -------------
pagesize | pagesize
page | page

Others: *version, ranktype, area_code, with_res_tag, plat*

#### Example
Getting top 5 songs for the DJ热歌榜 rankings
```
http://mobilecdnbj.kugou.com/api/v3/rank/song?volid=47843&rankid=24971&pagesize=5
```
<details><summary>Response:</summary>

```json
{
    "status": 1,
    "error": "",
    "data": {
        "timestamp": 1608368317,
        "info": [{
            "pay_type_320": 3,
            "m4afilesize": 0,
            "price_sq": 200,
            "first": 0,
            "filesize": 4048130,
            "bitrate": 128,
            "trans_param": {
                "cid": 120368453,
                "cpy_grade": 5,
                "pay_block_tpl": 1,
                "musicpack_advance": 0,
                "display_rate": 0,
                "cpy_level": 1,
                "display": 0,
                "cpy_attr0": 0
            },
            "price": 200,
            "inlist": 1,
            "old_cpy": 0,
            "fail_process_sq": 4,
            "pay_type": 3,
            "musical": null,
            "topic_url": "",
            "fail_process_320": 4,
            "pkg_price": 1,
            "feetype": 0,
            "filename": "花僮 - 浪子闲话 (DJ沈念(5)版)",
            "price_320": 200,
            "extname": "mp3",
            "hash": "972735F8B0DF5455EC3BCAFE7B07A9A3",
            "mvhash": "",
            "topic_url_320": "",
            "privilege": 8,
            "album_audio_id": 279832674,
            "addtime": "2020-12-16 11:50:42",
            "pkg_price_320": 1,
            "recommend_reason": "",
            "rp_type": "audio",
            "pkg_price_sq": 1,
            "audio_id": 85639214,
            "320filesize": 10120032,
            "rp_publish": 1,
            "has_accompany": 1,
            "topic_url_sq": "",
            "320privilege": 10,
            "isfirst": 0,
            "album_id": "39906034",
            "fail_process": 4,
            "320hash": "84894ECBB9D69861E6F69A482C0A97F8",
            "sqhash": "52AE1F6A03ED48E9A03EB24C4FD696D4",
            "remark": "浪子闲话",
            "pay_type_sq": 3,
            "duration": 252,
            "sqprivilege": 10,
            "sqfilesize": 33447569,
            "issue": 51
        }, {
            "pay_type_320": 3,
            "m4afilesize": 0,
            "price_sq": 200,
            "first": 0,
            "filesize": 2911295,
            "bitrate": 128,
            "trans_param": {
                "cid": 119281356,
                "cpy_grade": 5,
                "pay_block_tpl": 1,
                "musicpack_advance": 0,
                "display_rate": 0,
                "cpy_level": 1,
                "display": 0,
                "cpy_attr0": 0
            },
            "price": 200,
            "inlist": 1,
            "old_cpy": 0,
            "fail_process_sq": 4,
            "pay_type": 3,
            "musical": null,
            "topic_url": "",
            "fail_process_320": 4,
            "pkg_price": 1,
            "feetype": 0,
            "filename": "IN-K、王忻辰 - 迷失幻境 (DJ版)",
            "price_320": 200,
            "extname": "mp3",
            "hash": "FA18CD000786E17834BC4CA24FB9F0D7",
            "mvhash": "A4A38C28554FD7E9B5D9E9CD91544C4F",
            "topic_url_320": "",
            "privilege": 8,
            "album_audio_id": 278512735,
            "addtime": "2020-12-16 11:50:42",
            "pkg_price_320": 1,
            "recommend_reason": "",
            "rp_type": "audio",
            "pkg_price_sq": 1,
            "audio_id": 84786849,
            "320filesize": 7277407,
            "rp_publish": 1,
            "has_accompany": 1,
            "topic_url_sq": "",
            "320privilege": 10,
            "isfirst": 0,
            "album_id": "39379466",
            "fail_process": 4,
            "320hash": "C066B727AD0DCBF3C86FA4F286109FDE",
            "sqhash": "9E1E1425312ACFA30076CD44D9E68F2E",
            "remark": "迷失幻境",
            "pay_type_sq": 3,
            "duration": 181,
            "sqprivilege": 10,
            "sqfilesize": 25702287,
            "issue": 51
        }, {
            "pay_type_320": 3,
            "m4afilesize": 0,
            "price_sq": 200,
            "first": 0,
            "filesize": 3871182,
            "bitrate": 128,
            "trans_param": {
                "cid": 119280727,
                "cpy_attr0": 0,
                "pay_block_tpl": 1,
                "musicpack_advance": 0,
                "display_rate": 0,
                "cpy_level": 1,
                "display": 0,
                "cpy_grade": 5
            },
            "price": 200,
            "inlist": 1,
            "old_cpy": 0,
            "fail_process_sq": 4,
            "pay_type": 3,
            "musical": null,
            "topic_url": "",
            "fail_process_320": 4,
            "pkg_price": 1,
            "feetype": 0,
            "filename": "IN-K、王忻辰 - 落差 (DJ版)",
            "price_320": 200,
            "extname": "mp3",
            "hash": "607770C67A77F3B25FEB16DD9FE313B6",
            "mvhash": "",
            "topic_url_320": "",
            "privilege": 8,
            "album_audio_id": 278512296,
            "addtime": "2020-12-16 11:50:42",
            "pkg_price_320": 1,
            "recommend_reason": "",
            "rp_type": "audio",
            "pkg_price_sq": 1,
            "audio_id": 84786502,
            "320filesize": 9677889,
            "rp_publish": 1,
            "has_accompany": 1,
            "topic_url_sq": "",
            "320privilege": 10,
            "isfirst": 0,
            "album_id": "39769503",
            "fail_process": 4,
            "320hash": "EBD5858692A84BA751B392D1CF0347B9",
            "sqhash": "86A54D7CB5524890E389937D83A6D646",
            "remark": "落差",
            "pay_type_sq": 3,
            "duration": 241,
            "sqprivilege": 10,
            "sqfilesize": 34219490,
            "issue": 51
        }, {
            "pay_type_320": 3,
            "m4afilesize": 0,
            "price_sq": 200,
            "first": 0,
            "filesize": 1936703,
            "bitrate": 128,
            "trans_param": {
                "cid": 120708058,
                "cpy_grade": 20,
                "pay_block_tpl": 1,
                "musicpack_advance": 0,
                "display_rate": 0,
                "cpy_level": 1,
                "display": 0,
                "cpy_attr0": 0
            },
            "price": 200,
            "inlist": 1,
            "old_cpy": 0,
            "fail_process_sq": 4,
            "pay_type": 3,
            "musical": {
                "publish_type": 1,
                "publish_time": "2020-11-09 12:33:14",
                "uploader": "好乐无荒"
            },
            "topic_url": "",
            "fail_process_320": 4,
            "pkg_price": 1,
            "feetype": 0,
            "filename": "是七叔呢 - 燕无歇 (DJ黑桃A版)",
            "price_320": 200,
            "extname": "mp3",
            "hash": "91EF65B249A18B14760B359E9711FE69",
            "mvhash": "",
            "topic_url_320": "",
            "privilege": 8,
            "album_audio_id": 280554181,
            "addtime": "2020-12-16 11:50:42",
            "pkg_price_320": 1,
            "recommend_reason": "",
            "rp_type": "audio",
            "pkg_price_sq": 1,
            "audio_id": 86121893,
            "320filesize": 4844416,
            "rp_publish": 1,
            "has_accompany": 1,
            "topic_url_sq": "",
            "320privilege": 10,
            "isfirst": 0,
            "album_id": "40020779",
            "fail_process": 4,
            "320hash": "2DB2BEE7E8CF6551FBA175CBDD05379F",
            "sqhash": "A0D2EC38F7378E75F90B33638A628DC0",
            "remark": "燕无歇（DJ黑桃A）( feat.是七叔呢)",
            "pay_type_sq": 3,
            "duration": 120,
            "sqprivilege": 10,
            "sqfilesize": 15186642,
            "issue": 51
        }, {
            "pay_type_320": 3,
            "m4afilesize": 0,
            "price_sq": 200,
            "first": 0,
            "filesize": 3930950,
            "bitrate": 128,
            "trans_param": {
                "cid": 115825960,
                "cpy_grade": 5,
                "pay_block_tpl": 1,
                "musicpack_advance": 0,
                "display_rate": 0,
                "cpy_level": 1,
                "display": 0,
                "cpy_attr0": 0
            },
            "price": 200,
            "inlist": 1,
            "old_cpy": 0,
            "fail_process_sq": 4,
            "pay_type": 3,
            "musical": null,
            "topic_url": "",
            "fail_process_320": 4,
            "pkg_price": 1,
            "feetype": 0,
            "filename": "小乐哥 - 执迷不悟 (DJ版)",
            "price_320": 200,
            "extname": "mp3",
            "hash": "F5D9FF3093BE6861506D058A851FAF0F",
            "mvhash": "69455D3D8F47F373C0B9C3759A20D71A",
            "topic_url_320": "",
            "privilege": 8,
            "album_audio_id": 275046110,
            "addtime": "2020-12-16 11:50:43",
            "pkg_price_320": 1,
            "recommend_reason": "",
            "rp_type": "audio",
            "pkg_price_sq": 1,
            "audio_id": 82521984,
            "320filesize": 9827309,
            "rp_publish": 1,
            "has_accompany": 1,
            "topic_url_sq": "",
            "320privilege": 10,
            "isfirst": 0,
            "album_id": "39117070",
            "fail_process": 4,
            "320hash": "BD489F4D4C5E4CC0A4AAECFE818D90BA",
            "sqhash": "B6E521EB298EE8396CA68F6D67EE6C1B",
            "remark": "执迷不悟",
            "pay_type_sq": 3,
            "duration": 245,
            "sqprivilege": 10,
            "sqfilesize": 31687954,
            "issue": 51
        }],
        "total": 100
    },
    "errcode": 0
}
```
</details>

## Others

#### List of New Songs
This is listed as 新歌首发 on the home page
```
http://mobilecdnbj.kugou.com/api/v3/rank/newsong?version=9108&plat=0&with_cover=1&pagesize=100&type=1&area_code=1&page=1&with_res_tag=1
```
#### Get all songs from an Album based on Album ID
```
http://mobilecdn.kugou.com/api/v3/album/song?version=9108&albumid=1589936&plat=0&pagesize=100&area_code=1&page=1&with_res_tag=1
```