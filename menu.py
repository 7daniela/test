import os


def limpiar():
    os.system("cls")


def menu():
    """Muestra un menú simple en consola y responde a la elección del usuario."""
    while True:
        limpiar()
        print("Menu")
        print("1. Saludar")
        print("2. Despedirse")
        print("3. Salir\n")
        opcion = int(input("Seleccione una opción: "))
        match opcion:
            case 1:
                limpiar()
                print("Hola")
                input("Presione enter para continuar")
            case 2:
                limpiar()
                print("Adios")
                input("Presione enter para continuar")
            case 3:
                limpiar()
                print("Saliendo del programa")
                break
            case _:
                limpiar()
                continue
menu()
        