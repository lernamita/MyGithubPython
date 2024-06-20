# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:02:06 2022

@author: Ludovico
"""
def divide(a,b):
    """
    funcion que ejecuta divisiones:

    >>> divide(84, 2)
    42.0
    >>> divide(15, 3)
    5.0
    >>> divide(42, -2)
    -21.0
    >>> divide(8, 0)  #este test deberia devolver un error, por lo tanto se pone el header comun de los exception traceback y la excepcion como tal con puntitos tambien 
    Traceback (most recent call last):
    ZeroD...
    """
    return float (a/b)



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags= doctest.ELLIPSIS)#se activa elipsis y se pone la primera linea del header y abajo una parte no mas con ...
    