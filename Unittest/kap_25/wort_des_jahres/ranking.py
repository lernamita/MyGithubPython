#----------------------------------------------------
# Dateiname:  ranking.py 
# Modul mit Klasse Ranking für Wahl des "Wortes des Jahres"
# Demonstration der Funktion doctest.testmod()
# 
# Python 3
# Kap. 25
# Michael Weigend 29.1.2013
#----------------------------------------------------

"""
Modul mit der Klasse Ranking


>>> r = Ranking("not_existing.txt")                   #A prueba de la clase ranking y se crea un archivo donde se agregan esas palabras
>>> r.add("Titan")
>>> r.add("Titan")
>>> r.add("Titan")
>>> r.add("Einstein")
>>> r.add("Methan")
>>> r.add("Einstein")
>>> r.getRank("Titan")                                #B prueba de la funcion getRank
1
>>> r.getRank("Methan")
3
>>> r.getTop(0)                                       #C prueba el metodo Top que devuelve un texto formateado html
''
>>>                                                   #D or lo tanto se normaliza con espacios cualquier suciedad de textp
>>> r.getTop(2) #doctest: +NORMALIZE_WHITESPACE
'Titan 3 <br>
Einstein 2 <br> '
>>>                                                            #E # se usan elipses cuando hay muchos datos para que salgan "...."
>>> r.getTop(1000) #doctest:+ELLIPSIS, +NORMALIZE_WHITESPACE  
'Titan 3
...'
>>> d = {'Einstein': 2, \
         'Methan': 1,   \
         'Titan': 3}                                  #F forma de probar diccionarios con el archivo previo creado nonexisting.txt con igualdad para comparar contenido de diccs
>>> r.voting == d  
True
"""

import pickle 
class Ranking:                                        #1
  def __init__ (self, filename):
    self.filename = filename
    try:                                              #2
        f = open(filename, "rb")
        self.voting = pickle.load(f)
        f.close()
    except: self.voting = {}

  def add (self, word):                               #3 se agrega los keys (words) del archivo abierto en caso de existir y si la palbra ya existe se agrega una unidad
      if word in self.voting.keys():
          self.voting[word] += 1                    # voting es el diccionario y word es la word o key de ese diccionario, y me devuelve su value sumado 1
      else: self.voting[word] = 1

  def getTop(self, n):
      items = [(self.voting[word], word)              #4
               for word in self.voting.keys()]
      items.sort(reverse = True)                      #5
      top = items[:n]                                 #6
      response = ""                                   #7
      for (votes, word) in top:
          response += "{} {} <br> ".format(word, votes)
      return response

  def getRank (self, word):                           #8
      votes = self.voting[word]                       
      vote_list = list(self.voting.values())          #9 se crea una lista de los values del diccionario que son de hecho los rankings
      vote_list.sort(reverse = True)
      return vote_list.index(votes)+1                #10 list index retorna la posicion de la palabra en la lista, el +1 es una adaptacion del index pues empizea en 0

  def save (self): #guarda la representacion serial del archivo f en forma de pickl
      f = open (self.filename, "wb")# abre el archivo en formato binary con derecho a escriutra
      pickle.dump(self.voting, f) #guarda el archivo de forma de pickl serializado o codificado en secuencia de bytes para ser almacenado con compatibilidad universal
      f.close()

if __name__ == "__main__":                           #11
    import doctest
    doctest.testmod(verbose=True)


    

