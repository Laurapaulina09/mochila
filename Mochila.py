# Generación de la población inicial según el problema
import random
import numpy as np
import pandas as pd
import numpy
import GenerarPoblacion
import Aptitud
import Sumatoria
import probabilidad
import Matar_Generar


cromosomas = 6  # numero de individuos
genes = 11  # Genes
suma_calorias = 0
suma_peso = 0
probabilidad_peso = []
probabilidad_calorias = []
total = []
datos = int(input("ingrese la cantidad de generaciones que desea: "))
genPob=[]


# Datos del problema: Leche de soya (500,0.5), Galletas (300,0.1), Agua (100,0.5), sanduche (700,0.25), Huevo (300,0.15), Nueces (400,0.15), Yogurt (500,0.5), Manzana (400,0.3),snicker (248,0.05),aguacate(240,0.15),mandarina(61,0.11)

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
print("Paso 1")
print("POBLACION INICIAL",genPob.shape)
print("")
print(genPob)
z = 0
while z < datos:
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

    print("")
    print("Probabilidad Peso")
    print("[")
    for i in probabilidad_peso:
        print(f"[ % .2f ]" % i)
    print("]")
    print("")

    print("Probabilidad calorias")
    print("[")
    for i in probabilidad_calorias:
        print(f"[ % .2f ]" % i)
    print("]")
    print("")

    total = prob_total(probabilidad_peso, probabilidad_calorias)
    print("Probabilidad total")
    print("[")
    for i in total:
        print(f"[ % .2f ]" % i)
    print("]")
    print("")

    # Paso 3 Seleccion                     
    print("Paso 3")
    def ordenarPorPosicionSubLista(lista: genPob, posicionOrdenar: int) -> genPob:
        return(sorted(genPob, key = lambda elemento: elemento[posicionOrdenar-1],reverse = True))
    genPob=np.c_[genPob,total]

    genPob=ordenarPorPosicionSubLista(genPob,12)
    print("")
    print("Matriz ordenada")
    print ("")
    df = pd.DataFrame(genPob, columns=['-', '-', '-','G', 'E', 'N','E', 'S', '-','-', '-', 'Total'])
    print(df)
    genPob[5]=genPob[0]
    print("")
    #Muere el individuo con menor resultado, y es reemplazado por el mejor
    df = pd.DataFrame(genPob, columns=['-', '-', '-','G', 'E', 'N','E', 'S', '-','-', '-', 'Total'])
    print(df)


    # Paso 4 Cruce de individuos                     
    #Concatenar la matriz poblacion con el vector obtenido
    cruce=[]
    #hijo 1
    cruce.append(np.concatenate([genPob[0][0:5], genPob[1][5:11]]))

    #hijo 2
    cruce.append(np.concatenate([genPob[1][0:5],genPob[0][5:11]]))

    #hijo 3
    cruce.append(np.concatenate([genPob[2][0:5],genPob[3][5:11]]))

    #hijo 4
    cruce.append(np.concatenate([genPob[3][0:5],genPob[2][5:11]]))

    #hijo 5
    cruce.append(np.concatenate([genPob[4][0:5],genPob[5][5:11]]))

    #hijo 6
    cruce.append(np.concatenate([genPob[5][0:5],genPob[4][5:11]]))
    print("")
    print("Paso 4")
    print("Hijos")
    df = pd.DataFrame(cruce, columns=['-', '-', '-','-', '-', '-','-', '-', '-','-', '-',])
    print(df)

    #Paso 5
    #Mutacion

    def mutacion(cruce):
        for i in range (cromosomas):
            mutar=random.randint(0, 10)
            print("")
            print("gen mutado individuo",[i+1],mutar+1)
            if cruce [i][mutar]==1:
                cruce[i][mutar]=0
            else:
                cruce[i][mutar]=1

    mutacion(cruce)
    print("")
    print("Paso 5")
    print("Mutación")
    df = pd.DataFrame(cruce, columns=['-', '-', '-','-', '-', '-','-', '-', '-','-', '-',])
    print(df)


    #Paso 6 
    #Evaluacion de los Hijos

    # Aptitud peso Hijos
    aptitud = Aptitud()
    aptitud.peso(Pesos,cruce)
    # Aptitud Calorias Hijos 
    aptitud.calorias(calorias,cruce)

    # sumatoria arreglo peso Hijos
    suma_peso = Sumatoria(aptitud.arreglopeso)
    # sumatoria arreglo calorias Hijos 
    suma_calorias = Sumatoria(aptitud.arreglocalorias)

    # Probabilidad peso
    probabilidad_peso = probabilidad(aptitud.arreglopeso, suma_peso)
    # probabilidad calorias
    probabilidad_calorias = probabilidad(aptitud.arreglocalorias, suma_calorias)

    print("")
    print("Probabilidad Peso Hijos")
    print("[")
    for i in probabilidad_peso:
        print(f"[ % .2f ]" % i)
    print("]")
    print("")

    print("Probabilidad calorias Hijos")
    print("[")
    for i in probabilidad_calorias:
        print(f"[ % .2f ]" % i)
    print("]")
    print("")

    total = prob_total(probabilidad_peso, probabilidad_calorias)
    print("Probabilidad total")
    print("[")
    for i in total:
        print(f"[ % .2f ]" % i)
    print("]")
    print("")

    genPob = Matar_Generar(cruce,aptitud.arreglopeso,aptitud.arreglocalorias)
    z = z+1

    


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

total = prob_total(probabilidad_peso, probabilidad_calorias)

def ordenarPorPosicionSubLista(lista: genPob, posicionOrdenar: int) -> genPob:
        return(sorted(genPob, key = lambda elemento: elemento[posicionOrdenar-1],reverse = True))
genPob=np.c_[genPob,total]

genPob=ordenarPorPosicionSubLista(genPob,12)
print("Total")
print(total)
genPob[0]


print("La mejor opción es: ")
if genPob[0][0] == 1:
    print("Leche de soya")
if genPob[0][1] == 1:
    print("Galletas")
if genPob[0][2] == 1:
    print("Agua")
if genPob[0][3] == 1:
    print("sanduche")
if genPob[0][4] == 1:
    print("Huevo")
if genPob[0][5] == 1:
    print("Nueces")
if genPob[0][6] == 1:
    print("Yogurt")
if genPob[0][7] == 1:
    print("Manzana")
if genPob[0][8] == 1:
    print("Snicker")
if genPob[0][9] == 1:
    print("Aguacate")
if genPob[0][10] == 1:
    print("Mandarina")
