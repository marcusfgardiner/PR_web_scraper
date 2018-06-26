#import libraries
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

# text to find: 'Preston and Lancashire'

web_page = 'https://en.wikipedia.org/wiki/PR'
page = urlopen(web_page)
print(page)
soup = BeautifulSoup(page, 'html.parser')

for elem in soup(text=re.compile(r'Preston')):
    print(elem)
