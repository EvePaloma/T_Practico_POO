#Importa las clases Electronico y Alimento
from electronico import Electronico
from alimento import Alimento

#Define la función principal
def main():
    #Solicita al usuario que ingrese la información del producto electrónico.
    print("Producto electrónico:")
    nombre_elect = input("Ingrese Nombre: ")
    precio_elect = input("Ingrese Precio: ")
    cantidad_elect = input("Ingrese Cantidad: ")
    marca = input("Ingrese Marca: ")
    modelo = input("Ingrese Modelo: ")
    #Se crea una instancia de la clase Electrónico con su información.
    electronico = Electronico(nombre_elect, precio_elect, cantidad_elect, marca, modelo)
    #Imprime la información del producto electrónico.
    print(electronico.mostrarInfoProducto())

    #Solicita al usuario que ingrese la información del producto alimenticio.
    print("\nProducto alimenticio:")
    nombre_alim = input("Ingrese Nombre: ")
    precio_alim = input("Ingrese Precio: ")
    cantidad_alim = input("Ingrese Cantidad: ")
    fecha_expiracion = input("Ingrese Fecha de expiración: ")
    #Se crea una instancia de la clase Alimento con su información.
    alimento = Alimento(nombre_alim, precio_alim, cantidad_alim, fecha_expiracion)
    #Imprime la información del producto alimenticio.
    print(alimento.mostrarInfoProducto())


if __name__== "__main__":
    main()    