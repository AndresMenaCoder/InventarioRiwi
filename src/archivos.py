# Importamos el módulo csv para manejar archivos CSV
import csv


# Función para guardar el inventario en un archivo CSV
def guardar_csv(inventario, ruta, incluir_header=True):
    # Verificamos si el inventario está vacío
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return  # Salimos de la función si no hay productos

    try:
        # Abrimos el archivo en modo escritura ('w'), con nueva línea vacía y codificación utf-8
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)  # Creamos un escritor CSV

            # Escribimos la fila de encabezado si se indica
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            # Escribimos cada producto en una fila
            for producto in inventario:
                writer.writerow([
                    producto["nombre"],
                    producto["precio"],
                    producto["cantidad"]
                ])

        print(f"Inventario guardado en: {ruta}")  # Confirmamos que se guardó el archivo

    except Exception as e:
        # Capturamos cualquier error inesperado al escribir el archivo
        print(f"Error al guardar el archivo: {e}")


# Función para cargar inventario desde un archivo CSV
def cargar_csv(ruta):
    inventario = []  # Lista donde almacenaremos los productos cargados

    try:
        # Abrimos el archivo en modo lectura
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)  # Creamos un lector CSV
            encabezado = next(reader)  # Leemos la primera fila (encabezado)

            # Validamos que el encabezado sea correcto
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("encabezado invalido")
                return [], 0  # Retornamos lista vacía y 0 errores

            errores = 0  # Contador de filas inválidas

            # Iteramos por cada fila del archivo
            for fila in reader:
                # Verificamos que la fila tenga exactamente 3 columnas
                if len(fila) != 3:
                    print("fila invalida")
                    errores += 1
                    continue  # Saltamos a la siguiente fila

                try:
                    # Convertimos los valores de precio y cantidad
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    # Creamos el diccionario del producto
                    producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    # Agregamos el producto a la lista de inventario
                    inventario.append(producto)

                except ValueError:
                    # Captura errores si los datos no se pueden convertir
                    print("Error en los datos")
                    errores += 1
                    continue

            # Mostramos cuántas filas inválidas se omitieron
            print(f"{errores} filas invalidas omitidas")
            return inventario, errores  # Retornamos el inventario cargado y la cantidad de errores

    except FileNotFoundError:
        # Capturamos si el archivo no existe
        print("Este archivo no existe")
        return [], 0

    except UnicodeDecodeError:
        # Capturamos errores de codificación
        print("Error de codificacion del archivo")
        return [], 0

    except Exception as e:
        # Capturamos cualquier otro error inesperado
        print(f"Error inesperado: {e}")
        return [], 0