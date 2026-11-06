def imprimir_matriz(matriz):
    for fila in matriz:
        print("\t".join(str(elemento) for elemento in fila))
    print()

def main():
    n = int(input("Ingrese el tamaño de la matriz cuadrada (ej. 6): "))
    
    matriz_1 = [[0] * n for _ in range(n)]
    contador = 1
    for i in range(n):
        for j in range(n):
            matriz_1[i][j] = contador
            contador += 1
            
    print("--- Matriz 1 ---")
    imprimir_matriz(matriz_1)

    matriz_2 = [[0] * n for _ in range(n)]
    contador = 1
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                matriz_2[i][j] = contador
                contador += 1
        else:
            for j in range(n - 1, -1, -1):
                matriz_2[i][j] = contador
                contador += 1
                
    print("--- Matriz 2 ---")
    imprimir_matriz(matriz_2)

    matriz_3 = [[0] * n for _ in range(n)]
    for i in range(n):
        matriz_3[i][i] = 1
        
    print("--- Matriz 3 (Identidad) ---")
    imprimir_matriz(matriz_3)

    matriz_4 = [[0] * n for _ in range(n)]
    for i in range(n):
        matriz_4[i][n - 1 - i] = 1
        
    print("--- Matriz 4 ---")
    imprimir_matriz(matriz_4)

    matriz_5 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            matriz_5[i][j] = 1
            
    print("--- Matriz 5 ---")
    imprimir_matriz(matriz_5)

    matriz_6 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            matriz_6[i][j] = 1
            
    print("--- Matriz 6 ---")
    imprimir_matriz(matriz_6)

    matriz_7 = [[0] * n for _ in range(n)]
    contador = 1
    for j in range(n):
        for i in range(n):
            matriz_7[i][j] = contador
            contador += 1
            
    print("--- Matriz 7 ---")
    imprimir_matriz(matriz_7)

    matriz_8 = [["" ] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j % 2 == 0:
                matriz_8[i][j] = 'A'
            else:
                matriz_8[i][j] = 'B'
                
    print("--- Matriz 8 ---")
    imprimir_matriz(matriz_8)

if __name__ == "__main__":
    main()