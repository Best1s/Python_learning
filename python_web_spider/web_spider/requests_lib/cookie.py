#-*- coding: utf-8 -*-
import requests
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.baidu.com',headers=headers)
for cookie in r.cookies.keys():  #get cookie
  print cookie + ':' + r.cookies.get(cookie)

'''  def cookie
cookies = dict(name='qiye',age='10')
r = requests.get('http://www.baidu.com',headers=headers,cookies=cookies)
print r.text
'''