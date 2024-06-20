# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 00:21:31 2022

@author: Ludovico
"""
def greetings(name= "World"):
    """ Diese Funktion Prints a greeting to the screen.
    
    Beispile:
    >>> greetings("Pythonist")#considerar espacios deben coincidir
    Hello, Pythonist!
    >>> greetings("dariyankee")
    Hello, dariyankee!
    >>> greetings()
    Hello, World!
    """
    print(f"Hello, {name}!")
    
    
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)