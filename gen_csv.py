from bs4 import BeautifulSoup
import unicodecsv as csv
import os

soups = []
for i in range(107):
	with open(os.path.join('html', 'page') + str(i) + '.html', 'r') as f:
		soups.append(BeautifulSoup(f.read(), 'html.parser'))


race_names = []
for s in soups:
	race_divs = s.find_all('div', {'class':'itemname'})
	for div in race_divs:
		race_names.append(div.a.get_text().encode('utf-8'))

print 'TOTAL', len(race_names)
with open('race_name.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(sorted(race_names, key=len))

