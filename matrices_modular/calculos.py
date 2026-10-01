from .validaciones import (
    validar_cuadrada,
    validar_matriz,
    validar_multiplicacion,
    validar_suma,
)


def multiplicar_por_escalar(matriz, escalar):
    validar_matriz(matriz)
    return [[valor * escalar for valor in fila] for fila in matriz]


def sumar_matrices(matriz_a, matriz_b):
    validar_suma(matriz_a, matriz_b)
    resultado = []
    for i in range(len(matriz_a)):
        fila = []
        for j in range(len(matriz_a[0])):
            fila.append(matriz_a[i][j] + matriz_b[i][j])
        resultado.append(fila)
    return resultado


def multiplicar_matrices(matriz_a, matriz_b):
    validar_multiplicacion(matriz_a, matriz_b)
    resultado = []
    for i in range(len(matriz_a)):
        fila = []
        for j in range(len(matriz_b[0])):
            valor = 0
            for k in range(len(matriz_b)):
                valor += matriz_a[i][k] * matriz_b[k][j]
            fila.append(valor)
        resultado.append(fila)
    return resultado


def convertir_a_identidad(matriz):
    validar_cuadrada(matriz)
    dimension = len(matriz)
    return [
        [1 if i == j else 0 for j in range(dimension)]
        for i in range(dimension)
    ]