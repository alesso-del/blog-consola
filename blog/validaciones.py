estados_post = ("borrador", "publicado", "archivado")


def error_post(post):
    """Revisa la representación en diccionario de un post."""
    if not isinstance(post, dict):
        return "el post debe ser un diccionario"
    for clave in ("id", "titulo", "contenido", "autor", "tags", "estado"):
        if clave not in post:
            return f"falta la clave '{clave}'"
    if type(post.get("id")) is not int or post["id"] <= 0:
        return "el id debe ser un entero positivo"
    for campo in ("titulo", "contenido"):
        valor = post.get(campo)
        if not isinstance(valor, str) or not valor.strip():
            return f"'{campo}' debe ser un texto no vacío"
    autor = post.get("autor")
    if not isinstance(autor, dict):
        return "el autor debe ser un diccionario"
    nombre = autor.get("nombre")
    if not isinstance(nombre, str) or not nombre.strip():
        return "el autor debe tener un nombre no vacío"
    tags = post.get("tags")
    if not isinstance(tags, list):
        return "tags debe ser una lista"
    for tag in tags:
        if not isinstance(tag, str) or not tag.strip():
            return "cada tag debe ser un texto no vacío"
    if post.get("estado") not in estados_post:
        return "el estado no pertenece a los estados permitidos"
    return None


def validar_post(post):
    return error_post(post) is None
