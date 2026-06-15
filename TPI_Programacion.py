# Tomas Aguirre
# Lis Sonnleintner
import csv


# Menú principal
def mostrar_menu():
    print(" GESTION DE PAISES ")
    print("1 - Agregar pais")
    print("2 - Actualizar pais")
    print("3 - Buscar pais")
    print("4 - Filtrar por continente")
    print("5 - Filtrar por poblacion")
    print("6 - Filtrar por superficie")
    print("7 - Ordenar por nombre")
    print("8 - Ordenar por poblacion")
    print("9 - Ordenar por superficie")
    print("10 - Mostrar estadisticas")
    print("0 - Salir")


# Cargar los paises desde el CSV de la otra carpeta
def cargar_paises(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }

                    paises.append(pais)

                except:
                    print("Error en una fila del CSV")

    except FileNotFoundError:
        print("No se encontro el archivo CSV")

    return paises


# Guarda los cambios en el CSV por si agregas otro pais
def guardar_csv(paises):

    with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:

        campos = ["nombre", "poblacion", "superficie", "continente"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)

    print("Datos guardados correctamente")


# Agrega un nuevo pais
def agregar_pais(paises):

    nombre = input("Nombre: ").strip()
    continente = input("Continente: ").strip()

    if nombre == "" or continente == "":
        print("No se permiten campos vacios")
        return

    try:

        poblacion = int(input("Poblacion: "))
        superficie = int(input("Superficie: "))

        nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }

        paises.append(nuevo_pais)

        print("Pais agregado correctamente")

    except:
        print("Error al ingresar datos")


# Actualiza la poblacion y la superficie
def actualizar_pais(paises):

    nombre = input("Nombre del pais: ").lower()

    for pais in paises:

        if pais["nombre"].lower() == nombre:

            try:

                pais["poblacion"] = int(input("Nueva poblacion: "))
                pais["superficie"] = int(input("Nueva superficie: "))

                print("Datos actualizados")

            except:
                print("Datos inválidos")

            return

    print("Pais no encontrado")


# Busca un pais por coincidencia parcial
def buscar_pais(paises):

    texto = input("Ingrese nombre a buscar: ").lower()

    encontrados = []

    for pais in paises:

        if texto in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron resultados")

    else:

        for pais in encontrados:
            print(pais)


# Filtra por continente
def filtrar_continente(paises):

    continente = input("Continente: ").lower()

    encontrados = []

    for pais in paises:

        if pais["continente"].lower() == continente:
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron paises")

    else:

        for pais in encontrados:
            print(pais)


# Filtra por rango de poblacion
def filtrar_poblacion(paises):

    try:

        minimo = int(input("Poblacion minima: "))
        maximo = int(input("Poblacion máxima: "))

        for pais in paises:

            if minimo <= pais["poblacion"] <= maximo:
                print(pais)

    except:
        print("Datos inválidos")


# Filtra por rango de superficie
def filtrar_superficie(paises):

    try:

        minimo = int(input("Superficie minima: "))
        maximo = int(input("Superficie máxima: "))

        for pais in paises:

            if minimo <= pais["superficie"] <= maximo:
                print(pais)

    except:
        print("Datos inválidos")


# Ordena por nombre
def ordenar_nombre(paises):

    ordenados = sorted(
        paises,
        key=lambda pais: pais["nombre"]
    )

    for pais in ordenados:
        print(pais)


# Ordena por poblacion
def ordenar_poblacion(paises):

    opcion = input("A Ascendente - D Descendente: ").upper()

    if opcion == "D":

        ordenados = sorted(
            paises,
            key=lambda pais: pais["poblacion"],
            reverse=True
        )

    else:

        ordenados = sorted(
            paises,
            key=lambda pais: pais["poblacion"]
        )

    for pais in ordenados:
        print(pais)


# Ordena por superficie
def ordenar_superficie(paises):

    opcion = input("A Ascendente - D Descendente: ").upper()

    if opcion == "D":

        ordenados = sorted(
            paises,
            key=lambda pais: pais["superficie"],
            reverse=True
        )

    else:

        ordenados = sorted(
            paises,
            key=lambda pais: pais["superficie"]
        )

    for pais in ordenados:
        print(pais)


# Muestra estadisticas generales
def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("No hay datos")
        return

    mayor = max(paises, key=lambda pais: pais["poblacion"])
    menor = min(paises, key=lambda pais: pais["poblacion"])

    promedio_poblacion = sum(pais["poblacion"] for pais in paises) / len(paises)
    promedio_superficie = sum(pais["superficie"] for pais in paises) / len(paises)

    continentes = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("ESTADISTICAS")
    print("Mayor poblacion:", mayor["nombre"])
    print("Menor poblacion:", menor["nombre"])
    print("Promedio poblacion:", round(promedio_poblacion, 2))
    print("Promedio superficie:", round(promedio_superficie, 2))

    print("Paises por continente")

    for clave, valor in continentes.items():
        print(clave, ":", valor)


# Funcion principal
def main():

    paises = cargar_paises("paises.csv")

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            buscar_pais(paises)

        elif opcion == "4":
            filtrar_continente(paises)

        elif opcion == "5":
            filtrar_poblacion(paises)

        elif opcion == "6":
            filtrar_superficie(paises)

        elif opcion == "7":
            ordenar_nombre(paises)

        elif opcion == "8":
            ordenar_poblacion(paises)

        elif opcion == "9":
            ordenar_superficie(paises)

        elif opcion == "10":
            mostrar_estadisticas(paises)

        elif opcion == "0":
            guardar_csv(paises)
            print("Programa finalizado")
            break

        else:
            print("Opcion inválida")


# Inicio del programa
main()