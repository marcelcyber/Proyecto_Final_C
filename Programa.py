
import os

MAX_PRODUCTOS = 100

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def cargar_inventario():
    inventario = []
    if os.path.exists("inventario.txt"):
        with open("inventario.txt", "r") as archivo:
            for linea in archivo:
                nombre, cantidad, precio = linea.split()
                inventario.append(Producto(nombre, int(cantidad), float(precio)))
    return inventario

def guardar_inventario(inventario):
    with open("inventario.txt", "w") as archivo:
        for producto in inventario:
            archivo.write(f"{producto.nombre} {producto.cantidad} {producto.precio}\n")

def ingresar_producto(inventario):
    if len(inventario) < MAX_PRODUCTOS:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        inventario.append(Producto(nombre, cantidad, precio))
    else:
        print("Inventario lleno, no se pueden agregar más productos.")

def editar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a editar: ")
    for producto in inventario:
        if producto.nombre == nombre:
            producto.cantidad = int(input("Ingrese la nueva cantidad: "))
            producto.precio = float(input("Ingrese el nuevo precio: "))
            return
    print("Producto no encontrado.")

def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for i, producto in enumerate(inventario):
        if producto.nombre == nombre:
            del inventario[i]
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

def listar_productos(inventario):
    for producto in inventario:
        print(f"Producto: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio:.2f}")

def main():
    inventario = cargar_inventario()

    while True:
        print("\nSistema de inventario de papelería")
        print("1. Ingresar producto")
        print("2. Editar producto")
        print("3. Eliminar producto")
        print("4. Listar productos")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ingresar_producto(inventario)
        elif opcion == 2:
            editar_producto(inventario)
        elif opcion == 3:
            eliminar_producto(inventario)
        elif opcion == 4:
            listar_productos(inventario)
        elif opcion == 5:
            print("Saliendo del programa...")
            guardar_inventario(inventario)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()


