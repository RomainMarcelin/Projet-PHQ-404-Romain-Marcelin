# Code utilisé pour calculer et tracer les exposants de Lyapunov. 
#Si ce code retourne un fichier appelé "exposant_temps.txt" qui ne comporte zéro ou une seule ligne ou un message d'erreur,
# alors c'est qu'il faut utiliser le fichier exposant_temps_2.py (avec les conditions initiales que vous avez essayé).
#=======================================================================================================================#

#Dépendances :
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from functions import *

##Temps
t_max = 100
#Nombre de pas
n = 20000
#Liste des temps pour l'intégration numérique des équations
h = np.linspace(0,t_max,n)

#Conditions initiales
#Particule 1 (particule de référence)
#Positions en x et y
x0_1 = 0.201
y0_1 = 0
#Vitesses en x et y
vx0_1 = 0
vy0_1 = 0.48

#Particule 2 (particule test)
#Positions en x et y
x0_2 = 4                #C'est cette coordonnée que l'on fait varier dans le rapport mais il est possible de varier les autres
y0_2 = 0
#Vitesses en x et y
vx0_2 = 0
vy0_2 = 0.48


#Intégration des équations du mouvement par la méthode scipy pour les 2 particules.
x1,y1,px1,py1 = scipy_method(x0_1,y0_1,vx0_1,vy0_1,h)
x2,y2,px2,py2 = scipy_method(x0_2,y0_2,vx0_2,vy0_2,h)


#=================================================================================================
#Calcul exposant de Lyapunov pour position x

diff_x1 = []
expo_x = []
t = np.delete(h,0)
t = t.tolist()

for i in range(len(x1)):
    diff_x1.append(abs(x1[i]-x2[i]))
diff_x1.remove(diff_x1[0])

diff_x2 = []
pt_crit = 0

for i in range(len(diff_x1)):
    if diff_x1[i] > 20000:
        pt_crit = i
for i in range(len(diff_x1)):
    if i < pt_crit:
        diff_x2.append(diff_x1[i])
    elif i > pt_crit or i == pt_crit:
        if diff_x1[i]>diff_x1[i+1]:
            pt_crit = i
            diff_x2.append(diff_x1[i])
            break
        else:
            diff_x2.append(diff_x1[i])
for i in range(len(diff_x2)):
    expo_x.append(log(diff_x2[i]/t[i]))

tx = []
for i in range(len(t)):
    if i <= pt_crit:
        tx.append(t[i])
    else :
        break

# print(expo_x)


# #=================================================================================================
# #Calcul exposant de Lyapunov pour position y

diff_y1 = []
expo_y = []

for i in range(len(y1)):
    diff_y1.append(abs(y1[i]-y2[i]))
diff_y1.remove(diff_y1[0])

diff_y2 = []
pt_crit = 0

for i in range(len(diff_y1)):
    if diff_y1[i] > 20000:
        pt_crit = i
for i in range(len(diff_y1)):
    if i < pt_crit:
        diff_y2.append(diff_y1[i])
    elif i > pt_crit or i == pt_crit:
        if diff_y1[i]>diff_y1[i+1]:
            pt_crit = i
            diff_y2.append(diff_y1[i])
            break
        else:
            diff_y2.append(diff_y1[i])
for i in range(len(diff_y2)):
    expo_y.append(log(diff_y2[i]/t[i]))

ty = []
for i in range(len(t)):
    if i <= pt_crit:
        ty.append(t[i])
    else :
        break

# print(expo_y[-1],ty[-1])


# #=================================================================================================
# #Calcul exposant de Lyapunov pour vitesse selon x

diff_px1 = []
expo_px = []

for i in range(len(px1)):
    diff_px1.append(abs(px1[i]-px2[i]))
diff_px1.remove(diff_px1[0])

diff_px2 = []
pt_crit = 0

for i in range(len(diff_px1)):
    if diff_px1[i] > 20000:
        pt_crit = i
for i in range(len(diff_px1)):
    if i < pt_crit:
        diff_px2.append(diff_px1[i])
    elif i > pt_crit or i == pt_crit:
        if diff_px1[i]>diff_px1[i+1]:
            pt_crit = i
            diff_px2.append(diff_px1[i])
            break
        else:
            diff_px2.append(diff_px1[i])
for i in range(len(diff_px2)):
    expo_px.append(log(diff_px2[i]/t[i]))

tpx = []
for i in range(len(t)):
    if i <= pt_crit:
        tpx.append(t[i])
    else :
        break

# print(expo_px)


# #=================================================================================================
# #Calcul exposant de Lyapunov pour vitesse selon y

diff_py1 = []
expo_py = []

for i in range(len(py1)):
    diff_py1.append(abs(py1[i]-py2[i]))
diff_py1.remove(diff_py1[0])

diff_py2 = []
pt_crit = 0

for i in range(len(diff_py1)):
    if diff_py1[i] > 20000:
        pt_crit = i
for i in range(len(diff_py1)):
    if i < pt_crit:
        diff_py2.append(diff_py1[i])
    elif i > pt_crit or i == pt_crit:
        if diff_py1[i]>diff_py1[i+1]:
            pt_crit = i
            diff_py2.append(diff_py1[i])
            break
        else:
            diff_py2.append(diff_py1[i])
for i in range(len(diff_py2)):
    expo_py.append(log(diff_py2[i]/t[i]))

tpy = []
for i in range(len(t)):
    if i <= pt_crit:
        tpy.append(t[i])
    else :
        break

# print(expo_py)


#=================================================================================================
#Calcul de la moyenne des exposants de Lyapunov


expo_moy = []

for i in range(len(tx)):
    expo_moy.append((expo_x[i]+expo_y[i]+expo_px[i]+expo_py[i])/4)

#=================================================================================================
#Enregistrement des exposants dans un fichier texte nommé "exposant_temps.txt"


with open('exposant_temps.txt', 'w') as f:
    # Parcourir les listes simultanément
    for i in range(len(tx)):
        # Écrire les éléments dans chaque liste dans une colonne séparée
        f.write(f"{tx[i]}\t{expo_x[i]}\t{expo_y[i]}\t{expo_px[i]}\t{expo_py[i]}\t{expo_moy[i]}\n")

print("Fichier text créé")

#=================================================================================================
#Tracé des exposants de Lyapunov en fonction du temps


# figsize=(10,6)
plt.figure()

plt.title('')
plt.xlabel('Temps en secondes')
plt.ylabel('Exposant')
plt.plot(tpy, expo_py, marker = '.', markersize = 3,linestyle = 'none',c='k',label="Exposant moyen")
plt.xlim(0,7)
plt.legend()
plt.savefig('x=4 avec epsilon=4 .png')
