tamano=int(input("ingrese la lista"))
lista=[]
while tamano !=0:
    tamano -=1
    print(f'el valor a ingresar es: {tamano}')
    valor=input()
    lista.append(valor)
print(lista)