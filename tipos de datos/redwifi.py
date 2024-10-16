datos=[]
while True:
    print("==========================")
    print("///////WIFI TECH//////////")
    print("=====Elige una opcion=====")
    print("Opcion 1: Agregar wifi")
    print("Opcion 2: Ver Wifi")
    print("Opcion 3: Salir")
    print("==========================")
    opcion=int(input("Elige la opcion:"))
    print("==========================")

    if opcion==1:
        wifi={}
        usuario=input("Ingrese el usuario:")
        wifi["usuario"]=usuario
        print("==========================")
        contrasena=input("Ingrese la contrasena:")
        wifi["contrasena"]=contrasena
        datos.append(wifi)
        print("==========================")
    elif opcion==2:
        for i in range(len(datos)):
            print(datos[i])
    elif opcion== 3:
        break