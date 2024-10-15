datos=[]
def agregrar():
    nombre=input("Pon tu nombre")
    apellido=input("Pon tu apellido")
    telefono=int(input("Pon tu telefono"))


while True:
    print("=====Banco Talento Tech=====")
    print("Opcion 1: Agregar Clientes")
    print("Opcion 2: Ver Clientes")
    print("Opcion 3: Borrar Clientes")
    print("Opcion 4: Editar Clientes")
    print("Opcion 5: Salir")
    print("============================")
    opcion=int(input("Ingrese la opcion"))
    print("============================")
    if opcion==1:
        agregrar()
    elif opcion==2:
        print("Selecciono la opcion 2")
    elif opcion==3:
        print("Selecciono la opcion 3")
    elif opcion==4:
        print("Selecciono la opcion 4")
    else:
        print("Error de digito")
