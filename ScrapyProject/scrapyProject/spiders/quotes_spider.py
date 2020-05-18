import scrapy
from ..items import QuotesItem
from ..pipelines import MysqlPipeline

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
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
        for quote in response.css('div.quote'):
            item = QuotesItem()
            #item = MysqlPipeline(): this does not work
            # yield {
            #     'text': quote.css('span.text::text').get(),
            #     'author': quote.css('small.author::text').get(),
            #     'tags': quote.css('div.tags a.tag::text').getall(),
            # }
            item['text'] = quote.css('span.text::text').get(),
            item['author'] = quote.css('small.author::text').get(),
            item['tags'] = quote.css('div.tags a.tag::text').getall()
            item['last_upd_timestamp'] = '2020-05-17 21:30:00'
            yield item