def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")


def leer_dimension(mensaje):
    while True:
        dimension = leer_entero(mensaje)
        if dimension > 0:
            return dimension
        print("La dimensión debe ser mayor que cero.")


def validar_matriz(matriz):
    if not matriz or not matriz[0]:
        raise ValueError("La matriz debe tener al menos una fila y una columna.")

    cantidad_columnas = len(matriz[0])
    if any(len(fila) != cantidad_columnas for fila in matriz):
        raise ValueError("Todas las filas deben tener la misma cantidad de columnas.")


def validar_suma(matriz_a, matriz_b):
    validar_matriz(matriz_a)
    validar_matriz(matriz_b)
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        raise ValueError("Para sumar, las matrices deben tener las mismas dimensiones.")


def validar_multiplicacion(matriz_a, matriz_b):
    validar_matriz(matriz_a)
    validar_matriz(matriz_b)
    if len(matriz_a[0]) != len(matriz_b):
        raise ValueError(
            "Las columnas de la primera matriz deben coincidir con las filas de la segunda."
        )


def validar_cuadrada(matriz):
    validar_matriz(matriz)
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada.")