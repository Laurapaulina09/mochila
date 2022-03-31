
import random
import numpy as np
import sys


def GenerarPoblacion(cromosomas,genes,Pesos,calorias):
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
  
sys.modules[__name__] = GenerarPoblacion