inventario = []

while True:
    try:
        print("····Menu····")
        print("1. Agregar Productos")
        print("2. Mostrar Inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        opcion = int(input("Por favor escoge de las opciones cuales deseas realizar: "))


        if opcion == 1:
                nombre_del_producto = input("Por favor escribe el nombre del producto: ")
                precio_del_producto = float(input("Por favor escribe el precio del producto: "))
                Cantidad_del_producto = int(input("Por favor escribe la cantidad del producto: "))
                producto = {"nombre": nombre_del_producto,
                        "precio": precio_del_producto,
                        "cantidad": Cantidad_del_producto

                }
                inventario.append(producto)
                print("Producto agregado correctamente.")

        if opcion == 2:
                if len(inventario) == 0:
                    print("Inventario vacio.")
                else:
                    for producto in inventario:
                        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

        if opcion == 3:
                print("")

        if opcion == 4:
                
                break
            
    except ValueError:
        print("Valor invalido, por favor vuelva a ingresar una de las opciones disponibles")
    