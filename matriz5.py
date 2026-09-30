# Convierte una matriz cuadrada en matriz de identidad y muestra la diagonal en azul.

def leer_entero(mensaje):
	while True:
		try:
			return int(input(mensaje))
		except ValueError:
			print("Entrada no válida. Ingrese un número entero.")

dimension = leer_entero("Ingrese el tamaño de la matriz cuadrada: ")
while dimension <= 0:
	print("El tamaño debe ser mayor que cero.")
	dimension = leer_entero("Ingrese el tamaño de la matriz cuadrada: ")

matriz = []
for i in range(dimension):
	matriz.append([])
	for j in range(dimension):
		matriz[i].append(leer_entero(f"Ingrese el valor [{i}][{j}]: "))

for i in range(dimension):
	for j in range(dimension):
		matriz[i][j] = 1 if i == j else 0

print("Matriz de identidad:")
for i, fila in enumerate(matriz):
	valores = []
	for j, valor in enumerate(fila):
		if i == j:
			valores.append(f"\033[94m{valor}\033[0m")
		else:
			valores.append(str(valor))
	print("[" + ", ".join(valores) + "]")