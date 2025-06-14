def fibFBR(n):
    global op
    op += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibFBR(n-1) + fibFBR(n-2)

def fibPDUtil(n, tabla):
    global op
    op += 1
    if tabla[n] != -1:
        return tabla[n]
    elif n == 0:
        tabla[n] = 0
        return tabla[n]
    elif n == 1:
        tabla[n] = 1
        return tabla[n]
    else:
        tabla[n] = fibPDUtil(n-1, tabla) + fibPDUtil(n-2, tabla)
        return tabla[n]


def fibPD(n):
    tabla = [-1]*(n+1)
    return fibPDUtil(n, tabla)

    
###
op = 0
print(fibFBR(35), " op:", op)
op = 0
print(fibPD(35), " op:", op)