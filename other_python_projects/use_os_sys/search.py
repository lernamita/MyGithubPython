# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:30:10 2024

@author: Ludovico
"""
from os import walk
from os.path import join, normcase 


class Searchdirectory():
    
    def __init__(self, suchwort, root):
        
        self.word= suchwort
        self.directoryname= root
        self.SUCHBERICHT =""
        self.result = []
        self.nicht_lesbar= 0
        self.durchsucht= 0
        self.inhalt = ""
        self.liste= walk(root) ##walk from os module, to generate a list with 3 values, root directory, hierarchical and files
        
        
        for (path, directories, data) in self.liste:
            for d in data:
                self.durchsucht += 1
                try:
                    
                    f = open(join(path, d), 'r') 
                    text = f.read() #read files are saved as strings, however, only text files can be read, not binary files, so a try is used.
                    f.close()
                    n = text.count(self.word) 
                    if n > 0:
                        p = normcase(join(path, d))# normcase path normalization
                        self.result += [(n,p)]#fill the list result with count and directory where it was found

                except: 
                    
                    self.nicht_lesbar += 1
                    
        self.result.sort(reverse= True)


        for (n, path) in self.result:
            self.SUCHBERICHT += '{} \n ({} Coincidences) the word to search was : {} \n Results \n ------------ \n It were {} Files scanned \n {} not readable \n'.format(
            path, n, self.word, self.durchsucht, self.nicht_lesbar )
        print("this is the report \n",self.SUCHBERICHT)

