# Se solicita el nombre del producto
nombre=input("por favor ingrese el nombre del producto:")

# Se solicita el precio y la cantidad de los productos
while True:
    try:
        precio=float(input("Por favor ingresa el precio del producto:"))

        if precio <= 0:
          print("valor invalido, por favor ingresa un valor valido:")
        else:
            break
    except ValueError:
        print("por favor ingresa un valor valido ")

            
while True:
    try:
        cantidad=int(input("Por favor ingresa cuantos productos son:"))

        if cantidad <= 0:
          print("valor invalido, por favor ingresa un numero mayor a 0:")
        else:
            break
    except ValueError:
        print("por favor ingresa un valor valido ")

# Se calcula el costo total 
costo_total=(precio*cantidad)
print(f"el costo total es de: ${costo_total:,.0f}")

# Se hace un resumen visual en que el se muestran todos los resultados
print(f"producto: {nombre} | precio: {precio:,.0f} | cantidad: {cantidad} | total: {costo_total:,.0f}")


# programa sencillo en el cual se solicitan datos como nombre, precio y la cantidad de un producto
# y calcula el costo total de un producto     













