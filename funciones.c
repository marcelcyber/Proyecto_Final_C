#include <stdio.h>
#include <string.h>
#include "funciones.h"

void cargarInventario(struct Producto inventario[], int *numProductos) {
    FILE *archivo = fopen("inventario.txt", "r");
    if (archivo != NULL) {
        *numProductos = 0;
        while (fscanf(archivo, "%s %d %f", inventario[*numProductos].nombre, &inventario[*numProductos].cantidad, &inventario[*numProductos].precio) != EOF) {
            (*numProductos)++;
        }
        fclose(archivo);
    }
}

void guardarInventario(struct Producto inventario[], int numProductos) {
    FILE *archivo = fopen("inventario.txt", "w");
    if (archivo != NULL) {
        for (int i = 0; i < numProductos; i++) {
            fprintf(archivo, "%s %d %f\n", inventario[i].nombre, inventario[i].cantidad, inventario[i].precio);
        }
        fclose(archivo);
    }
}

void ingresarProducto(struct Producto inventario[], int *numProductos) {
    if (*numProductos < MAX_PRODUCTOS) {
        printf("Ingrese el nombre del producto: ");
        scanf("%s", inventario[*numProductos].nombre);
        printf("Ingrese la cantidad: ");
        scanf("%d", &inventario[*numProductos].cantidad);
        printf("Ingrese el precio: ");
        scanf("%f", &inventario[*numProductos].precio);
        (*numProductos)++;
    } else {
        printf("Inventario lleno, no se pueden agregar más productos.\n");
    }
}

void editarProducto(struct Producto inventario[], int numProductos) {
    char nombre[50];
    printf("Ingrese el nombre del producto a editar: ");
    scanf("%s", nombre);

    for (int i = 0; i < numProductos; i++) {
        if (strcmp(inventario[i].nombre, nombre) == 0) {
            printf("Ingrese la nueva cantidad: ");
            scanf("%d", &inventario[i].cantidad);
            printf("Ingrese el nuevo precio: ");
            scanf("%f", &inventario[i].precio);
            return;
        }
    }
    printf("Producto no encontrado.\n");
}

void eliminarProducto(struct Producto inventario[], int *numProductos) {
    char nombre[50];
    printf("Ingrese el nombre del producto a eliminar: ");
    scanf("%s", nombre);

    for (int i = 0; i < *numProductos; i++) {
        if (strcmp(inventario[i].nombre, nombre) == 0) {
            for (int j = i; j < *numProductos - 1; j++) {
                inventario[j] = inventario[j + 1];
            }
            (*numProductos)--;
            printf("Producto eliminado.\n");
            return;
        }
    }
    printf("Producto no encontrado.\n");
}

void listarProductos(struct Producto inventario[], int numProductos) {
    for (int i = 0; i < numProductos; i++) {
        printf("Producto: %s, Cantidad: %d, Precio: %.2f\n", inventario[i].nombre, inventario[i].cantidad, inventario[i].precio);
    }
}
