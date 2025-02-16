import requests
from bs4 import BeautifulSoup


def get_all_links(url):
    responce = requests.get(url).text
    soup = BeautifulSoup(responce, "html.parser")
    for link in soup.find_all("a"):
        print(link.get("href"))


url = input("Введите URL-адрес веб-страницы: ")

get_all_links(url)

