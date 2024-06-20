# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:56:28 2023

@author: Ludovico
"""


def sort_string(s):
    print('orignal string:', s)
    s = s.split()
    lista = []
    listanueva = []
    for i in range(len(s)):
        lista.append(s[i].lower()+s[i])
        lista.sort()
    for j in lista:
        listanueva.append(j[len(j)//2:])
    print("sorted string: ", listanueva)
    return ' '.join(listanueva)

c = sort_string('banana zanahoria PERA REMOLACHA')
print(c)


# simplified solution with list comprehension


# def sort_string(s):
#     print('orignal string:', s)
#     s = s.split()
#     s = [i.lower() + i for i in s]
#     s.sort()
#     s = [i[len(i)//2:] for i in s]
#     return ' '.join(s)



# c = sort_string('banana zanahoria PERA REMOLACHA')
