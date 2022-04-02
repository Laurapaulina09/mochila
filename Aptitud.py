import numpy
import sys

# Aptitud peso
class Aptitud:
    arreglopeso=[]
    arreglocalorias=[]

    def peso(self, pes,genPob):
      print("")
      print("Evaluación")
      print("")
      print("Aptitud peso") 
      print("[")
      self.arreglopeso=[]
      for i in genPob:# i representa las filas de la poblacion
        x = 0 #cada posicion de la fila 
        suma=0 #suma del peso
        while(x< numpy.size(i)):#recorre cada posicion de cada fila
          if i[x] != 0: #si la posicion de i en x es diferente de 0 , osea igual a 1
            suma += pes[x]#suma el peso donde sea 1 en posision x 
          x=x+1 #vuelve a iniciar el ciclo 
        print(f"[ % .2f ]" %suma)
        self.arreglopeso.append(suma)
      print("]")
    
    def calorias(self,cal,genPob):
      print("")
      print("Aptitud calorias")
      print("[")
      self.arreglocalorias=[]
      for j in genPob:
        y=0
        suma=0
        while (y<numpy.size(j)):
          if j[y] !=0:
            suma+=cal[y]
          y=y+1
        print("[",suma,"]")
        self.arreglocalorias.append(suma)
      print("]")
      
sys.modules[__name__] = Aptitud





