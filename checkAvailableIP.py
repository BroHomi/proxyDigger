#coding:utf-8

from requests import *
import re

for proxy in open("https.txt"):
	proxy = proxy.replace('\n','')
	proxies={"https":proxy}
	headers = {
		"Host": "www.baidu.com",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
		"Accept": "*/*",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://www.baidu.com/"
		}
		
	url = 'https://www.baidu.com'
	try:
		html = get(url,timeout=10,headers=headers,proxies=proxies)
		if html.status_code == 200:
			proxy = proxy.split('https://')[1]
		f =  open('./proxyip.txt','a')
		print(proxy,file=f)
	except Exception as e:
		print(e)
		pass
