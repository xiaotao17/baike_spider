# coding:utf8
import requests


class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None

        response = requests.get(url)
        #print(response.encoding)
        if response.status_code != 200:
            return None
        response.encoding = "utf-8"
        return response.text