def caracteres_en_una_sola_linea_matriz (matriz,n):
    matriz_usuario=matriz
    for x in range (n):
        entrada=input()
        cont=0
        for carac in entrada:
            if carac!=" ":
                matriz_usuario[x][cont]=int(carac)
                cont+=1
    return matriz_usuario
def mov_arriba (matriz,fila,columna,cont,suma):
    cont_mov=cont
    pos=columna
    pos1=fila
    m=matriz
    estrellas=suma
    for x in range (1,cont_mov+1):
        estrellas+=m[pos1-x][pos]
    return estrellas
def mov_derecha (matriz,fila,columna,cont,suma):
    cont_mov=cont
    pos=columna
    pos1=fila
    m=matriz
    estrellas=suma
    for x in range (1,cont_mov+1):
        estrellas+=m[pos1][pos+x]
    return estrellas
def mov_abajo (matriz,fila,columna,cont,suma):
    cont_mov=cont
    pos=columna
    pos1=fila
    m=matriz
    estrellas=suma
    for i in range (1,cont_mov+1):
        estrellas+=m[pos1+i][pos]
    return estrellas
def mov_izquierda ( matriz,fila,columna,cont,suma):
    cont_mov=cont
    pos=columna
    pos1=fila
    m=matriz
    estrellas=suma
    for x in range (1,cont_mov+1):
        estrellas+=m[pos1][pos-x]
    return estrellas
n=int(input())
while n!=0:
    matris=[[0 for x in range(n)]for x in range (n)]
    cont=1
    inicio_fila=n//2
    inicio_columna=n//2
    suma=0
    bandera=True
    matriz=caracteres_en_una_sola_linea_matriz (matris,n)
    suma+=matris[inicio_fila][inicio_columna]
    while bandera:
        if (cont-1)%4==0 and inicio_fila+1-cont>0:
            suma=mov_arriba(matris,inicio_fila,inicio_columna,cont,suma)
            inicio_fila-=cont
            cont+=1
        elif (cont-1)%4==1 and  inicio_columna+1+cont<=n:
            suma=mov_derecha(matris,inicio_fila,inicio_columna,cont,suma)
            inicio_columna+=cont
            cont+=1
        elif (cont-1)%4==2 and inicio_fila+1+cont<=n:
            suma=mov_abajo(matris,inicio_fila,inicio_columna,cont,suma)
            inicio_fila+=cont
            cont+=1
        elif (cont-1)%4==3 and inicio_columna+1-cont>=0:
            suma=mov_izquierda(matris,inicio_fila,inicio_columna,cont,suma)
            inicio_columna-=cont
            cont+=1
        else:
            if (cont-1)%4==0:
                cont-=1
                suma=mov_arriba(matris,inicio_fila,inicio_columna,cont,suma)
            elif (cont-1)%4==1:
                cont-=1
                suma=mov_derecha(matris,inicio_fila,inicio_columna,cont,suma)
            elif (cont-1)%4==2:
                cont-=1
                suma=mov_abajo(matris,inicio_fila,inicio_columna,cont,suma)
            elif (cont-1)%4==3:
                cont-=1
                suma=mov_izquierda(matris,inicio_fila,inicio_columna,cont,suma)
            bandera=False
    print (suma)
    n=int(input())
