tablero=[[1,1,1,1,0,1,1,1,1],
     [1,0,0,1,0,1,0,0,0],
     [1,1,0,1,1,1,1,0,1],
     [0,1,0,1,0,0,1,0,1],
     [1,1,1,1,1,1,1,1,1],
     [1,0,1,0,0,0,1,0,1],
     [1,1,1,1,0,1,1,0,1],
     [1,0,0,1,0,1,0,0,1],
     [1,1,1,1,0,1,1,1,1]]


def imprime(mat):
    for f in mat:
        for c in f:
            print(f"{c},",end="")
        print()
    print()



def valida(tablero, fil, col)->bool:
    #verificar que no se repita nro en las filas
    #verificar que no se repita nro en las columnas
    #verificar que no se repita nro en el mini cuadrado
    if fil >= len(lab):      
        return False
    if fil < 0:
        return False
    if col >= len(lab[0]):
        return False
    if col < 0:
        return False
    if tablero[fil][col] == 0:             
        return False
    if tablero[fil][col] == 1:
        return False

    return True

def estalleno():
    for
        for
    return fil, col
    
def sudoku(tablero, fil, col, num)->bool:
    fil,col = estalleno()
    if fil == -1 and col == -1:
        #ok
        return True

    else:

        if valida(tablero, fil, col):
            tablero[fil][col]=num
            imprime(tablero)

            if labbas(tablero, fil+1, col, num):
                return True
            elif labbas(tablero, fil, col+1, num):
                return True
            elif labbas(tablero, fil, col-1, num):
                return True
            elif labbas(tablero, fil-1, col, num):
                return True
            else:
                tablero[fil][col]=0
                return False

        else:

            return False

######

#imprime(lab)



if sudoku(lab, 0, 0, 0):
    print("Salio")
else:
    print("No hay salida")