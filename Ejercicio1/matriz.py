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
    #Creame funcion que permita llamar a las funciones imprimir y transpuesta de las clases Imprimir y Transpuesta y recoja los datos con un input
    def __init__(self):
        self.elementos=[]
        self.cantidad_filas = int(input("Ingrese la cantidad de filas: "))
        self.cantidad_columnas = int(input("Ingrese la cantidad de columnas: "))
        self.crear_matriz()
        super().__init__(self.elementos) 

    def crear_matriz(self):
        for i in range(self.cantidad_filas):
            fila = []
            for j in range(self.cantidad_columnas):
                fila.append(int(input("Ingrese el elemento: ")))
            self.elementos.append(fila)

    def lanzar(self):
        self.imprimir()
        print("La matriz transpuesta es: ")
        print(self.transpuesta()) 
        


class Main():
    def __init__(self):
        self.lanzar()

    def lanzar(self):
        Lanzador().lanzar()

if __name__ == "__main__":
    Main()