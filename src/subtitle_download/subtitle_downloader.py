import hashlib
import os
import requests
from bs4 import BeautifulSoup
import os


rating_list = []
linklist = []
name  = 'Batman Begins'
list_name = '+'.join(name.split(' '))
imdb_link = "http://www.imdb.com/find?&q="+list_name
r =requests.get(imdb_link)
soup = BeautifulSoup(r.text,"html.parser")
r_c = soup.find('table',{'class':'findList'}).a['href']
imdb_code = r_c.split('/')[2]

response = BeautifulSoup(requests.get("http://www.yifysubtitles.com/movie-imdb/"+imdb_code).text,"html.parser")

for x in response.findAll('tr'):

    data = x.text
    if 'English' in data:
        for y in x.findAll('span',{'class':'label label-success'}):
            rating_list.append(int(y.text))
            r1_c = x.find('a').get('href')
            linklist.append("http://www.yifysubtitles.com" + r1_c)


print(rating_list)


n = int(input("Want to Download the subtitles with best ratings or choose from options ( 1 or 2)"))
if n == int(1):
    i = rating_list.index(max(rating_list))
    imp_link = linklist[i]


    soup = BeautifulSoup(requests.get(imp_link).text,"html.parser")
    d_link = soup.find('a',{'class':'btn-icon download-subtitle'}).get('href')
    # print(d_link)



    d = requests.get(d_link)
    with open("code.zip","wb") as f:
        f.write(d.content)


