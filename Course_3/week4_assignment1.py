# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl



url = input('Enter the URL: ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
numlist = []
for span in spans:
    num = int(span.contents[0])
    numlist.append(num)

print('Total of all the numbers is :', sum(numlist))

    