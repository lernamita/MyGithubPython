#----------------------------------------------------
# Dateiname:  rankingtest_fortgeschritten.py 
# Fortgeschrittene Testumgebung für das Modul ranking
# 
# Python 3
# Kap. 25 
# Michael Weigend 15. 11. 2009
#----------------------------------------------------

import unittest, os, random, ranking

class TestRanking1 (unittest.TestCase):              #1 subclase de la clase testcase
  """Funktionstests"""

  def setUp(self):                                   #2 inicialozacion de la subclase
    """Erzeuge Testdaten und Ranking-Objekt """
    self.words = ["Titan", "Jupiter", "Titan",
                  "Titan", "Huygens", "Jupiter"]      
    self.r = ranking.Ranking("not_existing.txt")
    for w in self.words:
            self.r.add(w)
    self.r.save()

  def tearDown(self):
    """Lösche Testdatei """
    try:
        os.remove("not_existing.txt")                #3
    except: pass

  def testRank(self):                                #4
    """Prüfe, ob Rang richtig berechnet wird"""
    self.assertTrue (self.r.getRank("Titan") == 1)
    self.assertTrue (self.r.getRank("Jupiter") == 2)
    self.assertTrue (self.r.getRank("Huygens") == 3)

  def testSave(self):
    """ Pruefe, ob alle Woerter uebernommen wurden"""
    r = ranking.Ranking("not_existing.txt")
    for w in set(self.words): #convierte los elementos de esa lista en un set de elementos para contarlos abajo mejor
        self.assertTrue (r.voting[w]==self.words.count(w)) #cuenta si los values son iguales al conteo que hace el test

  def testGetTop(self):
    """ Wird das am häufigsten gewählte Wort erkannt?"""
    expected = "Titan 3 <br> "
    text = self.r.getTop(1)
    self.assertEqual(text, expected)

class TestRanking2 (unittest.TestCase):              #5
  """Belastungstest"""
  def setUp(self):  
    """erzeuge Zufallsliste von Wörtern"""
    f = open("willkommen.txt", "r")                  #6 texto cualquiera con muchas palabras
    text = f.read()
    f.close()
    words = text.split()                             #7 separa cada palabra de ese texto en conmas
    self.words = [random.choice(words)
                       for i in range(1000)]         #8 escoje aleatoriamente 1000 palabras solas o repetidas de ese texto y las graba en una lista llamada selfwords

  def tearDown(self):
    """Lösche Datei, die durch den Test erzeugt worden ist"""
    try: os.remove("testfile.txt")
    except: pass

  def testAdd(self):   
    """Belastungstest"""
    for w in self.words:                             #9 crea un nuevo archivo formado por esas 1000 palabras
      r = ranking.Ranking("testfile.txt")             #y prueba si los values(numero de veces de la palabra) que la funcion voting calculo coinicden con el conteo
      r.add(w)
      r.save()
    for w in set(self.words):
      self.assertTrue(r.voting[w]==self.words.count(w))

suite = unittest.TestSuite()                         #10 el testsuite en este caso contiene 4 testcases
suite.addTests((TestRanking1("testRank"),
                TestRanking1("testSave"),
                TestRanking1("testGetTop"),
                TestRanking2("testAdd")))
testrunner = unittest.TextTestRunner(verbosity=2)    #11 y umuestra los resultados en un informe de texto basico por cada testcase
testrunner.run(suite)


 
