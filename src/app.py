from servicios import agregar_producto , mostrar_inventario , buscar_producto , actualizar_producto , eliminar_producto , calcular_estadisticas
from archivos import guardar_csv , cargar_csv

inventario = []


while True:
    try:
        print("············Menu············")
        print("1. Agregar Productos")
        print("2. Mostrar Inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Calcular estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir\n")
        print("·····························\n")

        opcion = int(input("Por favor escoge la opcion que deseas realizar: "))

        if opcion == 1:

            nombre_del_producto = input("Por favor escribe el nombre del producto: ") 
            precio_del_producto = float(input("Por favor escribe el precio del producto: "))
            Cantidad_del_producto = int(input("Por favor escribe la cantidad del producto: "))

            agregar_producto(inventario,nombre_del_producto,precio_del_producto,Cantidad_del_producto)

            print("Producto agregado correctamente.\n")

        elif opcion == 2:

            mostrar_inventario(inventario)

        elif opcion == 3:
            buscar_nombre = input("Ingresa el producto que deseas buscar: ")

            producto = buscar_producto(inventario,buscar_nombre)

            if producto:
                print("Se encontro el producto:")
                print(producto)
            else:
                print("No se encontro el producto")

        elif opcion == 4:

            nombre = input("Por favor escribe el producto al cual deseas actualizar: ")
            nuevo_precio = float(input("Nuevo precio: "))
            nueva_cantidad = int(input("Nueva cantidad: "))

            actualizado = actualizar_producto(inventario,nombre,nuevo_precio,nueva_cantidad)

            if actualizado:
                print("Se actualizo el producto correctamente")
            else:
                print("No se encontro el producto")

            mostrar_inventario(inventario)

        elif opcion == 5:
            nombre = input("Por escribe el producto que deseas eliminar: ")

            eliminado = eliminar_producto(inventario,nombre)

            if eliminado:
                print("Se ha eliminado el producto\n")
            else:
                print("No se ha encontrado el producto\n")

        elif opcion == 6:
            estadisticas = calcular_estadisticas(inventario)

            if estadisticas:
                print(f"Unidades totales: {estadisticas['unidades_totales']}")
                print(f"Valor total: {estadisticas['valor_total']}")
                print(f"Producto mas caro: {estadisticas['producto_mas_caro']['nombre']} - {estadisticas['producto_mas_caro']['precio']}")
                print(f"Producto mayor stock: {estadisticas['producto_mayor_stock']['nombre']} - {estadisticas['producto_mayor_stock']['cantidad']}")
            else:
                print("Inventario vacio")

        elif opcion == 7:

            ruta = input("Por escribe el nombre del archivo CSV (ej: nombre.csv): ")
            guardar_csv(inventario,ruta)

        elif opcion == 8:


            ruta = input("Ingresar el nombre del archivo CSV: ")
            datos_cargados,errores = cargar_csv(ruta)
            opcion = input("¿Deseas sobrescribir el inventario actual? (S/N): ").upper()
            print("opcion elegida",opcion)

            if opcion == "S":
                inventario = datos_cargados
                print("Se sobreescribio el inventario correctamente")
                print("Accion: Remplazo")
            
            elif opcion == "N":
                for producto in datos_cargados:
                    existente = buscar_producto(inventario,producto["nombre"])

                    if existente:
                        existente["cantidad"] += producto["cantidad"]
                        existente["precio"] += producto["precio"]
                    else:
                        inventario.append(producto)
                print("Se ha fusionado correctamente")
                print("Accion: Fusion")
                

            print(f"Productos cargados: {len(datos_cargados)}")
            print(f"Filas invalidas: {errores}")

        elif opcion == 9:
            break
        
        else:
            print("Opcion invalidad, por favor ingresa una de las opciones disponibles\n")
    
    except ValueError:
        print("Valor invalido, por favor ingresa una de las opciones disponibles\n")