# KuGou API
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
<details><summary>Response:</summary><p>
  
  ```
  test
  ```
  
</p></details>
