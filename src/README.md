# Entendendo as Funções
## Documentação do src

A pasta SRC contém funções de captura de dados da fonte SEAGRI-BA

Arquivo HTML_SOUP:
> Há apenas uma função no arquivo **generate_soup** que recebe uma **url** e retorna um **Objeto BS4**.
> É necessária devido a quantidade massiva de requisições que deve-se fazer e isolar o processo de fazer a requisição 
> e transformar em objeto bs4 ajudou muito a organizar o código.

Arquivo URLS:
> Há 3 funções no arquivo de URLS descritas abaixo:
> 
> generate_date_format recebe um texto de data formatado como 02/05/2021 
> e devolve esta data formatada como 02%2F05%2F2021. Essa formatação é necessária, pois
> esta url irá servir para fazer requisições ao navegador e não pode ter caracteres inválidos.
> 
> generate_url_seagri recebe como parâmetros a url padrão,  start_date e end_date, ou seja, recebe a url e um período dividido por duas datas.
>  A url padrão tem o formato como  http://www.seagri.ba.gov.br, mas precisamos adicionar o periodo e os outros atributos
> A url final fica assim: http://www.seagri.ba.gov.br/cotacao?produto=&praca=&tipo=&data_inicio=01%2F01%2F2021&data_final=02%2F01%2F2022
> 
> generate_pagination_url recebe dois parâmetros index e url, em que index é o indice da página acessada.
> A função faz um corte na url e adiciona o atributo page= e o valor do indice retornando uma url com paginação correta.

Arquivo LATEST_PATTERN:
> Há 3 funções no arquivo de Latest_pattern descritas abaixo:
> 
> its_latest_item recebe um objeto bs4 e verifica se o texto desse elemento contém a palavra
> "fim". Essa função será aplicada em uma série de links e o link que contém o texto fim 
> é provavelmente o ultimo link da paginação validando esse elemento.
> 
> get_pattern_index recebe um objeto bs4 e extrai o índice da paginação contido href do elemento.
> Por exemplo: O formato em que chega o href do objeto é  http://www.seagri.ba.gov.br/cotacao?produto=page=25&praca=&tipo=[...] 
> e é extraido o indice 25.
> 
> find_last_index_pagination aplica as duas funções anteriores numa lista de elementos assim obtendo o indice
> do elemento de paginação final.

Arquivo DATA:
> Há 2 funções no arquivo Data descritas abaixo:
> 
> get_data_line recebe um elemento bs4 e retorna uma lista de elementos de tabela.
> Ou seja, recebe um objeto linha de tabela (tr) e retorna a lista de itens presentes nessa linha.
> 
> generate_data recebe um objeto bs4, captura a tabela presente na página, seleciona todas as linhas da tabela
> e aplica a função anterior obtendo todos itens da tabela em listas.

### Skills
🕷️ Web Scrapping

🦉 Programação Funcional

🎮 Visual interativo

🐍 Python

📊 Power Bi Desktop
