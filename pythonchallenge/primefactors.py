# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:44:14 2023

@author: Ludovico
"""


def findprimefactors(number):
    factorlist = []
    primefactor = 2
    while (number > 1):
        cociente = number // primefactor
        residuo = number % primefactor
        if residuo == 0:
            factorlist.append(primefactor)
            number = cociente
            cociente = cociente // primefactor
        else:
            primefactor += 1
    return factorlist


a = findprimefactors(780)
print(a)
