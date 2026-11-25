# Blog por consola con objetos y JSON

Autor: Alessandro Del Valle.

Continuación del proyecto modular del Módulo 5. Esta versión usa Programación Orientada a Objetos y persistencia en `posts.json`. No necesita dependencias externas ni una base de datos.

## Ejecutar

Requiere Python 3. Descarga el repositorio y abre una terminal en la carpeta que contiene `main.py`:

```bash
python main.py
```

Si tu sistema usa `python3`, ejecuta `python3 main.py`.

## Clases principales

- **Autor:** guarda nombre, biografía, especialidad y redes sociales. `a_dict()` lo convierte a un diccionario y `desde_dict()` reconstruye el objeto.
- **Post:** guarda id, título, contenido, categoría, tags y estado. Su atributo `autor` es un objeto `Autor`. Convierte también el autor al serializar y lo reconstruye al cargar.
- **Blog:** contiene una lista de objetos `Post`. Sus métodos centralizan listado, búsqueda por título, filtrado por tag, creación y validación. Asigna a cada nuevo post un id superior al mayor id cargado, y rechaza ids repetidos.

## Organización

| Archivo | Responsabilidad |
| --- | --- |
| `main.py` | Cargar los datos, crear un objeto `Blog` y coordinar el menú. |
| `posts.json` | Guardar los posts como una lista de diccionarios compatibles con JSON. |
| `blog/__init__.py` | Identificar el paquete. Está vacío intencionalmente. |
| `blog/modelos.py` | Definir `Autor`, `Post` y `Blog`, sus métodos y conversiones. |
| `blog/datos.py` | Cargar y guardar JSON, reconstruyendo objetos y atendiendo errores de archivo. |
| `blog/menu.py` | Mostrar el menú y solicitar datos del usuario. |
| `blog/operaciones.py` | Presentar los objetos `Post` en consola. |
| `blog/validaciones.py` | Comprobar claves, tipos, textos obligatorios, autor, tags y estados. |

Las validaciones no importan otros módulos del paquete. Los modelos usan las validaciones, y la persistencia usa los modelos. No hay imports circulares. Importar `main.py` no inicia el menú.

## Menú

1. Ver todos los posts: título, autor y estado.
2. Buscar por título: coincidencia parcial, sin distinguir mayúsculas.
3. Filtrar por tag: etiqueta completa, sin distinguir mayúsculas.
4. Crear nuevo post: solicita título, contenido, nombre del autor, categoría, tags separados por comas y estado.
5. Validar posts: muestra si cada objeto tiene datos correctos.
6. Guardar posts en JSON: escribe los cambios actuales.
7. Salir: termina el programa.

**El guardado es manual. Usa la opción 6 antes de salir si quieres conservar los cambios.** Una creación rechazada o cancelada no agrega un post al blog.

## Carga y guardado

Al iniciar, `cargar_posts()` lee `posts.json`, comprueba que contenga una lista y convierte cada registro con `Post.desde_dict()`. Este método crea también un `Autor`. Los objetos válidos se entregan a `Blog`.

Al guardar, `Blog.a_lista_dict()` convierte cada `Post` y su `Autor` a diccionarios; después `json.dumps()` genera texto JSON. Se usa UTF-8 y `ensure_ascii=False` para conservar acentos. Los objetos personalizados no se entregan directamente al serializador.

La ruta se obtiene a partir de la ubicación de `blog/datos.py`: el archivo de datos se encuentra en la raíz del proyecto.

Si el archivo no existe, está vacío, tiene JSON mal formado o una estructura principal incorrecta, se muestra un mensaje y el blog inicia vacío. Los registros incompletos, de tipos incorrectos o con ids duplicados se omiten con una explicación. Los problemas de lectura y escritura se informan sin cerrar inesperadamente el programa. La carga no modifica el archivo original; guardar con la opción 6 reemplaza su contenido por los posts actuales.

## Continuidad con la entrega anterior

Se mantienen los tres posts válidos de las preentregas anteriores, ahora como datos iniciales en JSON. El cuarto registro incompleto era una prueba de validación; no forma parte de los datos iniciales válidos. Esta versión rechaza o informa los registros incompletos durante la carga o creación.

Las funciones de búsqueda y filtrado se transformaron en métodos de `Blog`. El menú se amplió para crear posts y guardarlos. Se añadió `blog/modelos.py` y `blog/datos.py` pasó a gestionar persistencia, en lugar de definir una lista global como fuente principal.

## Prueba de persistencia

1. Ejecuta `python main.py` y lista los tres posts iniciales.
2. Busca `PYTHON` o filtra por `wEb` para comprobar las comparaciones.
3. Elige la opción 4 y completa los campos. Estados permitidos: `borrador`, `publicado`, `archivado`.
4. Usa la opción 6 para guardar y la opción 7 para salir.
5. Vuelve a ejecutar el programa: el post creado debe aparecer en la opción 1 y en las búsquedas que coincidan.
6. Prueba texto u opciones inexistentes en el menú y campos vacíos: debe aparecer un aviso y continuar.

Para probar errores de carga, usa una copia del proyecto y renombra temporalmente `posts.json`, déjalo vacío o coloca JSON inválido. El sistema debe informar el caso y permitir crear posts. Restaura la copia de los datos después de la prueba.
