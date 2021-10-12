# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 12:22:01 2021

@author: Gurkan
"""

#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#kodlar
#veri yükleme

veriler = pd.read_csv("veriler.csv")

print(veriler)
#veri ön işleme
boy = veriler[["boy"]]
print(boy)

boykilo = veriler[["boy","kilo"]]
print(boykilo)

x = 10

class insan:
    boy = 180
    def kosmak(self,b):
        return b + 10
    
ali = insan()
print(ali.boy)
print(ali.kosmak(90))

