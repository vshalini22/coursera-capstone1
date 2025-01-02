from bs4 import BeautifulSoup
from urllib import request
url = input('Enter - ')
html=request.urlopen(url).read()
soup = BeautifulSoup(html)
tag = soup("span")
count = 0
total = 0
for i in tag:
	x = int(i.text)
	count += 1
	total += x
print("Count " + str(count))
print("Sum" + str(total))