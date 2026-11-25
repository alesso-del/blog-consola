from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu, pedir_texto, pedir_datos_post
from blog.modelos import Blog
from blog.operaciones import mostrar_posts


def ejecutar():
    blog = Blog(cargar_posts())
    print("Usa la opción 6 para guardar los cambios antes de salir.")
    while True:
        opcion = mostrar_menu()
        if opcion is None:
            continue
        if opcion == 1:
            mostrar_posts(blog.listar_posts())
        elif opcion == 2:
            termino = pedir_texto("Buscar por titulo: ")
            if termino is not None:
                mostrar_posts(blog.buscar_por_titulo(termino))
        elif opcion == 3:
            tag = pedir_texto("Tag para filtrar: ")
            if tag is not None:
                mostrar_posts(blog.filtrar_por_tag(tag))
        elif opcion == 4:
            datos = pedir_datos_post()
            if datos is not None:
                try:
                    post = blog.crear_post(**datos)
                    print(f"Post {post.id} creado. Usa la opción 6 para guardarlo.")
                except ValueError as exc:
                    print(f"No se creó el post: {exc}.")
        elif opcion == 5:
            resultados = blog.validar_posts()
            if not resultados:
                print("No hay posts para validar.")
            for id_post, error in resultados:
                if error:
                    print(f"Post {id_post}: error - {error}")
                else:
                    print(f"Post {id_post}: válido")
        elif opcion == 6:
            guardar_posts(blog)
        elif opcion == 7:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo")


if __name__ == "__main__":
    ejecutar()
