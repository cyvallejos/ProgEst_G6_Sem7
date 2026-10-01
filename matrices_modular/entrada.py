from .validaciones import leer_dimension, leer_entero


def leer_matriz(nombre, cuadrada=False):
    print(f"Ingrese los valores de {nombre}:")
    if cuadrada:
        filas = leer_dimension("Ingrese el tamaño de la matriz cuadrada: ")
        columnas = filas
    else:
        filas = leer_dimension("Ingrese la cantidad de filas: ")
        columnas = leer_dimension("Ingrese la cantidad de columnas: ")

    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(leer_entero(f"Ingrese el valor [{i}][{j}]: "))
        matriz.append(fila)
    return matriz