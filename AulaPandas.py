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

print('A mediana dos dados foi: ', statistics.median(dados))
print('A moda dos dados foi: ', statistics.mode(dados))