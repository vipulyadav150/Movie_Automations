from src.subtitle_download.extract_code import *
from src.subtitle_download.scrape_file_link import *
from src.subtitle_download.scrape_main_content import *
from src.subtitle_download.storage import *
from src.subtitle_download.user_input import *
from src.subtitle_download.user_choice_of_ratings import *
from src.subtitle_download.retrieve_zip import *


def subtitle_download():
    movie_name  = user_input()
    r_c = scrape_content(movie_name)
    imdb_code = extract_code(r_c)
    linklist,rating_list = scrape_file_link(imdb_code)
    n = user_choice()
    if n == int(1):
        d = retrieve_zip(linklist,rating_list)
        storage_choice(d,movie_name)


