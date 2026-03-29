# Funcion para agregar un producto
def agregar_producto():

# Se le piden los datos sobre el producto al usuario
        nombre_del_producto = input("Por favor escribe el nombre del producto: ") 
        precio_del_producto = float(input("Por favor escribe el precio del producto: "))
        Cantidad_del_producto = int(input("Por favor escribe la cantidad del producto: "))
        
# Se crea un diccionario para representar el producto
        producto = {    "nombre": nombre_del_producto,
                        "precio": precio_del_producto,
                        "cantidad": Cantidad_del_producto
        }
# Se agrega el producto en el inventario 
        inventario.append(producto)

# El sistema notifica que se ha agregado el producto correctamente
        print("Producto agregado correctamente.\n")

# Funcion para mostrar un producto
def mostrar_productos():

# Verifica si el inventario esta vacio
        if len(inventario) == 0:
                print("Inventario vacio.\n")
        else:
# Se recorre la lista y vizualiza los productos
                for producto in inventario:
                        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


# Funcion para calcular estadisticas
def calcular_estadisticas():

# Variables acumuladoras
        valor_total = 0
        cantidad_total= 0

# Se recorre el inventario para calcular:
# Valor total = (precio * cantidad)
# Cantidad total de productos
        for productos in inventario:
                valor_total += productos["precio"]* productos["cantidad"]
                cantidad_total += productos["cantidad"]

# Se visualiza los resultados 
        print(f"el valor total es de: {valor_total}")
        print(f"la cantidad total es: {cantidad_total}\n")





# Lista en la cual se guardan los productos
inventario = []

# Menu principal
# Bucle que  mantiene al sistema en ejecucion hasta que el usuario decida salir 
while True:
        try:
# Se visualizan las opciones al usuario
                print("····Menu····")
                print("1. Agregar Productos")
                print("2. Mostrar Inventario")
                print("3. Calcular estadísticas")
                print("4. Salir\n")

# Se solicita que el usuario seleccione una opcion
                opcion = int(input("Por favor escoge de las opciones cuales deseas realizar: "))


# Opciones disponibles
                if opcion == 1:
                        agregar_producto() 

                elif opcion == 2:
                        mostrar_productos()

                elif opcion == 3:
                        calcular_estadisticas()

                elif opcion == 4:
# Opcion para salir del programa
                        print("Saliendo del Sistema...")
                        break

# Se ejecuta si el usuario selecciona una opcion no disponible 
                else:
                        print("Opcion invalidad, por favor ingresa una de las opciones disponibles\n")

# Se ejecuta si el usuario ingresa un valor no numerico 
        except ValueError:
                print("Valor invalido, por favor vuelva a ingresar una de las opciones disponibles\n")

# ------------------------- COMENTARIO FINAL -------------------------
# El objetivo de este programa y de la semana era realizar un inventario que permitiera 
# Registrar valores como Nombre, precio y cantidad de productos para la gestion de un inventario
# Ademas de Visualizar el inventario, calcular el coste total de estos y
# la cantidad total de todos los productos registrados.