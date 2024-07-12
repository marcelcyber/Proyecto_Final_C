from funciones_inventario import (cargar_inventario, guardar_inventario, 
                                  ingresar_producto, editar_producto, 
                                  eliminar_producto, listar_productos)

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
