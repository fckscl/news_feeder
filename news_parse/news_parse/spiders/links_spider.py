# from urllib import response
import scrapy

from news_parse.news_parse.items import NewsParseItem
from scrapy.loader import ItemLoader

class LinksSpider(scrapy.Spider):
    name = "links"
    trashbox = ''
    start_urls = ['https://trashbox.ru/texts/' + trashbox, ]
    
    def parse(self, response):
        self.trashbox = str(int (response.css('span.span_item_active::text').get()) - 1)
        for link in response.css('a.a_topic_cover::attr(href)'):
            yield response.follow(link, callback=self.parse_trashbox)
        

    def parse_trashbox(self, response):
        ld = ItemLoader(item=NewsParseItem(), response=response)

        ld.add_value('next', self.trashbox)
        ld.add_css('text', 'p::text')
        ld.add_css('title', 'title::text')

        yield ld.load_item()