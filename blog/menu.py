from blog.modelos import Autor


def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")
    try:
        return int(input("Elige una opción: "))
    except ValueError:
        print("Debes ingresar un número.")
        return None
    except (EOFError, KeyboardInterrupt):
        print("\nFin de la entrada.")
        return 7


def pedir_texto(mensaje):
    try:
        texto = input(mensaje).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada cancelada.")
        return None
    if not texto:
        print("El campo no puede estar vacío.")
        return None
    return texto


def pedir_datos_post():
    # Un campo obligatorio vacío cancela esta creación y vuelve al menú.
    campos = {}
    for clave, mensaje in [
        ("titulo", "Título: "), ("contenido", "Contenido: "),
        ("nombre", "Nombre del autor: "), ("categoria", "Categoría: "),
        ("tags", "Tags separados por comas: "),
        ("estado", "Estado (borrador/publicado/archivado): "),
    ]:
        valor = pedir_texto(mensaje)
        if valor is None:
            return None
        campos[clave] = valor
    tags = [tag.strip() for tag in campos["tags"].split(",") if tag.strip()]
    if not tags:
        print("Debes indicar al menos un tag.")
        return None
    return {
        "titulo": campos["titulo"], "contenido": campos["contenido"],
        "autor": Autor(campos["nombre"]), "categoria": campos["categoria"],
        "tags": tags, "estado": campos["estado"].lower(),
    }
