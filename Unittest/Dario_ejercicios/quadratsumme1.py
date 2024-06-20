# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

def quadratsumme (s):
    """summe der Quadrate der Elemente einer Zahlenliste
    >>> quadratsumme ([1, 2, 3]) # 1+4+9
    13
    >>> quadratsumme ([10,10,10,]) # 100+100+100
    300
    >>> quadratsumme ([])
    0
    >>> quadratsumme ()
    0
    """
    summe = 0
    for n in s:
        summe = summe + n**2
    return summe

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) #muestra un informe completo de lo que prueba y resultado
    #este metodo permite llamar a la funcion y correrlo como en el python shell con el y entrega >>> tres
    #tres resultado, el primero es lo que debe correr la funcion, el resultado esperado"
    #doctest.testmod() # muestra algo solo si hay errores en un informe sencillo
    #doctest muestra errores 