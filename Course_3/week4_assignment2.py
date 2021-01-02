# http://py4e-data.dr-chuck.net/known_by_Amrinder.html

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter Count: ')) 
position = int(input('Enter Position:')) 

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags_lst = list()

for x in range(0,count):
    tags = soup('a')
    my_tags = tags[position-1]
    needed_tag = my_tags.get('href', None)
    url = str(needed_tag)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    print('Retrieved: ', my_tags.get('href', None))

    
    