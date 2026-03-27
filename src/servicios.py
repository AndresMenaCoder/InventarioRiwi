def agregar_producto(inventario,nombre,precio,cantidad):
    if precio < 0 or cantidad < 0:
        print("no se puede agregar un producto con precio o cantidad negativa")
        return False
    producto ={
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
        }
    inventario.append(producto)
    return True


def mostrar_inventario(inventario):
    if len(inventario) == 0:
                print("Inventario vacio.\n")
    else:
        for producto in inventario:
                        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}\n")


def buscar_producto(inventario,nombre):
    for producto in inventario:
        if producto["nombre"].lower().strip() == nombre.lower().strip():
            return producto
    return None


def actualizar_producto(inventario,nombre,nuevo_precio=None,nueva_cantidad=None):
    
    for producto in inventario:
        if producto ["nombre"].lower().strip() == nombre.lower().strip():
            
            if nuevo_precio is not None:
                producto["precio"] = nuevo_precio
            if nueva_cantidad is not None:
                producto["cantidad"] = nueva_cantidad
            return True
        
    return False


def eliminar_producto (inventario,nombre):
    for producto in inventario:
        if producto ["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            return True
        
    return False

def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        return None
    
    unidades_totales = 0
    valor_total = 0 
    
    subtotal = (lambda p: p["precio"] * p["cantidad"])
    
    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]
    
    for producto in inventario:
        
        
        unidades_totales += producto["cantidad"]
        valor_total += subtotal(producto)
        
        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto
        
        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto
    
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    } 

