# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 10:20:37 2023

@author: Ludovico
"""
# import os
import unittest
import Kap13_auf3_coincidencia_re as kap


class TestCoincidencia(unittest.TestCase):
    """Funktiontest für Kap13_auf3"""

    def setUp(self):
        """Initialisation"""
        self.testfile = "testfile.txt"
        self.testread = []
        self.testlistofwords = ['revision', 'carajo', 'vales', 'osadia']
        # self.testlistofwords2 = ["Revision", "caRajo", "vales ", " osadia"]
        self.a = kap.Haufigkeit(self.testfile, self.testlistofwords)

    def testreadfile(self):
        """test the function readfile for opening and editing text to lowercase"""
        self.testread = self.a.read_file()
        self.assertTrue(self.testread.islower())

    def testfindcoincidencia(self):
        """Test the funcion findcoincidence to see if all the coincidence where detected"""
        self.testlistcoincidence = []
        self.testread = self.a.read_file()
        self.testlistcoincidence = self.a.find_coincidence()
        for i, j in self.testlistcoincidence:
            self.assertEqual(j, 2)


suite = unittest.TestSuite()  # se crea un objeto de la clases testsuite (no es subclase de testcase)
# test = TestCoincidencia("testreadfile")  #se crrea un objeto de la clase creada y como entrada se ponen el nombre del testcase
# suite.addTest(test) #se agrega el testcase "testadd" al suite creado usando los metodos de agregacion de testsuite
# test = TestCoincidencia("testfindcoincidencia")  #se crrea un objeto de la clase creada y como entrada se ponen el nombre del testcase
# suite.addTest(test)
suite.addTests((TestCoincidencia("testreadfile"),
                TestCoincidencia("testfindcoincidencia")))  # se agrega el testcase "testadd" al suite creado usando los metodos de agregacion de testsuite
testrunner = unittest.TextTestRunner(verbosity=2)  # se crea un objeto de running de la clase texttestrunning con un detalle del informe del test en texto plano
testrunner.run(suite)  # se corre el testsuite
