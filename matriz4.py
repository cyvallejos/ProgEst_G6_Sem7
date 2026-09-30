# Multiplicación de matrices cuadradas 2x2.

def leer_entero(mensaje):
	while True:
		try:
			return int(input(mensaje))
		except ValueError:
			print("Entrada no válida. Ingrese un número entero.")

matriz1 = []
print("Ingrese los valores de la primera matriz:")
for i in range(2):
	matriz1.append([])
	for j in range(2):
		matriz1[i].append(leer_entero(f"Ingrese el valor [{i}][{j}]: "))

matriz2 = []
print("Ingrese los valores de la segunda matriz:")
for i in range(2):
	matriz2.append([])
	for j in range(2):
		matriz2[i].append(leer_entero(f"Ingrese el valor [{i}][{j}]: "))

matrizResultado = []
for i in range(2):
	matrizResultado.append([])
	for j in range(2):
		valor = 0
		for k in range(2):
			valor += matriz1[i][k] * matriz2[k][j]
		matrizResultado[i].append(valor)

print("Matriz resultante de la multiplicación:")
for fila in matrizResultado:
	print(fila)