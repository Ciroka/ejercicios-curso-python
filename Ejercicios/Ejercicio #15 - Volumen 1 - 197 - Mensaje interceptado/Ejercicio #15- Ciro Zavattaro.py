cadena=input()
aux1=""
aux2=""
x1=""
x2=""
for x in range (len(cadena)):
    if x%2==0:
        aux1+=cadena[x]
    else:
        aux2+=cadena[x]
aux2=aux2[::-1]
x1=aux1+aux2
cont=0
vec_vocales=["A","E","I","O","U"]
vocales=[0]*len(x1)
cont=0
for x in range (len(x1)):
    for i in range (5):
        if x1[x].upper()==vec_vocales[i]:
            vocales[cont]=x
            cont+=1
aux=""
cont1=0
vector_entremedio=[""]*cont
for x in range (cont-1):
    vector_entremedio[x]=x1[vocales[x]+1:vocales[x+1]]
vector_entremedio[cont1-1]=x1[vocales[cont-1]+1:]
contador=0
contador1=0
vector_resul=[""]*(cont*2)
resultado=""
for  x in range (cont*2):
    if x%2==0:
        vector_resul[x]=x1[vocales[contador]]
        contador+=1
    else:
        aux=vector_entremedio[contador1]
        aux=aux[::-1]
        vector_resul[x]=aux
        contador1+=1
if vocales[0]!=0:
    resultado+=x1[:vocales[0]]
    for x in range (cont*2):
        resultado+=vector_resul[x]
else:
    for x in range (cont*2):
        resultado+=vector_resul[x]
if cont==len(x1):
    print (cadena,"=>",cadena)
else:
    print (cadena,"=>",resultado)