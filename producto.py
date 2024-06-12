class Producto: #clase Padre

    def __init__(self, nombre, precio, cantidad):
    #Constructor   
    #Inicializa los atributos.
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def getNombre(self):
        return self.nombre #Devuelve el nombre del producto.

    def getPrecio(self):
        return self.precio #Devuelve el precio del producto.

    def getCantidad(self):
        return self.cantidad #Devuelve la cantidad del producto.   

    #Método poara mostrar info de producto.
    def mostrarInfoProducto(self):
        print ("\nLos datos ingresados son: " + "\n" 
                +"\nNombre: "+str(self.getNombre())
                +"\nPrecio: "+str(self.getPrecio())
                +"\nCantidad: "+str(self.getCantidad()))

