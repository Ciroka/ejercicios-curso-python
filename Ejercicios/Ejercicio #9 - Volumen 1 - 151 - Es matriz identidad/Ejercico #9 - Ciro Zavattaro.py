n=int(input())
while n!=0:
    matriz_usuario=[[n for x in range(n)]for x in range (n)]
    for x in range (n):
        entrada=input()
        cont=0
        for carac in entrada:
            if carac!=" ":
                matriz_usuario[x][cont]=int(carac)
                cont+=1
    for x in range (n):
        for i in range (n):
            if i==x and matriz_usuario[x][i]==1:
                bandera=False
            elif matriz_usuario[x][i]==0 and i!=x:
                bandera=False
            else:
                bandera=True
                break
        if bandera:
            break
    if bandera:
        print ("NO")
    else:
        print ("SI")
    n=int(input())