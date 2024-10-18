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
def siguiente(num, letras):
    nueva = ""
    if int(num) < 9999:
        nueva = str(int(num) + 1) + " " + letras
        return nueva
    else:
        num = "0000"
        vocales="AEIUO"
        cont = 2
        contador = 1
        aux = letras
        while cont >= 0:
            if ord(letras[cont]) < 90: 
                nueva_letra = chr(ord(letras[cont]) + contador)
                for x in range (5):
                    if nueva_letra==vocales[x]:
                        contador += 1
                        nueva_letra = chr(ord(letras[cont]) + contador)
                nueva = num + " " + aux[:cont] + nueva_letra + aux[cont+1:]
                return nueva
            else:
                aux = aux[:cont] + "B" + aux[cont+1:]
                cont -= 1
        return nueva

matricula=input()
resultado=""
matricula=slpitmio(matricula," ")
resultado=siguiente(matricula[0],matricula[1])
print (resultado)