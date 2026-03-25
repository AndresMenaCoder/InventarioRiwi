from servicios import agregar_producto , mostrar_inventario , buscar_producto

inventario = []

nombre_del_producto = input("Por favor escribe el nombre del producto: ") 
precio_del_producto = float(input("Por favor escribe el precio del producto: "))
Cantidad_del_producto = int(input("Por favor escribe la cantidad del producto: "))

agregar_producto(inventario,nombre_del_producto,precio_del_producto,Cantidad_del_producto)
print("Producto agregado correctamente.\n")


mostrar_inventario(inventario)

buscar_nombre = input("Ingresa el producto que deseas buscar: ")
producto = buscar_producto(inventario,buscar_nombre)

if producto:
    print("Se encontro el producto:")
    print(producto)
else:
    print("No se encontro el producto")