def buscar_numero(lista, numero):
    """
    Devuelve el índice del número en la lista, o -1 si no existe.
    Usa .index() con manejo de excepciones.
    """
    try:
        indice = lista.index(numero)
        return indice
    except ValueError:
        return -1


def numeros_mayores(lista, umbral):
    """
    Devuelve una nueva lista con todos los números mayores que el umbral.
    Usa comprensión de listas.
    """
    return [numero for numero in lista if numero > umbral]


def promedio_lista(lista):
    """
    Calcula y devuelve el promedio de todos los elementos.
    Usa sum() y len() para simplificar el cálculo.
    """
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


def ordenar_lista(lista):
    """
    Ordena los números de menor a mayor y devuelve la lista ordenada.
    Usa sorted() para no modificar la lista original.
    """
    return sorted(lista)


def mostrar_lista(lista):
    """Muestra la lista actual de forma formateada"""
    print(f"\nLista actual: {lista}")


def menu_buscar(lista):
    """Menú para buscar un número"""
    print("\n--- BUSCAR NÚMERO ---")
    try:
        numero = int(input("Ingresa el número a buscar: "))
        indice = buscar_numero(lista, numero)
        
        if indice != -1:
            print(f"✓ El número {numero} se encuentra en el índice {indice}")
        else:
            print(f"✗ El número {numero} no existe en la lista")
    except ValueError:
        print("✗ Ingresa un número válido")


def menu_mayores(lista):
    """Menú para obtener números mayores a un umbral"""
    print("\n--- NÚMEROS MAYORES A UN UMBRAL ---")
    try:
        umbral = int(input("Ingresa el umbral: "))
        resultado = numeros_mayores(lista, umbral)
        
        if resultado:
            print(f"✓ Números mayores a {umbral}: {resultado}")
        else:
            print(f"✗ No hay números mayores a {umbral}")
    except ValueError:
        print("✗ Ingresa un número válido")


def menu_promedio(lista):
    """Menú para calcular el promedio"""
    print("\n--- CALCULAR PROMEDIO ---")
    prom = promedio_lista(lista)
    print(f"✓ El promedio de la lista es: {prom:.2f}")


def menu_ordenar(lista):
    """Menú para ordenar la lista"""
    print("\n--- ORDENAR LISTA ---")
    lista_ordenada = ordenar_lista(lista)
    print(f"✓ Lista ordenada: {lista_ordenada}")


def menu_principal():
    """Menú principal del programa"""
    # Lista inicial de números
    numeros = [12, 45, 78, 23, 56, 89, 34, 67]
    
    while True:
        mostrar_lista(numeros)
        print("\n========== OPERACIONES CON LISTAS ==========")
        print("1. Buscar número")
        print("2. Números mayores a un umbral")
        print("3. Calcular promedio")
        print("4. Ordenar lista")
        print("5. Salir")
        print("===========================================")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            menu_buscar(numeros)
        elif opcion == "2":
            menu_mayores(numeros)
        elif opcion == "3":
            menu_promedio(numeros)
        elif opcion == "4":
            menu_ordenar(numeros)
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        else:
            print("✗ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()
