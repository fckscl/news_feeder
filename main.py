from cgitb import text
from optparse import Values
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from bs4 import BeautifulSoup
from kivy.uix.spinner import Spinner
import requests
from news_parse.news_parse.spiders.links_spider import LinksSpider
#from mnist import res
 

class News(BoxLayout):
    t = 'Заглавие новости'
    parse = 'You can bind to events in Kv using the “:” syntax, that is, associating a callback to an event:Widget:    on_size: my_callback()You can pass he values dispatched by the signal using the args eyword:TextInput:    on_text: app.search(args[1])More omplex expressions can be used, like:pos: self.enter_x - self.texture_size[0] / 2., self.center_y - elf.texture_size[1] / 2.This expression listens for a hange in center_x, center_y, and texture_size. If one of them changes, the expression will be re-evaluated to update the pos field.'

    def __init__(self, url, **kwargs):
        super().__init__(**kwargs)
        #url = 'https://habr.com/ru/post/544828/'
        r = requests.get(url)
        page = BeautifulSoup(r.text, 'html.parser')
        self.t = page.title.text
        print(self.t)
        self.parse = page.find('div', xmlns="http://www.w3.org/1999/xhtml").text
    
    def button_clicked(self):
        print(self.t)
        #self.parent.ids.label_text.text = self.parent.parse
        #self.ids.label_text.text = self.parse
    

class Stack(BoxLayout):
    def site_selected(spinner, text):
        for i in range(0, 10):
            n = News('https://habr.com/ru/post/544828/')
            n.t = str(i+1)
            #n.parse = "Hello!"
            spinner.parent.add_widget(n)
            print(text)
        btn_next = Button(text='next page')
        btn_next.size_hint = (1, None)
        btn_next.height = dp(48)
        spinner.parent.add_widget(btn_next)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dd = Spinner(size_hint_y=None, height=dp(48), values=('Habr', 'Tproger', 'Trashbox'), text='Сайт')
        dd.bind(text = Stack.site_selected)
        self.add_widget(dd)


class MainApp(App):
    pass


MainApp().run()