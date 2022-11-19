

archivo = open("lemario.txt","r")
cont = 0
letras="qwertyuiopasdfghjklñzxcvbnm"
for palabra in archivo:
    for i in palabra[:-1]:
        if i not in letras:
            print(palabra,cont)
    cont+=1
    if cont>100:
        break