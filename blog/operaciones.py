def mostrar_posts(posts):
    """Presenta objetos Post; la búsqueda y el filtrado pertenecen a Blog."""
    if not posts:
        print("No hay posts para mostrar.")
        return
    for post in posts:
        print(f"- {post.titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")
