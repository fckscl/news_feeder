from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.uix.spinner import Spinner

from news_parse.news_parse.spiders.links_spider import LinksSpider
# from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
 
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDFillRoundFlatButton, MDRoundFlatButton
from kivymd.uix.menu import MDDropdownMenu


class News(BoxLayout):
    t = 'Заглавие новости'
    parse = 'You can bind to events in Kv using the “:” syntax, that is, associating a callback to an event:Widget:    on_size: my_callback()You can pass he values dispatched by the signal using the args eyword:TextInput:    on_text: app.search(args[1])More omplex expressions can be used, like:pos: self.enter_x - self.texture_size[0] / 2., self.center_y - elf.texture_size[1] / 2.This expression listens for a hange in center_x, center_y, and texture_size. If one of them changes, the expression will be re-evaluated to update the pos field.'

    def __init__(self, title, text, **kwargs):
        super().__init__(**kwargs)
        #url = 'https://habr.com/ru/post/544828/'
        self.t = title
        self.parse = text
        # print(self.t)
    
    def button_clicked(self):
        print(self.t)
        #self.parent.ids.label_text.text = self.parent.parse
        #self.ids.label_text.text = self.parse
    

class Stack(BoxLayout):
    def site_selected(self, text_site):
        print(self)
        configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
        runner = CrawlerRunner()

        # process = CrawlerProcess({
        #     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        # })

        # process.crawl("links", domain='scrapy.org')
        # process.start(stop_after_crawl=False)
        d = runner.crawl(LinksSpider)
        d.addBoth(lambda _: reactor.stop())
        reactor.run()
        # # for i in data:
        # #     print(i)
        for i in range(10):
            n = News('text', 'title')
            n.t = str(i+1)
            self.add_widget(n)
        btn_next = MDFillRoundFlatButton(text=f'Следующая страница {text_site}', on_release=lambda _: self.site_selected(text_site=text_site))
        btn_next.size_hint = (1, None)
        btn_next.height = dp(48)
        # btn_next.on_release = self.
        self.add_widget(btn_next)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        site = MDRoundFlatButton(
            text='Сайт',
            size_hint = (1, None),
            height = dp(48)
            )
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                'on_release': lambda x=f"{i}": self.site_selected(x)
            } for i in ('Habr', 'Trashbox', 'Tproger')
        ]
        select = MDDropdownMenu(
            width_mult=4,
            caller=site, 
            items=menu_items
            )
        site.on_release = select.open
        self.add_widget(site)
        

class MainApp(MDApp):
    theme_cls = ThemeManager()
    title = 'JankYard'
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return super().build()


MainApp().run()