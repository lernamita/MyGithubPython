"""
Ejercicio 13.3 donde se buscan coincidencias en un archivo de texto de ciertas palabras dadas en el main en un archivo de texto y el numero de veces que se
repiten

"""

import re


class Haufigkeit:

    def __init__(self, file, list_of_words):
        self.file = file
        # self.text=[i.lower() for i in list_of_words]
        self.list_words= list_of_words
        # self.list_words=[i.lower() for i in list_of_words]# convert the list of words in lower case
        self.pattern = re.compile('[,;.:!?]+\s*') #descarta ese grupo de simolos ademas espacios y cada repeticion de esos simbolos
        self.g = []
        self.list_of_coincidence = []
        self.text = []

    def read_file(self):

        f = open(self.file, 'r')
        self.text = f.read()
        #print("este es el texto sin editar:\n {a}".format(a= self.text))
        self.text = self.text.lower()#hace minuscula al texto para poder standarizarlo
        self.text = self.pattern.sub('', self.text) #remplaza todos esos patrones especificados con un espacio en blanco
        print("este es el texto del archivo:\n{a!r} \neste es el tipo de dato:\n {b}".format(a= self.text, b= type(self.text)))
        f.close()
        return self.text

    def find_coincidence(self):

        for ele in self.list_words:
            self.g = re.findall(ele, self.text)
            if len(self.g) > 0: #lo que encuentra que tenga mas de 0 coincidencia entones sera trabajado

                self.list_of_coincidence += [(ele, len(self.g))] #armo la lista de lo encontrado basado en los elementos encontrados y sus veces encontradas
                
        print("list of coincidence: ", self.list_of_coincidence)
       
        return self.list_of_coincidence


    # def __str__(self):

    #     presentation = 'Der Text ist: \n'
    #     for t in self.text:
    #         presentation += t[0]

    #     return presentation

if __name__ == "__main__":
    words = ['sex', 'anal', 'hot', 'asian', 'price', 'won']
    data = Haufigkeit("prueba1.txt", words)  
    data.read_file()
    data.find_coincidence()



