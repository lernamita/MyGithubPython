# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 07:59:40 2022

@author: Ludovico
"""
import unittest
import suchen2 as su
#import re



class TestSuchen(unittest.TestCase):
    """Funktionstest"""

    def setUp(self):
        """Initialisation"""

        self.input1= ['Kenntnis<e','Kenntnis>e','Kenntnis:e','Kenntnis?e','Kenntni*se','Kenntnis"e','Kenntnis|e','Kenntnis/e',
                    'Kenntnis\e','Kenntnisse.','Kenntnisse']
        self.input2= ['lola', 'luna']
        self.input3= [""] #para probar en testsearch si reconoce valores vacios como input
        self.input4= ['Kenntnisse', 'kenntnisse', 'Kenntnis<e', 'Kenntnisse ', ' Kenntnisse']
        self.inputpath= r"c:\users\ludovico\desktop\Bewerungen SW_Testing\Modis_AIE_Ingenieur"
            
    def testSearch(self):
        """Prueba la correcta busqueda del input"""
        for i in self.input3:
            self.obj= su.Searchdirectory(i, self.inputpath)
            if self.assertIs(len(self.obj.result),0)== True: #comprueba que el input haya sido vacio
                print("todo boun")    
            # for x in self.obj.result:
            #     if x[0]==0:
            #         TestSuchen().fail(msg="blank word not excepted, input should not be empty vacia")
    
    def testInputFilename(self):
        """Prueba la correcta busqueda del input y si coincide con la palabra Kenntnisse"""
        for i in self.input1:
            self.obj = su.Searchdirectory(i, self.inputpath)
            for x in self.obj.result:
                self.assertTrue(x[0]==2) # 2 coincidencias conocidas de la palabra kenntnisse en dicho directorio
                print ("resultado correcto:",self.obj.result[0][0])
                    
suite = unittest.TestSuite() # se crea un objeto de la clases testsuite (no es subclase de testcase)
#test = TestSuchen("testSearch")  #se crrea un objeto de la clase creada y como entrada se ponen el nombre exacto del testcase
#test =  TestSuchen("testInputFilename")
suite.addTests((TestSuchen("testSearch"), 
              TestSuchen("testInputFilename"))) #se agrega el testcase "testadd" al suite creado usando los metodos de agregacion de testsuite
testrunner = unittest.TextTestRunner(verbosity=2) #se crea un objeto de running de la clase texttestrunning con un detalle del informe del test en texto plano
testrunner.run(suite) # se corre el testsuite
