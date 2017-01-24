from bs4 import BeautifulSoup
import requests
import unicodecsv as csv
import os
import time

race_url = 'http://zuicool.com/events?page={0}&per-page=15'

try:
	os.makedirs('html_zuicool')
except Exception as e:
	pass

page = 0
while True:
	r = requests.get(race_url.format(page))
	while r.status_code != 200:
		time.sleep(1)
		r = requests.get(race_url.format(page))

	soup = BeautifulSoup(r.content)
	if soup.find('h4',{'class':'name'}) is None :
		break

	with open(os.path.join('html_zuicool','page')+str(page)+'.html', 'w') as f:
		f.write(r.content)

	time.sleep(0.5)
	page += 1