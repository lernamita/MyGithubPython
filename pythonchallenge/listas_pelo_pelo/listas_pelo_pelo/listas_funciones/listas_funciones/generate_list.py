# -*- coding: utf-8 -*-
"""
Created on Tue May 30 23:18:05 2023

@author: Ludovico
"""
import random


def listgenerieren(große, ranges):
    """Function that generates a list of int elements without duplicate values
    """
    myset = set()  # se guardan los numeros repetidos de la lista generada
    u = []
    s = [random.randint(0, ranges) for i in range(große)]  # genera una lista aleatoria de ranges numero de elementos
    for x in s:
        if x not in myset:
            u.append(x)
            myset.add(x)
    return u


def listsortieren(liste):
    """Function that sorts a list"""
    unsortierte = []
    liste.sort()
    for i in liste:
        unsortierte.append(i)
    return unsortierte
