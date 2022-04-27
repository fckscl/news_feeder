from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

from news_parse.news_parse.spiders.links_spider import LinksSpider
from news_parse.news_parse.spiders.habr_spider import HabrSpider
from news_parse.news_parse.spiders.tproger_spider import TprogerSpider
from scrapy.crawler import CrawlerProcess
from twisted.internet.error import ReactorAlreadyInstalledError
import webbrowser    
import csv
 
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.toast import toast


class News(BoxLayout):
    link = ''

    def __init__(self, title, text, link, **kwargs):
        super().__init__(**kwargs)
        self.ids.button_title.text = title
        self.ids.label_text.text = text
        self.link = link
    
    def button_clicked(self):
        print(self.link)    
        webbrowser.open(self.link)
    

class Stack(BoxLayout):
    def site_selected(self, text_site):
        try:
            process = CrawlerProcess(settings={
                "FEEDS": {
                    "items.csv": {
                        "format": "csv",
                        'overwrite': 'True'},
                },
                'LOG_ENABLED': 'False'
            })

            if text_site == 'Trashbox':
                process.crawl(LinksSpider)
            elif text_site == 'Habr':
                process.crawl(HabrSpider)
            elif text_site == 'Tproger':
                process.crawl(TprogerSpider)

            process.start()
            process.stop()
        except ReactorAlreadyInstalledError:
            toast('Для выбора другого сайта перезапустите приложение')

        with open("items.csv", encoding='utf-8') as r_file:
            # Создаем объект DictReader, указываем символ-разделитель ","
            file_reader = csv.DictReader(r_file, delimiter = ",")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count == 0:
                    # Вывод строки, содержащей заголовки для столбцов
                    print(f'Файл содержит столбцы: {", ".join(row)}')
                # Вывод строк
                count += 1
                topick = row['text'][:1000] + '...\nДля просмотра полной статьи нажмите на кнопку-заголовок'
                n = News(row['title'], topick, row['link'][6:-2])
                self.add_widget(n)
            print(f'Всего в файле {count + 1} строк.')
        self.children[-1].text = text_site

    
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
            items=menu_items,
            max_height=dp(168),
            background_color = '#4869D6',
            radius=[24, 4, 24, 4]
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