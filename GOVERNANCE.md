# Gobernanza

Este proyecto se gobierna como un proyecto de software de código abierto con **maintainer único**, no como una democracia de votación. La distinción es deliberada y vale la pena explicarla.

## Por qué no es una democracia de votación

Los manifiestos colaborativos (como OpenPolitics en el Reino Unido) deciden por votación de los contribuyentes: el contenido es colectivo desde su origen. Eso funciona para un documento que nace sin dueño para que cualquiera lo escriba.

Este documento es distinto: es un **plan de autor**, con una tesis propia y un punto de vista. Si su contenido se decidiera por votación, una mayoría organizada podría vaciar la tesis y el plan dejaría de ser lo que es. Por eso el modelo correcto no es la votación, sino el del **"dictador benevolente"** del software libre: el código es público, cualquiera propone, pero hay un responsable que decide qué se integra y custodia la coherencia de la visión.

## Roles

- **Maintainer (autor).** Decide qué propuestas se integran. Mantiene la coherencia entre el núcleo y la ejecución. Documenta públicamente la razón de cada decisión relevante. Es el garante de la visión.
- **Contribuyentes.** Cualquier persona que abra un *issue* o un *pull request*. No necesitan ser de un partido, tener edad de votar ni vivir en Colombia: las buenas ideas y las buenas objeciones vienen de cualquier parte.

## El principio que ordena las decisiones: núcleo vs. ejecución

- Las propuestas sobre **ejecución** (cifras, vías jurídicas, plazos, parámetros, redacción) se evalúan por su mérito y su evidencia. Si mejoran el plan, se integran.
- Las propuestas que tocan el **núcleo** (la tesis de las dos raíces, el modelo de nodos, los principios) no se integran por defecto. Se conversan, pero el sesgo es a preservar la tesis. Cambiar el núcleo no es corregir el plan: es escribir otro.

La frontera exacta entre núcleo y ejecución está en [CONTRIBUTING.md](CONTRIBUTING.md), y cada archivo lleva un banner que indica su capa.

## Trazabilidad

El activo de este modelo es que **todo queda registrado**. El historial de Git muestra qué cambió, cuándo y por qué. Las decisiones relevantes se anotan en [CHANGELOG.md](CHANGELOG.md). Cualquiera puede auditar cómo evolucionó el plan, incluidas las correcciones de fondo, como los ajustes de viabilidad jurídica tras verificar el estado real del derecho colombiano, .

## Salvaguardas contra la captura

Un documento político abierto atrae intentos de captura por grupos organizados que sobre-representan un interés. Las defensas:

- **El filtro no es la mayoría, es el criterio del autor a la vista de todos.** No se gana integrando un cambio por acumular votos.
- **Evidencia obligatoria.** Las propuestas sin argumento ni fuente no avanzan.
- **El núcleo es inmodificable por propuesta.** El intento de vaciar la tesis por volumen de PRs no tiene efecto.
- **Código de conducta.** El [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) protege la conversación.

## Bifurcación (fork) como derecho

Si alguien está en desacuerdo profundo con el núcleo o con las decisiones del maintainer, la licencia abierta (CC BY-SA 4.0) le permite **bifurcar**: tomar todo el documento y construir su propia versión, citando el origen. Eso es una característica, no un fallo: garantiza que ninguna visión quede secuestrada y que las buenas ideas circulen aunque los autores discrepen.

## Sucesión

Si el maintainer deja el proyecto, puede designar a otro o declarar el documento congelado y plenamente disponible para que cualquiera lo bifurque y continúe. En cualquier caso, la licencia asegura que el trabajo nunca quede inaccesible.
