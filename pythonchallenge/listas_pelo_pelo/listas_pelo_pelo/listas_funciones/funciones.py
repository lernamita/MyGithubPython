# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:26:53 2023

@author: Ludovico
"""


def suma(l):
    "sum elements of a list"
    
    sumatoria=0
    for i in l:
        sumatoria += i
    return sumatoria

c = suma([2,5,6,7,1,100])
print("suma de elementos:", c)

def suma2(l):
    "sum elements od a list second version"
    c = len(l)
    sumatoria=0
    for i in range(1, c+1):
        sumatoria += l[c-i]
    return sumatoria
d = suma2([2,5,6,7,1,100])
print("sumatoria mi forma con index", d)

def mayor(l):
    "print the highst value of a list"
    mayor = l[0]
    for i in l:
        if i > mayor:
            mayor =i
    return mayor

f = mayor([1,5,8,2])
print("the highest number of the list is: ", f)

def mayor2(l):
    "function to print the highst number of a list"
    mayor = l[0]
    c = len(l)
    for i in range(1,c):
        if mayor > l[c-i]:
            continue
        else:
            mayor = l[c-i]
    return mayor

g = mayor2([1,5,201,202,8,200,2,10,20]) 
print("the highst number of the list second version: ", g)

def match_words(words):
    """ function that prints the count of repeated words"""
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr

h= match_words(['abc',  'xyz', 'aba', '1221'])
print("the repeated letters are:", h)    

def remove_duplicate(liste):
    """ function to remove the repeated elements of a list"""
    result= set()
    duplicate=[]
    for i in liste:
        if i not in result:
            duplicate.append(i)
            result.add(i)
    return result
    
j= remove_duplicate([2,4,5,5,3,4,'r', 'r', 't'])
print(j)

def is_greater(str,n):
    """function to print if a the length of string is greater than a value n """
    g= set()
    txt= str.split(" ")
    for i in txt:
        if len(i)>n:
            g.add(i)
    print("this ist the longest word {a}: {b}".format(a=n, b=g))     
    return g
k= is_greater("la vid esw una tombola de noche y de dia", 6)



def remove_item2(l):
    """function to deleted the item 0, 4 and 5 of a list"""
    resultado=[ele for index,ele in enumerate(l) if index not in (0,4,5) ]
    return resultado
l2= [4,2,'black', 'panter', 'loco',10,7, 8]
c= remove_item2(l2)
    
def collatz_sequenz(x):
    """ Write a Python program where you take any positive integer n, if n is
    even,divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1
    to obtain 3n + 1.  Repeat the process until you reach 1"""
    collatz_liste=[x]
    if x < 1:
        return []
    while x > 1:
        if x%2==0:
            x= x/2
        else:
            x = x * 3 + 1
        collatz_liste.append(x)
    return collatz_liste

z= collatz_sequenz(6)

def listadelista(l):
    """function to search the highst sum of the elements"""
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
print("the highst sum is: ", m)

def deep(l):
    """function of a nested list and print the elements in one list
    """
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
    """function to concatenate a list of chars n times"""
    newlist=[]
    for i in range(1,n+1):
        for ele in l:
            newlist.append(ele+str(i))
    return newlist
a= concatenado(['p','q','r'], 3)
print(a)

def concatenado2(l,n):
    """function to concatenate a list of chars n times with list comprehnsion"""
    return [ele+str(i) for ele in l for i in range(1,n+1)]

b= concatenado2(['p','q','r'], 2)
print("result with list comprehension",b)

def interseccion(l):
    """function to find common elements in a list"""
    compara=set(l[0])
    for i in l[1:]:
        compara &= set(i)
    return list(compara)

c= interseccion([[1,2,3,4],[7,8,2,3],[9,20,2,1,3]])
print("the common elements are: ",c)

def interseccion2(lst):
    """function to find common elements in a list short version"""
    temp = set(lst[0]).intersection(*lst)
    return list(temp) 
f= interseccion2([[1,2,3,4],[7,8,2,3],[9,20,2,1,3]])
print("the common elements are",f)

def rotatelist(list, index, direction ):
    """function to rotated a list by its direction and index defined"""
    a=[]
    for i, j in enumerate(range(len(list)-1)):
        if (i==int(index) and direction==('left')):
            a=list[j:]
            a.extend(list[:j])
        elif (i==int(index) and direction ==('right')):
            a = list[len(list)-j:]
            a.extend(list[:len(list)-j])
    return a


    
    
    
    
    