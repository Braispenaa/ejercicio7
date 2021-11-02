lista = []

while True:
    nombre =input("nombre: ")
    if nombre == "fin":
        break
    numero_de_telefono = input("Numero de telefono: ")
    linea = {}
    linea["nombre"] = nombre
    linea["Numero de telefono"] = numero_de_telefono
    lista.append(linea)
    for linea in lista:
        print("lista:\n",linea)