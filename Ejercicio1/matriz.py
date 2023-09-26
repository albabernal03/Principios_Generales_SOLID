class Matriz():
    def __init__(self,elementos: list):
        self.elementos = elementos

class Transpuesta(Matriz):
    def __init__(self,elementos: list):
        super().__init__(elementos) #este super es para heredar el constructor de la clase padre, que seria Matriz
        self.elementos = elementos

    def transpuesta(self):
        return [[self.elementos[j][i] for j in range(len(self.elementos))] for i in range(len(self.elementos[0]))] #esto es una funcion lambda que significa lo mismo que el for 
    

class Imprimir(Matriz):
    def __init__(self,elementos: list):
        super().__init__(elementos) #este super es para heredar el constructor de la clase padre, que seria Matriz
        self.elementos = elementos

    def imprimir(self):
        for i in range(len(self.elementos)):
            for j in range(len(self.elementos[0])):
                print(self.elementos[i][j], end=" ")
            print()