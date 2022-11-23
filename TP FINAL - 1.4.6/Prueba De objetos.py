archivo = open("lemario.txt","r")
primero = True
mayor = []
for a in archivo:
    linea = a[:-1]
    if primero:
        primero = False
        mayor = [len(linea),linea]
    elif len(linea) > mayor[0]:
        mayor = [len(linea),linea]
    
