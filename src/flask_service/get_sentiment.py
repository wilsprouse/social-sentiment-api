import requests
from bs4 import BeautifulSoup


class Request:

    def __init__(self, ticker):
        self.url = ('https://eresearch.fidelity.com/eresearch/evaluate/news/basicNews.jhtml?symbols=' + ticker)

    def make_request(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        #results = soup.find(id='index')

        articles = soup.find_all('li', class_='news-item')

        return articles

