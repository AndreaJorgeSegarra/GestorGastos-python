

from funciones import añadirGasto, verGastos, totalGastos
#Menú bienvenida
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
            precio = input("Indica el precio del gasto: ")
            añadirGasto(descripcion, precio, gastos)
            
        case "2":
            verGastos(gastos)
            
        case "3":
            totalGastos(gastos)
            
        case "4":
            print("Gracias por usar el programa!")
            break
        
        case _:
            print("Opción no válida. Selecciona 1, 2, 3 o 4.")

