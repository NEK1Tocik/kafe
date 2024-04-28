from bs4 import BeautifulSoup
from selenium import webdriver
from .models import PizzaItem
from time import sleep
from random import random


class Parser:

    def __init__(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.set_window_position(1919, 1079)
        driver.get("https://dodopizza.by/minsk")
        driver.execute_script("window.scrollTo(0, 1700);")
        sleep(0.1)
        driver.execute_script("window.scrollTo(0, 3500);")
        sleep(0.1)
        driver.execute_script("window.scrollTo(0, 5000);")
        self.resp = driver.page_source
        driver.quit()

    def get_pizza_by_link(self):
        resp = self.resp
        pizza_items = []
        to_parse = BeautifulSoup(resp, 'html.parser')
        pizza_menu = to_parse.find('section', attrs={'id': 'qooaq'})
        raw_menu = pizza_menu.find_all('main', class_='sc-1tpn8pe-0 dszYBt')
        for elem in raw_menu:
            try:
                description = elem.text
            except:
                description = ''
            try:
                name = elem.find('div', {'data-gtm-id': 'product-title'}).text
            except:
                name = ''
            try:
                img_url = elem.find('img', {'class': 'img'}).attrs['src']
            except:
                img_url = ''

            pizza_items.append((description, name, img_url, round(15 + random() * 10, 2)))

        return pizza_items


    def run(self):
        pizza_items = self.get_pizza_by_link()
        PizzaItem.objects.all().delete()
        for item in pizza_items:
            PizzaItem.objects.create(description=item[0], name=item[1], image_url=item[2], price=item[3])
