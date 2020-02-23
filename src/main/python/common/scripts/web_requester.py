import logging
import requests


class WebRequester:

    def __init__(self):
        self._response_dic = {}

    @staticmethod
    def __check_valid_response(response):
        return response.status_code == 200

    def request_response(self, web_page_dic):

        for theater_name in web_page_dic.keys():
            web_page_response = requests.get(web_page_dic[theater_name])
            if self.__check_valid_response(web_page_response):
                web_page_response_text = web_page_response.text.strip()
                self._response_dic[theater_name] = web_page_response_text
            else:
                logging.info(f" Web page not retrieved successfully, {theater_name}")
        return self._response_dic
