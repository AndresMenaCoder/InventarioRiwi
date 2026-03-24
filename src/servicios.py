def agregar_producto (inventario,nombre,precio,cantidad):
    producto ={
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
    }

    inventario.append(producto)

print("Producto agregado correctamente.\n")

inventario = []