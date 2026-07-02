# Estado en el Territorio

**Un plan de gobierno para Colombia: abierto, versionado y de autor.**

> Empleo de calidad, instituciones honestas y carga justa.

Este repositorio contiene un plan de gobierno completo para Colombia. No es el manifiesto colaborativo de un partido ni una ley redactada por multitud: es **el ejercicio de un autor**, un experimento mental disciplinado sobre cómo se resolverían los problemas estructurales del país, publicado en abierto para que cualquiera lo lea, lo critique, lo corrija en su ejecución, lo cite o lo adapte.

Se publica en abierto por una razón simple: como no hay nada electoral que proteger, lo único en juego es si las ideas son buenas. Eso permite exponer el plan entero al escrutinio y dejar que la realidad lo corrija a la vista de todos.

---

## La tesis en una página

Casi todas las crisis grandes de Colombia cuelgan de **dos raíces**: (1) el Estado no controla ni sirve buena parte de su territorio, y (2) sus instituciones son débiles o capturadas y su fisco es frágil. Atacar síntomas sin tocar esas raíces es gastar sin resultado.

La respuesta es un **modelo de nodos**: concentrar y secuenciar el Estado en pocos municipios a la vez, seguridad + economía + servicios + instituciones + tierra desplegados juntos, expandiendo por **olas que dispara el resultado, no el calendario**. Todo el plan se sostiene en cuatro compromisos: honestidad fiscal, atacar raíces y no síntomas, contrapesos antes que confianza, y que la carga (en seguridad, impuestos y ajuste) nunca recaiga sobre los más pobres. Y usa **diseño de mecanismos** para que el plan funcione aun cuando algunos actores intenten capturarlo.

Esa tesis es el **núcleo** del proyecto y no se cambia por propuesta. Todo lo demás, cifras, vías jurídicas, secuencia, detalles, es **ejecución**, y está abierto a corrección con evidencia. La distinción se explica en [CONTRIBUTING.md](CONTRIBUTING.md) y [GOVERNANCE.md](GOVERNANCE.md).

---

## Cómo leerlo

El documento completo está partido en archivos por sección (la fuente de verdad). El documento consolidado en un solo archivo y el Word no se versionan: se *generan* con el build (ver más abajo) y se publican como artefactos y releases en GitHub. Para tenerlos en tu máquina, corre `./build.sh`.

### Fundamentos (núcleo)
1. [Visión Colombia 2042](docs/01-vision-2042.md), el horizonte de generación
2. [El Modelo de País](docs/02-modelo-de-pais.md), la brújula
3. [Diagnóstico: dos raíces](docs/03-diagnostico.md)
4. [Principios rectores](docs/04-principios.md)
5. [La Columna Vertebral: Estado en el territorio](docs/05-columna-vertebral.md), el modelo de nodos

### Los catorce frentes (ejecución)
- [I, Empleo de calidad](docs/frentes/frente-01-empleo.md)
- [II, Reforma agraria integral](docs/frentes/frente-02-reforma-agraria.md)
- [III, Seguridad, soberanía e inteligencia](docs/frentes/frente-03-seguridad.md)
- [IV, Anticorrupción](docs/frentes/frente-04-anticorrupcion.md)
- [V, Sostenibilidad fiscal](docs/frentes/frente-05-fiscal.md)
- [VI, Salud](docs/frentes/frente-06-salud.md)
- [VII, Educación](docs/frentes/frente-07-educacion.md)
- [VIII, Capacidad operativa del Estado](docs/frentes/frente-08-capacidad-estatal.md)
- [IX, Infraestructura estratégica](docs/frentes/frente-09-infraestructura.md)
- [X, Industria avanzada](docs/frentes/frente-10-industria.md)
- [XI, Piso universal de servicios básicos](docs/frentes/frente-11-servicios-basicos.md)
- [XII, Ciudades, turismo y productividad urbana](docs/frentes/frente-12-ciudades-turismo.md)
- [XIII, Integridad estructural y diseño de mecanismos](docs/frentes/frente-13-integridad-mecanismos.md)
- [XIV, Servicio Nacional de Vida](docs/frentes/frente-14-servicio-nacional.md)

### Secciones transversales
- [El rendimiento compuesto del modelo](docs/06-rendimiento-compuesto.md)
- [Viabilidad jurídica de los mecanismos](docs/transversal/viabilidad-juridica.md)
- [Cuadro fiscal de dos escenarios](docs/transversal/cuadro-fiscal.md)
- [Fundamentos en la investigación reciente](docs/transversal/fundamentos-investigacion.md)
- [Productividad y competitividad nacional](docs/transversal/productividad-competitividad.md)
- [Plataforma de trazabilidad del gasto](docs/transversal/plataforma-trazabilidad.md)
- [Comunicación pública y derecho a la información](docs/transversal/comunicacion-publica.md)

### Cierre
- [Secuencia de gobierno y transición](docs/cierre/secuencia-gobierno.md)
- [Medición y blindaje](docs/cierre/medicion-blindaje.md)
- [Riesgos y límites honestos](docs/cierre/riesgos-limites.md)
- [El patriotismo como resultado](docs/cierre/patriotismo.md)
- [Hitos de credibilidad](docs/cierre/hitos-credibilidad.md)

### Anexo
- [A, Colombia Viva](docs/anexos/anexo-a-colombia-viva.md) *(fuera del núcleo: idea a explorar)*

---

## Cómo contribuir

Cualquiera puede proponer. El modelo de gobernanza es el de un proyecto de código abierto con **maintainer**: el documento es público, cualquiera abre un *issue* o un *pull request*, pero hay un autor que decide qué se integra y custodia la coherencia de la visión.

- **Se reciben:** correcciones con evidencia, objeciones jurídicas o fiscales, datos territoriales, mejoras de redacción y claridad.
- **No se reciben:** reescrituras de la tesis (las dos raíces, el modelo de nodos, los principios). Esas se cierran con respeto.

Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de proponer, y [GOVERNANCE.md](GOVERNANCE.md) para entender cómo se decide. El historial técnico de cambios está en [CHANGELOG.md](CHANGELOG.md), y el relato de por qué el plan fue cambiando, en la [bitácora](BITACORA.md).

---

## Una nota honesta sobre qué es esto y qué no

Esto es un ejercicio intelectual, no una campaña. Su valor no depende de que alguien lo adopte ni de que reciba muchos colaboradores. La constitución crowdsourced de Islandia nunca se ratificó y aun así cambió la conversación global sobre cómo se escriben las constituciones. Un plan como este puede importar como referencia, como provocación o como material para pensar problemas de país, aunque nadie gobierne jamás con él, .

Los análisis jurídicos y fiscales son **análisis de política, no conceptos vinculantes**, y deben confirmarse con asesoría especializada. Las cifras provienen de fuentes oficiales 2025-2026 y están sujetas a revisión.

## Cómo se construye (build)

La fuente de verdad son los archivos de `docs/`. El documento completo (`programa-completo.md`) y el Word (`dist/estado-en-el-territorio.docx`) se *generan* a partir de ellos; no se editan a mano. El orden de las secciones está en [`build/manifest.txt`](build/manifest.txt).

Para construir en tu máquina (requiere `python3` y, para el Word, `pandoc`):

```bash
./build.sh
```

Esto une los archivos de `docs/` en el orden del manifiesto, quita los banners de capa, arma `programa-completo.md` y produce el Word. Si añades una sección nueva en `docs/`, agrégala también al manifiesto; el build avisa si un archivo de `docs/` quedó fuera.

En GitHub, el flujo de Actions ([`.github/workflows/build.yml`](.github/workflows/build.yml)) corre el build en cada push y deja el markdown y el Word como *artefactos* descargables. Al publicar una etiqueta de versión (por ejemplo `v1.7`), además crea un *Release* con ambos archivos adjuntos.

## Ver el plan como sitio web

El repositorio ya viene listo para publicarse como un sitio navegable (con barra lateral y buscador) usando GitHub Pages. Los archivos necesarios ya están incluidos. Los pasos están en [COMO-PUBLICAR.md](COMO-PUBLICAR.md): en resumen, Settings, Pages, Source "Deploy from a branch", rama `main`, carpeta `/ (root)`, y el sitio queda en `https://TU-USUARIO.github.io/TU-REPO/`.

## Licencia

Este trabajo se publica bajo **Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)**. Puedes usarlo, citarlo y adaptarlo, incluso para una campaña real, siempre que des crédito y compartas bajo la misma licencia. Ver [LICENSE](LICENSE).
