#ifndef FUNCIONES_H
#define FUNCIONES_H

#define MAX_PRODUCTOS 100

struct Producto {
    char nombre[50];
    int cantidad;
    float precio;
};

void cargarInventario(struct Producto inventario[], int *numProductos);
void guardarInventario(struct Producto inventario[], int numProductos);
void ingresarProducto(struct Producto inventario[], int *numProductos);
void editarProducto(struct Producto inventario[], int numProductos);
void eliminarProducto(struct Producto inventario[], int *numProductos);
void listarProductos(struct Producto inventario[], int numProductos);

#endif
