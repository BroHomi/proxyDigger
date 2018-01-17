#coding:utf-8

from requests import *
import re

headers = { "accept":"text/html,application/xhtml+xml,application/xml;",
            "accept-encoding":"gzip",
            "accept-language":"zh-cn,zh;q=0.8",
            "referer":"Mozilla/5.0(compatible;Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
            "connection":"keep-alive",
            "user-agent":"mozilla/5.0(windows NT 6.1;wow64) applewebkit/537.36 (khtml,like gecko)chrome/42.0.2311.90 safari/537.36"
            }

for i in range(1,835):
	url = 'http://www.xicidaili.com'
	url = url + '/wn/'
	url = url + str(i)
	html = get(url,timeout=3,headers=headers)
	html.encoding = html.apparent_encoding
	proxyip = r'(<td>.*</td>)'
	iplist = re.findall(proxyip,html.text)
	i = 1
	for ip in iplist:
		ip = (ip.split('<td>')[1]).split('</td>')[0]
		f =  open('./ip.txt','a')
		print(ip,file=f)
		if i%5==0:
			print('\n',file=f)
		i = i + 1
