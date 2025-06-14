tablero=[[0, 6, 0, 1, 0, 4, 0, 5, 0],
    [0, 0, 8, 3, 0, 5, 6, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 1],
    [8, 0, 0, 4, 0, 7, 0, 0, 6],
    [0, 0, 6, 0, 0, 0, 3, 0, 0],
    [7, 0, 0, 9, 0, 1, 0, 0, 4],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 7, 2, 0, 6, 9, 0, 0],
    [0, 4, 0, 5, 0, 8, 0, 7, 0]]


def imprime(mat):
    for f in mat:
        for c in f:
            print(f"{c},",end="")
        print()
    print()



def es_valido(tablero, fila, col, num):
    if num in tablero[fila]:
        return False

    for i in range(len(tablero)):
        if tablero[i][col] == num:
            return False

    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_col + j] == num:
                return False

    return True

def resolver_sudoku(tablero):
    #recorro cada celda del laberinto buscando las disponibles = 0
    for fila in range(len(tablero)):
        for col in range(len(tablero[0])):
            if tablero[fila][col] == 0:
                #si encuentro disponible le pongo valor (1-9)
                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        tablero[fila][col] = num
                        if resolver_sudoku(tablero):
                            return True
                        tablero[fila][col] = 0
                return False
    return True

######

#imprime(lab)


imprime(tablero)
if resolver_sudoku(tablero):
    print("Salio")
    imprime(tablero)
else:
    print("No hay salida")