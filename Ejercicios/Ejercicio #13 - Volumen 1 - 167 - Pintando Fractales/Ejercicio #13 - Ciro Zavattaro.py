n = int(input()) 
cont=0
resultado1=0
def fractal(numero,contador,pasar_un_0):
    cont=contador
    divisor = 2 ** cont
    multiplicador = 4 ** (cont + 1)
    pasar_un_0 += (numero // divisor) * multiplicador
    if numero // divisor == 1:
        print (pasar_un_0)
    else:
        fractal(numero,cont+1,pasar_un_0) 
fractal(n,cont,resultado1)
