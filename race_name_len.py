import unicodecsv as csv
import matplotlib.pyplot as plt
import random
import numpy as np

names = []
with open('race_name.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		names = row

name_lens = []
for n in names:
	name_lens.append(len(n))

print names[0], len(names[0])
print min(name_lens),max(name_lens)

 
data = name_lens



bins = np.arange(1,max(data),1) 


fig, ax = plt.subplots() 
plt.xlim([0, max(data)+5])
plt.hist(data, bins=bins, alpha=0.5)
plt.title('histogram of race names\' length')
plt.xlabel('length')
plt.ylabel('count')


# plt.grid()
plt.show()