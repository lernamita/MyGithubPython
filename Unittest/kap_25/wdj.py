# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:47:11 2022

@author: Ludovico
"""
#cgi skrip
import cgi, cgitb # cgi es la libreria de soporte para utilidades de cgi escritos en python
#es invocado por un servidor http, usualmeete para procesar inputs ingresados desde un formulario
#de html
#cgitb es un traceback de cgi para proveer exception handler para python scripts, y generar
#un reporte de excepciones no detectadas en el codigo y buscar bugs y lo puedes eliminar
#cuando ya confirmes que esta todo bien

cgitb.enable()
from ranking import *

RESPONSE = """Content-Type: text/html

<html>
<meta http-equiv="Content-Type" content="charset=utf-8" />
<head><title>Wort des Jahres</title></head>
<body>
<font face="VERDANA,ARIAL,HELVETICA">
<h2> Danke f&uuml;r Ihr Votum!</h2>
Hier sind die bisherigen Top Ten: <br>
{}
Ihr Vorschlag {} steht auf Platz {}.<br>
</font>
</body>
</html>"""

#PATH = "word_des_jahres/words.txt"
PATH = "words.txt"

class Responder:
    def __init__(self, datafile):
        form = cgi.FieldStorage()#to get at submitted form data
        self.word = form.getvalue("word")
        self.ranking = Ranking(datafile)
        self.ranking.add(self.word)
        self.ranking.save()
        
    def respond(self):
        topFive = self.ranking.getTop(5)
        rank = self.ranking.getRank(self.word)
        print(RESPONSE.format(topFive, self.word, rank))
r = Responder(PATH)
r.respond()

