def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    try:
        return int(input("Elige una opción: "))
    except ValueError:
        print("Debes ingresar un número.")
        return None


def pedir_texto(mensaje):
    # La captura de datos de consola se concentra en este módulo.
    texto = input(mensaje).strip()
    if not texto:
        print("El término no puede estar vacío.")
        return None
    return texto
