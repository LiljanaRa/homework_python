import requests
from bs4 import BeautifulSoup


def get_headings(url, heading_level):
    responce = requests.get(url).text
    soup = BeautifulSoup(responce, "html.parser")
    headings = soup.find_all(heading_level)
    for heading in headings:
        print(heading_level, heading.text)


url = input("Введите URL-адрес веб-страницы: ")
heading_level = input("Выберите уровень заголовка(h1, h2, h3, h4, h5 или h6): ")

get_headings(url, heading_level)
