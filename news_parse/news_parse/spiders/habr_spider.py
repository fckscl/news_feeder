# from urllib import response
import scrapy

from news_parse.news_parse.items import NewsParseItem
from scrapy.loader import ItemLoader

class HabrSpider(scrapy.Spider):
    name = "habr"
    trashbox = ''
    start_urls = ['https://habr.com/ru/flows/develop/' + trashbox, ]
    
    def parse(self, response):
        # self.trashbox = str(int (response.css('span.span_item_active::text').get()) - 1)
        for link in response.css('a.tm-article-snippet__title-link::attr(href)'):
            yield response.follow(link, callback=self.parse_habr)
        

    def parse_habr(self, response):
        ld = ItemLoader(item=NewsParseItem(), response=response)
        
        ld.add_value('next', self.trashbox)
        ld.add_css('text', 'p::text')
        ld.add_css('title', 'title::text')
        ld.add_value('link', response)

        yield ld.load_item()