import csv
from src import generate_soup

# Arquivo responsável por capturar os nomes e cidades das subregiões da bahia para agrupamento no visual.

soup = generate_soup('http://www.cultura.ba.gov.br/modules/conteudo/conteudo.php?conteudo=314')
print("[SPIDER] -> HTML gerado da páfina cultura ba finalizado.")

table = soup.find('table')
body = table.find('tbody')
lines = body.find_all('tr')
print("[SPIDER] -> Obtido dados da tabela.")

with open('output/regiões.csv', 'w') as csvfile:
    print("[SPIDER] -> Arquivo csv inicializado")
    writer = csv.writer(csvfile, delimiter=',')
    for line in lines:
        data = [item.text.replace('\n', '') for item in line.find_all('td')]
        print(f"[SPIDER] -> Adicionando ao csv: {data}")

        for item in data[1].split(','):
            writer.writerow([data[0], item])
