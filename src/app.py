# Se importan funciones específicas desde otros módulos
from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, calcular_estadisticas
from archivos import guardar_csv, cargar_csv

# Se Crea la lista principal de inventario que almacenará diccionarios de productos
inventario = []

# Es el bucle principal del programa se ejecuta hasta que el usuario decida salir
while True:
    try:
        # El menú de opciones para el usuario
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

        # Se pide al usuario que seleccione una opción y convertimos la entrada a entero
        opcion = int(input("Por favor escoge la opcion que deseas realizar: "))

        # OPCIÓN 1: AGREGAR PRODUCTOS
        if opcion == 1:

            # Se solicita el nombre del producto
            nombre_del_producto = input("Por favor escribe el nombre del producto: ") 
            
            # Validación de que el precio del producto (debe ser número y no negativo)
            while True:
                try:
                    precio_del_producto = float(input("Por favor escribe el precio del producto: "))
                    if precio_del_producto < 0:
                        print("El precio no puede ser negativo. Intenta de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido. Por favor ingresa un número para el precio.")
            
            # Validación de que la cantidad del producto (debe ser número y no negativo)
            while True:
                try:
                    cantidad_del_producto = int(input("Por favor escribe la cantidad del producto: "))
                    if cantidad_del_producto < 0:
                        print("La cantidad no puede ser negativa. intenta de nuevo")
                        continue
                    break
                except ValueError:
                    print("Valor invalido. por favor ingresa un numero entero para la cantidad")

            # Verificamos si el producto ya existe en el inventario
            existente = buscar_producto(inventario, nombre_del_producto)
            if existente:
                # Si existe, sumamos la cantidad
                existente["cantidad"] += cantidad_del_producto
                # Si el precio difiere, lo actualizamos
                if existente["precio"] != precio_del_producto:
                    existente["precio"] = precio_del_producto
                print("Producto existente actualizado correctamente.\n")
            else:
                # Si no existe, agregamos el producto al inventario
                agregar_producto(inventario, nombre_del_producto, precio_del_producto, cantidad_del_producto)
                print("Producto agregado correctamente.\n")

        # OPCIÓN 2: MOSTRAR INVENTARIO
        elif opcion == 2:
            mostrar_inventario(inventario)

        # OPCIÓN 3: BUSCAR PRODUCTO
        elif opcion == 3:
            buscar_nombre = input("Ingresa el producto que deseas buscar: ")
            producto = buscar_producto(inventario, buscar_nombre)

            if producto:
                print("Se encontro el producto:")
                print(producto)  # Muestra el diccionario del producto
            else:
                print("No se encontro el producto")

        # OPCIÓN 4: ACTUALIZAR PRODUCTO
        elif opcion == 4:

            nombre = input("Por favor escribe el producto al cual deseas actualizar: ")

            # Se valida el nuevo precio
            while True:
                try:
                    nuevo_precio = float(input("Nuevo precio: "))
                    if nuevo_precio < 0:
                        print("El precio no puede ser negativo. Intenta de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido. Por favor ingresa un número para la cantidad.")

            # Se valida la nueva cantidad
            while True:
                try:
                    nueva_cantidad = int(input("Nueva cantidad: "))
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa. Intenta de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido. Por favor ingresa un número entero para la cantidad.")

            # Intentamos actualizar el producto
            actualizado = actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

            if actualizado:
                print("Se actualizo el producto correctamente")
            else:
                print("No se encontro el producto")

            mostrar_inventario(inventario)  # Mostramos el inventario actualizado

        # OPCIÓN 5: ELIMINAR PRODUCTO
        elif opcion == 5:
            nombre = input("Por escribe el producto que deseas eliminar: ")
            eliminado = eliminar_producto(inventario, nombre)

            if eliminado:
                print("Se ha eliminado el producto\n")
            else:
                print("No se ha encontrado el producto\n")

        # OPCIÓN 6: CALCULAR ESTADÍSTICAS
        elif opcion == 6:
            estadisticas = calcular_estadisticas(inventario)

            if estadisticas:
                # Mostramos estadísticas calculadas
                print(f"Unidades totales: {estadisticas['unidades_totales']}")
                print(f"Valor total: {estadisticas['valor_total']}")
                print(f"Producto mas caro: {estadisticas['producto_mas_caro']['nombre']} - {estadisticas['producto_mas_caro']['precio']}")
                print(f"Producto mayor stock: {estadisticas['producto_mayor_stock']['nombre']} - {estadisticas['producto_mayor_stock']['cantidad']}")
            else:
                print("Inventario vacio")

        # OPCIÓN 7: GUARDAR INVENTARIO EN CSV
        elif opcion == 7:
            ruta = input("Por escribe el nombre del archivo CSV (ej: nombre.csv): ")
            guardar_csv(inventario, ruta)

        # OPCIÓN 8: CARGAR INVENTARIO DESDE CSV
        elif opcion == 8:
            ruta = input("Ingresar el nombre del archivo CSV: ")
            datos_cargados, errores = cargar_csv(ruta)

            if not datos_cargados:
                print("No se cargaron productos desde el CSV.")
                continue

            # Limpiar duplicados en inventario actual
            inventario_limpio = {}
            for producto in inventario:
                key = producto["nombre"].lower().strip()
                if key in inventario_limpio:
                    inventario_limpio[key]["cantidad"] += producto["cantidad"]
                    if inventario_limpio[key]["precio"] != producto["precio"]:
                        inventario_limpio[key]["precio"] = producto["precio"]
                else:
                    inventario_limpio[key] = producto.copy()

            inventario.clear()
            inventario.extend(inventario_limpio.values())

            # Preguntamos al usuario si quiere sobrescribir o fusionar
            Decision = input("¿Deseas sobrescribir el inventario actual? (S/N): ").upper()

            if Decision == "S":
                inventario.clear()
                inventario.extend(datos_cargados)
                print("Se sobreescribió el inventario correctamente")
                print("Acción: Remplazo")

            elif Decision == "N":
                # Fusión usando el diccionario temporal
                temp_dict = {}
                for producto in inventario:
                    key = producto["nombre"].lower().strip()
                    temp_dict[key] = producto.copy()
                for producto_csv in datos_cargados:
                    key = producto_csv["nombre"].lower().strip()
                    if key in temp_dict:
                        temp_dict[key]["cantidad"] += producto_csv["cantidad"]
                        if temp_dict[key]["precio"] != producto_csv["precio"]:
                            temp_dict[key]["precio"] = producto_csv["precio"]
                    else:
                        temp_dict[key] = producto_csv.copy()

                # Actualizamos inventario final
                inventario.clear()
                inventario.extend(temp_dict.values())
                print("Se ha fusionado correctamente")
                print("Acción: Fusión")

            # Mostramos resumen de la carga
            print(f"Productos cargados: {len(datos_cargados)}")
            print(f"Filas inválidas: {errores}")

        # OPCIÓN 9: SALIR DEL PROGRAMA
        elif opcion == 9:
            break
        
        # Opción inválida
        else:
            print("Opcion invalidad, por favor ingresa una de las opciones disponibles\n")
    
    except ValueError:
        # Captura errores si el usuario no ingresa un número al elegir opción
        print("Valor invalido, por favor ingresa una de las opciones disponibles\n")