tamano=input("Dame un valor de la lista")
lista=[]
for i in range (int(tamano)):
    print(f'el valor a ingresar es: {i}')
    valor=input()
    lista.append(valor)
print(lista)