# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:20:30 2023

@author: Ludovico
"""
def suma(l):
    "funtion to sum the elements of a list"
    sumatoria = 0
    for i in l:
        sumatoria += i
    return sumatoria


c = suma([2, 5, 6, 7, 1, 100])

print("suma de elementos:", c)

def suma2(l):
    """funtion to sum the elements of a list"""
    c = len(l)
    sumatoria = 0
    for i in range(1, c+1):
        sumatoria += l[c-i]
    return sumatoria
d = suma2([2,5,6,7,1,100])
print("sumatoria mi forma con index", d)


def mayor(l):
    """function to print the major number of a list"""
    mayor = l[0]
    for i in l:
        if i > mayor:
            mayor =i
    return mayor

f = mayor([1,5,8,2])
print("el numero mayor de la lista: ", f)


def mayor2(l):
    """function to print the major number of a list"""
    mayor = l[0]
    c = len(l)
    for i in range(1, c):
        if mayor > l[c-i]:
            continue
        else:
            mayor = l[c-i]
    return mayor


g = mayor2([1, 5, 201, 202, 8, 200, 2, 10, 20])
print("el numero mayor de la lista mi forma: ", g)


def duplicate_characters(string):
    """ Function that print a list of duplicated characteres and its number of
    repetitions from a string"""
    # Create an empty dictionary
    chars = {}
    repetitions = 0
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
 

def match_words1(liste):
    """ function that prints the total number of repeated characteres of a 
        list of strings"""
    result=[]
    sum_of_repetitions= 0
    for i in liste:
        a = duplicate_characters(i)
        if len(a[0])>0:
            result.append(a)
            sum_of_repetitions += a[1]
    print("the total of duplicated characteres is {a} ".format(a= sum_of_repetitions))
    return sum_of_repetitions

f= match_words1(['abc', 'aba', 'thlti','hrz', '21r12'])
# print("the total of duplicated characters:", f)


def match_words(words):
    """ funcion que imprime el numero de caracteres repetidas de un elemento 
    de lista, but function has errors is not strong"""
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr

# h= match_words(['abc', 'xyz', 'aba', '121'])
h= match_words(['abc', 'aba', 'hrz', '21r12'])
print("las letras repetidas:", h)


def remove_duplicate(liste):
    """ funcion que elimina los elementos repetidos de una lista"""
    result = set()
    #duplicate = []
    for i in liste:
        if i not in result:
            #duplicate.append(i) //store the duülicated elements
            result.add(i)
    return result

def remove_duplicate2(liste):
    """ funcion que elimina los elementos repetidos de una lista 
      e ingonar el CASE"""
    result = set()
    #duplicate = []
    for i in liste:
        if isinstance(i,str)== True: 
            i = i.lower()
        if i not in result:
            #duplicate.append(i)  //store the duülicated elements
            result.add(i)
    return result

# j = remove_duplicate([2, 4, 5, 5, 3, 4, 'r', 'r', 't'])
# print(j)


def is_greater(str, n):
    """function to print if a the length of string is greater than a
        value n """
    g = set()
    txt = str.split(" ")
    for i in txt:
        if len(i) > n:
            g.add(i)
    print("esta es la palabra mayor {a}: {b}".format(a=n, b=g))
    return g


k = is_greater("la vid esw una tombola de noche y de dia", 6)


def remove_item2(l):
    """function to delete the 1th 4th and 5th element of a list"""
    resultado = [ele for index, ele in enumerate(l) if index not in (0, 4, 5)]
    return resultado


l2 = [4, 2, 'black', 'panter', 'loco', 10, 7, 8]
c = remove_item2(l2)


def collatz_sequenz(x):
    """ Write a Python program where you take any positive integer n, if n is
    even,divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1
    to obtain 3n + 1.  Repeat the process until you reach 1"""
    collatz_liste=[x]
    if x < 1:
        return []
    while x > 1:
        if x % 2 == 0:
            x = x/2
        else:
            x = x * 3 + 1
        collatz_liste.append(x)
    return collatz_liste


z= collatz_sequenz(6)



def listadelista(l):
    """funtion to find the major summ of elements of a list"""
    suma=0
    res=[]
    for ele in l:
        for j in ele:
            suma += j
        res.append(suma)
        suma=0
        mas= res[0]
        for i in range(len(res)-1):
            if res[i] > mas:
                mas = res[i]
    return mas
m= listadelista([[1,2,3],[4,50,8],[20,11,10]])
print("la suma mayor", m)


def deep(l):
    """Function to go through a nested list and print elements in only one 
        list"""
    res=[]
    def loop(x):
        for i in range(0,len(x)):
            if type(x[i])== list:
                loop(x[i])
            else:
                res.append(x[i])
    loop(l)
    return res

n= deep([1,2,[3,4],5,[8,9]])
print("la lista sin nesteaded:", n)



def concatenado(l,n):
    """function to concatenate a list of characteres n times"""
    newlist=[]
    for i in range(1,n+1):
        for ele in l:
            newlist.append(ele+str(i))
    return newlist
a= concatenado(['p','q','r'], 3)
print(a)


def concatenado2(l,n):
    """function to concatenate a list of characteres n times with 
        list comprehnsion"""
    return [ele+str(i) for ele in l for i in range(1,n+1)]

b= concatenado2(['p','q','r'], 2)
print("resultado con list comprehension",b)


def interseccion(l):
    """function to find common elements on different lists"""
    compara=set(l[0])
    for i in l[1:]:
        compara &= set(i)
    return list(compara)

c= interseccion([[1,2,3,4],[7,8,2,3],[9,20,2,1,3]])
print("the common elements",c)


def interseccion2(lst):
    """function to find common elements on different lists, shorter version"""
    temp = set(lst[0]).intersection(*lst)
    return list(temp) 




def rotatelist(list, index, direction ):
    """Function to rotate a list according to the selected index and direction"""
    a=[]
    for i, j in enumerate(range(len(list)-1)):
        if (i==int(index) and direction==('left')):
            a=list[j:]
            a.extend(list[:j])
        elif (i==int(index) and direction ==('right')):
            a = list[len(list)-j:]
            a.extend(list[:len(list)-j])
    return a


def removechars(list, chars):
    """Function to find special characters in words and delete it in case the 
        characters are predefined on another list"""
    new_list=[]
    new_words=""
    for i in chars:
        for x in list:
            for y in x:
                if i in y:
                    new_words=x.replace(y,"")
                    new_list.append(new_words)
    return new_list


def removechars2(list, chars):
    """Function to find special characters in words and delete it in case the 
        characters are predefined on another list with list comprehnesion"""
    new_list = []
    for line in list:
        new_words = ''.join([x for x in line if not any([i in x for i in chars])]) # recorre el string de una lista caracter por caracter y lo hace hasta que ya no encuentre un caracter especial en la lista
        new_list.append(new_words)
    print("palabras con caracteres removidos list comprehnsion: ", new_list)
    return new_list