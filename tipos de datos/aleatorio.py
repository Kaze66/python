import random

numero=random.randint(3,9)
intentos=0
while True:
    valor=int(input("Ingrese el numero"))
    if valor == numero:
        print("Has acertado y ganado")
        break
    else:
        print("Has perdido")
        intentos+=1
    if intentos >5:
        print("Game Over")
