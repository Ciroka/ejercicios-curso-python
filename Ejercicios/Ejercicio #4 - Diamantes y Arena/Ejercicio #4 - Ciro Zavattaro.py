n=int(input())
vector_diamantes=[int(0)]*n
for x in range (n):
    cadena=input()
    cont_abrir=0
    cont_cerrar=0
    bandera=False
    for i in range (len(cadena)):
        if cadena[i]=="<":
            cont_abrir+=1
            bandera=True
        elif cadena[i]==">" and bandera==True:
            cont_cerrar+=1
    if cont_abrir<cont_cerrar:
        vector_diamantes[x]=cont_abrir
    elif cont_cerrar<cont_abrir:
        vector_diamantes[x]=cont_cerrar
    else:
        vector_diamantes[x]=cont_abrir
for i in range (n):
    print (vector_diamantes[i])