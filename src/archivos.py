import csv

def guardar_csv(inventario,ruta,incluir_header = True):
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return

    with open(ruta,mode="w",newline="",encoding="utf-8")as archivo:
        write = csv.writer(archivo)
    if incluir_header:
        write.writerow(["nombre","precio","cantidad"])
        
    