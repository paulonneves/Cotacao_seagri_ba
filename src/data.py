from bs4 import BeautifulSoup


def get_data_line(element: BeautifulSoup):
    data = element.find_all('td')
    if data:
        return list(map(lambda dt: dt.text, data))


def generate_data(element: BeautifulSoup):
    table = element.find('table', class_='cotacoes')
    body = table.find('tbody')
    lines = body.find_all('tr')
    data = list(map(get_data_line, lines))

    return data

