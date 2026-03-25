def agregar_producto(inventario,nombre,precio,cantidad):
    producto ={
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
    }

    inventario.append(producto)

print("Producto agregado correctamente.\n")

def mostrar_inventario(inventario):
    if len(inventario) == 0:
                print("Inventario vacio.\n")
    else:
        for producto in inventario:
                        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")