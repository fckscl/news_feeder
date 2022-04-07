from bs4 import BeautifulSoup
import requests

def trashbox():
    url = 'https://trashbox.ru/link/how-to-safely-store-cryptocurrency'

    r = requests.get(url)
    page = BeautifulSoup(r.text, 'html.parser')
    t = page.title.text
    print(t)
    parse = page.findAll('p')
    for i in parse:
        print(i.text)

def tproger():
    url = 'https://tproger.ru/articles/pishem-simuljator-estestvennogo-otbora-na-python/'

    r = requests.get(url)
    page = BeautifulSoup(r.text, 'html.parser')
    t = page.title.text
    print(t)
    parse = page.findAll('p')
    for i in parse:
        print(i.text)

def links():
    pass