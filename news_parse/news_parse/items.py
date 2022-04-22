# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose


class NewsParseItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(output_processor = TakeFirst())
    text = scrapy.Field()
    next = scrapy.Field()
    link = scrapy.Field()
