from servicios import agregar_producto

inventario = []

nombre_del_producto = input("Por favor escribe el nombre del producto: ") 
precio_del_producto = float(input("Por favor escribe el precio del producto: "))
Cantidad_del_producto = int(input("Por favor escribe la cantidad del producto: "))

agregar_producto(inventario,nombre_del_producto,precio_del_producto,Cantidad_del_producto)
print(inventario)