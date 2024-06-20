# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:29:50 2024

@author: Ludovico
"""
import tkinter as tk
import search as su



class Entrydirectory(tk.Button):
    word =""
    directoryname= ""

    def __init__(self):



        # main window
        self.fenster = tk.Tk()
        self.fenster.geometry('600x600')
        self.fenster.title('Find a word')
        self.ausgabe = tk.Label(master= self.fenster, width=30, height = 2)
        self.rahmen = tk.Frame(self.fenster, relief='ridge', borderwidth=5)
        self.rahmen.pack(fill=tk.BOTH, expand=1)
        self.ausgabe.pack()
        # First label arrangement

        self.label1 = tk.Label(master = self.rahmen, text='Enter the word:')
        self.label1.config(font=("Arial", 10, "bold"))
        self.label1.pack(side =tk.TOP)


        #Button 1
        self.button1 = tk.Button(self.rahmen, text='Enter Name', command=self.eingabe_general, width=10, height=1)
        self.button1.config(font=('Arial', 10))
        self.button1.place(x= 480, y= 30)
        #Entry configuration where the inputs come
        self.entry = tk.Entry(master = self.rahmen, borderwidth= 3, width=55)
        self.entry.pack(pady=10, padx =10)
        self.entry.focus()



        self.label2 = tk.Label(master = self.rahmen, text='Enter the path:')
        self.label2.config(font=("Arial", 10, "bold"))
        self.label2.pack(side =tk.TOP)
        #Entry configuration where the inputs come

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
        # second window
        self.label5 = tk.Label(self.rahmen, text='the current result is:')
        self.label5.config(font=("Arial", 14, "bold"))
        self.label5.pack(pady=10)

        # window arrangement where the results come
        self.rahmen2 = tk.Frame(self.rahmen, relief='ridge', borderwidth=1)
        self.rahmen2.pack(pady=30, padx=30)

        # Srollbar using a list
        self.scrollbar = tk.Scrollbar(self.rahmen2)
        self.liste = tk.Listbox(self.rahmen2, yscrollcommand=self.scrollbar.set, width=50)
        self.liste.pack()

        #  scrollbar for the content
        self.scrollbar.config(command=self.liste.yview)
        self.liste.pack(side='left', fill='both')
        self.scrollbar.pack(side='left', fill='y')

        # Button OK 
        self.button4 = tk.Button(self.rahmen, text='OK', command=self.fenster.destroy, width=10, height=2)
        self.button4.config(font=('Arial', 10))
        self.button4.pack(pady=10)


        self.fenster.mainloop()



    def eingabe_general(self):

        data_in = self.entry.get()
        if not data_in:
            self.ausgabe.config(text= 'Field empty, no searching available' )


        else:
             Entrydirectory.word = data_in
             self.ausgabe.config(text= 'searching the word {b}'.format(b= data_in ))
             self.entry.delete(0, 'end')

    def eingabe_directoryname(self):
        data_in2 = self.entry2.get()
        if not data_in2:
            self.ausgabe.config(text= 'Field empty, no path available' )

        else:
            Entrydirectory.directoryname = data_in2
            self.ausgabe.config(text= 'it will be scanned {a} '.format(a=data_in2))
            self.entry2.delete(0, 'end')



    def showing(self, word, directory):

        obj2 = su.Searchdirectory(word, directory)
        self.inhalt = obj2.SUCHBERICHT.splitlines()
        for zeile in self.inhalt:
            self.liste.insert(0, zeile)
