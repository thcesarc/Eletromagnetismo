# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 05:01:21 2022

@author: thiago césar ceará
Lê um conjunto de cargas e suas posições e calcula o campo elétrico num ponto fornecido
"""
import numpy as np #biblioteca para tratar com matrizes

numero_cargas = int(input('Informe quantas cargas estão dispostas no espaço: ')) 

vetor_ponto_prova = []
vetor_ponto_prova.append(float(input('Qual a coordenada x do ponto de prova?')))
vetor_ponto_prova.append(float(input('Qual a coordenada y do ponto de prova?')))
vetor_ponto_prova.append(float(input('Qual a coordenada z do ponto de prova?')))

Carga = np.zeros((numero_cargas,4)) #cria matriz vazia de mxn = numero de cargas x 4 (3 colunas de coordenada e 1 do valor da carga)

for linha in range(0,numero_cargas):#fornecimentos das cargas e suas posições
    print('Informe a coordenada x da carga ',linha+1)
    Carga[linha][0] = input()
    print('Informe a coordenada y da carga ',linha+1)
    Carga[linha][1] = input()
    print('Informe a coordenada z da carga ',linha+1)
    Carga[linha][2] = input()
    print('Informe o valor da carga ',linha+1)
    Carga[linha][3] = input()
    
#do princípio da superposição, somar cada distribuição de campo de cada carga
#Campo elétrico = constante k * carga * componente vetorial da equação
k = 9 * 10**(9) #constante elétrica 
campo_eletrico = 0
for linha in range(0, numero_cargas):
        
        #A componente vetorial depende da posição da carga, que são os dados da matriz Carga: da coluna zero à coluna 2
        posicao_carga = Carga[linha][0:3]
        componente_vetorial = (vetor_ponto_prova - posicao_carga) 
        print(componente_vetorial)
        
        campo_eletrico_temp = k * Carga[linha][3] * componente_vetorial / (np.linalg.norm((componente_vetorial)))**3
        campo_eletrico = campo_eletrico + campo_eletrico_temp
      
print('Campo Elétrico =', campo_eletrico)     
    
a = input('Aperte Enter para terminar')
