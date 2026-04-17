def agregar_articulo(lista_articulos):
    """Agrega un nuevo artículo a la lista de compras"""
    print("\n--- AGREGAR ARTÍCULO ---")
    producto = input("Nombre del producto: ")
    
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        
        if precio < 0 or cantidad < 0:
            print("Error: El precio y la cantidad deben ser positivos.")
            return
        
        # Crear diccionario del artículo
        articulo = {
            "producto": producto,
            "precio": precio,
            "cantidad": cantidad
        }
        
        # Agregar a la lista con append()
        lista_articulos.append(articulo)
        print(f"✓ Artículo '{producto}' agregado exitosamente.")
    
    except ValueError:
        print("Error: Ingrese valores válidos para precio (decimal) y cantidad (entero).")


def ver_lista(lista_articulos):
    """Ver lista de compras iterando con for e .items()"""
    if not lista_articulos:
        print("\n✗ La lista de compras está vacía.")
        return
    
    print("\n--- LISTA DE COMPRAS ---")
    print(f"{'#':<3} {'Producto':<20} {'Precio':<10} {'Cantidad':<10}")
    print("-" * 50)
    
    for i, articulo in enumerate(lista_articulos, 1):
        # Iterar sobre el diccionario con .items()
        for clave, valor in articulo.items():
            if clave == "producto":
                producto = valor
            elif clave == "precio":
                precio = valor
            elif clave == "cantidad":
                cantidad = valor
        
        print(f"{i:<3} {producto:<20} ${precio:<9.2f} {cantidad:<10}")
    
    print("-" * 50)


def calcular_total(lista_articulos):
    """Calcula el total acumulando precio × cantidad de cada artículo"""
    if not lista_articulos:
        print("\n✗ La lista de compras está vacía.")
        return 0
    
    print("\n--- CALCULAR TOTAL ---")
    total = 0
    
    for articulo in lista_articulos:
        # Acumular precio × cantidad para cada artículo
        subtotal = articulo["precio"] * articulo["cantidad"]
        total += subtotal
        print(f"{articulo['producto']}: ${articulo['precio']:.2f} × {articulo['cantidad']} = ${subtotal:.2f}")
    
    print("-" * 40)
    print(f"TOTAL A PAGAR: ${total:.2f}")
    
    return total


def eliminar_articulo(lista_articulos):
    """Elimina un artículo de la lista por nombre usando remove()"""
    if not lista_articulos:
        print("\n✗ La lista de compras está vacía.")
        return
    
    print("\n--- ELIMINAR ARTÍCULO ---")
    producto_buscar = input("Nombre del producto a eliminar: ")
    
    # Buscar el diccionario correspondiente
    articulo_encontrado = None
    for articulo in lista_articulos:
        if articulo["producto"].lower() == producto_buscar.lower():
            articulo_encontrado = articulo
            break
    
    if articulo_encontrado:
        # Usar remove() para borrarlo
        lista_articulos.remove(articulo_encontrado)
        print(f"✓ Artículo '{producto_buscar}' eliminado exitosamente.")
    else:
        print(f"✗ Producto '{producto_buscar}' no encontrado en la lista.")


def menu_principal():
    """Menú principal del gestor de compras"""
    lista_articulos = []
    
    while True:
        print("\n========== GESTOR DE COMPRAS ==========")
        print("1. Agregar artículo")
        print("2. Ver lista de compras")
        print("3. Calcular total")
        print("4. Eliminar artículo")
        print("5. Salir")
        print("=====================================")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            agregar_articulo(lista_articulos)
        elif opcion == "2":
            ver_lista(lista_articulos)
        elif opcion == "3":
            calcular_total(lista_articulos)
        elif opcion == "4":
            eliminar_articulo(lista_articulos)
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        else:
            print("Error: Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()
