#Importa la clase Producto desde el archivo producto.py
from producto import Producto

#clase que representa un producto electronico, heredando de Producto
class Electronico(Producto):

    def __init__(self, nombre, precio, cantidad, marca, modelo):
        #Llama al constructor de la clase padre (Producto) para inicializar los atributos heredados.
        super().__init__(nombre, precio, cantidad)
        #Inicializa los atributos agregados.
        self.marca = marca
        self.modelo = modelo

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo    

    #Método para mostrar info completa del producto electrónico.
    def mostrarInfoProducto(self):
        super().mostrarInfoProducto()
        print ("Marca: "+ str(self.getMarca())
               +"\nModelo: "+ str(self.getModelo()))
    


