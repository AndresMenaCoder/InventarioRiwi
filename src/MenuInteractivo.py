inventario = []

while True:
    try:
        print("····Menu····")
        print("1. Agregar Productos")
        print("2. Mostrar Inventario")
        print("3. Calcular estadísticas")
        print("4. Salir\n")

        opcion = int(input("Por favor escoge de las opciones cuales deseas realizar: "))


        if opcion == 1:
                nombre_del_producto = input("Por favor escribe el nombre del producto: ")
                precio_del_producto = float(input("Por favor escribe el precio del producto: "))
                Cantidad_del_producto = int(input("Por favor escribe la cantidad del producto: "))
                producto = {    "nombre": nombre_del_producto,
                                "precio": precio_del_producto,
                                "cantidad": Cantidad_del_producto

                }
                inventario.append(producto)
                print("Producto agregado correctamente.\n")

        elif opcion == 2:
                if len(inventario) == 0:
                    print("Inventario vacio.\n")
                else:
                    for producto in inventario:
                        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}\n")

        elif opcion == 3:
                valor_total = 0
                cantidad_total= 0
                for productos in inventario:
                        valor_total += productos["precio"]* productos["cantidad"]
                        cantidad_total += productos["cantidad"]
                        
                
                print(f"el valor total es de: {valor_total}")
                print(f"la cantidad total es: {cantidad_total}\n")

        elif opcion == 4:
                
                break
        
        else:
                print("Opcion invalidad, por favor ingresa una de las opciones disponibles\n")
            

    except ValueError:
                print("Valor invalido, por favor vuelva a ingresar una de las opciones disponibles\n")

    