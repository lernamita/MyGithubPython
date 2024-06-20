# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:32:43 2022

@author: MALIN
"""

import tkinter as tk
import suchen2 as su
#import re

class Entrydirectory(tk.Button):
    word =""
    directoryname= ""                    
    count=0 # contador para controlar las veces que se ingresa mal el input
 
    def __init__(self):
        

        # Rahmen Gestaltung la principal
        self.fenster = tk.Tk()
        self.fenster.geometry('600x600')
        self.fenster.title('Suchwort anzeigen')
        self.ausgabe = tk.Label(master= self.fenster, width=30, height = 2)
        self.rahmen = tk.Frame(self.fenster, relief='ridge', borderwidth=5)
        self.rahmen.pack(fill=tk.BOTH, expand=1)
        self.ausgabe.pack()
        #self.pattern = re.compile('^[a-z]:\\(?:[^\\/:*?"<>"]')
        # erte Label Gestaltung o palabra
        
        self.label1 = tk.Label(master = self.rahmen, text='Suchwort eingeben:')
        self.label1.config(font=("Arial", 10, "bold"))
        self.label1.pack(side =tk.TOP)
        
        
        #Button 1 
        self.button1 = tk.Button(self.rahmen, text='Enter Name', command=self.eingabe_general, width=10, height=1)
        self.button1.config(font=('Arial', 10))
        self.button1.place(x= 480, y= 30)
        #Entry Gestaltung donde va a escribirse
        self.entry = tk.Entry(master = self.rahmen, borderwidth= 3, width=55)
        self.entry.pack(pady=10, padx =10)
        self.entry.focus()
        

        
        self.label2 = tk.Label(master = self.rahmen, text='Pfad eingeben:')
        self.label2.config(font=("Arial", 10, "bold"))
        self.label2.pack(side =tk.TOP)
        #Entry Gestaltung donde va a escribirse
        
        self.button2 = tk.Button(self.rahmen, text='Enter Path', command=self.eingabe_directoryname, width=10, height=1)
        self.button2.config(font=('Arial', 10))
        self.button2.place(x= 480, y= 95)
        
        
        self.button3 = tk.Button(self.rahmen, text='Search', command= lambda: self.showing( Entrydirectory.word, Entrydirectory.directoryname), width=10, height=1)
        self.button3.config(font=('Arial', 10))
        self.button3.place(x= 480, y= 140)
        
        self.entry2 = tk.Entry(self.rahmen, borderwidth= 3, width=55)
        self.entry2.pack(pady=10, padx =10)
        self.entry2.focus()
#        
        # zweite Label Gestaltung
        self.label5 = tk.Label(self.rahmen, text='Das aktuelle Ergebnis ist:')
        self.label5.config(font=("Arial", 14, "bold"))
        self.label5.pack(pady=10)
        
        # Rahmen Gestaltung la mas pequena donde esta el resultado
        self.rahmen2 = tk.Frame(self.rahmen, relief='ridge', borderwidth=1)
        self.rahmen2.pack(pady=30, padx=30)
        
        # Srollbar Gestaltung mittels einer Liste
        self.scrollbar = tk.Scrollbar(self.rahmen2)
        self.liste = tk.Listbox(self.rahmen2, yscrollcommand=self.scrollbar.set, width=50)
        self.liste.pack()
 
#  este es el scroll de la parte donde viene el contenido      
        
        self.scrollbar.config(command=self.liste.yview)
        self.liste.pack(side='left', fill='both')
        self.scrollbar.pack(side='left', fill='y')

        # Button OK Gestaltung
        self.button4 = tk.Button(self.rahmen, text='Exit', command=self.fenster.destroy, width=10, height=2)
        self.button4.config(font=('Arial', 10))
        self.button4.pack(pady=10)
        

        self.fenster.mainloop()
    
         
#####funciona perfectamente 
    # def eingabe_general(self):
    #     data_in = self.entry.get()
    #     if not data_in:
    #         self.ausgabe.config(text= 'Feld leer, es wird nicht gesucht' )
    #         self.count +=1
    #         if self.count == 3:
    #             self.ausgabe.config(text= 'too many tries' )
    #             self.fenster.destroy()    
    
    #     else:
    #         Entrydirectory.word = data_in
    #         self.ausgabe.config(text= 'das Wort {b} wird gesucht'.format(b= data_in ))
    #         self.entry.delete(0, 'end')
                
             
        
#segunda oopcion funciona tambien pero usando Error Handling
    def eingabe_general(self):
        """
        function que gestiona desde pantalla el ingreso de la palabra a buscar 
        """
        try:
            data_in = self.entry.get()
            if not data_in:
                self.count +=1
                raise ValueError("Volue should not be empty, please insert a name \n")
            else:
                #he desactivado la revision de pattern porque no lo entiendo y no funciona el programa si lo activo, hay que revisarlo despues.
                #data_in = self.pattern.sub('', data_in) # comando que substrae cualquier caracter especial en el texto ingresado y lo reemplaza con un espacio vacio
                Entrydirectory.word =data_in
                self.ausgabe.config(text= 'das Wort {b!r} wird gesucht'.format(b= data_in ))
                self.entry.delete(0, 'end')    
        except (ValueError) as f:
            print (f)

        finally:
            if self.count == 3:
                print("time out to many tries \n")
                self.fenster.destroy()

    def eingabe_directoryname(self):
        """
        function que gestiona desde pantalla el ingreso del directorio 
        """
        data_in2 = self.entry2.get()
        if not data_in2:
            self.ausgabe.config(text= 'Feld leer, keine Directory gefunden' )
            self.count +=1
            if self.count == 3:
                self.ausgabe.config(text= 'too many tries' )
                self.fenster.destroy()  
        else:
            Entrydirectory.directoryname = data_in2
            self.ausgabe.config(text= 'es wird in {a} gesucht'.format(a=data_in2))
            self.entry2.delete(0, 'end')
        
    def showing(self, word, directory):
        """
        function que gestiona la busqueda dela palabra en los contenidos de los archivos el directorio 
        """
        #print("esta es la parole piteada", word)
        obj2 = su.Searchdirectory(word, directory) #crea una instancia de la clase Searchdirectory
        #self.resultadodebusqueda = obj2.SUCHBERICHT
        #self.inhalt = self.resultadodebusqueda.splitlines()
        self.inhalt = obj2.SUCHBERICHT.splitlines() #toma el reporte y lo guarda en una nueva variables inhalt
        #print("esto es inhalt \n", self.inhalt)
        for zeile in self.inhalt: # voy poniendo el contenido de ese inhalt en mi listbox del tk 
            #self.liste.insert(tk.END, zeile)
            self.liste.insert(0, zeile)

#obj1 = su.Searchdirectory.SUCHBERICHT
#obj1 = Entrydirectory()
