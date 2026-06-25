# Cómo publicar el sitio en GitHub Pages

Este repositorio ya trae todo lo necesario para verse como un sitio web navegable, con barra lateral y buscador, usando Docsify (no requiere compilación). Los archivos `index.html`, `_sidebar.md` y `.nojekyll` ya están en la raíz.

## Pasos

1. Sube el repositorio a GitHub (si aún no lo has hecho).
2. En `index.html`, cambia la línea `repo: 'TU-USUARIO/TU-REPO'` por la ruta real de tu repositorio (por ejemplo, `tunombre/estado-en-el-territorio`). Eso solo agrega el enlace "ver en GitHub"; no es obligatorio.
3. En tu repositorio, entra a **Settings**.
4. En la barra lateral, sección "Code and automation", haz clic en **Pages**.
5. En "Build and deployment", en "Source", elige **Deploy from a branch**.
6. En "Branch", elige la rama `main` y la carpeta `/ (root)`. Guarda con **Save**.
7. Espera unos minutos. Tu sitio quedará en `https://TU-USUARIO.github.io/TU-REPO/`.

## Por qué Docsify y no Jekyll

GitHub Pages, por defecto, procesa el repositorio con Jekyll y convierte cada archivo `.md` en `.html`. Eso rompería los enlaces internos del plan, que apuntan a archivos `.md`. Docsify, en cambio, sirve los `.md` directamente en el navegador, así que todos los enlaces funcionan sin tocar el contenido. El archivo `.nojekyll` (vacío) le indica a Pages que no use Jekyll, lo que también evita que ignore archivos que empiezan por guion bajo como `_sidebar.md`.

## Si ves un error 404 al principio

La primera publicación a veces tarda o falla. Suele resolverse esperando unos minutos o haciendo un commit adicional (incluso vacío) para forzar un nuevo despliegue.

## Cuando el sitio esté vivo

Pega la URL en el campo "About" del repositorio (el engranaje junto a la descripción) para que sea visible y fácil de compartir.

## Opción más pulida (futuro)

Si más adelante quieres un sitio con aspecto de documentación profesional (tema con modo claro/oscuro, búsqueda indexada), MkDocs con el tema Material es el estándar. Requiere un archivo `mkdocs.yml` y un flujo de GitHub Actions, y en Pages elegirías "Source: GitHub Actions" en lugar de "Deploy from a branch".
