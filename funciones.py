from errores import comprobarDescripcion, verificarPrecio, DescripcionVacia, PrecioNoValido
def añadirGasto(descripcion, precio, gastos):
        try:
            comprobarDescripcion(descripcion)
            precioBueno = float(precio)
            verificarPrecio(precioBueno)
            gasto = {"descripcion": descripcion.strip(), "precio": precioBueno}
            gastos.append(gasto)
        except DescripcionVacia as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: El precio debe ser un número entero o decimal.")
        except PrecioNoValido as e:
            print(f"Error: {e}")
            
def verGastos(gastos):
    print("========== GASTOS ==========")
    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. {gasto['descripcion']} - {gasto['precio']:.2f}€")
        
def totalGastos(gastos):
    total = 0
    print("Has elegido ver el total")
    for gasto in gastos:
        total += gasto['precio']
    print(f"El total de gastos es: {total}€")