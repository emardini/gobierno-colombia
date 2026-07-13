> **EJECUCIÓN, abierto a corrección con evidencia.** Cifras, vías jurídicas, plazos y detalles de diseño se discuten vía *issues* y *pull requests*; ver [CONTRIBUTING](../../CONTRIBUTING.md).

# Frente II: Reforma Agraria Integral

**Metas:** titular 3 millones de ha en 4 años; Gini de tierras de ~0.89 a ≤0.82; cero entregas sin paquete habilitador.

| Paso | Medida concreta | Responsable | Plazo |
|---|---|---|---|
| 1. Catastro | Mapear para titular, cobrar predial y planear. Misma inversión que Frente I. | IGAC + SNR | Años 1-8 |
| 2. Titulación masiva | Proceso administrativo simplificado; 750.000 ha/año; prioridad mujeres y jóvenes rurales | ANT | Años 1-4 |
| 3. Redistribución | Fondo de Tierras alimentado por extinción por origen ilícito y por inexplotación (Ley 160/1994), más motor georgista municipal; incentivo tributario de salida a quien vende al Fondo, no compra negociada; siempre con paquete habilitador | ANT + SGC + Min. Agricultura + municipios | Años 2-8 |
| 4. Paquete habilitador | Ninguna tierra sin crédito + asistencia técnica + acceso a mercado + vía | Min. Agricultura + Finagro + SENA | Por entrega |
| 5. Blindaje | No-enajenación 10 años; registro cruzado IGAC-ANT-PILA; informes semestrales públicos | ANT + IGAC | Permanente |

## Jurisdicción Agraria y Rural: ya creada, falta implementarla

La titulación masiva genera conflictos (traslapes, ocupaciones superpuestas, disputas de linderos). Sin un mecanismo judicial ágil y territorialmente presente, esos conflictos bloquean la titulación o producen títulos impugnables. La buena noticia es que la jurisdicción especializada **ya existe**: el Acto Legislativo 03 de 2023 la incorporó a la Constitución y la Ley Estatutaria 2570 de 2026 definió su estructura. El trabajo del programa no es crearla: es **implementarla, financiarla y conectarla a los nodos**, además de empujar la ley ordinaria de competencias y procedimiento que aún está en trámite.

| Componente | Qué hace | Responsable | Plazo |
|---|---|---|---|
| Despliegue de jueces y tribunales en los nodos | El Consejo Superior de la Judicatura crea los despachos agrarios priorizando zonas de nodos y PDET; el Gobierno garantiza los recursos | Consejo Superior de la Judicatura + Min. Justicia + MinHacienda | Años 1-2 |
| Ley ordinaria de competencias y procedimiento | Apoyar el trámite de la ley que define el procedimiento especial agrario (audiencias ágiles, plazos máximos, acceso sin abogado para casos pequeños) | Congreso + Min. Justicia | En curso |
| Articulación con ANT y catastro | El juez accede en tiempo real a la base catastral y a títulos de la ANT; los fallos se registran en IGAC | ANT + IGAC + Rama Judicial | Año 2 |
| Prioridad étnica | Procedimientos diferenciados que respetan la consulta previa y las formas propias de resolución | Min. Interior + Rama Judicial | Año 1 |

**Vía jurídica (verificado):** la jurisdicción ya está constitucionalmente creada (AL 03/2023) y tiene su ley estatutaria de estructura (Ley 2570/2026). Lo pendiente es la ley ordinaria de procedimiento y, sobre todo, la implementación operativa y presupuestal, que depende del Consejo Superior de la Judicatura y del Gobierno, no de un nuevo trámite estatutario. Es, por tanto, mucho más factible de lo que parecía: el plan acelera y financia algo que el ordenamiento ya decidió.

## Tecnología de punta para el catastro: el multiplicador de velocidad

La meta de 750.000 ha/año exige duplicar la velocidad histórica del IGAC. Con detección automática de linderos por IA, drones y registro digital integrado, la productividad por técnico se multiplica de 3 a 5 veces. La tecnología no es adorno, es la condición de posibilidad de la meta.

**Base ya existente en Colombia:** el IGAC tiene contrato activo con Planet Labs (monitoreo satelital diario con IA). En enero de 2026, investigadores colombianos validaron extracción automática de linderos por fusión SAR + óptica con el modelo Segment Anything (SAM), desarrollada para la Reforma Rural Integral. **Referente:** Ruanda registró 10,3 millones de parcelas en menos de cinco años, con costo por título de ~$7 USD, escalando de 15.000 a 376.686 archivos/año (×25) con levantamiento comunitario + verificación tecnológica.

| Capa tecnológica | Cómo se usa | Estado en Colombia | Impacto |
|---|---|---|---|
| IA + imágenes satelitales | Borrador catastral automático (SAR + óptica, SAM reentrenado) que el técnico verifica en campo en vez de levantar desde cero | Metodología validada ene-2026; contrato Planet Labs activo | El técnico verifica, no mide. Productividad ×3-5. |
| Drones UAV ala fija + LiDAR | Levantamiento fotogramétrico (500-2.000 ha/vuelo); LiDAR para dosel denso (Caquetá, Chocó) | CIAC certifica pilotos; SENA incorpora operación en el Servicio (modalidad ambiental) | Cubre zonas inaccesibles; jóvenes del Servicio como operadores |
| Registro digital integrado (modelo Estonia) | El lindero verificado entra una vez y fluye a IGAC, ANT y SNR; sin reentrada manual | Requiere integración IGAC-ANT-SNR; articulado con la plataforma de trazabilidad | Elimina el principal cuello de botella administrativo |
| Inteligencia ambiental en tiempo real | Detección de deforestación, minería ilegal y cambio de uso post-catastro | IGAC ya usa Planet Labs para detección de cambios | Protege la inversión del catastro; alerta antes del daño irreversible |

> El cuello de botella del catastro no es la tecnología, es la integración. Hacer que IA-satelital, drones y registro operen como un sistema único articulado con ANT y SNR, con un solo ingreso de dato, es una decisión de arquitectura institucional, no una inversión tecnológica nueva.

## Redistribuir de verdad: dos carriles según quién controla el territorio

Titular y hacer productiva la tierra que la gente ya ocupa es una cosa. Redistribuir la tierra concentrada e improductiva es otra, mucho más difícil, y es donde casi todas las reformas agrarias democráticas del mundo han fracasado. La razón, documentada por Albertus con la base histórica más completa que existe, es que en una democracia el gran propietario tiene con qué vetar: bancada, tribunales, notarías y catastros locales, y por eso la redistribución de tierra ocurre más bajo dictadura que bajo democracia. El reto del plan es hacerla por la vía democrática sin caer ni en la parálisis ni en la coacción, y para eso hay que entender que no existe una sola herramienta, sino dos carriles, según quién controle el territorio.

**El carril de la frontera: el nodo.** Donde el Estado está ausente y la violencia manda, la tierra no se redistribuye con un impuesto ni con una ley, porque organizar campesinos alrededor de la tierra sin que el Estado controle primero el territorio no reparte tierra, fabrica víctimas. La historia colombiana lo probó con sangre: los líderes de restitución asesinados, las entregas suspendidas por amenazas. Ahí el instrumento es el nodo, que lleva el Estado completo, seguridad y justicia incluidas, antes de tocar la tierra, y solo se expande donde ya controla. El nodo trae el catastro, el paquete habilitador (título, crédito, asistencia y mercado, nunca el título solo, que es papel muerto) y las cooperativas que se organizan protegidas dentro de un territorio ya controlado, no expuestas. La seguridad no es un acompañamiento del programa, es el criterio que decide dónde entra: donde no hay control estatal no entra, porque entrar sin él es fabricar víctimas.

**El carril de lo controlado: el motor georgista municipal.** Buena parte de la tierra concentrada del país no está en la frontera violenta, está en zonas relativamente pacíficas y con catastro casi completo, donde el Estado ya controla y el nodo no tiene por qué llegar. Ahí el instrumento es otro: hacer que retener tierra ociosa sea ruinoso. Un impuesto progresivo al valor del suelo (no de las mejoras) que escala con la concentración del beneficiario final y con la brecha entre lo que el suelo puede producir y lo que produce, invierte la lógica del vendedor: ya no es el Estado rogando comprar, es el dueño calculando cada año cuánto le cuesta no vender la tierra que no explota. La oferta de tierra aparece sola, a precios que bajan en vez de inflarse, sin un solo acto de coacción. Es la idea de Henry George, que hasta Milton Friedman llamó el impuesto menos distorsionante que existe. Con un límite jurídico que hay que respetar de frente: el artículo 317 de la Constitución reserva el predial a los municipios, así que este motor no puede ser nacional, se enciende municipio por municipio donde converjan catastro actualizado, alcaldía dispuesta y control territorial. Es el mismo patrón que el plan ya aplica al SGP y las regalías: la puerta nacional está cerrada, la municipal está abierta.

**La zanahoria que divide a la élite, no la compra negociada.** El plan no compra tierra al que quiera vender, al precio y al ritmo que ponga, porque ese modelo, el de Sudáfrica, no elimina el veto del terrateniente, lo monetiza, y treinta años después la reforma sigue incumplida. En su lugar, un incentivo de salida: quien venda su tierra al Fondo de Tierras o a cooperativas acreditadas recibe tratamiento tributario preferente sobre la ganancia. Combinado con el motor georgista, el gran propietario enfrenta un menú donde vender es lo racional, y una fracción de la élite se vuelve aliada porque le resuelve su salida patrimonial. Es la lección profunda de las reformas que sí funcionaron: no se gana contra una élite unida, se gana contra una élite dividida entre la que quiere salida rentable y la que quiere acumular para siempre.

**Usar la extinción que ya es ley.** Antes de inventar instrumentos, el plan activa uno que duerme: la extinción administrativa de dominio por inexplotación, que ya es ley (Ley 160 de 1994, heredera de la Ley 200 de 1936 de López Pumarejo), apoyada en la función social de la propiedad del artículo 58 de la Constitución. Tierra ociosa por tres años puede extinguirse sin compensación, y el componente agrológico del catastro (uso real contra vocación del suelo) es la prueba. Es litigio predio a predio, lento, pero constitucionalmente blindado y sin necesidad de ley nueva. Alimenta el mismo Fondo de Tierras, junto con la extinción por origen ilícito del Frente IV.

**Que la tierra no se reconcentre.** La tierra adjudicada lleva la no enajenación de 10 años que ya fijan las metas, y después el derecho de preferencia del Fondo a precio catastral, para que el acaparador o el narcotraficante no recompren todo en una generación, que es literalmente lo que pasó en la contrarreforma de los años ochenta y noventa. La tensión con el crédito (que el título sirva de respaldo) se resuelve permitiendo hipoteca al Fondo o a la banca pública y prohibiendo la venta a terceros.

**Un Fondo blindado por interés, no solo por ley.** Colombia ya intentó blindar la reforma en una institución autónoma, el INCORA, y la élite no lo derogó, lo capturó y lo vació por dentro (el Pacto de Chicoral de 1972). La lección es que la autonomía de papel no basta cuando la institución opera contra un poder concentrado. Por eso el Fondo de Tierras se apoya en actores con interés propio en que funcione: cooperativas beneficiarias con asiento en su junta, banca multilateral como financiador condicionado, veeduría independiente, y junta de periodos escalonados que no coinciden con el ciclo presidencial. El blindaje no es la autonomía formal, es que haya quien pierda si lo capturan.

Los dos carriles corren en paralelo, cada uno donde le toca, y la seguridad territorial es el criterio que decide cuál aplica dónde. El nodo es la parte crítica de la solución, porque crea la precondición sin la cual nada más funciona, pero no es toda la solución: buena parte de la concentración está fuera de la frontera dura, y ahí el motor georgista municipal es el que mueve la tierra. Juntos son la vía democrática a una redistribución que ni se paraliza ni coacciona.

## Módulo de Productividad Rural: activar el campo que ya existe

El campo concentra la peor productividad del país y, a la vez, la mejor palanca para subirla. La informalidad rural ronda el 83% y la productividad por trabajador agrícola está muy por debajo del promedio nacional, pero la tierra titulada, el riego y la asistencia técnica producen saltos de productividad que ninguna otra inversión iguala. Este módulo es el gemelo rural del Módulo de Productividad Urbana (12.3): aplica al campo el principio de "activar lo que ya existe" en vez de solo repartir, y persigue competitividad, no solo subsistencia.

> **Por qué importa para la competitividad nacional.** Las exportaciones no minero-energéticas que el país necesita para no depender del petróleo salen en buena parte del agro: cacao, café especial, frutas, ganadería sostenible. Subir la productividad rural no es solo justicia con el campesino, es la base de la canasta exportadora que diversifica al país. El campo improductivo es un techo a la competitividad de Colombia.

### A. El título como activo productivo, no solo como derecho

La titulación masiva del Frente II ya entrega seguridad jurídica; este módulo la convierte en productividad. El título muerto en un cajón no sube la producción; el título usado como colateral, sí.

| Medida | Concreción | Vía jurídica | Plazo |
|---|---|---|---|
| Crédito contra título | Que el título recién entregado sirva de inmediato como garantía ante Banco Agrario y Finagro, con producto financiero diseñado para el pequeño productor | Decreto + Finagro + Banco Agrario | Año 1 |
| Catastro como base de extensión | Los datos del catastro multipropósito identifican qué produce cada predio y dónde falta asistencia, riego o vía, para dirigir la inversión con precisión | Vía administrativa (IGAC + ADR) | Años 1-2 |

### B. Extensión agropecuaria moderna: difusión, no solo insumos

La brecha entre el campesino promedio y el productivo es de conocimiento y técnica disponible, no de esfuerzo. Colombia desmanteló su sistema de extensión rural; reconstruirlo es de las inversiones de mayor retorno.

| Medida | Concreción | Vía jurídica | Plazo |
|---|---|---|---|
| Extensionismo rural por resultados | Asesores técnicos en territorio (vía ADR y el Servicio Nacional de Vida ambiental) con metas de rendimiento por hectárea verificadas, no por número de visitas | Decreto + ADR + AGROSAVIA | Año 1 (piloto en nodos), 2-4 (escala) |
| Paquete tecnológico apropiado | Semilla mejorada, riego eficiente, manejo de suelos y poscosecha, adaptados a cada cadena; transferencia de AGROSAVIA al productor | Vía administrativa | Por ola |
| Sanidad e inocuidad para exportar | Fortalecer al ICA y al Invima para que la producción cumpla los estándares fitosanitarios que abren mercados externos (el cuello de botella real de la exportación agro) | Decreto + presupuesto | Años 1-3 |

### C. Agregar valor y conectar al mercado

El campesino que vende materia prima al intermediario captura una fracción del valor. La productividad sube cuando el territorio procesa, asocia y vende mejor.

| Medida | Concreción | Vía jurídica | Plazo |
|---|---|---|---|
| Procesamiento local | Apoyar centros de acopio, frío y primera transformación de propiedad cooperativa en los nodos (cacao seco y fermentado, café trillado, fruta procesada) | Decreto + ADR + cooperativas | Años 1-4 |
| Compra pública como demanda ancla | El PAE, las guarniciones militares y los hospitales compran a las cooperativas de los nodos con contratos previsibles, dando escala para invertir | Reglamento de contratación | Año 1 |
| Asociatividad que baja costos | Cooperativas para comprar insumos en volumen, compartir maquinaria y negociar precio, con el costo de formación reducido (Frente I) | Ley + decreto | Años 1-2 |
| Acceso directo a mercado y exportación | Vincular las marcas territoriales y las denominaciones de origen (cacao del Caquetá, café del Cesar) con ProColombia y los canales de exportación | Decreto + ProColombia | Años 2-4 |

### D. Riego y bienes públicos que multiplican el rendimiento

| Medida | Concreción | Vía jurídica | Plazo |
|---|---|---|---|
| Distritos de riego pequeños y medianos | Riego tecnificado donde la cadena lo justifica; el riego puede duplicar el rendimiento por hectárea | Decreto + ADR + presupuesto | Años 1-4 |
| Vías terciarias y conectividad | El mismo paquete de bienes públicos del nodo (Frente I); sin vía, la cosecha se pierde o el flete se come el margen | INVIAS + Min. TIC | Por ola |

### Métricas de productividad rural (no solo hectáreas tituladas)

| Indicador | Qué mide | Meta |
|---|---|---|
| Rendimiento por hectárea en cadenas priorizadas | Productividad agrícola real | Subir de forma sostenida frente a la línea base del nodo |
| Ingreso neto del productor formalizado | Que la productividad llega al campesino, no solo al intermediario | Crecimiento verificable en PILA y registros de cooperativa |
| Valor agregado retenido en el territorio | Que el nodo procesa, no solo extrae | % de producción con primera transformación local |
| Exportaciones agro no tradicionales de los nodos | Aporte a la competitividad nacional | Crecimiento real en el período |
| Tasa de uso del título como colateral | Que el título es activo productivo, no papel | % de títulos nuevos con crédito asociado a 24 meses |

### La advertencia honesta

Titular sin paquete habilitador produce papeles, no productividad: es el error histórico que el Frente II ya busca evitar con su regla de "ninguna tierra sin crédito, asistencia técnica, vía y mercado". Este módulo es esa regla vuelta sistema. Y, como en el caso urbano, el riesgo es capturar el beneficio en los grandes; por eso prioriza al pequeño y mediano productor y la propiedad cooperativa, no la agroindustria ya consolidada.
