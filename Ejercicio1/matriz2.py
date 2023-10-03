#MEJORA DEL CÓDIGO RIGIENDOSE POR PRINCIPIOS DE SOLID

#TEORIA
''' 
El principio SOLID es un conjunto de cinco principios:

1.Principio de Responsabilidad Única (SRP - Single Responsibility Principle): Este podedmos ver que antes
se cumplia ya que cada clase tenia una única responsabilidad, por ejemplo

-Transpuesta: Calcular la transpuesta de una matriz
-Imprimir: Imprimir una matriz
-Lanzador: Controla la interacción con el usuario para crear y mostrar la matriz.
-Matriz: Representa una matriz

2.Principio de Abierto/Cerrado (OCP - Open/Closed Principle): Este principio nos dice que las clases 
deben estar abiertas para la extensión pero cerradas para la modificación. En el código anterior
podemos ver que se puede agregar nuevas funcionalidades sin modificar las clases existentes. 
Por ejemplo, podrías agregar métodos adicionales a Matriz, Transpuesta, o Imprimir sin tener que cambiar el código
existente en estas clases.

3.Principio de Sustitución de Liskov (LSP - Liskov Substitution Principle):

El principio LSP se refiere a la capacidad de sustituir una instancia de una clase derivada por una instancia de 
su clase base sin afectar el comportamiento del programa. En el codig anterior no hay clases derivadas, por lo que
no se aplica este principio.

4.Principio de Segregación de Interfaces (ISP - Interface Segregation Principle):El principio ISP sugiere que las interfaces deben ser específicas 
para los clientes que las utilizan. En tu código, no se implementan interfaces explícitas, por lo que este principio no
 es relevante en este caso.

5.Principio de Inversión de Dependencias (DIP - Dependency Inversion Principle): El principio DIP sugiere que los módulos de alto nivel 
no deben depender de módulos de bajo nivel, sino que ambos deben depender de abstracciones. 
En el código anterior, la clase Lanzador depende de las clases' Matriz', 'Transpuesta' e 'Imprimir', que son clases de bajo nivel. 
Esto lo podemos mejorar haciendo que la clase Lanzador dependa de una abstracción, por ejemplo, una clase MatrizOperacion, que permitiría una 
mayor flexibilidad y extensibilidad.
'''

#APLICANDO LO ULTIMO DICHO EN LA TEORIA, QUEDARÍA EL CÓDIGO DE LA SIGUIENTE MANERA:

class Matriz:
    def __init__(self, elementos: list):
        self.elementos = elementos

class MatrizOperacion:
    def __init__(self, matriz: Matriz):
        self.matriz = matriz

class Transpuesta(MatrizOperacion):
    def calcular(self):
        return Matriz([[fila[i] for fila in self.matriz.elementos] for i in range(len(self.matriz.elementos[0]))])

class Imprimir(MatrizOperacion):
    def imprimir(self):
        for fila in self.matriz.elementos:
            print(fila)

class Lanzador:
    def __init__(self):
        self.elementos = []
        self.cantidad_filas = int(input("Ingrese la cantidad de filas: "))
        self.cantidad_columnas = int(input("Ingrese la cantidad de columnas: "))
        self.crear_matriz()
        self.matriz = Matriz(self.elementos)
        self.transpuesta = Transpuesta(self.matriz)
        self.imprimir = Imprimir(self.matriz)

    def crear_matriz(self):
        for i in range(self.cantidad_filas):
            fila = []
            for j in range(self.cantidad_columnas):
                fila.append(int(input(f"Ingrese el elemento {i+1},{j+1}: ")))
            self.elementos.append(fila)

    def lanzar(self):
        print("La matriz es: ")
        self.imprimir.imprimir()
        print("La matriz transpuesta es: ")
        transpuesta_result = self.transpuesta.calcular()
        Imprimir(transpuesta_result).imprimir()

if __name__ == "__main__":
    lanzador = Lanzador()
    lanzador.lanzar()
