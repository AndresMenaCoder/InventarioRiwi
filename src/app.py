from servicios import agregar_producto , mostrar_inventario , buscar_producto , actualizar_producto , eliminar_producto , calcular_estadisticas
from archivos import guardar_csv , cargar_csv

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

nombre = input("Por favor escribe el producto al cual deseas actualizar: ")
nuevo_precio = float(input("Nuevo precio: "))
nueva_cantidad = int(input("Nueva cantidad: "))

actualizado = actualizar_producto(inventario,nombre,nuevo_precio,nueva_cantidad)

if actualizado:
    print("Se actualizo el producto correctamente")
else:
    print("No se encontro el producto")

mostrar_inventario(inventario)

nombre = input("Por escribe el producto que deseas eliminar: ")

eliminado = eliminar_producto(inventario,nombre)

if eliminado:
    print("Se ha eliminado el producto\n")
else:
    print("No se ha encontrado el producto\n")


estadisticas = calcular_estadisticas(inventario)

if estadisticas:
    print(f"Unidades totales: {estadisticas['unidades_totales']}")
    print(f"Valor total: {estadisticas['valor_total']}")
    print(f"Producto mas caro: {estadisticas['producto_mas_caro']['nombre']} - {estadisticas['producto_mas_caro']['precio']}")
    print(f"Producto mayor stock: {estadisticas['producto_mayor_stock']['nombre']} - {estadisticas['producto_mayor_stock']['cantidad']}")
else:
    print("Inventario vacio")

ruta = input("Por escribe el nombre del archivo CSV (ej: nombre.csv): ")
guardar_csv(inventario,ruta) 


ruta = input("Ingresar el nombre del archivo CSV: ")
datos_cargados,errores = cargar_csv(ruta) 
opcion = input("¿Deseas sobrescribir el inventario actual? (S/N): ").upper()

if opcion == "S":
    inventario = datos_cargados
    print("Se sobreescribio el inventario correctamente")
    print("Accion: Remplazo")
elif opcion == "N":
    for producto in datos_cargados:
        existente = buscar_producto(inventario,producto["nombre"])

        if existente:
            existente["cantidad"] += producto["cantidad"]
            existente["precio"] = producto["precio"]
        else:
            inventario.append(producto)
    print("Se ha fusionado correctamente")
    print("Accion: Fusion")

print(f"Productos cargados: {len(datos_cargados)}")
print(f"Filas invalidas: {errores}")