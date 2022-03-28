# Generación de la población inicial según el problema
import random
from re import X
import numpy as np
import numpy

cromosomas = 6 #numero de individuos
genes = 11 #Genes
arreglocalorias=[]
arreglopeso=[]
sumatoriaArregloCalorias = 0
sumatoriaArregloPeso = 0
#Datos del problema: Leche de soya (500,0.5), Galletas (300,0.1), Agua (100,0.5), Pan (700,0.25), Huevo (300,0.15), Nueces (400,0.15), Yogurt (500,0.5), Manzana (400,0.3),snicker (248,0.05),aguacate(240,0.15),mandarina(61,0.11)

Pesos = [0.5, 0.1, 0.5, 0.25, 0.15, 0.15, 0.5, 0.3, 0.05, 0.15, 0.11]
calorias = [500, 300, 100, 700, 300, 400, 500, 400, 248, 240,61]

# generacion de poblacion

def GenerarPoblacion():
  poblacion = np.zeros([cromosomas, genes])
  #Se llena la poblacion aleatoriamente
  for i in range(cromosomas):
      n = 1
      while n > 0:
        Apt_p= 0
        Apt_c= 0
        for j in range(genes):
          poblacion[i, j] = random.randint(0, 1)
          Apt_p = Apt_p + poblacion[i, j]*Pesos[j]
          Apt_c = Apt_c + poblacion[i, j]*calorias[j]
        
        #Muere el individuo que no cumpla las condiciones

        if Apt_p <= 2  and Apt_c >= 2300:
            n = 0

  return poblacion

genPob= GenerarPoblacion()
print(genPob)
# Actitud peso
def imprimirPeso():
  print ("")
  print("Actitud peso") 
  print("")
  print("[")
  # i representa las filas de la poblacion
  for i in genPob:
    x = 0 #cada posicion de la fila 
    suma=0 #suma del peso
    while(x< numpy.size(i)):#recorre cada posicion de cada fila
      if i[x] != 0: #si la posicion de i en x es diferente de 0 , osea igual a 1
        suma += Pesos[x]#suma el peso donde sea 1 en posision x 
      x=x+1 #vuelve a iniciar el ciclo 
    print(f"[ % .2f ]" %suma)
    arreglopeso.append(suma)
  print("]")
  

# Actitud Calorias

def imprimirCalorias():
  print("")
  print("Actitud calorias")
  print("")
  print("[")
  

  for j in genPob:
    y=0
    suma=0
    while (y<numpy.size(j)):
      if j[y] !=0:
        suma+=calorias[y]
      y=y+1
    print("[",suma,"]")
    arreglocalorias.append(suma)
  print("]")

#sumatoria 
def suma_arreglo(arreglo):
  sumatoria=0
  for i in arreglo:
    sumatoria+=i
  return sumatoria


imprimirPeso()
imprimirCalorias()
sumatoriaArregloCalorias = suma_arreglo(arreglocalorias)
sumatoriaArregloPeso = suma_arreglo(arreglopeso)


