import requests
from bs4 import BeautifulSoup

rating_list = []
linklist = []
def scrape_file_link(imdb_code):
    response = BeautifulSoup(requests.get("http://www.yifysubtitles.com/movie-imdb/" + imdb_code).text, "html.parser")

    for x in response.findAll('tr'):

        data = x.text
        if 'English' in data:
            for y in x.findAll('span', {'class': 'label label-success'}):
                rating_list.append(int(y.text))
                r1_c = x.find('a').get('href')
                linklist.append("http://www.yifysubtitles.com" + r1_c)
    return linklist,rating_list