import requests
from bs4 import BeautifulSoup



def retrieve_zip(linklist,rating_list):
    i = rating_list.index(max(rating_list))
    imp_link = linklist[i]

    soup = BeautifulSoup(requests.get(imp_link).text, "html.parser")
    d_link = soup.find('a', {'class': 'btn-icon download-subtitle'}).get('href')
    d = requests.get(d_link)
    return d

