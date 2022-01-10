from bs4 import BeautifulSoup
from typing import List, Union
import re


def its_latest_item(element: BeautifulSoup) -> bool:
    text = element.text
    return 'fim' in text.lower()


def get_pattern_index(element: BeautifulSoup):
    pattern = re.compile(r'page=(\d+)&')
    href = element.get('href')
    index_pattern = pattern.findall(href)
    index_page = int(index_pattern[0]) if index_pattern else None
    return index_page


def find_last_index_pagination(links: List[BeautifulSoup]) -> Union[int, None]:
    last_element = list(filter(its_latest_item, links))

    if last_element:
        index_page = get_pattern_index(last_element[0])
        return index_page
