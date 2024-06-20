# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:37:38 2022

@author: Ludovico
"""


from collections import deque #libreria que esta especializada en container datatypes
# like queue taht are list like container with fast appends and pops on either end
class Queue:
    def __init__(self):
        self._elements = deque()
    
    def enqueue(self, element):
        """add Items to the right end of the queue.
        
        >>> numbers = Queue() #crea una instancia de la clase llamada numbers
        >>> numbers #comprueba que haya sido creada exitosamentevy que este vacia 
        Queue([])
        >>> for number in range(1, 4): #necesita un espacio despues del prompt
        ...    numbers.enqueue(number)#llena la cola con numeros 1,2,3
        >>> numbers # compruea que se creo y que esta llena
        Queue([1, 2, 3])
        """
        self._elements.append(element)#add element to the end of the queue
        
    def dequeue(self):
        """remove and return an Item from the left end of the queue.
        
        >>> numbers = Queue() #crea la instancia otra vez
        >>> for number in range(1, 4): #llena la lista
        ...     numbers.enqueue(number)
        >>> numbers
        Queue([1, 2, 3])
        
        >>> numbers.dequeue() #va sacando poco a poco los elemeenos hasta que comprobar que este vacia
        1
        >>> numbers.dequeue()
        2
        >>> numbers.dequeue()
        3
        >>> numbers
        Queue([])
        """
        return self._elements.popleft()#remove elements from the beginnn of the queue
    
    def __repr__(self):# strings representation 
        return f"{type(self).__name__}({list(self._elements)})"

if __name__== "__main__":
    import doctest
    doctest.testmod(verbose= True)
    