# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 23:09:39 2022

@author: Ramon Barros

Criar gráfico mostrando o crescimento populacional brasileiro 1980-2016
Dados: DataSus
"""
import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))
        
plt.bar(x, y, color="#87CEFA")
plt.plot(x, y, color="#00008b", linestyle="-")

plt.title("Vitórias do Flamengo no Brasileiro")
plt.xlabel("Ano")
plt.ylabel("Vitórias")
#plt.show()
plt.savefig("Grafico_Fla.pdf")