class MayorDistintoCero(Exception):
    pass
def verificarPrecio(precio):
    if precio < 0 or precio == 0:
        raise MayorDistintoCero("El precio no puede ser menor o igual a 0.")
print("Bienvenido al gestor de gastos")
gastos = []
while True:
    print("\n==============================")
    print("GESTOR DE GASTOS")
    print("==============================")
    print("1. Añadir gasto")
    print("2. Ver gastos")
    print("3. Ver total")
    print("4. Salir")
    opcion = input("Seleccione 1, 2, 3 o 4 para continuar: ")
    match opcion:
        case "1":
            print("Has elegido añadir un gasto")
            descripcion = input("Describe brevemente el gasto: ")
            try:
                precio = input("Indica el precio del gasto: ")
                precioBueno = float(precio)
                verificarPrecio(precioBueno)
                gasto = {"descripcion": descripcion, "precio": precioBueno}
                gastos.append(gasto)
            except ValueError:
                print("Error: El precio debe ser un número entero o decimal.")
            except MayorDistintoCero as e:
                print(f"Error: {e}")
        case "2":
            print("========== GASTOS ==========")
            for i, gasto in enumerate(gastos, start=1):
                print(f"{i}. {gasto['descripcion']} - {gasto['precio']:.2f}€")
        case "3":
            total = 0
            print("Has elegido ver el total")
            for gasto in gastos:
                total += gasto['precio']
            print(f"El total de gastos es: {total}€")
        case "4":
            print("Gracias por usar el programa!")
            break
        case _:
            print("Opción no váldia. Selecciona 1, 2, 3 o 4.")

