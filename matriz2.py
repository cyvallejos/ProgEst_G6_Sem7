matriz = []
for i in range(2):
    matriz.append([])
    for j in range(2):
        matriz[i].append(int(input(f"Ingrese el valor [{i}][{j}]: ")))

for i in range(2):
    print(matriz[i])