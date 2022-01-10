import requests
from bs4 import BeautifulSoup


def generate_soup(url: str) -> BeautifulSoup:
    page = requests.get(url)

    if page.status_code == 200:
        return BeautifulSoup(page.content, 'html.parser')
    return BeautifulSoup('', 'html.parser')
