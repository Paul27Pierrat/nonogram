# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:15:58 2023

@author: Paul_
"""

"""Etude des nonograms"""


import numpy as np
import random as rd

#Tableau 1D
a = np.array([1, 2, 3, 4])
#Premier élément de a:
a[0]
#dernier élément de a:
a[-1]

#Tableau 2D
b = np.array([[1, 2, 3], [4, 5, 6]])

#b a deux lignes. 
#première ligne de b:
b[0]
#dernière
b[-1]
#
#première ligne première colonne:
b[0,0]

#Affiche les éléments de la liste a
for i in a:
    print(i)
    
    
#Affiche b ligne par ligne:
for i in b:
    print(i)
    
#fonction transposee (change les lignes en colonnes d'un tableau array)
c=np.transpose(b)
c

'''Remarque: les objets créés ci-dessus sont des objets de type numpy.darray'''
type(a)
type(b)

#Exemple carré logimage 3*3 rempli de la manière suivante
#1,0,1
#1,0,0
#0,1,1

#L'écrire de la façon suivante:
carre3=np.array([[1,0,1],[1,0,0],[0,1,1]])
#La traduction souhaitée est un ensemble de 6 listes: 3 listes pour chaque ligne et 3 pour chaque colonne.
#On peut l'écrire sous la forme d'une liste de lignes et d'une liste de colonnes:

solcarre3=[[[1,1],[1],[2]],[[2],[1],[1,1]]]
solcarre3[0]#la listes des lignes
solcarre3[0][0]#l'écriture de la première ligne
'''Remarque: on ne peut pas utiliser numpy pour cette solution car le tableau n'est pas homogène:'''

#solcarre3=np.array([[[1,1],[1],[2]],[[2],[1],[1,1]]])#erreur


#fonction auxiliaire qui retourne le pattern d'une ligne:
#Entrée: une ligne d'un logimage liste
#sortie: une liste de bloc de cette ligne
def pattern(ligne):
    res=[]
    l=len(ligne)
    aux=0#longueur du bloc
    ok=False#il y a un 1 sur la case d'avant
    for i in range (l):
        if ligne[i]==0 and ok==True:
            res.append(aux)
            aux=0
            ok=False
        if ligne[i]==1:
            aux+=1
            ok=True
    if aux!=0:
        res.append(aux)#On ajoute le dernier bloc
    return(res)

pattern([1,0,1])#return [1,1]
pattern([0,1,1])#return [2]
pattern(carre3[0])#return [1,1]


#Description: retourne les instructions des lignes et des colonnes à partir du logimage
#Entrée: le logimage: matrice au format numpy
#sortie: Les instructions de chaque lignes et de chaque colonne
def solution(logimage):
    #recherche de la dimension du logimage (nombre de lignes et nombre de colonnes)
    (nbligne,nbcolonne)=np.shape(logimage)
    Tlogimage=np.transpose(logimage)
    listeligne=[]
    listecolonne=[]
    for i in range (nbligne):
        listeligne.append(pattern(logimage[i]))
    for j in range (nbcolonne):
        listecolonne.append(pattern(Tlogimage[j]))#on utilise la transposé
    solcarre=[listeligne,listecolonne]
    return(solcarre)

solution(carre3)
'''On retrouve le solcarre3'''

#Description: genere aléatoirement un logimage
#Entrée: les dimensions du logimage nbligne et nbcolonne
#sortie: un logimage de taille nbligne et nbcolonne au format numpy
def genererlogimage(nbligne,nbcolonne):
    logimage=np.zeros((nbligne,nbcolonne))
    for i in range (nbligne):
        for j in range (nbcolonne):
            logimage[i,j]=rd.randint(0,1) #un 0 ou un 1 aléatoirement
    return(logimage)
genererlogimage(3, 3)
genererlogimage(10, 10)


'''Remarque: le nombre de logimages différents est exponentiel en les dimensions 
du logimage en 2 puissance n avec n le nombre de cases.'''
#Si il y a 3 lignes et 3 colonnes:
2**9
#10 lignes et colonnes
2**100
#50lignes et colonnes:
2**2500
#Imaginer combien d'images sont possibles avec le format 1920*1080:
from math import *
log(2**(1920*1080))/log(10)
#un nombre avec plus de 624000 chiffres.


logimage=genererlogimage(5, 5)
print(logimage)
solution(logimage)
