# Generación de la población inicial según el problema
import random
import numpy as np
import numpy
import GenerarPoblacion
import Aptitud
import Sumatoria
import probabilidad

cromosomas = 6  # numero de individuos
genes = 11  # Genes
suma_calorias = 0
suma_peso = 0
probabilidad_peso = []
probabilidad_calorias = []
total = []
menor_elemento = 1
# Datos del problema: Leche de soya (500,0.5), Galletas (300,0.1), Agua (100,0.5), Pan (700,0.25), Huevo (300,0.15), Nueces (400,0.15), Yogurt (500,0.5), Manzana (400,0.3),snicker (248,0.05),aguacate(240,0.15),mandarina(61,0.11)

Pesos = [0.5, 0.1, 0.5, 0.25, 0.15, 0.15, 0.5, 0.3, 0.05, 0.15, 0.11]
calorias = [500, 300, 100, 700, 300, 400, 500, 400, 248, 240, 61]


def prob_total(prob_calorias, prob_peso):
    total = []
    n = 0
    while n < 6:
        total.append(prob_peso[n]+prob_calorias[n])
        n += 1
    return total


# generacion de poblacion
genPob = GenerarPoblacion(cromosomas, genes, Pesos, calorias)
print(genPob)

# Aptitud peso
aptitud = Aptitud()
aptitud.peso(Pesos, genPob)
# Aptitud Calorias
aptitud.calorias(calorias, genPob)

# sumatoria arreglo peso
suma_peso = Sumatoria(aptitud.arreglopeso)
# sumatoria arreglo calorias
suma_calorias = Sumatoria(aptitud.arreglocalorias)


# Probabilidad peso
probabilidad_peso = probabilidad(aptitud.arreglopeso, suma_peso)
# probabilidad calorias
probabilidad_calorias = probabilidad(aptitud.arreglocalorias, suma_calorias)

print("probabilidad Peso")
print("")
print("[")
for i in probabilidad_peso:
    print(f"[ % .2f ]" % i)
print("]")
print("")


print("probabilidad calorias")
print("")
print("[")
for i in probabilidad_calorias:
    print(f"[ % .2f ]" % i)
print("]")
print("")

total = prob_total(probabilidad_peso, probabilidad_calorias)
print("probabilidad total")
print("")
print("[")
for i in total:
    print(f"[ % .2f ]" % i)
print("]")
print("")
# Paso 3 Seleccion                     
##Concatenar la matriz poblacion con el vector obtenido
print("Paso 3")
def ordenarPorPosicionSubLista(lista: genPob, posicionOrdenar: int) -> genPob:
    return(sorted(genPob, key = lambda elemento: elemento[posicionOrdenar-1],reverse = True))
genPob=np.c_[genPob,total]
print("Matriz con fitness")
genPob=ordenarPorPosicionSubLista(genPob,12)
print(genPob)
genPob.pop(5)
genPob.append(genPob[0])
print("Matriz final")
print(genPob)
# Paso 4 Cruce de individuos                     


