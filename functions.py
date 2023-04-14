#Fichier contenant les fonctions permettant l'intégration des équations du mouvement. Ce fichier utilise la fonction henon définie dans le 
#fichier henon_heiles.py

from math import *
import numpy as np
from scipy.integrate import odeint
from random import randint
from henon_heiles import *

def acceleration(X,h=[np.linspace(0,10,2000)]):

	vx,vy,ax,ay = henon(X,h)

	return vx,vy,ax,ay


def scipy_method(x0,y0,vx0,vy0,h):

	sol = odeint(acceleration,(x0,y0,vx0,vy0),h)
	#Transformer le tableau numpy en liste
	sol = np.array(sol).T.tolist()
	x = sol[0]
	y = sol[1]
	px = sol[2]
	py = sol[3]

	return x,y,px,py