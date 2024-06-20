# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 19:48:25 2023

@author: Ludovico
"""


def ispalindromo():

    palabra = input("ingrese palabra: ").lower().replace(" ", "")
    counter = 0
    for i in range(len(palabra)):
        if (palabra[i] == palabra[len(palabra) - 1-i]):
            counter += 1
        else:
            print("False")
            return False
        if counter == len(palabra)//2:
            print("True")
            return True


a = ispalindromo()
