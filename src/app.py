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
            while True:
                try:
                    precio_del_producto = float(input("Por favor escribe el precio del producto: "))
                    if precio_del_producto < 0:
                        print("El precio no puede ser negativo. Intenta de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido. Por favor ingresa un número para el precio.")
                    
            while True:
                try:
                    cantidad_del_producto = int(input("Por favor escribe la cantidad del producto: "))
                    if cantidad_del_producto < 0:
                        print("La cantidad no puede ser negativa. intenta de nuevo")
                        continue
                    break
                except ValueError:
                    print("Valor invalido. por favor ingresa un numero entero para la cantidad")

            existente = buscar_producto(inventario, nombre_del_producto)
            if existente:
                # Sumar cantidades
                existente["cantidad"] += cantidad_del_producto
                # Actualizar precio si difiere
                if existente["precio"] != precio_del_producto:
                    existente["precio"] = precio_del_producto
                print("Producto existente actualizado correctamente.\n")
            else:
                # Agregar nuevo producto
                agregar_producto(inventario, nombre_del_producto, precio_del_producto, cantidad_del_producto)
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
            while True:
                try:
                    nuevo_precio = float(input("Nuevo precio: "))
                    if nuevo_precio < 0:
                        print("El precio no puede ser negativo. Intenta de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido. Por favor ingresa un número para el precio.")

            while True:
                try:
                    nueva_cantidad = int(input("Nueva cantidad: "))
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa. Intenta de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido. Por favor ingresa un número entero para la cantidad.")

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
    
            datos_cargados, errores = cargar_csv(ruta)
            
            if not datos_cargados:
                print("No se cargaron productos desde el CSV.")
                continue

            # Paso 1: limpiar duplicados en inventario actual
            inventario_limpio = {}
            for producto in inventario:
                key = producto["nombre"].lower().strip()
                if key in inventario_limpio:
                    # Sumar cantidades si hay duplicados
                    inventario_limpio[key]["cantidad"] += producto["cantidad"]
                    # Actualizar precio si difiere
                    if inventario_limpio[key]["precio"] != producto["precio"]:
                        inventario_limpio[key]["precio"] = producto["precio"]
                else:
                    inventario_limpio[key] = producto.copy()
            
            inventario.clear()
            inventario.extend(inventario_limpio.values())

            # Paso 2: decidir sobrescribir o fusionar
            Decision = input("¿Deseas sobrescribir el inventario actual? (S/N): ").upper()
            
            if Decision == "S":
                inventario.clear()
                inventario.extend(datos_cargados)
                print("Se sobreescribió el inventario correctamente")
                print("Acción: Remplazo")

            elif Decision == "N":
                # Fusión robusta usando diccionario temporal
                temp_dict = {}
                # Productos actuales
                for producto in inventario:
                    key = producto["nombre"].lower().strip()
                    temp_dict[key] = producto.copy()
                # Productos del CSV
                for producto_csv in datos_cargados:
                    key = producto_csv["nombre"].lower().strip()
                    if key in temp_dict:
                        temp_dict[key]["cantidad"] += producto_csv["cantidad"]
                        if temp_dict[key]["precio"] != producto_csv["precio"]:
                            temp_dict[key]["precio"] = producto_csv["precio"]
                    else:
                        temp_dict[key] = producto_csv.copy()

                # Actualizar inventario final
                inventario.clear()
                inventario.extend(temp_dict.values())

                print("Se ha fusionado correctamente")
                print("Acción: Fusión")
            
            print(f"Productos cargados: {len(datos_cargados)}")
            print(f"Filas inválidas: {errores}")
            
        elif opcion == 9:
            break
        
        else:
            print("Opcion invalidad, por favor ingresa una de las opciones disponibles\n")
    
    except ValueError:
        print("Valor invalido, por favor ingresa una de las opciones disponibles\n")