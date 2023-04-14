#Dépendances :
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from functions import *

##Temps
t_max = 100
#Nombre de pas
n = 20000

#Etapes
h = np.linspace(0,t_max,n)

#Conditions initiales
#Particule 1
#Positions en x et y
x0_1 = 0.201
y0_1 = 0
#Vitesses en x et y
vx0_1 = 0
vy0_1 = 0.48

#Particule 2
#Positions en x et y
x0_2 = 0.1                #C'est cette coordonnée que l'on fait varier dans le rapport mais il est possible de varier les autres
y0_2 = 0
#Vitesses en x et y
vx0_2 = 0
vy0_2 = 0.48


#Intégration des équations du mouvement par la méthode scipy pour les 2 particules.
x1,y1,px1,py1 = scipy_method(x0_1,y0_1,vx0_1,vy0_1,h)
x2,y2,px2,py2 = scipy_method(x0_2,y0_2,vx0_2,vy0_2,h)


#=================================================================================================
#Calcul exposants de Lyapunov pour position x

diff_x1 = []
expo_x = []
t = np.delete(h,0)
t = t.tolist()

for i in range(len(x1)):
    diff_x1.append(abs(x1[i]-x2[i]))
diff_x1.remove(diff_x1[0])

for i in range(len(diff_x1)):
    if diff_x1[i]!=0:
        expo_x.append(log(diff_x1[i]/t[i]))

# print(expo_x)


# #=================================================================================================
#Calcul exposants de Lyapunov pour position y

diff_y1 = []
expo_y = []

for i in range(len(y1)):
    diff_y1.append(abs(y1[i]-y2[i]))
diff_y1.remove(diff_y1[0])

for i in range(len(diff_y1)):
    if diff_y1[i]!=0:
        expo_y.append(log(diff_y1[i]/t[i]))

# print(expo_y[-1],t[-1])


#==================================================================================================#
#Calcul exposants de Lyapunov pour vitesse selon x

diff_px1 = []
expo_px = []

for i in range(len(px1)):
    diff_px1.append(abs(px1[i]-px2[i]))
diff_px1.remove(diff_px1[0])

for i in range(len(diff_px1)):
    if diff_px1[i]!=0:
        expo_px.append(log(diff_px1[i]/t[i]))

# print(expo_px)


#==================================================================================================#
#Calcul exposants de Lyapunov pour vitesse selon y

diff_py1 = []
expo_py = []

for i in range(len(py1)):
    diff_py1.append(abs(py1[i]-py2[i]))
diff_py1.remove(diff_py1[0])

for i in range(len(diff_py1)):
    if diff_py1[i]!=0:
        expo_py.append(log(diff_py1[i]/t[i]))

# print(expo_py)


#==================================================================================================#
#Calcul de la moyenne des exposants de Lyapunov


expo_moy = []

for i in range(min(len(expo_x),len(expo_y),len(expo_px),len(expo_py))):
    expo_moy.append((expo_x[i]+expo_y[i]+expo_px[i]+expo_py[i])/4)

#=================================================================================================
#Enregistrement des exposants dans un fichier text nommé "exposant_temps.txt"


with open('exposant_temps.txt', 'w') as f:
    # Parcourir les listes simultanément
    for i in range(min(len(expo_x),len(expo_y),len(expo_px),len(expo_py))):
        # Écrire les éléments dans chaque liste dans une colonne séparée
        f.write(f"{t[i]}\t{expo_x[i]}\t{expo_y[i]}\t{expo_px[i]}\t{expo_py[i]}\t{expo_moy[i]}\n")

print("Fichier text créé")

#=================================================================================================
#Tracé des exposants en fonction du temps

plt.figure(figsize=(10,6))

plt.title('')
plt.xlabel('temps en secondes')
plt.ylabel('exposants')
plt.plot(t, expo_py, marker = '.', markersize = 2,linestyle = 'none',c='k',label="Exposant moyen")
plt.legend()
plt.savefig('Var epsilon=1 x=0.1.png')