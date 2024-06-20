# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 19:10:01 2022

@author: Ludovico
"""
"""
Modul mit der Klasse Ranking


>>> r = Ranking("not_existing.txt")
>>> r.add("Titan")
>>> r.add("Titan")
>>> r.add("Titan")
>>> r.add("Einstein")
>>> r.add("Methan")
>>> r.add("Einstein")
>>> r.getRank("Titan")
1
>>> r.getRank("Methan")
3
>>> r.getTop(0)
''

>>>
>>> r.getTop(2) #doctest: +NORMALIZE_WHITESPACE
'Titan 3 <br>'
>>>
>>> r.getTop(1000) #doctest:+ELLIPSIS, +NORMALIZE_WHITESPACE
'Titan 3
...'
>>> d = {'Einstein' : 2, /
         'Methan' : 1,   /
         'Titan': 3}
>>> r.voting == d
True
"""
import pickle # modulo to implement binary protocols for serializing a Python object structure
#a byte stream is coverterd into a Python object and viceversa
class Ranking:
    def __init__(self, filename):
        self.filename = filename
        try:
            f = open(filename, "rb")#reading binary 
            self.voting = pickle.load(f)#lee la representacion pickl del objeto desde un archivo f
            f.close()
        except:
             self.voting = {}
             
    def add (self, word):
        if word in self.voting.keys():
            self.voting[word] += 1
        else: self.voting[word] = 1
    
    def getTop(self, n):
        items = [(self.voting[word], word)
                 for word in self.voting.keys()] #list comprehension
        items.sort(reverse = True)
        top = items[:n]
        response = ""
        for (votes, word) in top:
            response += "{} {} <br>".format(word, votes)
        return response
    
    def getRank(self, word):
        
        votes = self.voting[word]
        vote_list = [self.voting.values()]
        vote_list.sort(reverse = True)
        print(type(vote_list))
        return vote_list.index(votes)+1
    
    def save(self):
        f = open (self.filename, "wb")
        pickle.dump(self.voting, f) #escribe la representacion de pickled al archivo f
        f.close()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
          
            
            
            
            
            
            
            
            
            
            
            
            