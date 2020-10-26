#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 08:39:35 2020

@author: kiran
"""

import numpy
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

transaction = [] 


for i in range(0, 7501):
    
    transaction.append([str(dataset.values[i,j]) for j in range(0, 20)]) 
    
    
from apyori import apriori

rules = apriori(transaction, min_support = 0.003 , min_confidence = 0.2 , min_lift = 3, min_length = 2)

result = list(rules)

print(result)  