import scrapy
from ..items import QuotesItem
from ..pipelines import MysqlPipeline
from bs4 import BeautifulSoup
from ..items import CoreyMSItem

class CoreymsSpider(scrapy.Spider):
    name = "coreyms"

    def start_requests(self):
        urls = [
            'https://coreyms.com/'
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    def parse(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = CoreyMSItem()
        soup = BeautifulSoup(response.text, 'lxml')
        # print(soup.prettify())
        for article in soup.find_all('article'):
            header = article.find('header').h2.a.text
            summary = article.find('div', class_='entry-content').p.text
            try:
                vid_src = article.find('iframe', class_='youtube-player')['src']
                vid_id = vid_src.split('/')[4]
                vid_id_orig = vid_id.split('?')[0]
                youtube_link = f'https://www.youtube.com/watch?v={vid_id_orig}'
            except:
                youtube_link = None
            item['header'] = header
            item['summary'] = summary
            item['youtube_link'] = youtube_link
            print(item)
            yield item