def agregar_contacto(directorio):
    """Agrega un nuevo contacto al directorio"""
    print("\n--- AGREGAR CONTACTO ---")
    nombre = input("Nombre del contacto: ").strip()
    
    # Verificar si el contacto ya existe
    if nombre in directorio:
        print(f"✗ El contacto '{nombre}' ya existe en el directorio.")
        return
    
    email = input("Email: ").strip()
    telefono = input("Teléfono: ").strip()
    ciudad = input("Ciudad: ").strip()
    
    # Crear la entrada en el diccionario principal
    directorio[nombre] = {
        "email": email,
        "telefono": telefono,
        "ciudad": ciudad
    }
    
    print(f"✓ Contacto '{nombre}' agregado exitosamente.")


def ver_todos_contactos(directorio):
    """Ver todos los contactos iterando con .items()"""
    if not directorio:
        print("\n✗ El directorio de contactos está vacío.")
        return
    
    print("\n--- DIRECTORIO DE CONTACTOS ---")
    print("=" * 70)
    
    # Iterar sobre el diccionario con .items()
    for nombre, datos in directorio.items():
        print(f"\nNombre: {nombre}")
        # Iterar sobre los campos del contacto
        for campo, valor in datos.items():
            campo_mayuscula = campo.capitalize()
            print(f"  {campo_mayuscula}: {valor}")
        print("-" * 70)


def buscar_por_nombre(directorio):
    """Busca un contacto por nombre usando .get()"""
    print("\n--- BUSCAR CONTACTO ---")
    nombre = input("Nombre a buscar: ").strip()
    
    # Usar .get() para evitar errores si no existe
    contacto = directorio.get(nombre)
    
    if contacto:
        print(f"\n✓ Contacto encontrado:")
        print(f"  Nombre: {nombre}")
        for campo, valor in contacto.items():
            campo_mayuscula = campo.capitalize()
            print(f"  {campo_mayuscula}: {valor}")
    else:
        print(f"✗ El contacto '{nombre}' no existe en el directorio.")


def actualizar_telefono(directorio):
    """Actualiza el teléfono de un contacto"""
    print("\n--- ACTUALIZAR TELÉFONO ---")
    nombre = input("Nombre del contacto: ").strip()
    
    # Verificar si el contacto existe using .get()
    contacto = directorio.get(nombre)
    
    if contacto:
        print(f"Teléfono actual: {contacto['telefono']}")
        nuevo_telefono = input("Nuevo teléfono: ").strip()
        
        # Acceder al diccionario anidado y actualizar el campo "teléfono"
        directorio[nombre]["telefono"] = nuevo_telefono
        print(f"✓ Teléfono de '{nombre}' actualizado exitosamente.")
    else:
        print(f"✗ El contacto '{nombre}' no existe en el directorio.")


def eliminar_contacto(directorio):
    """Elimina un contacto del directorio usando .pop()"""
    print("\n--- ELIMINAR CONTACTO ---")
    nombre = input("Nombre del contacto a eliminar: ").strip()
    
    # Usar .pop() para eliminar la entrada completa
    contacto_eliminado = directorio.pop(nombre, None)
    
    if contacto_eliminado:
        print(f"✓ Contacto '{nombre}' eliminado exitosamente.")
    else:
        print(f"✗ El contacto '{nombre}' no existe en el directorio.")


def menu_principal():
    """Menú principal del directorio de contactos"""
    directorio = {}
    
    while True:
        print("\n========== DIRECTORIO DE CONTACTOS ==========")
        print("1. Agregar contacto")
        print("2. Ver todos los contactos")
        print("3. Buscar por nombre")
        print("4. Actualizar teléfono")
        print("5. Eliminar contacto")
        print("6. Salir")
        print("=============================================")
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "1":
            agregar_contacto(directorio)
        elif opcion == "2":
            ver_todos_contactos(directorio)
        elif opcion == "3":
            buscar_por_nombre(directorio)
        elif opcion == "4":
            actualizar_telefono(directorio)
        elif opcion == "5":
            eliminar_contacto(directorio)
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("Error: Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()
