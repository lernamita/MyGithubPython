#! /usr/bin/env python3                              #1

#----------------------------------------------------
# Dateiname:  rankingtest.py 
# Einfache Testumgebung für das Modul ranking
# 
# Python 3
# Kap. 25 
# Michael Weigend 29.1.2013
#----------------------------------------------------
import unittest, ranking  #se importa el modulo de unittest y el programa que se va a testear
class TestRanking (unittest.TestCase):   #se crea una subclase de la clase madre testcase, por cada test case con su funcion
  def setUp(self):
    """Erzeuge Liste von Woertern und Ranking-Objekt"""
    self.words = ["Jupiter", "Titan", "Jupiter", "Jupiter"]
    self.r = ranking.Ranking("not_existing.txt") # se crea el objeto de la clase ranking donde se guardan los diccionarios
        
  def testAdd(self): #es un metodo de la subclase, pero pueden haber mas de un metodo
    """se agrega x numero de palabras al diccionario y se verifica si el conteo es correcto"""
    for w in self.words: # se agregan esas palabras al diccionario r
        self.r.add(w)  
    for word in self.r.voting.keys():   #se contea el numero de votaciones de cada palabra y se evalua si coincide
        n_voting = self.r.voting[word]  #que el numero de votaciones con el numero de veces que aparece
        n_words = self.words.count(word)
        self.assertTrue(n_voting == n_words) # se hace la condicion assert para diccionarios si son el mismo numero
             
suite = unittest.TestSuite() # se crea un objeto de la clases testsuite (no es subclase de testcase)
test = TestRanking("testAdd")  #se crrea un objeto de la clase creada y como entrada se ponen el nombre del testcase
suite.addTest(test) #se agrega el testcase "testadd" al suite creado usando los metodos de agregacion de testsuite
testrunner = unittest.TextTestRunner(verbosity=2) #se crea un objeto de running de la clase texttestrunning con un detalle del informe del test en texto plano
testrunner.run(suite) # se corre el testsuite
