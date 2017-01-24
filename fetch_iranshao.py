from bs4 import BeautifulSoup
import requests
import time
import unicodecsv
import os

# start_url = 'http://iranshao.com/bundled_races?page=1&sort=time'
# start_url = 'http://iranshao.com/bundled_races?month=all&page=1'

if not os.path.exists('html_iranshao'):
	os.makedirs('html_iranshao')

# r = requests.get(start_url)
# while r.status_code != 200:
# 	time.sleep(10)
# 	r = requests.get(start_url)

# soup1 = BeautifulSoup(r.content, 'html.parser')
# ul = soup1.find('ul', {'class':'pagination'})
# page_num = len(ul.find_all('li')) - 2
# print 'TOTAL', page_num, 'PAGES'
page_num = 107
failed_urls = []
for i in range(page_num):
	time.sleep(2)
	url = 'http://iranshao.com/bundled_races?month=all&page=%s' % (i+1)
	response = requests.get(url)
	times_tried = 0
	while (response.status_code != 200) and (times_tried < 10):
		time.sleep(10)
		times_tried += 1
		response = requests.get(url)

	if times_tried >= 10:
		print 'FAIL', url
		failed_urls.append(url)
		continue

	with open(os.path.join('html', 'page') + str(i) + '.html', 'wb') as f0:
		f0.write(response.content)

	print 'GOT', url

with open('failed_urls.txt', 'w') as f:
	f.writelines(failed_urls)