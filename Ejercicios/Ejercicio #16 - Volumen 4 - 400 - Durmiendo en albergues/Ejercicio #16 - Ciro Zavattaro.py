cadena=input()
inicio=10000000000000
final=0
cont_med=[int(0)]*10
for i in range(len(cadena)):
    if cadena[i]=="X" and i<inicio:
        inicio=i
    if cadena[i]=="X":
        final=i
cont_antes=0
cont_desp=0
cont_medio=0
indice=0
for x in range (len(cadena)):
    if x<inicio:
        cont_antes+=1
    elif x>final:
        cont_desp+=1
    elif x>inicio and x<final:
        cont_medio+=1
        if cadena[x]=="X":
            cont_med[indice]=cont_medio
            indice+=1
            cont_medio=0
for x in range(indice):
    if cont_med[x]>cont_medio:
        cont_medio=cont_med[x]
if cont_medio==0:
    if cont_desp>cont_antes:
        print(cont_desp-1)
    else:
        print(cont_antes-1)
else:
    if cont_medio>cont_antes and cont_medio>cont_desp:
        if cont_medio%2==0:
            cont_medio=cont_medio//2-1
        else:
            cont_medio//=2
        print (cont_medio)
    elif cont_desp>cont_antes and cont_desp>=cont_medio:
        print(cont_desp-1)
    else:
        print(cont_antes-1)