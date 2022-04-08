from urllib import response
import scrapy


class LinksSpider(scrapy.Spider):
    name = "links"
    start_url = ['https://trashbox.ru/texts/']

    def start_requests(self):
        
        urls = ['https://trashbox.ru/texts/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for link in response.css('a.a_topic_cover::attr(href)'):
            yield response.follow(link, callback=self.parse_trashbox)

    def parse_trashbox():
        title = response.css('title::text').get()
        article = response.css('p::text')
        t = map(response.css.get, article)
        yield {
            'title': title,
            'text' : t
        }