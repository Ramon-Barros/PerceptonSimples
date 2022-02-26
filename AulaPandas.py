# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 21:37:53 2022

@author: Ramon Barros
"""

import statistics 
import numpy as np
import pandas as pd

dados = [9, 10, 13, 12, 9, 14, 9, 13, 10, 14, 10, 13, 11, 11, 9, 12, 13, 13,
         
12, 12, 13, 10, 11, 11, 11]

print('ROL', dados)

#usando o modulo statistics
print('A mediana dos dados foi: ', statistics.median(dados))
print('A moda dos dados foi: ', statistics.mode(dados))
print('O número minimos dos dados foi: ', min(dados))
print('O número máximos dos dados foi: ', max(dados))
print("A media dos Dados foi: ", statistics.mean(dados))
print("O Desvio padrao foi: ", statistics.stdev(dados))
print("A variancia foi: ", statistics.variance(dados),"\n")

#usando a biblioteca pandas
example_series =  pd.Series([214, 222, 215, 218, 206, 238, 217, 213,
                             196, 234, 195, 205, 249])

print('A Média dos Dados foi: ', example_series.mean())
print('A Mediana dos Dados foi: ', example_series.median())
print('A Moda dos Dados foi: ', example_series.mode())
print('A Quantil dos Dados foi: ', example_series.quantile())
print('A Quantil 25% dos Dados foi: ', example_series.quantile(q=0.25))
print('A Amplitude dos Dados foi: ', example_series.max() - example_series.min())
print('A Variancia dos Dados foi: ', example_series.var())
print('A Desvio Padrão dos Dados foi: ', example_series.std())

size, scale = 1000,10
import matplotlib.pyplot as plt

commutes = pd.Series(np.random.gamma(scale, size=size)**1.5)
commutes.plot.hist(grid=True, bins=20, rwidth=0.9, color='#597586')
plt.title('Commute Times for 1,000 Commuters')
plt.xlabel('Counts')
plt.ylabel('Commute Time')
plt.grid(axis='y', alpha=0.75)