def slpitmio (cadena,separacion):
    vector_palabras=[""]*len(cadena)
    inicio=0
    cadena+=separacion
    cont=0
    for x in range (len(cadena)):
        if cadena[x]==separacion:
            vector_palabras[cont]=cadena[inicio:x]
            inicio=x+1
            cont+=1
    vec_real=[""]*cont
    for x in range (len(cadena)):
        if x<cont:
            vec_real[x]=vector_palabras[x]
    return vec_real
entrada=input()
while entrada!="00 : 00":
    entrada=slpitmio(entrada," ")
    hora=entrada[0]
    minutos=entrada[2]
    hora=23-int(hora)
    minutos=60-int(minutos)
    faltante=hora*60+minutos
    print (faltante)
    entrada=input()