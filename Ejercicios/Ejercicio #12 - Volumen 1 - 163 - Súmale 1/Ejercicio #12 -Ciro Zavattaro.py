try:
    numero=str(input())
    while numero!="FIN":
        vector_hexa=["A","B","C","D","E","F"]
        vector=[str(0)]*len(numero)
        vector_resutado=[0]*len(numero)
        numero=numero[::-1]
        num=numero.upper()
        numero=num
        suma=0
        resultado=""
        vec_resul=[0]*100
        for x in range (len(numero)):
            vector[x]=numero[x]
            for i in range (6):
                if vector[x]==vector_hexa[i]:
                    vector_resutado[x]=i+10
                    break
                elif vector[x]!=vector_hexa[i] and i==5:
                    vector_resutado[x]=int (vector[x])
        for j in range (len(numero)):
            vector_resutado[j]=int(vector_resutado[j])*(16**j)
            suma+=vector_resutado[j]
        suma+=1
        cont=0
        bandera=False
        if suma>=16:
            bandera=True
        if bandera:
            while bandera:
                if suma%16>9:
                    vec_resul[cont]=vector_hexa[(suma%16)-10]
                else:
                    vec_resul[cont]=suma%16
                cont+=1
                suma=suma//16
                if suma==0:
                    bandera=False
            for x in range (cont-1,-1,-1):
                resultado+=str(vec_resul[x])
        else:
            if suma%16>9:
                resultado=vector_hexa[(suma%16)-10]
            else:
                resultado=suma%16
        print(resultado)
        numero=str(input())
except:
    print ("El limite es de 100 digitos :(")