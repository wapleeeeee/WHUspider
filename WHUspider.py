# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup as bs
import sys
import json
import time

class WHUspider:

	def __init__(self):
		self.WHUCSurl = "http://cs.whu.edu.cn/"
		self.WHUurl = "http://www.whu.edu.cn/"

	#调用该方法返回WHUCS信息JSON
	def WHUCSrequestFromUrl(self):	
		para = []
		requestsUrl = requests.get(self.WHUCSurl)
		requestsUrl.encoding = 'utf-8'
		msgSoup = bs(requestsUrl.text,'lxml')
		msgList = msgSoup.article.find_all('dd')

		for singleMsg in msgList:
			_dict = dict.fromkeys(('title','time','address'),None)
			_dict['title'] = singleMsg.a.string
			_dict['time'] = singleMsg.span.string[1:-1]
			_dict['address'] = self.WHUCSurl[:-1] + singleMsg.a.get('href')
			if _dict['title'] != u'更多':
				para.append(_dict)
		_json = json.dumps(para)

		return _json

	#调用该方法返回WHU信息JSON
	def WHUrequestFromUrl(self):
		para = []
		msgList = []
		requestsUrl = requests.get(self.WHUurl)
		requestsUrl.encoding = 'utf-8'
		msgSoup = bs(requestsUrl.text,'lxml')
		for partMsg in msgSoup.find_all('div',attrs={'class':'col-sm-4'}):
			msgList.extend(partMsg.find_all('a',attrs={'target':'_blank','title':re.compile('.+')}))
		
		for singeMsg in msgList:
			_dict = dict.fromkeys(('title','time','address'),None)
			_dict['title'] = singeMsg.string
			addressTmp = singeMsg.get('href')
			_dict['address'] = addressTmp if addressTmp[:4] == 'http' else self.WHUurl+addressTmp
			_dict['time'] = time.strftime("%m-%d",time.localtime())
			para.append(_dict)
		_json = json.dumps(para)

		return _json

def main():
	#spider = WHUspider()
	#WHUCSjson = spider.WHUCSrequestFromUrl()
	#para = json.loads(WHUCSjson)
	#WHUjson = spider.WHUrequestFromUrl()
	#para = json.loads(WHUjson)
	

if __name__ == '__main__':
	main()