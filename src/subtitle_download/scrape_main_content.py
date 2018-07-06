import requests
from bs4 import BeautifulSoup



def scrape_content(movie_name):
    list_name = '+'.join(movie_name.split(' '))
    imdb_link = "http://www.imdb.com/find?&q=" + list_name
    r = requests.get(imdb_link)
    soup = BeautifulSoup(r.text, "html.parser")
    r_c = soup.find('table', {'class': 'findList'}).a['href']
    return r_c