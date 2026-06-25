# Historial de cambios

Todas las decisiones relevantes sobre el plan se registran aquí. El formato sigue, de manera informal, la idea de *Keep a Changelog*: agrupar por versión y describir qué cambió y por qué.

## [1.17] La plataforma fuera de la ruta crítica del arranque

- **Nuevo, lado positivo:** se explicita que desarrollar y operar la plataforma genera empleo de alta calificación, capacidad estatal instalable y conocimiento anticorrupción exportable, no solo gasto.
- **Nuevo, riesgo y mitigación:** se reconoce que, al habilitar cinco frentes, la plataforma entra en la ruta crítica y es un riesgo de cronograma y de "elefante blanco tecnológico". La solución es desacoplarla del arranque: los primeros nodos operan con control tradicional reforzado (viable para tres nodos), la plataforma se construye en paralelo y habilita el escalamiento, no el inicio, y se diseña por módulos desde la experiencia de campo. Se deja explícito el costo del período manual.

## [1.16] La plataforma de trazabilidad pasa a sección transversal

- **Movido:** la descripción de la plataforma de trazabilidad del gasto sale del Frente X (Industria Avanzada), donde encajaba forzada, y pasa a una sección transversal propia. La plataforma no es política industrial, es infraestructura del Estado entero (habilita los frentes IV, VI, XIII, III y los nodos), así que ahora tiene una sola casa coherente con su naturaleza.
- En el Frente X queda solo una mención breve, como ejemplo del principio de "primer cliente" (el Estado se compra una capacidad tecnológica nacional), con remisión a la sección transversal.
- Actualizadas las referencias cruzadas (Frentes IV, VI y Columna Vertebral) para apuntar a la sección transversal en vez de al Frente X.

## [1.15] Sistema Nervioso conectado con la plataforma de integridad

- **Conectado:** la sección "Sistema Nervioso" del Frente X deja de describir el motor de alertas por su cuenta y se presenta como la infraestructura (la cañería de datos) sobre la que corre la plataforma de integridad detallada en el Frente IV, con remisión explícita. Se evita la duplicación que causaba el riesgo de desincronización entre las dos secciones.
- Se aligera la fila del motor (las señales y módulos viven en el IV), se conserva la inteligencia financiera (flujos de grupos armados) como uso propio de seguridad distinto de la detección de corrupción, y se subraya el rol transversal y de primer cliente del Frente X.

## [1.14] Diagrama de la plataforma de integridad

- **Nuevo:** diagrama en docs/img/ (PNG y SVG) que muestra la plataforma de integridad del gasto: los módulos por dominio alimentan un motor común y este produce alertas con dos salidas (territorial: congela el desembolso; nacional: alimenta la Unidad de Macrocorrupción), con la banda de gobernanza. Incrustado en el Frente IV, en el sitio y en el Word.

## [1.13] La herramienta como plataforma de integridad con módulos por dominio

- **Reencuadrado:** la herramienta anticorrupción se presenta como lo que es, una plataforma de integridad del gasto público con un motor común y módulos por sector (contratación, salud, subsidios, nómina, PAE), no como una herramienta exclusiva de contratos. Regla clave: el mismo motor con reglas distintas por dominio, diseñadas por quien conoce cada sector.
- **Nuevo:** orden de despliegue por madurez del dato (no por dónde duele más el robo) y salvaguarda reforzada de privacidad para el dominio de salud (datos agregados y de facturación, no diagnósticos; anonimización; habeas data).
- **Conectado:** el Frente VI (Salud) enlaza su "castigo inescapable" con el módulo de salud de la plataforma, con su salvaguarda de privacidad explícita.

## [1.12] Herramienta tecnológica anticorrupción

- **Nuevo:** el Frente IV abre con un mapa de la estrategia anticorrupción en dos escalas (nacional y sistémica en el IV, territorial y municipal en el XIII) más la herramienta compartida (plataforma del Frente X), con remisiones, para que se lea como un solo cuerpo sin mover las piezas de donde su método las necesita.
- **Nuevo:** sección detallada de la herramienta tecnológica de detección por dato: qué es y qué no es, las fuentes que cruza, el motor de alertas (señales concretas), cómo cose la escala territorial con la nacional, su gobernanza para que no sea un arma política, y los límites honestos de lo que NO puede hacer.

## [1.11] Diagramas del nodo y de la historia de Wílmer

- **Nuevo:** dos figuras en docs/img/ (PNG para el Word y SVG editable como fuente). Un diagrama del concepto de nodo (las cinco piezas que entran juntas y las fases 0 a graduación) y una línea de tiempo de la historia de Wílmer (del año cero a la graduación). Quedan incrustadas en el sitio y en el Word.
- El build ahora pasa --resource-path a pandoc para incrustar las imágenes en el documento generado.

## [1.10] El nodo, contado y mirado al espejo

- **Nuevo:** sección 3.0.1 "Un nodo visto desde adentro: la historia de Wílmer", un escenario ilustrativo y detallado (cacao de Tierralta, el título que se vuelve crédito, la cooperativa, Jóvenes en Paz y la salida de los primos) que muestra cómo encajan las piezas y cómo nace el empleo. Marcado como ilustrativo, con componentes reales y honestidad sobre a quién el programa no alcanza.
- **Nuevo:** sección 3.8 "El nodo es ejecución de alta precisión", donde el plan reconoce de frente que el modelo exige planeación de detalle, distingue ingeniería de condiciones de ingeniería de personas, muestra cómo el Gerente de Nodo, los Equipos Territoriales, el protocolo de 100 días, la trazabilidad y el diseño de mecanismos existen para sostener esa exigencia, y nombra la capacidad de ejecución como su mayor fortaleza y su mayor riesgo.

## [1.9] Explicación clara del nodo

- **Nuevo:** sección 3.0 "Qué es un nodo, en lenguaje claro" al inicio de la Columna Vertebral. Explica en lenguaje sencillo qué es un nodo, qué trae (las cinco piezas que entran juntas y por qué juntas), cómo funciona (fases, graduación, expansión por resultado) y qué NO es. Antes el documento entraba directo a fases e índices sin comunicar primero el concepto central del plan.

## [1.8] Evolución visible

- Los archivos generados (programa-completo.md y el Word de dist/) dejan de versionarse: se producen con el build y se publican como artefactos y releases. Así el historial muestra con claridad qué cambió en cada sección, sin el ruido del documento consolidado regenerándose entero.
- **Nuevo:** BITACORA.md, el relato en lenguaje natural de por qué el plan fue cambiando versión a versión (el CHANGELOG dice qué cambió; la bitácora, por qué).

## [1.7] Proceso de build

- **Nuevo:** sistema de build que define los archivos de docs/ como única fuente de verdad y genera el documento completo (programa-completo.md) y el Word a partir de ellos. Incluye build/manifest.txt (orden canónico), build/build.py (con validación: avisa si un archivo de docs/ queda fuera del manifiesto), y build.sh para construir en local.
- **Nuevo:** flujo de GitHub Actions que construye en cada push, publica los entregables como artefactos descargables y, en etiquetas de versión, crea un Release con el markdown y el Word adjuntos.
- Esto elimina el riesgo de desincronización entre los archivos partidos y el documento consolidado que causó errores en versiones anteriores.

## [1.6] Productividad rural y simetría campo-ciudad

- **Nuevo:** Módulo de Productividad Rural en el Frente II, gemelo del urbano: el título como activo productivo (crédito contra título), extensión agropecuaria por resultados, sanidad e inocuidad para exportar, agregación de valor y procesamiento local, riego y bienes públicos, con métricas propias (rendimiento por hectárea, valor agregado retenido en el territorio, exportación agro, uso del título como colateral).
- **Reforzado:** la sección de Productividad y Competitividad Nacional trata campo y ciudad de forma simétrica y subraya que el agro es la base de la canasta exportadora no minero-energética.
- **Corregido:** el script de partición del repositorio reconocía mal los títulos de los frentes tras el cambio de estilo; ahora todos los archivos de frentes se regeneran limpios desde el documento maestro.

## [1.5] Edición de estilo, productividad y publicación

- **Estilo humano:** se eliminaron los guiones largos en todo el documento (convertidos en dos puntos, comas o paréntesis según el contexto) y se normalizaron los rangos numéricos. Cambios de léxico: "lío" por "lío" y "Jaguar Andino" por "Jaguar Andino".
- **Productividad y competitividad:** nueva sección transversal "Productividad y Competitividad Nacional" con objetivo nacional, metas duras (PTF, productividad laboral, inversión, exportaciones no minero-energéticas, costo logístico, ranking de competitividad), ocho palancas fuertes ordenadas y gobernanza de la meta.
- **Publicación:** el repositorio queda listo para GitHub Pages (Docsify) con index.html, _sidebar.md, .nojekyll y la guía COMO-PUBLICAR.md.

## [1.4]: Módulo de Productividad Urbana

Incorporación de una agenda explícita de productividad y competitividad sobre la economía que ya existe, tras constatar que el país crea empleo formal mientras la productividad por trabajador cae (diagnóstico 2025-2026).

- **Nuevo:** sección 12.3 "Módulo de Productividad Urbana" en el Frente XII, con seis componentes: recualificación del trabajador en activo, extensionismo tecnológico para pymes (difusión, no invención), fin del castigo al crecimiento (el "enano fiscal"), competencia con dientes y costos de insumos, profundización de los clústeres urbanos existentes, y la ciudad que funciona. Aplica el principio "activar lo que ya se pagó" al tejido productivo, no solo a la infraestructura.
- **Nuevo:** métricas de productividad (valor agregado por trabajador, tasa de graduación de firmas) en el módulo y en la sección global de Medición, para corregir la trampa de "más empleo, menos productividad".
- Renumeración de las secciones de turismo del Frente XII (12.3→12.4, 12.4→12.5).

## [1.3]: Verificación jurídica

Contraste de las clasificaciones jurídicas con el estado real del derecho colombiano (a 2026).

- **Corregido:** la Jurisdicción Agraria y Rural ya existe (Acto Legislativo 03/2023 + Ley Estatutaria 2570/2026). El plan la implementa y financia, no la crea.
- **Corregido:** la objeción de conciencia al servicio exige ley estatutaria (no ordinaria) y su diseño "canalizar, no eximir" se marca como constitucionalmente discutible.
- **Corregido:** la interventoría nacional sobre contratos de entidades territoriales requiere ley, no decreto (autonomía territorial).
- **Acotado:** la condicionalidad presupuestal aplica a inversión nacional, no a transferencias constitucionales (SGP/regalías).
- **Confirmado:** el catastro multipropósito ya es servicio público (Ley 1955/2019, Decreto 148/2020): ejecutable por vía administrativa.
- **Precisado:** "Ley Marco de Nodos" es, técnicamente, una ley ordinaria; la Unidad de Macrocorrupción cabe en ley ordinaria en su versión sin autonomía.

## [1.2]: Fundamentos en investigación reciente

Incorporación de hallazgos de frontera (posteriores al Nobel 2007 de diseño de mecanismos) como ajustes concretos.

- Disciplina por exportación verificada en el Frente X (nueva economía de la política industrial).
- Pago por desempeño en la DIAN y asignación por desempeño del Gerente de Nodo (experimentos de capacidad estatal).
- Diseño de la divulgación, competencia por comparación y auditoría de robustez como mecanismos 6, 7 y 8 del Frente XIII.
- Calibración del *sunset* a la curva de maduración (~7 años) y puente al empleo asalariado (evidencia de "big push").
- Umbral de irreversibilidad del enclave (Nobel 2024 sobre instituciones).
- Nueva sección transversal "Fundamentos en la investigación reciente".

## [1.1]: Reorganización e integración de soluciones

- Integración de siete soluciones a las debilidades de la versión original (viabilidad jurídica explícita, cuadro fiscal de dos escenarios, irreversibilidad simétrica con *sunset*, enforcement atado a palancas ejecutivas, piso universal y nodo de aprendizaje, capital humano escalonado, orden y limpieza).
- Numeración consistente (un solo conjunto de Frentes I-XIV).
- Colombia Viva movida al Anexo A.
- Nuevas secciones: Viabilidad Jurídica y Cuadro Fiscal de Dos Escenarios.

## [1.0]: Versión base

- Plan de gobierno original: tesis de las dos raíces, modelo de nodos, 14 frentes, Visión 2042 y transición.
