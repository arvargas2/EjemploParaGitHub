canciones_list = []  # BD


# ------- validadores ---------------------------
# Para el titulo y el artista
def validar_texto_vacio(texto):
    if len(texto.strip()) > 0:
        return True
    else:
        print("Error no puede ser vacio")
        return False


def validar_duracion(duracion):
    if duracion > 0:
        return True
    else:
        print("Error debe ser mayor a cero!!")
        return False


def imprimir_cancion(cancion):
    es_favorita = "Si" if cancion["favorita"] == True else "No"
    print(f"""
    ---------------------------
    Titulo: {cancion["titulo"]}
    Artista: {cancion["artista"]}      
    Duración: {cancion["duracion"]} seg
    Favorita: {es_favorita}   """)


# ------- transacciones ---------------------------
def agregar_cancion():
    titulo = str(input("Ingrese titulo:")).strip()
    while not validar_texto_vacio(titulo):
        titulo = str(input("Ingrese titulo:")).strip()

    artista = str(input("Ingrese artista:")).strip()
    while not validar_texto_vacio(artista):
        artista = str(input("Ingrese artista:")).strip()

    while True:
        try:
            duracion = int(input("Ingrese duración:"))
            while not validar_duracion(duracion):
                duracion = int(input("Ingrese duración:"))

            break
        except:
            print("Error deber ser un N°")}
    
    #--- armamos json cancion ------------------
    cancion = {
        "titulo" : titulo,
        "artista" : artista,
        "duracion" : duracion,
        "favorita" : False
    } 
    #----- agregamos el json a la lista -----
    canciones_list.append(cancion)
    print(" << registro almacenado >> ")
    

# ----------------------------------------------
def mostrar_canciones():
    if len(canciones_list) == 0:
        print("No hay datos cargados!!!!")
    else:
        for cancion in canciones_list:
            imprimir_cancion(cancion)        
