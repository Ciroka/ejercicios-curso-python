n = int(input())
while n!=0:
    vec_similares = [0] * n
    vec_entrada = [""] * n
    for i in range(n):
        vec_entrada[i] = input()
    for i in range(n):
        for j in range(i + 1, n):  
            cadena1 = vec_entrada[i]
            cadena2 = vec_entrada[j]
            cont_letras = 0
            cont_comparaciones = 0
            bandera_igual = True
            for k in range(len(cadena1)):
                if cadena1[k] != "-": 
                    cont_letras += 1
                    if cadena1[k]==cadena2[k] or cadena2[k] == "-": 
                        cont_comparaciones += 1
                    else:
                        bandera_igual = False 
                        break
            if bandera_igual and cont_letras == cont_comparaciones:
                vec_similares[i] += 1
                vec_similares[j] += 1
    for x in range (n):
        print (vec_similares[x],end=" ")
    print (" ")
    n = int(input())