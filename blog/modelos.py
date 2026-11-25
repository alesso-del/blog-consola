from blog.validaciones import error_post


class Autor:
    def __init__(self, nombre, bio="", especialidad="", redes_sociales=None):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El autor debe tener un nombre no vacío.")
        if not isinstance(bio, str) or not isinstance(especialidad, str):
            raise ValueError("La biografía y especialidad deben ser textos.")
        if redes_sociales is None:
            redes_sociales = []
        if not isinstance(redes_sociales, list):
            raise ValueError("Las redes sociales deben ser una lista.")
        if any(not isinstance(red, str) for red in redes_sociales):
            raise ValueError("Cada red social debe ser un texto.")
        self.nombre = nombre.strip()
        self.bio = bio.strip()
        self.especialidad = especialidad.strip()
        self.redes_sociales = list(redes_sociales)

    def a_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": list(self.redes_sociales),
        }

    @classmethod
    def desde_dict(cls, datos):
        if not isinstance(datos, dict):
            raise ValueError("Los datos del autor deben ser un diccionario.")
        return cls(datos.get("nombre"), datos.get("bio", ""),
                   datos.get("especialidad", ""), datos.get("redes_sociales", []))


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado="borrador",
                 categoria="General"):
        if not isinstance(autor, Autor):
            raise ValueError("El autor del post debe ser una instancia de Autor.")
        datos = {"id": id, "titulo": titulo, "contenido": contenido,
                 "autor": autor.a_dict(), "tags": tags, "estado": estado}
        error = error_post(datos)
        if error:
            raise ValueError(error)
        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("La categoría debe ser un texto no vacío.")
        self.id = id
        self.titulo = titulo.strip()
        self.contenido = contenido.strip()
        self.autor = autor
        self.tags = [tag.strip() for tag in tags]
        self.estado = estado
        self.categoria = categoria.strip()

    def a_dict(self):
        if not isinstance(self.autor, Autor):
            raise ValueError("El autor del post debe ser una instancia de Autor.")
        return {
            "id": self.id, "titulo": self.titulo, "contenido": self.contenido,
            "autor": self.autor.a_dict(), "categoria": self.categoria,
            "tags": list(self.tags), "estado": self.estado,
        }

    @classmethod
    def desde_dict(cls, datos):
        error = error_post(datos)
        if error:
            raise ValueError(error)
        return cls(datos["id"], datos["titulo"], datos["contenido"],
                   Autor.desde_dict(datos["autor"]), datos["tags"],
                   datos["estado"], datos.get("categoria", "General"))


class Blog:
    def __init__(self, posts=None):
        self.posts = []
        for post in posts if posts is not None else []:
            self.agregar_post(post)

    def agregar_post(self, post):
        if not isinstance(post, Post):
            raise ValueError("Solo se pueden agregar objetos Post al blog.")
        error = error_post(post.a_dict())
        if error:
            raise ValueError(error)
        if any(actual.id == post.id for actual in self.posts):
            raise ValueError("Ya existe un post con ese id.")
        self.posts.append(post)

    def listar_posts(self):
        return list(self.posts)

    def buscar_por_titulo(self, termino):
        termino = termino.strip().lower()
        if not termino:
            return []
        return [post for post in self.posts if termino in post.titulo.lower()]

    def filtrar_por_tag(self, tag):
        tag = tag.strip().lower()
        if not tag:
            return []
        return [post for post in self.posts
                if any(tag == etiqueta.lower() for etiqueta in post.tags)]

    def crear_post(self, titulo, contenido, autor, tags, estado="borrador",
                   categoria="General"):
        nuevo_id = max((post.id for post in self.posts), default=0) + 1
        post = Post(nuevo_id, titulo, contenido, autor, tags, estado, categoria)
        self.agregar_post(post)
        return post

    def validar_posts(self):
        resultados = []
        for post in self.posts:
            try:
                error = error_post(post.a_dict())
            except (ValueError, TypeError, AttributeError) as exc:
                error = str(exc)
            resultados.append((post.id, error))
        return resultados

    def a_lista_dict(self):
        datos = []
        for post in self.posts:
            registro = post.a_dict()
            error = error_post(registro)
            if error:
                raise ValueError(f"Post {post.id}: {error}")
            datos.append(registro)
        return datos
