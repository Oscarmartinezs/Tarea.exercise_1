"""
cliente:
    quiero escribir un programa python que reciba de input del usuario
    un nombre, un producto, costo
    y se guarde en una lista con diccinarios, el registro es un diccionario
    y va a ser guardado en una lista
programador:
    vaya

cliente:
    mira me gusta pero cada vez que inicio el programa, me borra el cliente anterior
    y solo puedo guardar el que he ingresado en ese momento, no habria forma de
    que se guarde a los 3 clientes que tengo?
programador:
    vaya
mente:
    y pollo no queres?
    

"""

# creando la lista vacia
listaRegistro = []

CostoTotal = 0
opcion = input("Desea ingresar un cliente?: ")
while opcion == "Si":
    cliente = input("Nombre Cliente: ")
    producto = input("Nombre Producto: ")
    costo = float(input("Costo ($0.00): "))
    registro = dict(cliente=cliente, producto=producto, costo=costo)

    listaRegistro.append(registro)
    opcion = input("Desea ingresar otro cliente?: ")
# guardar
for registro in listaRegistro:
    print(registro)
CostosTotales = "Losc costos hasta el momento son: "
for Registro in listaRegistro:
    CostoTotal = CostoTotal + registro.get("costo")
print(f"El costo total es de {CostoTotal}")

# Oscar Martínez
