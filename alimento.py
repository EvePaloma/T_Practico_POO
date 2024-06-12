#Importa la clase Producto desde el archivo producto.py
from producto import Producto

#clase que representa un producto alimenticio, heredando de Producto
class Alimento(Producto):

    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        #Llama al constructor de la clase padre (Producto) para inicializar los atributos heredados.
        super().__init__(nombre, precio, cantidad)
        #Inicializa el atributo agregado.
        self.fecha_expiracion = fecha_expiracion

    def getFechaExpiracion(self):
        return self.fecha_expiracion

    #Método para mostrar info completa del producto alimenticio.
    def mostrarInfoProducto(self):
        super().mostrarInfoProducto()
        print("Fecha de Expiracion: "+ str(self.getFechaExpiracion()))


