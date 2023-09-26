class Matriz():
    def __init__(self,elementos: list):
        self.elementos = elementos

class Transpuesta(Matriz):
    def __init__(self,elementos: list):
        super().__init__(elementos) #este super es para heredar el constructor de la clase padre, que seria Matriz
        self.elementos = elementos

    def transpuesta(self):
        return [[self.elementos[j][i] for j in range(len(self.elementos))] for i in range(len(self.elementos[0]))] #esto es una funcion lambda que significa lo mismo que el for 
    #en este caso es correcto usar la funcion ya que no estamos trabajando con grandes volunes de datos
    #si manejamos muchos datos es mejor usar el for, ya que la funcion lambda es mas lenta

class Imprimir(Matriz):
    def __init__(self,elementos: list):
        super().__init__(elementos) #este super es para heredar el constructor de la clase padre, que seria Matriz
        self.elementos = elementos

    def imprimir(self):
        for fila in self.elementos:
            print(fila)

class Lanzador(Imprimir, Transpuesta):
    #Creame funcion que permita llamar a las funciones imprimir y transpuesta de las clases Imprimir y Transpuesta y recoja los datos de la clase Matriz


