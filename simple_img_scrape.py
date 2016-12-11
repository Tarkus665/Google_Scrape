import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('http://www.google.com').read()
soup = BeautifulSoup(page, 'lxml')
counter = 0
for img in soup.find_all('img'):
    with open("image" + str(counter),'wb') as f:
        f.write(urllib.request.urlopen(img['src']).read())
    counter += 1
