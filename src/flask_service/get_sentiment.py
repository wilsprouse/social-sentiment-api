import requests
from bs4 import BeautifulSoup


class Request:

    def __init__(self, ticker, company):
        self.url = ('https://eresearch.fidelity.com/eresearch/evaluate/news/basicNews.jhtml?symbols=' + ticker)
        self.ticker = ticker
        self.company = company

    def make_request(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        #results = soup.find(id='index')

        articles = soup.find_all('li', class_='news-item')
        
        links = []
        for article in articles:
            for href in article.find_all('a', href=True):
                if href.text and '&' in href['href']:
                    links.append(href['href'])

        return links

    def get_articles(self, parsed_urls):
        """Takes the raw url, converts it into a workable format, then retrieves article text and returns it"""
        request = self.make_request()
        working_urls = []
        for url in parsed_urls:
            url = 'https://eresearch.fidelity.com' + url + 'sb=1&sc=1&san=1'
            working_urls.append(url)

        return working_urls

    def parse_article(self, article_url):
        """ Returns article text"""
        page = requests.get(article_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        article = soup.find(id='articleContainer')
        title = soup.find('title')
        title = title.text.replace('\n', '').replace('\t', '')
        if self.company.lower() in title.lower():
            # We want to know if the entire article is about the company, or just a sentence.
            # Will entire this if the comapny is in the title
            return article.text
        else:
            # Will enter this if whole article is not about the company
            sentences = article.text.split('.')
            
            sentences_list = []
            for sentence in sentences:
                if self.ticker in sentence:
                    sentences_list.append(sentence)
            return sentences_list


    def Request_main(self):
        """Main driver for request method"""
        get_urls = self.make_request()

        sentiment_list = []
        for article in self.get_articles(get_urls):
            sentiment_list.append(self.parse_article(article))
        return sentiment_list
