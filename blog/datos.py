import json
from pathlib import Path

from blog.modelos import Post

RUTA_POSTS = Path(__file__).resolve().parent.parent / "posts.json"


def cargar_posts(ruta=RUTA_POSTS):
    """Lee JSON y reconstruye objetos Post y Autor; omite registros inválidos."""
    ruta = Path(ruta)
    try:
        texto = ruta.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("No existe posts.json. El blog iniciará vacío.")
        return []
    except (OSError, UnicodeError) as exc:
        print(f"No se pudo leer el archivo: {exc}. El blog iniciará vacío.")
        return []
    if not texto.strip():
        print("posts.json está vacío. El blog iniciará vacío.")
        return []
    try:
        registros = json.loads(texto)
    except json.JSONDecodeError:
        print("posts.json contiene JSON inválido. El blog iniciará vacío.")
        return []
    if not isinstance(registros, list):
        print("El JSON debe contener una lista de posts. El blog iniciará vacío.")
        return []
    posts = []
    ids = set()
    for numero, datos in enumerate(registros, start=1):
        try:
            post = Post.desde_dict(datos)
            if post.id in ids:
                raise ValueError("id duplicado")
            posts.append(post)
            ids.add(post.id)
        except (ValueError, TypeError) as exc:
            print(f"Registro {numero} omitido: {exc}.")
    return posts


def guardar_posts(blog, ruta=RUTA_POSTS):
    """Convierte los objetos antes de abrir el archivo para escribir."""
    try:
        datos = blog.a_lista_dict()
        texto = json.dumps(datos, ensure_ascii=False, indent=4)
        Path(ruta).write_text(texto + "\n", encoding="utf-8")
    except (OSError, UnicodeError, ValueError, TypeError, AttributeError) as exc:
        print(f"No se pudieron guardar los posts: {exc}.")
        return False
    print("Posts guardados en JSON.")
    return True
