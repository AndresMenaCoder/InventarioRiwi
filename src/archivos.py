import csv

def guardar_csv(inventario,ruta,incluir_header = True):
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return

    try:
        with open(ruta,mode="w",newline="",encoding="utf-8")as archivo:
            writer = csv.writer(archivo)
            if incluir_header:
                writer.writerow(["nombre","precio","cantidad"])
            for producto in inventario:
                writer.writerow([
                
                producto["nombre"],
                producto["precio"],
                producto["cantidad"]      
    ])
        print(f"Inventario guardado en: {ruta}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def cargar_csv(ruta):
    inventario = []
    try: 
        with open(ruta,mode="r",encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            encabezado = next(reader)
            
            if encabezado != ["nombre","precio","cantidad"]:
                print("encabezado invalido")
                return [],0
            
            errores = 0
            
            for fila in reader:
                if len(fila) != 3:
                    print("fila invalida")
                    continue
                
                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    
                    producto = {
                        
                        "nombre":nombre,
                        "precio":precio,
                        "cantidad":cantidad
                    }
                    
                    inventario.append(producto)
                    
                except ValueError:
                    print("Error en los datos")
                    errores += 1
                    continue
            
            print(f"{errores} filas invalidas omitidas")
            return inventario , errores
    
    except FileNotFoundError:
        print("Este archivo no existe")
        return [],0
    
    except UnicodeDecodeError:
        print("Error de codificacion del archivo")
        return [],0
    
    except Exception as e:
        print(f"Error inesperado: {e}")
        return [],0