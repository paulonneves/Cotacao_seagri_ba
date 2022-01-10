import csv
from src import (
    generate_url_seagri,
    generate_pagination_url,
    generate_soup,
    find_last_index_pagination,
    generate_data
)

# Arquivo responsável por obter os dados de paginação disponíveis no portal de cotação seagri-ba.


url = generate_url_seagri(url_base='http://www.seagri.ba.gov.br',
                          start_date='01/01/2021',
                          end_date='02/01/2022')
print("[SPIDER] -> URL inicial formatada")
soup = generate_soup(url=url)

links = soup.find_all('a')
print("[SPIDER] -> Links da página inicial obtidos.")
latest_index = find_last_index_pagination(links)

if latest_index:
    with open('output/dados.csv', 'w') as csvfile:
        print("[SPIDER] -> Arquivo csv inicializado")
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['DATA', 'PRODUTO', 'PRAÇA', 'TIPO', 'UNIDADE', 'PREÇO'])

        for index in range(latest_index):
            url = generate_pagination_url(index=index,
                                          url=url)
            soup = generate_soup(url)
            data = generate_data(soup)

            print(f"[SPIDER] -> adicionando a csv: {data}")
            writer.writerows(data)


