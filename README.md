# WHUspider
an easy spider to get news from WHU and WHUCS

### 使用方法：
1. 创建WHUspider类对象。
2. 使用WHUCSrequestFromUrl方法获取实时武汉大学计算机学院新闻信息，返回json格式表单。
3. 使用WHUrequestFromUrl方法获取实时武汉大学官网新闻信息，返回json格式表单。
4. 使用`json.loads(yourjson)`得到表单数据。
***

### 表单格式
##### WHUCSrequestFromUrl
key | 类型 | 说明
---|---|---
title | str | 新闻标题
time | str | 新闻发布的时间
address | str | 新闻链接

##### WHUrequestFromUrl
key | 类型 | 说明
---|---|---
title | str | 新闻标题
time | str | 缺省（统一为系统时间，最好不用）
address | str | 新闻链接
