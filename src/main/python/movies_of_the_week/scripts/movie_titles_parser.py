import logging

from bs4 import BeautifulSoup

class MovieTitleParser:

    def __init__(self):
        self._movie_titles_dic = {}
        self._munich_theater_Cinema = "CINEMA Filmtheater"

    @staticmethod
    def __clean_movie_titles_list_cinema( web_page_soup):

        def __clean_title_cinema(movie_title_html):
            title_clean_front = str(movie_title_html).strip('<div class="toggler">')
            title_clean_front_and_end = title_clean_front[:title_clean_front.find("\t\t")]
            return title_clean_front_and_end

        movie_list_raw = web_page_soup.find_all("div", class_="toggler")
        return [__clean_title_cinema(movie) for movie in movie_list_raw]

    def clean_movie_titles(self, web_page_response_dic):
        for theater_name in web_page_response_dic.keys():
            web_page_soup = BeautifulSoup(web_page_response_dic[theater_name], 'html.parser')
            if theater_name == self._munich_theater_Cinema:
                self._movie_titles_dic[theater_name] = self.__clean_movie_titles_list_cinema(web_page_soup)

            else:
                logging.info(f" Theater Name {theater_name} not recongnised")
        return self._movie_titles_dic