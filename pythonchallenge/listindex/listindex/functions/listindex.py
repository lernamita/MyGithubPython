# -*- coding: utf-8 -*-
"""
Crelista_originalted on Thu Feb 16 15:27:09 2023

@lista_originaluthor: Ludovico
"""

lista_original =[1, 1, 2, 4, 5, 6, [1, 2]]
item = 2

def depth(l):
    """function that calculate how deep a nested list is"""
    if isinstance(l, list):             #consulta si la lista es una lista
        return 1 + max(depth(item) for item in l)       # calcula el mayor de los dephts + 1
    else:
        return 0


def listindex (a,item):
    """list to present all indexs where a value appears on a list"""
    newlist =[]             #lista donde se guardan los indices finales
    for index, value in enumerate(a):       #dos itirerantes que vienen de enumerate
        if value == item:
            newlist.append([index])         # el valor del index inicial se lo agrega a la lista
        elif isinstance(a[index], list):    # si hay otra lista dendtro del elemento del indice, hace una recursion
            for i in listindex(a[index], item): # si tienes una sublista  dentro del indice que es igual que el item a buscar
                newlist.append([index]+i)       # se agrega a la lista de resultados a el indice dentro de la sublista
    return newlist

c = listindex(lista_original, 2)
print(c)