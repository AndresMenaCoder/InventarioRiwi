# Función para agregar un producto al inventario
def agregar_producto(inventario, nombre, precio, cantidad):
    # Validación: precio y cantidad no pueden ser negativos
    if precio < 0 or cantidad < 0:
        print("no se puede agregar un producto con precio o cantidad negativa")
        return False  # Retornamos False si los datos son inválidos
    
    # Creamos un diccionario que representa el producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    # Agregamos el producto a la lista de inventario
    inventario.append(producto)
    return True  # Retornamos True indicando que el producto se agregó correctamente


# Función para mostrar todos los productos en el inventario
def mostrar_inventario(inventario):
    # Verificamos si el inventario está vacío
    if len(inventario) == 0:
        print("Inventario vacio.\n")
    else:
        # Iteramos por cada producto y mostramos sus datos
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}\n")


# Función para buscar un producto por su nombre
def buscar_producto(inventario, nombre):
    for producto in inventario:
        # Comparamos ignorando mayúsculas y espacios al inicio/final
        if producto["nombre"].lower().strip() == nombre.lower().strip():
            return producto  # Retornamos el producto si coincide
    return None  # Retornamos None si no se encontró


# Función para actualizar precio y/o cantidad de un producto
def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    for producto in inventario:
        # Buscamos el producto ignorando mayúsculas y espacios
        if producto["nombre"].lower().strip() == nombre.lower().strip():
            # Actualizamos el precio si se proporciona
            if nuevo_precio is not None:
                producto["precio"] = nuevo_precio
            # Actualizamos la cantidad si se proporciona
            if nueva_cantidad is not None:
                producto["cantidad"] = nueva_cantidad
            return True  # Producto actualizado correctamente
    return False  # Producto no encontrado


# Función para eliminar un producto del inventario
def eliminar_producto(inventario, nombre):
    for producto in inventario:
        # Comparamos nombre ignorando mayúsculas
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)  # Eliminamos el producto
            return True  # Producto eliminado correctamente
    return False  # Producto no encontrado


# Función para calcular estadísticas del inventario
def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        return None  # Retornamos None si el inventario está vacío

    unidades_totales = 0  # Total de unidades en inventario
    valor_total = 0       # Valor monetario total del inventario

    # Función lambda para calcular subtotal de un producto (precio * cantidad)
    subtotal = lambda p: p["precio"] * p["cantidad"]

    # Inicializamos productos más caro y mayor stock con el primero de la lista
    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    # Recorremos todos los productos para acumular estadísticas
    for producto in inventario:
        unidades_totales += producto["cantidad"]
        valor_total += subtotal(producto)

        # Verificamos si el producto actual es más caro que el registrado
        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        # Verificamos si el producto actual tiene mayor cantidad que el registrado
        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    # Retornamos un diccionario con todas las estadísticas calculadas
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
