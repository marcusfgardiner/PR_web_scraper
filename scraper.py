#import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# text to find: 'Preston and Lancashire'

web_page = 'https://en.wikipedia.org/wiki/PR'
page = urlopen(web_page)
print(page)
