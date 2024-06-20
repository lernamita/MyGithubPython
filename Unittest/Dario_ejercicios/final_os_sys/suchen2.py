# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:38:05 2022

@author: MALIN
"""

from os import walk
from os.path import join, normcase 


class Searchdirectory():
    
    def __init__(self, suchwort, root):
        """Clase que gestiona los procesos de busqueda y el informe de resultado de la busqueda
        >>> busqueda= Searchdirectory("conjunto","D:\Machinelearning_Alfa\Projektarbeit")# doctest: +ELLIPSIS
        d:\machinelearning_alfa\projektarbeit\projekt_alberto_marcos_diana_final\projektarbeit_diana_dario_marcos.ipynb
         (1 Vorkommen) das Suchwort war : conjunto 
         Suchbericht 
         ------------ 
         Es wurden 36 Datein durchsucht 
         27 nicht les...
        """
        self.word= suchwort
        self.directoryname= root
        self.SUCHBERICHT =""
        self.result = []
        self.nicht_lesbar= 0
        self.durchsucht= 0
        self.inhalt = ""
        self.liste= walk(root) #forma parte del modulo os y genera una lista con tres valores, el directorio raiz, los directorios de abajo que busco y los archivos
        
        
        for (path, directories, data) in self.liste:#self liste guarda todo lo recorrido por walk currentpath, directoris y archivos
            for d in data:
                self.durchsucht += 1
                try:
                    
                    f = open(join(path, d), 'r') #archivos se abrirar en modo de lectura y join permite presentar el directorio correctamente
                    #text = f.read() #los archivos leidos se guardan como string sin embargo solo podran leerle los que son textos y no binarios, por eso se hace un try
                    text = f.read().split()
                    f.close()                  
                    n = text.count(self.word) #cuantas veces se encontro la palabra en el archivo
                    if n > 0:
                        p = normcase(join(path, d))# normcase es metodo de os que normaliza un nombre de directorio en una forma general standar 
                        self.result += [(n,p)]#se llena en la lista result un par de datos formado por las veces que aparece y el directoriodonde esta
                        # print ("hola dario, esto es selfresult:",self.result)
                        # print ("hola dario, esto es solo n:",self.result[0][0])
                    else:
                        #print ("hola dario, esto es selfresult:",self.result)
                        self.SUCHBERICHT= None
                        print("\n\nNo coincidences with word: {a!r} found, no SUCHBERICHT reached".format(a=self.word))#formateo de r! es corchete, a! es assci
                except: 
                    
                    self.nicht_lesbar += 1
                    
        self.result.sort(reverse= True)
        #print ("hola dario1, no hay resultados",self.result)

        for (n, path) in self.result:
            self.SUCHBERICHT += '{} \n ({} Vorkommen) das Suchwort war : {} \n Suchbericht \n ------------ \n Es wurden {} Datein durchsucht \n {} nicht lesbar \n'.format(
            path, n, self.word, self.durchsucht, self.nicht_lesbar )
  
        #print("esto es el reporte \n",self.SUCHBERICHT)
        #print("lo que se busca",suchwort, root)
        print(self.SUCHBERICHT)

#obj1= Searchdirectory("", r"C:\Users\Ludovico\Desktop\Bewerungen SW_Testing\Modis_AIE_Ingenieur")

#------------doctest para probar la salida de texto 
# if __name__== "__main__":
#     import doctest
#     doctest.testmod(verbose= True, optionflags= doctest.NORMALIZE_WHITESPACE)

