import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://nytimes.com"

urls = [url] #stack of urls to scrape
visited= [url] 

while len(urls) >0:
	try:
		htmltext = urllib.urlopen(urls[0]).read()

	except:
		print urls[0]

	soup = BeautifulSoup(htmltext)

	urls.pop(0)

	for tag in soup.findAll('a',href=True):
		tag['href'] = urlparse.urljoin(url,tag[href])
		if url in tag['href'] and tag['href'] not in visited:

			urls.append(tag['href'])
			visited.append(tag['href'])

print visited