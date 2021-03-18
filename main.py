#!/usr/bin/env python
#
#----------------------------------------------------------------------------------------------------------------------
#
#../MATRIZ_DISTANCIAS/main.py - gera uma matriz de distancias entre localizações utilizando API Google Maps
#
#Autor: Leandro Barroso <lrbarroso84@hotmail.com>
#
#Histórico:
#
#   v1.0 2021-03-15, Leandro Barroso
#       - versão inicial
#
#Licença: MIT No Attribution License
#----------------------------------------------------------------------------------------------------------------------

import googlemaps
import pandas as pd
import json

gmaps = googlemaps.Client(key='CHAVE_DA_API')
entrada = pd.read_excel('files/entrada.xlsx')
origens = entrada["NOME_ORIGEM"].tolist()
destinos = entrada["NOME_DESTINO"].tolist()
matriz = pd.DataFrame(index=origens,columns=destinos)
resultados = {}
resultados["consultas"] = []

#Cada origem da entrada percorre todos os destinos, calculando a origem e preencendo a matriz resultado
for id_origem, local_origem in enumerate(entrada["LOCAL_ORIGEM"].tolist()):
    
    #Quando o número de origens é maior que o de destinos, ocorrerá a leitura de células vazias na planilha de entrada.
    #Esses valores de células vazias são interpretados pela biblioteca pandas com o formato float.
    if type(local_origem) is float:
        break
    for id_destino, local_destino in enumerate(entrada["LOCAL_DESTINO"].tolist()):
        
        #Mesma lógica da condicional acima para o caso de número de origens maior que destinos
        if type(local_destino) is float:
            break
        try:
            consulta = gmaps.distance_matrix(local_origem, local_destino)
            print(consulta)
            #O resultado da distância na consulta é dado em metros, por isso a necessidade de dividir por 1000
            distancia = int(consulta['rows'][0]['elements'][0]['distance']['value'] / 1000)
            resultados["consultas"].append(consulta)
        except Exception as e:
            print(e)
            distancia = ''

        matriz.iat[id_origem, id_destino] = distancia

#imprime a matriz de distâncias no terminal e salva em formato excel
print(matriz)
escritor = pd.ExcelWriter('files/saida.xlsx')
matriz.to_excel(escritor, 'MATRIZ')
escritor.save()

#salva os resultados da consulta no formato JSON
with open('files/resultados.json', 'w') as outfile:
    json.dump(resultados, outfile)

#Possíveis falhas e propostas de melhorias
#FIXME: não funciona para a cidade de Macapá, capital do Amapá. Provável por falta de rota de terrestre 
#TODO: implementar consulta utilizando não apenas rotas terrestres
#TODO: implementar funcionalidade para não executar consultas repetidas, reduzindo consumo da API
