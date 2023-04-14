#Dépendances
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from functions import *


##Temps
t_max = 100000
#Nombre de pas
n = 20000000

#Etapes
h = np.linspace(0,t_max,n)

#Conditions initiales de la trajectoire de référence
#Positions
x0_1 = 0.201
y0_1 = 0
#Vitesses
vx0_1 = 0
vy0_1 = 0.48

#Résolution des équations du mouvement

x1,y1,px1,py1 = scipy_method(x0_1,y0_1,vx0_1,vy0_1,h)

#Tracé de la trajectoire au cours du temps

plt.figure(figsize=(10,6))

plt.title('')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x1, y1, marker = '.', markersize = 1,linestyle = 'none',c='b',label="Trajectoire de référence")
plt.legend()
plt.savefig('trajectoire de référence temps 100000.png')
