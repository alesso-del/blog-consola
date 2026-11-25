# Blog por consola

Autor: Alessandro Del Valle.

Sistema de consulta de publicaciones en memoria. Continúa el programa de los módulos anteriores, separando datos, interacción, operaciones y validaciones. No utiliza archivos de persistencia, bases de datos ni dependencias externas.

## Requisitos y ejecución

Requiere Python 3. Descarga el repositorio y abre una terminal en la carpeta que contiene `main.py` y la carpeta `blog/`. Ejecuta:

```bash
python main.py
```

Si tu sistema utiliza el comando `python3`, ejecuta `python3 main.py`.

El archivo de inicio es `main.py`. No ejecutes por separado los archivos internos de `blog/`.

## Organización del proyecto

| Archivo | Responsabilidad |
| --- | --- |
| `main.py` | Importar las piezas y coordinar el bucle principal. |
| `blog/__init__.py` | Identificar `blog` como paquete. Está vacío intencionalmente. |
| `blog/datos.py` | Definir `perfil_autor`, `estados_post`, `etiquetas_blog` y `posts`. |
| `blog/menu.py` | Mostrar el menú y capturar la opción y los textos del usuario. |
| `blog/operaciones.py` | Listar publicaciones, buscar por título y filtrar por tag. |
| `blog/validaciones.py` | Revisar campos, tipos y estados; informar errores de los posts. |

Los datos no importan otros módulos. Las validaciones utilizan los estados definidos en los datos; las operaciones utilizan las validaciones. `main.py` coordina el conjunto, sin imports circulares.

## Opciones del menú

1. Ver todos los posts: muestra título, nombre del autor y estado de los registros válidos. Si un registro es inválido, informa su error.
2. Buscar por título: acepta una palabra o fragmento, ignorando mayúsculas y minúsculas.
3. Filtrar por tag: busca una etiqueta completa, ignorando mayúsculas y minúsculas.
4. Validar posts: indica cuáles son válidos y cuál es el primer error encontrado en los demás.
5. Salir: muestra una despedida y termina el programa.

Las búsquedas y los filtros excluyen los posts inválidos. Los términos vacíos y las opciones no numéricas o fuera de rango muestran un aviso y permiten continuar.

## Datos y prueba manual

Se conservan los tres posts de las entregas anteriores y se incluye un cuarto post sin `contenido` intencionalmente. Cada post reutiliza el mismo diccionario `perfil_autor`.

Para probar:

- Usa la opción 1: los tres primeros posts deben mostrar a Alessandro Del Valle y sus estados; el cuarto debe indicar que falta `contenido`.
- Busca `PYTHON` con la opción 2: debe aparecer «Primeros pasos con Python».
- Filtra `wEb` con la opción 3: debe aparecer el post sobre Django.
- Usa la opción 4: los posts 1, 2 y 3 deben ser válidos y el cuarto debe mostrar el error intencional.
- Prueba una búsqueda inexistente, un término vacío, texto en el menú y una opción fuera de rango: el programa debe informar el problema y continuar.
- Usa la opción 5 para salir.
