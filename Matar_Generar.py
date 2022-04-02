import numpy
import random
import sys
import GenerarPoblacion


def matar_generar(cruce,peso,calorias):
    n=0
    new_cruce=[]
    while n<6:
        if peso[n] > 2 or calorias[n] < 2300:
            print("", end="")
        else:
            new_cruce.append(cruce[n])
        n=n+1
    n=0
    num_cruce=len(new_cruce)
    num_faltantes = 6-num_cruce
    

    Pesos = [0.5, 0.1, 0.5, 0.25, 0.15, 0.15, 0.5, 0.3, 0.05, 0.15, 0.11]
    calorias = [500, 300, 100, 700, 300, 400, 500, 400, 248, 240, 61]
    arreglo_faltantes = GenerarPoblacion(num_faltantes, 11, Pesos, calorias)
    new_cruce=numpy.r_[new_cruce,arreglo_faltantes]
    

    print("Nueva Generación")
    print(new_cruce)
    return new_cruce

sys.modules[__name__] = matar_generar



        

        
           
