import json


def generate_date_format(date: str):
    source = (date
              .replace('/', '%2F')
              .replace(' ', ''))
    return source


def generate_url_seagri(url_base, start_date, end_date):
    new_start_date = generate_date_format(start_date)
    new_end_date = generate_date_format(end_date)
    url = f'{url_base}/cotacao?produto=&praca=&tipo=' \
          f'&data_inicio={new_start_date}&data_final={new_end_date}'

    return url


def generate_pagination_url(index: int, url: str) -> str:
    url_split = url.split('/cotacao?')

    if url_split:
        pagination_url = f'{url_split[0]}/cotacao?page={index}{url_split[1]}'
        return pagination_url
    return ''
