cliente={
    "nombre":"jorge",
    "apellido":"rodriguez",
    "telefono":"312456788",
    "saldo":"5000",
    "edad":"40",
}
print(cliente)
valor=cliente.get("nombre")
print(valor)
cliente["profesion"]="ingeniero"
print(cliente)
print(cliente["telefono"])
del cliente ["saldo"]
print (cliente)
print(cliente.keys())
print(cliente.values())
cajero={
    "nombre":"jose",
    "apellido":"lopez"
}
cliente.update(cajero)
print(cliente)