#Fichier contenant la fonction définissant les accélérations dans un potentiel de Henon Heiles. 

from math import *
import numpy as np

def henon(X,h):
	x,y,vx,vy = X
										#Ici la valeur "1" est la constante de non linéarité que l'on peut faire varier
	ax = - x - 1*x*y
	ay = - y - 1*(x**2 + y**2)

	return vx,vy,ax,ay