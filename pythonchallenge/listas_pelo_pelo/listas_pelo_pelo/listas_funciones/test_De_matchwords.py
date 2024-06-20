# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:12:25 2023

@author: Ludovico
"""




def duplicate_characters(string):
    # Create an empty dictionary
    chars = {}
    repetitions=0
    # Iterate through each character in the string
    for char in string:
        # If the character is not in the dictionary, add it
        if char not in chars:
            chars[char] = 1
        else:
            # If the character is already in the dictionary, increment the count
            chars[char] += 1
 
    # Create a list to store the duplicate characters
    duplicates = []
    # Iterate through the dictionary to find characters with count greater than 1
    for char, count in chars.items():
        if count > 1:
            repetitions += 1
            duplicates.append(char)
    
    return [duplicates, repetitions]


def remove_duplicate(liste):
    """function to remove the repeated elements of a list"""
    result = set()
    duplicate = []
    new_liste=[]
    for i in liste:
        eso = isinstance(i,str)
        if eso == True: 
            i = i.lower()
        new_liste.append(i)
        print("nada")
    for j in new_liste:
        if j not in result:
            duplicate.append(j) 
            result.add(j)
    return result

# prueba= [5, 3, 1000, 10001, 1000, 'T', 'r', 't', 2, 5, 1000]
# d= remove_duplicate(prueba)
# print (d)


def remove_duplicate2(liste):
    """ function to remove the repeated elements of a list second version"""
    result = set()
    #duplicate = []
    for i in liste:
        if isinstance(i,str)== True: 
            i = i.lower()
        if i not in result:
            #duplicate.append(i) 
            result.add(i)
    return result

prueba= [5, 3, 1000, 10001, 1000, 'T', 'r', 't', 2, 5, 1000]
prueba2= [5, 3, 1000, 'R', 'x', 'T', 'r', 't', 2, 5, 1000]
d= remove_duplicate2(prueba2)
print (d)