# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:22:05 2023

@author: Ludovico
"""
import funciones_listas as fn
import generate_list as gen
import constants as c
import unittest


class TestFunctions(unittest.TestCase):
    """Funktiontest"""

    def setUp(self):
        """Initialisation"""
        self.liste = gen.listgenerieren(c.GROSSE, c.RANGES)
        self.sorted = gen.listsortieren(self.liste)
        self.listtosum = [2, 5, 6, 7, 1, 100, -2, -100, -5, 0]
        self.match_words = ['abc', 'xyz', 'aba', '1221']
        self.match_words2 = ['fjz', '1m0', 'ltr', 'zga', 'hxv']
        self.match_words3 = ['12', '1231', '125', '24']
        self.match_words4 = ['rfrjz', '1m0', 'ltr', 'zga', 'hxv']
        self.duplicatelist = [5, 3, 1000, 10001, 1000, 't', 'r', 't', 'T', 2, 5, 1000]

    def rightsum(self):
        """Test the correct sum of the elements"""
        expected_result = 14
        obtained_result = fn.suma(self.listtosum)
        print("obtained result {a}".format(a=obtained_result))
        self.assertEqual(expected_result, obtained_result)

    def rightmayor(self):
        """Test the correct major number"""
        expected_result = 100
        obtained_result = fn.mayor(self.listtosum)
        print("the major number {a}".format(a=obtained_result))
        self.assertEqual(expected_result, obtained_result)

    def right_number_macht_words(self):
        """Test the right number of repeated characters"""
        expected_result1 = 3
        obtained_result1 = fn.match_words1(self.match_words)
        print("the number of repetaed characters on first list was {a}".format(a=obtained_result1))
        self.assertEqual(expected_result1, obtained_result1)
        expected_result2 = 0
        obtained_result2 = fn.match_words1(self.match_words2)
        print("the number of repetaed characters on second list was: {a}".format(a=obtained_result2))
        self.assertEqual(expected_result2, obtained_result2)
        expected_result3 = 1
        obtained_result3 = fn.match_words1(self.match_words3)
        print("the number of repetaed characters on the third list was {a}".format(a=obtained_result3))
        self.assertEqual(expected_result3, obtained_result3)
        expected_result4 = 1
        obtained_result4 = fn.match_words1(self.match_words3)
        print("the number of repetaed characters on the fourth list was {a}".format(a=obtained_result4))
        self.assertEqual(expected_result4, obtained_result4)
    
    def right_remove_duplicate(self):
        """Test the fuction that remove duplicate elements on a list"""
        result_remove_duplicate = fn.remove_duplicate2(self.duplicatelist)
        expected_result = [5, 3, 1000, 10001, 't', 'r', 2]
        for i in expected_result:
            self.assertFalse(i not in fn.remove_duplicate2(self.duplicatelist), msg= "fnction to remove duplicated failed")
        print("list without duplicate elements {a} \nthe original list was: {b}". format( a= fn.remove_duplicate2(self.duplicatelist), b= self.duplicatelist))

        
    # def listfirstvalue(self):
    #     """Test the correctnes of first value of the sorted list"""
    #     a = self.sorted
    #     print("generated list: \n",a)
    #     print("first Value was: \n",a[0])
    #     print("min Value was: \n", min(a))
    #     self.assertEqual(a[0], min(a))

    # def listiscrecient(self):
    #     """test the crecient values of the list"""
    #     a = self.sorted
    #     for i in range(1, len(a)):
    #         self.assertFalse(a[i-1] > a[i], msg= 'List is not right crecient sorted')


# suite = unittest.TestSuite()
# test= TestFunctions("rightsum")
# suite.addTest(test)
# testrunner = unittest.TextTestRunner(verbosity=2)
# testrunner.run(suite)
                
suite = unittest.TestSuite()
suite.addTests((TestFunctions("rightsum"), 
              TestFunctions("rightmayor"),
              TestFunctions("right_number_macht_words"),
              TestFunctions("right_remove_duplicate")))
              #TestSort("listiscrecient")))
testrunner = unittest.TextTestRunner(verbosity=2) #se crea un objeto de running de la clase texttestrunning con un detalle del informe del test en texto plano
testrunner.run(suite)