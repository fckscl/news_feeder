# from urllib import response
import scrapy


class LinksSpider(scrapy.Spider):
    name = "links"
    trashbox = ''
    start_urls = ['https://trashbox.ru/texts/' + trashbox, ]
    
    def parse(self, response):
        self.trashbox = str(int (response.css('span.span_item_active::text').get()) - 1)
        for link in response.css('a.a_topic_cover::attr(href)'):
            yield response.follow(link, callback=self.parse_trashbox)
        

    def parse_trashbox(self, response):
        title = response.css('title::text').get()
        article = response.css('p::text').get()
        
        yield {
            'title': title,
            'text' : article,
            'next' : self.trashbox            
        }