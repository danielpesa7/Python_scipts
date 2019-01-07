#Este ejercicio nace de un juego propuesto por DataCamp, el cual consiste en:
## Estamos en el piso 0 de un gran edificio, queremos llegar al piso 60 y nuestro movimiento dentro del 
## edificio está determinado por un dado que lanzaremos 100 veces de la siguiente forma:
### * Si obtenemos un 1 ó 2 descendemos un piso ( en el caso del piso 0 permanecemos en él)
### * Si obtenemos un 3,4 ó 5 subimos un piso
### * Si obtenemos un 6 volvemos a lanzar el dado y subimos la cantidad de pisos correspondiente al número que hemos obtenido.
#### Aparte de eso, somos un poco torpes y tenemos una probabilidad de 0.1% de caernos, lo cual nos devolvería de inmediato al piso 0.
#### 1) Queremos saber cuál sería la probabilidad de llegar mínimo al piso 60 después de haber repetido el experimento 500 veces.
#### 2) Graficar con líneas continuas cada uno de los recorridos y mediante un histograma observar la distribución de probabilidades.

import numpy as np
import matplotlib.pyplot as plt

# Inicializar la lista que contendrá todos nuestros recorridos simulados
all_walks = []

# Simula nuestro recorrido por el edificio 500 veces
for i in range(500) :

    # Simula el lanzamiento del dado 100 veces y nuestro avance dentro del edificio
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        # Simula nuestra posible caida
        if np.random.rand() <= 0.001:
            step = 0
        #Adjunta nuestro avance a través del edificio a nuestro recorrido.
        random_walk.append(step)

    # Adjunta nuestro recorrido del edificio a la lista de los demás recorridos simulados
    all_walks.append(random_walk)

# Imprime todos los recorridos simulados (500)
#print(all_walks)

#Transpone la matriz de recorridos para que matplotlib la pueda entender y graficar bien
np_all_walks = np.transpose(np.array(all_walks))
final_step = np_all_walks[-1]
plt.figure(1)
plt.plot(np_all_walks)
plt.title('Walks')
plt.figure(2)
plt.hist(final_step)
plt.title('Final Step Distribution')
plt.show()
print('La probabilidad de llegar al piso 60 es de {} %'.format(len(final_step[final_step > 60])*100/500))