import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class LinksCrawlSpider(CrawlSpider):
    name = "links"
    start_url = ['https://trashbox.ru/texts/']

    rules = (
        Rule(LinkExtractor(allow='texts')),
        Rule(LinkExtractor(allow='link', callback='parse_links'))
    )

    def parse_links(self, response):
        pass
