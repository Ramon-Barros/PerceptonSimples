# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 22:50:31 2022

@author: Ramon Barros
"""
import matplotlib.pyplot as plt

#vizualização de dados em python

x = ['jan/21','fev/21','mar/21','abr/21','mai/21','jun/21','jul/21','ago/21','set/21','out/21','nov/21','dez/21','jan/22']
y = [217, 213, 196, 234, 195, 205, 249, 264, 254, 252, 280, 260, 280]

titulo = "Gráfico de consumo de Enegia"
eixox = "Meses"
eixoy = "Consumo"

plt.figure(figsize=(12,5))
#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.plot(x, y, color="#00008B", linestyle="-")
plt.scatter(x, y, label="pontos", color="r", marker=".", s=150)

plt.legend()
#plt.show()
plt.savefig("Grafico 1.png", dpi=300)
