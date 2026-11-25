from blog.validaciones import error_post, validar_post


def listar_posts(lista):
    if not lista:
        print("No hay posts para mostrar.")
        return
    for numero, post in enumerate(lista, start=1):
        if validar_post(post):
            print(
                f"- {post['titulo']} | Autor: {post['autor']['nombre']}"
                f" | Estado: {post['estado']}"
            )
        else:
            print(f"- Registro {numero}: error - {error_post(post)}")


def buscar_por_titulo(lista, termino):
    termino = termino.strip().lower()
    resultados = []
    if not termino:
        print("La búsqueda no puede estar vacía.")
        return resultados
    for post in lista:
        if validar_post(post) and termino in post.get("titulo", "").lower():
            resultados.append(post)
    return resultados


def filtrar_por_tag(lista, tag):
    tag = tag.strip().lower()
    resultados = []
    if not tag:
        print("El tag no puede estar vacío.")
        return resultados
    for post in lista:
        if validar_post(post):
            for etiqueta in post.get("tags", []):
                if tag == etiqueta.lower():
                    resultados.append(post)
                    break
    return resultados
