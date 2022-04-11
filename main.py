from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.spinner import Spinner
from news_parse.news_parse.spiders.links_spider import LinksSpider
#from mnist import res
 
# from KivyMD.kivymd.uix.button import MDRaisedButton
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu
# from kivy.properties import ObjectProperty


class News(BoxLayout):
    t = 'Заглавие новости'
    parse = 'You can bind to events in Kv using the “:” syntax, that is, associating a callback to an event:Widget:    on_size: my_callback()You can pass he values dispatched by the signal using the args eyword:TextInput:    on_text: app.search(args[1])More omplex expressions can be used, like:pos: self.enter_x - self.texture_size[0] / 2., self.center_y - elf.texture_size[1] / 2.This expression listens for a hange in center_x, center_y, and texture_size. If one of them changes, the expression will be re-evaluated to update the pos field.'

    def __init__(self, title, text, **kwargs):
        super().__init__(**kwargs)
        #url = 'https://habr.com/ru/post/544828/'
        self.t = title
        self.parse = text
        print(self.t)
    
    def button_clicked(self):
        print(self.t)
        #self.parent.ids.label_text.text = self.parent.parse
        #self.ids.label_text.text = self.parse
    

class Stack(BoxLayout):
    def site_selected(self, text):
        print(text)
        sp = LinksSpider
        data = sp.start_requests(sp)
        for i in range(10):
            n = News('text', 'title')
            n.t = str(i+1)
            #n.parse = "Hello!"
            self.add_widget(n)
        btn_next = MDRaisedButton(text='next page')
        btn_next.size_hint = (1, None)
        btn_next.height = dp(48)
        self.add_widget(btn_next)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        site = MDRaisedButton(
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
        dd = Spinner(size_hint_y=None, height=dp(48), values=('Habr', 'Tproger', 'Trashbox'), text='Сайт')
        dd.bind(text = Stack.site_selected)
        self.add_widget(dd)


class MainApp(MDApp):
    theme_cls = ThemeManager()
    title = 'Trash'
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return super().build()


MainApp().run()