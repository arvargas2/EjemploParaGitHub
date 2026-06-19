import os
import modulo_canciones as mc

# --------------------------------------------
opcion = ""

# --------------------------------------------
while True:
    os.system("cls")
    opcion = str(input("""
   ====== MENÚ PRINCIPAL ======
    1. Agregar canción
    2. Buscar canción
    3. Eliminar canción
    4. Marcar como favorita
    5. Mostrar canciones
    6. Salir
    ===========================                    
    Elija opción:   """)).strip()

    match (opcion):
        case "1":
            os.system("cls")
            mc.agregar_cancion()
            os.system("pause")

        case "2":
            os.system("cls")
            mc.mostrar_canciones()
            os.system("pause")

        case "3":
            os.system("cls")

            os.system("pause")

        case "4":
            os.system("cls")

            os.system("pause")

        case "5":
            os.system("cls")

            os.system("pause")

        case "6":
            print("Gracias por utilizar el sistema de gestión de canciones. Hasta pronto.")
            break

        case _:
            print("\n Error opción no valida!!!")
            os.system("pause")
