#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:14:40 2020

@author: kiran
"""

import pandas as pd




dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

transactions  = []

for i in range(0, len(dataset)):
    
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
    
    
from apyori import apriori

Ass_rules = apriori(transactions , min_support = 0.030 , min_confidence = 0.020 , min_lift = 0.03, min_length = 2)


result = list(Ass_rules)