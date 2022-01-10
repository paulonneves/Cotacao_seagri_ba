# Dashboard Cotação Seagri BA
![image](https://user-images.githubusercontent.com/48892066/148826412-b04823b4-ff6c-4475-87b3-a752ea02bbf4.png)


# Sobre o projeto
> Este projeto se é o código fonte do painel de cotações feito a partir do dados de preço dos produtos disponibilizados no pelo governo da bahia.
> O objetivo é construir uma visualização inteligente e intuitiva para os pequenos produtores que desejam acompanhar os preços e as cidades produtoras.

> Os dados foram coletados a partir da página <a href="http://www.seagri.ba.gov.br/cotacao?produto=&praca=&tipo=&data_inicio=01%2F01%2F2021&data_final=02%2F01%2F2022">Secretaria da Agricultura, Pecuária, Irrigação, Pesca e Aquicultura</a> e também foi utilizado os dados de regiões e cidades da página <a href="http://www.cultura.ba.gov.br/modules/conteudo/conteudo.php?conteudo=314">SECULTBA</a>
> utilizando para a coleta a linguagem de programação Python e as libs requests, bs4 (requisição e parser HTML) e toolz (Ferramenta de programação funcional).
>
> Foram gerados duas tabelas csv dados.csv e regiões.csv, respectivamente, dados de cotação da página seagri-ba e dados de regiões e cidades da página secult-ba.

> A visualização e integração foi feita a partir do software Microsoft Power BI e os elementos como segmentação flutuante e gráficos foram posicionados como forma de fácil seleção para o usuário.

# Instalação
> As tabelas já estão na pasta **output** do repositório, mas caso queira executar o código Python novamente é necessário instalar as dependências com o PIP seguindo o comando:
>> pip install -r requirements.txt
> Em seguida execute os dois comandos a seguir:
>> python regions.py
> 
>> python main.py

# Publicação
> Não foi possível publicar na web devido a falta da licensa Power Bi Pro, mas haverá versões futuras do painel apenas com Python.

# Amostra
![AnyConv com__2022-01-10_16-45-52](https://user-images.githubusercontent.com/48892066/148829846-97ef37d6-b437-4254-8c23-ea2845f677c3.gif)
