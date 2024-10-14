def calcular(x, y):
    return x * y

subtotal = 0
cantidad = 1

while cantidad != 0:
    print("Ingrese la cantidad del producto:")
    cantidad = float(input())
    if cantidad == 0:
        break
    print("Ingrese el valor del producto:")
    valor = float(input())
    total = calcular(cantidad, valor)
    subtotal += total
print("El total de los productos es: {subtotal}")
