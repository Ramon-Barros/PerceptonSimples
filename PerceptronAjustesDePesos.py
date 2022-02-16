# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 18:56:32 2022

@author: Ramon Barros
"""

import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0, 0, 0, 1])
pesos =  np.array([0.0, 0.0])
taxaAprendizagem = 0.1


def stepFucntion(soma):
    if(soma >= 1):
        return 1
    return 0
def calcularSaida(registro):
    s = registro.dot(pesos)
    return stepFucntion(s)

def treinar():
    erroTotal = 1
    while (erroTotal !=0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calcularSaida(np.asanyarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem*entradas[i][j]*erro)
                print('pesos atualizados: '+ str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))

treinar()
    