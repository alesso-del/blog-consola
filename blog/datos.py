# Datos compartidos del blog.
perfil_autor = {
    "nombre": "Alessandro Del Valle",
    "bio": "Estudiante de marketing digital e inteligencia artificial que aprende Python.",
    "especialidad": "Tecnología y creación de contenido",
    "redes_sociales": ["LinkedIn", "Instagram"],
}

estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "Django", "Web", "Datos", "Python"}

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "Cómo empezar a programar con variables y colecciones en Python.",
        "autor": perfil_autor,
        "categoria": "Programación",
        "tags": ["Python"],
        "estado": estados_post[1],
    },
    {
        "id": 2,
        "titulo": "Qué es Django y para qué sirve",
        "contenido": "Django es un framework de Python para desarrollar aplicaciones web.",
        "autor": perfil_autor,
        "categoria": "Desarrollo web",
        "tags": ["Python", "Django", "Web"],
        "estado": estados_post[0],
    },
    {
        "id": 3,
        "titulo": "Organizar datos con listas y diccionarios",
        "contenido": "Las listas y los diccionarios permiten organizar los datos del blog.",
        "autor": perfil_autor,
        "categoria": "Estructuras de datos",
        "tags": ["Python", "Datos"],
        "estado": estados_post[2],
    },
    {
        # Falta contenido intencionalmente para probar la validación.
        "id": 4,
        "titulo": "Publicación de prueba incompleta",
        "autor": perfil_autor,
        "categoria": "Pruebas",
        "tags": ["Python"],
        "estado": estados_post[0],
    },
]
