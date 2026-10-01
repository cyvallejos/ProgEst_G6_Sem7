import sys
from pathlib import Path

if __package__ in (None, ""):
	sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from matrices_modular.calculos import (
    convertir_a_identidad,
    multiplicar_matrices,
    multiplicar_por_escalar,
    sumar_matrices,
)
from matrices_modular.entrada import leer_matriz
from matrices_modular.presentacion import mostrar_matriz
from matrices_modular.validaciones import leer_entero


def ejecutar_mostrar_matriz():
    matriz = leer_matriz("la matriz")
    print("Matriz ingresada:")
    mostrar_matriz(matriz)


def ejecutar_escalar():
    matriz = leer_matriz("la matriz")
    escalar = leer_entero("Ingrese el escalar: ")
    print("Matriz multiplicada por el escalar:")
    mostrar_matriz(multiplicar_por_escalar(matriz, escalar))


def ejecutar_suma():
    matriz_a = leer_matriz("la primera matriz")
    matriz_b = leer_matriz("la segunda matriz")
    print("Resultado de la suma:")
    mostrar_matriz(sumar_matrices(matriz_a, matriz_b))


def ejecutar_multiplicacion():
    matriz_a = leer_matriz("la primera matriz")
    matriz_b = leer_matriz("la segunda matriz")
    print("Resultado de la multiplicación:")
    mostrar_matriz(multiplicar_matrices(matriz_a, matriz_b))


def ejecutar_identidad():
    matriz = leer_matriz("la matriz cuadrada", cuadrada=True)
    print("Matriz de identidad:")
    mostrar_matriz(convertir_a_identidad(matriz), diagonal_azul=True)


def mostrar_menu():
    print("\n--- Ejercicios de matrices ---")
    print("1. Ingresar y mostrar una matriz")
    print("2. Multiplicar una matriz por un escalar")
    print("3. Sumar dos matrices")
    print("4. Multiplicar dos matrices")
    print("5. Convertir una matriz cuadrada en identidad")
    print("0. Salir")


def consultar_salida():
    while True:
        respuesta = input(
            "Escriba 0 para salir o escriba 1 para volver al menú: " 
        ).strip()
        if respuesta == "0":
            return True
        if respuesta == "1":
            return False
        print("Respuesta no válida. Escriba 0 para salir o escriba 1 para volver al menú.")


def main():
    while True:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opción: ")
        if opcion == 0:
            print("Programa finalizado.")
            break

        try:
            if opcion == 1:
                ejecutar_mostrar_matriz()
            elif opcion == 2:
                ejecutar_escalar()
            elif opcion == 3:
                ejecutar_suma()
            elif opcion == 4:
                ejecutar_multiplicacion()
            elif opcion == 5:
                ejecutar_identidad()
            else:
                print("Opción no válida.")
        except ValueError as error:
            print(f"No se pudo realizar la operación: {error}")

        if opcion in (1, 2, 3, 4, 5) and consultar_salida():
            print("Programa finalizado.")
            break


if __name__ == "__main__":
    main()