# from urllib import response
import scrapy

from news_parse.news_parse.items import NewsParseItem
from scrapy.loader import ItemLoader

class TprogerSpider(scrapy.Spider):
    name = "tproger"
    next = ''
    start_urls = ['https://tproger.ru/articles/' + next, ]
    
    def parse(self, response):
        self.next = 'page2'
        for link in response.css('a.article__link::attr(href)'):
            yield response.follow(link, callback=self.parse_Tproger)
        

    def parse_Tproger(self, response):
        ld = ItemLoader(item=NewsParseItem(), response=response)
        
        ld.add_value('next', self.next)
        ld.add_css('text', 'p::text')
        ld.add_css('title', 'title::text')
        ld.add_value('link', response)

        yield ld.load_item()