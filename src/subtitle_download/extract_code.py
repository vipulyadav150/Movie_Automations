import requests
from bs4 import BeautifulSoup



def extract_code(r_c):
    imdb_code = r_c.split('/')[2]
    return imdb_code