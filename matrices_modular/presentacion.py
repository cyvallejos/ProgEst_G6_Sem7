def mostrar_matriz(matriz, diagonal_azul=False):
    for i, fila in enumerate(matriz):
        valores = []
        for j, valor in enumerate(fila):
            if diagonal_azul and i == j and valor == 1:
                valores.append(f"\033[94m{valor}\033[0m")
            else:
                valores.append(str(valor))
        print("[" + ", ".join(valores) + "]")