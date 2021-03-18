# MATRIZ DE DISTÂNCIAS - GOOGLE MAPS API

ENTRADA: Arquivo xlsx (plainlha excel) com dados de origens e destinos
SAÍDA: Arquivo xlsx (plainlha excel) com  a matriz de distâncias gerada e arquivo JSON com os resultados das consultas retornadas pela api do Google Maps

Script em Python que gera uma matriz de distâncias entre localizações utilizando a API Google Maps Distance.
Recebe como entrada uma planilha excel contendo os nomes dos locais, que serão usados como rótulos de linhas e colunas, e as descrições das localidades que serão utilizadas pela api do Google Maps na busca dos dados.
O resultado é uma matriz com as distâncias em quilômetros entre todos os locais de origem e destino.

### Especificações Técnicas

* Linguagem: Python 3.8
* Idioma: Postuguês Brasileiro (pt-BR)
* Bibliotecas externas:
  * Google Maps - https://pypi.org/project/googlemaps/1.0.2/
  * Pandas - https://pandas.pydata.org/

### Especificações da entrada

* Arquivo .xlsx (Microsoft Excel)

* COLUNAS: ID_ORIGEM, NOME_ORIGEM, LOCAL_ORIGEM, ID_DESTINO, NOME_DESTINO, LOCAL_DESTINO

  * ID_ORIGEM: número de identificação da origem. Índice sequencial iniciado em 1.
  * NOME_ORIGEM: rótulo de idenficação da origem na matriz de distâncias. Corresponde ao rótulo de linha na matriz.
  * LOCAL_ORIGEM: informações do local que será enviada à API Google Maps para consulta de rota e distância. Ex.: endereço completo ou coordenadas.
  * ID_DESTINO: número de identificação do destino. Índice sequencial iniciado em 1.
  * NOME_DESTINO: rótulo de idenficação do destino na matriz de distâncias. Corresponde ao rótulo de coluna na matriz.
  * LOCAL_DESTINO: informações do local que será enviada à API Google Maps para consulta de rota e distância. Ex.: endereço completo ou coordenadas.

Exemplo inicial: Matriz de distância entre as capitais brasileiras

Licença: MIT No Attribution License

#### Sobre o repositório:
matriz_distancias - Script Python para geração de matriz de distâncias entre localidades  utilizando API Google Maps
