from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post, error_post


# El archivo principal coordina los módulos, sin duplicar sus funciones.
if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion is None:
            continue

        if opcion == 1:
            print("\nPosts disponibles:")
            listar_posts(posts)

        elif opcion == 2:
            termino = pedir_texto("Buscar por titulo: ")
            if termino is not None:
                listar_posts(buscar_por_titulo(posts, termino))

        elif opcion == 3:
            tag = pedir_texto("Tag para filtrar: ")
            if tag is not None:
                listar_posts(filtrar_por_tag(posts, tag))

        elif opcion == 4:
            print("\nValidación de posts:")
            for numero, post in enumerate(posts, start=1):
                if validar_post(post):
                    print(f"Post {numero}: válido")
                else:
                    print(f"Post {numero}: error - {error_post(post)}")

        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo")
