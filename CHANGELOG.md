# Historial de cambios

Todas las decisiones relevantes sobre el plan se registran aquí. El formato sigue, de manera informal, la idea de *Keep a Changelog*: agrupar por versión y describir qué cambió y por qué.

## [1.38] Respuesta a la auditoría más rigurosa: costeo, ancestros, y corrección de un error real

Motivado por una tercera auditoría externa, la más profunda recibida hasta ahora. Se verificó cada señalamiento contra el texto antes de actuar; casi todos resultaron correctos.

- **Nuevo: costeo de un nodo y punto de equilibrio fiscal** (Cuadro Fiscal), con Montería-Tierralta como caso base, cada supuesto visible y su fuente. Cierra la grieta señalada ("hay fuentes, no hay usos"): el costo de los 3 nodos de Ola 1 es una fracción marginal (~0,1-0,3%) del espacio fiscal del escenario base; el punto de equilibrio del recaudo se estima entre el año 6 y el 10, no antes, dicho con honestidad en vez de prometer que "se paga solo".
- **Corregido un error real de conflación** en el stress test: la fila de "ahorros de eficiencia" usaba la cifra del dividendo ético (medido en empleos) para estresar la línea de "eficiencia del gasto" (medida en billones), que son conceptos distintos. Ahora cada línea se estresa contra su propia cifra.
- **Reconciliada la aritmética de la senda de déficit** con el PIB nominal: el escenario base no cierra por sí solo los ~$45B que exige el ajuste de 2,5 puntos; se explicita que el resto viene del crecimiento nominal y la composición del gasto, no de una cuarta palanca fantasma.
- **Nueva sección "Los cuatro ancestros muertos"** en el Frente VIII: Millennium Villages, Consolidación Territorial, PDET y ZOMAC, nombrados antes de que los nombre un crítico, con las tres diferencias de diseño verificables frente a Consolidación (fiducia + condicionalidad, activador por resultado, sunset con métricas pre-registradas) y la adicionalidad contra municipios control elevada de fila de tabla a argumento central.
- **Respuesta explícita a si el Gerente de Nodo es función o mímica**, aplicándose el propio test de mímica isomórfica: la fiducia, la condicionalidad presupuestal y el activador por resultado son la respuesta, dicha de frente y no dejada implícita.
- **Honestidad de escala en tres metas** (informalidad 54%→44%, Gini de tierras 0,89→0,82, 100.000 empleos): se explicita a qué nivel se demuestra cada una (nodo con adicionalidad) y a qué nivel es trayectoria de varios gobiernos (nacional), evitando la dilución que el propio Hallazgo 19 identifica como causa de muerte de reformas anteriores.
- Advertencia de validez externa agregada a la referencia de Ruanda (catastro), con el mismo estándar que el documento exige a otras analogías.
- Corregido el orden de numeración 3.4.2/3.4.3 (antes invertido) y todas sus referencias cruzadas en 6 archivos. Limpiadas 5 comas huérfanas residuales del build.

## [1.37] Servicio Nacional de Vida: cómo se cultiva el prestigio, sin fabricarlo

- **Nueva subsección 14.10** en el Frente XIV. El objetivo de largo plazo es que servir gane, con el tiempo, un valor social reconocido por sí solo, sin que el Estado fabrique la sombra social por decreto, exclusión de beneficios o campañas de estigma, que sería coerción heredable por el peor gobierno.
- **Cinco mecanismos legítimos de promoción**, que fomentan el ingrediente sin tocar el estigma: red de egresados con vida propia después del Servicio; altavoz financiado a la historia sin escribirla (el Estado no narra el testimonio); insignias y credenciales verificables que duran para toda la vida civil; preferencia de mercado ganada por datos reales de desempeño, no impuesta por decreto; y aniversarios recurrentes de cohorte.
- **La regla que distingue promoción de estigma:** si el mecanismo hace más visible lo bueno que ya existe, se promueve; si depende de nombrar, excluir o presionar a quien no participó, es la línea que no se cruza. Se acepta explícitamente que el prestigio así construido tarda una generación, no un cuatrienio.

## [1.36] Tres correcciones de una segunda auditoría externa: nombre legal, matriz de riesgos y anexo fiscal

- **Corrección de nomenclatura legal en todo el documento:** "Ley Marco de Nodos" renombrada a "Ley de Régimen de Nodos" en las 13 ocurrencias del texto (6 archivos). "Ley Marco" (art. 150-19) es una categoría constitucional reservada a otras materias; el nombre técnico correcto es ley ordinaria. Antes la precisión existía solo en una nota al pie de viabilidad jurídica; ahora es consistente en todo el documento, cerrando un flanco de ataque legal gratuito.
- **Matriz de riesgos ampliada** (Riesgos y Límites Honestos): de tres columnas (riesgo, probabilidad, mitigación) a seis, con dueño del riesgo, señal temprana y umbral de pausa explícitos para cada uno de los 13 riesgos ya identificados. Convierte el diagnóstico de riesgos en algo operable y no solo enunciado.
- **Nuevo: Anexo Fiscal Maestro** (docs/cierre/anexo-fiscal-maestro.md), consolidado por los 15 frentes con costo aproximado, fuente de financiación, si requiere ley y riesgo de realización. No inventa cifras nuevas: reúne las que ya estaban dispersas en cada frente, y es honesto donde el costeo fino todavía no existe (sobre todo Frente X y XV), en vez de aparentar un rigor que el plan no tiene.
- Motivado por una segunda auditoría externa detallada; se verificó cada señalamiento contra el texto actual antes de actuar (dos de sus siete recomendaciones ya estaban cubiertas y no se tocaron).

## [1.35] Cerrando vacíos de una crítica externa: discapacidad, no discriminación, vetting global y riesgo fiscal climático

- **Nueva sección 13.3b en el Frente XIII, Discapacidad y derechos civiles.** Un solo principio universal (misma protección ante la ley sin importar etnia, raza, género, orientación sexual, identidad de género o discapacidad, sin programas segmentados por categoría) más dos piezas de diseño concretas: la no discriminación auditable con los mismos datos abiertos del resto del plan, y un índice de brecha de accesibilidad y empleo para discapacidad, con la misma lógica de medición que el IBET ya aplica a la brecha étnica.
- **Vetting de proveedores con historial de corrupción global**, nueva pieza en la plataforma de trazabilidad: cruce automático de todo oferente en SECOP contra las listas de inhabilitación del Banco Mundial, el BID, la CAF y agencias anticorrupción de otros países, antes de adjudicar.
- **Integración fiscal explícita del riesgo climático** en el Cuadro Fiscal: dos filas nuevas en el stress test (caída de la renta fósil tratada como certeza de calendario incierto y no como cisne negro, y desastre climático mayor con fondo de contingencia dimensionado como compromiso duro).
- Motivado por una crítica externa recibida sobre el plan; se contrastó cada punto contra el documento actual antes de actuar, y se descartaron los señalamientos ya cubiertos (sunset por fracaso, riesgo político del cambio de gobierno, puntos ciegos de digitalización) para no engordar sin necesidad.

## [1.34] Redistribución afinada con la versión final del documento de activos

- **El motor protege al pequeño en la norma, no en el discurso:** la lección de la muerte por dilución del intento 2022-2026 (se fusionó con la actualización catastral general, se personalizó en un gobierno, se defendió reactivamente) convertida en tres respuestas de diseño: umbral y exención escritos en la norma misma, linaje bipartidista (Ley 200 de 1936 y aval de Friedman), y pilotos que producen evidencia antes de la batalla nacional.
- **El catastro como pieza irreversible y la más vulnerable,** con datos verificados a febrero de 2026 (67% del territorio con valores actualizados, 44+ millones de hectáreas con catastro multipropósito frente al 9,4% de 2022, recaudo potencial multiplicado por más de cinco) y su defensa por diseño: banca multilateral, veeduría, y los municipios como aliados fiscales. El avalúo actualizado no se des-actualiza: es información que ningún gobierno puede des-saber.
- **El cruce cartográfico como primer paso operativo:** el mapa de municipios con catastro + seguridad + brecha uso/vocación decide dónde se enciende el motor, con información que ya existe.
- **Dos límites honestos nuevos:** la captura del avalúo (con su mitigación: avalúo masivo automatizado satelital auditado centralmente) y la incógnita de secuencia (Kerala tenía el movimiento antes de la ley; este diseño apuesta al orden inverso, sin precedente claro).
- **Evidencia de reversibilidad en tiempo real** (julio 2026: propuesta de reducir a la mitad las hectáreas entregadas) reforzando el freno anti reconcentración. Cifra de Sudáfrica actualizada (menos del 14% frente a la meta del 30%). Hallazgo 19 en Fundamentos.
- Fuera del plan, como siempre: el blindaje comunicacional y la estrategia legislativa del documento (tácticas de coyuntura, Congreso 2026-2030), que viven en el documento de trabajo aparte.

## [1.33] La grieta de la subexplotación y la estrategia para cerrarla

- **Nuevo bloque en el Frente II** con los cuatro límites honestos de la redistribución (los topes nacionales que capan el motor municipal, la extinción de efecto definitivo pero trámite lento, el carril municipal que asume una colaboración escasa donde más se necesita, y la grieta: la subexplotación en municipio capturado, que ni la extinción ni el motor municipal alcanzan, y que es el rostro más común de la concentración colombiana).
- **Estrategia de cierre, no solo diagnóstico:** cinco frentes que no dependen de la alcaldía ni del artículo 317. Condicionar la inversión nacional (Finagro, riego, vías) al uso productivo por incentivo; recuperar los baldíos indebidamente acumulados por encima de la UAF; publicar la brecha uso contra vocación predio a predio para nombrar al subexplotador y fracturar al gremio; la renta presuntiva nacional (impuesto de renta, no de propiedad, escapa al 317) como destino construido por evidencia; y descapturar el municipio con la maquinaria del Frente XIII para desbloquear el carril municipal.

## [1.32] Reforma agraria: redistribución de dos carriles (a la luz del documento de redistribución de activos)

- **Nueva sección en el Frente II, "Redistribuir de verdad: dos carriles según quién controla el territorio".** Integra un documento de trabajo especializado sobre redistribución democrática de tierra, cuyo hallazgo central (la redistribución de stock exige antes el monopolio estatal de la fuerza en el territorio) coincide con la tesis del nodo.
- **Carril de la frontera:** el nodo, que trae el Estado completo con seguridad antes de tocar la tierra; la seguridad es el criterio de dónde entra, no un acompañamiento.
- **Carril de lo controlado:** el motor georgista municipal (impuesto progresivo al valor del suelo por concentración e improductividad), municipal por el artículo 317, mismo patrón que el SGP y las regalías.
- **La zanahoria que divide a la élite** (incentivo tributario de salida a quien vende al Fondo) en vez de la compra negociada, que solo monetiza el veto (corrige la antigua línea de "compra subsidiada"). Activación de la extinción por inexplotación que ya es ley (Ley 160/1994, art. 58). Freno anti reconcentración (no enajenación más derecho de preferencia). Fondo blindado por interés (cooperativas en la junta, banca multilateral, veeduría), no solo por autonomía formal, con la lección del INCORA y Chicoral.
- **Dos hallazgos nuevos en Fundamentos (17-18):** Albertus sobre la redistribución de stock y el veto de la élite, y los fracasos (Sudáfrica, COFOPRI, Kerala) leídos como especificaciones de diseño.
- Se dejó fuera del plan, a propósito, la estrategia legislativa y de comunicación coyuntural del documento (su equivalente a la difusión del proyecto): es táctica, no programa.

## [1.31] Sección transversal: La Dimensión Deliberativa

- **Nuevo:** respuesta a una crítica justa, que el plan es muy técnico y frío y subestima los procesos humanos de diálogo, participación y reconciliación. La sección lo reconoce de frente y lo corrige como parte de la teoría del cambio, no como decoración.
- Dos fuentes de legitimidad (de resultado y de origen), y por qué entregar sin escuchar produce beneficiarios y no ciudadanos. El nodo llega completo pero no llega hecho: lo que no se negocia es que el Estado llegue, lo que se co construye es cómo (prioridades, orden, adaptación), con el mapeo de los primeros 15 días como inicio de un codiseño. El conflicto como parte de la democracia y no como ruido a filtrar (la consulta que de verdad puede negar). La reconciliación y la memoria como el trabajo lento que ningún mecanismo captura y que el Estado acompaña sin dirigir.
- Por qué es teoría del cambio: la participación sostiene el nodo contra la reabsorción, completa la legitimidad de resultado, y forma ciudadanía, que es un fin y no un medio. Con su límite honesto: la participación también se captura y no se arregla con otro mecanismo frío.

## [1.30] Integración desde una versión paralela: candados de ejecución y política exterior durable

- **Cinco candados de ejecución (nueva sección 3.9 en la columna vertebral).** Complementan, sin repetir, el diagnóstico y las secciones G, H, I del Frente VIII. Derivados de teoría de frontera: auditoría de puntos de autorización (Pressman y Wildavsky: N firmas en serie multiplican el fallo), matching de talento al eslabón frágil (O-ring de Kremer: catastro y titulación primero), índice de confianza territorial (Holmström y Milgrom: no medir solo lo medible), registro de casi fallos (Weick, alta confiabilidad) y mapeo de conocimiento práctico local (Scott, mētis). Ninguno crea entidad ni ley.
- **Nueve hallazgos nuevos (8-16) en Fundamentos en la Investigación Reciente:** Pressman y Wildavsky, Kremer, Evans (autonomía enraizada), Acemoglu y Robinson (corredor angosto), Holmström y Milgrom, Weick y Sutcliffe, Ostrom, James Scott y Tendler. Forman la capa de capacidad de ejecución.
- **Dos aterrizajes concretos:** sanción graduada de Ostrom en la Empresa Operadora Comunitaria (Frente XI) y reconocimiento público nombrado de Tendler para el Cuerpo de Ejecutores y el Servicio Nacional de Vida (Frente VIII-F).
- **Política exterior, solo la capa durable** (se descartó la coyuntural para no caducar): aclaración sobre extradición (cumplir un tratado por delito de jurisdicción compartida no es lo mismo que alquilar el poder ajeno), doctrina de vecindario en cuatro reglas fijas para cualquier vecino y cualquier gobierno, y la carrera diplomática apoyada en el Decreto Ley 274 de 2000 (ya existe, cúmplase).

## [1.29] Blindar la ejecución: diagnóstico y cuatro refuerzos teóricos al Frente VIII

- **Diagnóstico nuevo (cimiento del frente):** por qué el Estado colombiano no ejecuta, con nombre propio. Mímica isomórfica (adoptar la forma de las instituciones que funcionan sin su función: leyes de primer mundo, ejecución de siempre) y sobrecarga prematura (Andrews, Pritchett, Woolcock). El modelo de nodos se reencuadra como iteración adaptativa dirigida por problemas (PDIA): construir capacidad haciendo, no decretando, y expandir por resultado para no caer en la sobrecarga.
- **G. Que la isla no se reabsorba:** convierte en cinco criterios de diseño las lecciones de la literatura de bolsones de efectividad (Roll, Leonard) sobre por qué unas islas de efectividad perduran y otras se disuelven.
- **H. La política de la ejecución:** economía política de las reformas (Fernández y Rodrik, Acemoglu). Las reformas no mueren solo por falta de capacidad, mueren por resistencia; producir ganadores visibles temprano, secuenciar para que cada victoria financie la siguiente, y escoger la pelea con cada perdedor.
- **I. La rutina de cumplimiento:** la disciplina de las unidades de cumplimiento (Barber), que es el standup o revisión de sprint de la ingeniería aplicado al gobierno. Pocas prioridades, trayectorias mes a mes, y el encuentro periódico mirando el tablero de frente, combinado con la regla anti Goodhart para que la presión no corrompa el dato.

## [1.28] Sección transversal: Política Exterior

- **Nuevo:** doctrina de política exterior de principios durables, sin catálogo de países ni agenda de bando. Un tercer camino frente a los dos vicios históricos (subordinarse a la potencia de turno o alinearse con un bloque por ideología): una política de interés nacional y autonomía.
- Eje: la soberanía completa. El plan ya la trabaja hacia adentro (llenar el territorio de Estado); esta sección añade la mitad externa, con el principio tajante de que un Estado resuelve sus asuntos internos con sus instituciones y no convoca a poderes extranjeros contra sus propios ciudadanos.
- Principios: interés nacional sobre afinidad ideológica; autonomía por diversificación; las reglas por encima de la fuerza; responsabilidad compartida en lo transnacional; comercio al servicio del desarrollo; la riqueza ambiental como posición negociadora; protección del nacional en el exterior; y política exterior de Estado y no de gobierno, con servicio diplomático meritocrático, diseñada para que no sea el instrumento personal del gobernante.

## [1.27] La doctrina anti captura local: no condicionar la transferencia, blindar la ejecución

- **Nuevo:** encuadre al inicio de la sección 13.9 que consolida los mecanismos contra la captura clientelista local bajo un principio explícito y respetuoso del límite constitucional. El SGP y las regalías son transferencias de base constitucional (arts. 356-357 y SGR) y no se pueden condicionar por decreto; por eso la estrategia no toca el derecho del municipio a recibir, sino la forma de gastar. Interventor que no elige el alcalde, pago directo nación-proveedor, rendición en vivo y techo de concentración atacan el momento del gasto y del contrato, no el giro del recurso. Se cierra la captura sin pisar el derecho del territorio a sus recursos.

## [1.26] Frente XV: conservación como empleo, minerales estratégicos y no al fracking

- **Nuevo:** sección "cuidar el bosque como empleo", que convierte la conservación en economía legal para las comunidades del bosque (pagos por servicios ambientales, acuerdos de conservación con pago, guardabosques comunitarios), atada al nodo y al Servicio Nacional de Vida del Frente XIV. Si conservar da hambre y deforestar da plata, gana la deforestación.
- **Nuevo:** sección sobre minerales estratégicos (oro, coltán, cobre) con cuatro condiciones no negociables: agua y áreas protegidas por delante, consulta previa que puede negar, renta que se queda en parte en el territorio, y trazabilidad del mineral que de paso cierra el mercado al ilegal. Explotar sí, sin repetir la maldición de los recursos.
- **Nuevo:** exclusión categórica del fracking, la única del frente, fundada en el principio del agua primero (riesgo irreversible sobre el recurso más estratégico), con criterio técnico y no de consigna.

## [1.25] Frente XV: Medio Ambiente, Agua y Uso de los Recursos Naturales

- **Nuevo frente** (el documento pasa de 14 a 15 frentes). Llena un vacío real: el plan no tenía política ambiental consolidada.
- **Tesis:** la naturaleza se pierde donde el Estado está ausente. La deforestación se concentra donde no hay título, catastro ni economía legal, así que el nodo y la reforma agraria son el instrumento ambiental más potente del plan. Conservar no es solo declarar un parque, es estar.
- El agua primero (páramos y ecosistemas estratégicos, hacer cumplir la prohibición de minería en páramos). Deforestación: atacar al que lucra a escala, no al colono que sobrevive, con detección satelital del IDEAM conectada a la plataforma. Minería: separar la legal de la ilegal, atacando el dinero del oro ilegal que financia a los armados. Transición energética con honestidad fiscal: ni extractivismo sin límite ni ambientalismo de decreto, sino hoja de ruta fiscal y transición justa para las regiones que viven del carbón y el petróleo. Protección a líderes ambientales. Límites y riesgos honestos.
- Datos verificados por web (junio-julio 2026): concentración de la deforestación en Meta, Caquetá, Guaviare y Putumayo; participación mínima de Colombia en emisiones y reservas globales frente a su alta dependencia fiscal de los fósiles; déficit de gas proyectado.

## [1.24] El propósito declarado de la arquitectura de medios

- **Nuevo:** encuadre al inicio de la sección de comunicación que declara su propósito de fondo: una arquitectura de medios para proteger la democracia, no para servir a un gobierno. Cuatro metas que parecen opuestas (dificultar el monopolio, dificultar la desinformación a escala, sin coerción, sin limitar libertades) se reconcilian con una sola regla: la intervención actúa sobre la estructura y la transparencia del sistema, nunca sobre el contenido ni la verdad del mensaje. La distinción entre el demócrata (que quiere el abuso imposible venga de donde venga) y el partidario (que quiere el control en manos amigas).

## [1.23] El pluralismo como función de gobierno

- **Nuevo:** subsección en comunicación pública sobre el pluralismo informativo. La resistencia de una democracia no está en un medio que dé la cara del gobierno de turno (frágil, lo captura el que gana), sino en muchas voces distribuidas que ningún poder apaga de un golpe. El Estado fomenta esa pluralidad sin controlarla, con reglas ciegas al contenido (espectro comunitario por criterios técnicos, apoyos regionales por fórmulas auditables, pauta reformada), porque financiar al "independiente" que aplaude es captura con otro nombre.
- Principio que lo ordena: la independencia de los medios se defiende igual cuando favorece al propio lado que cuando favorece al contrario. Un medio público inclinado al lado de uno no es un triunfo, es una captura que aún no cambia de dueño.

## [1.22] Comunicación de gobierno: aterrizaje en RTVC y bloque propositivo

- **Ampliado:** la subsección de medios públicos se aterriza sobre lo que ya existe, RTVC (Señal Colombia, Canal Institucional, Radio Nacional, Radiónica), reconociendo que su dependencia del Ministerio de las TIC lo vuelve capturable, vicio que cambia de bando pero no de naturaleza. El plan no crea un canal nuevo, blinda el que existe con el modelo de radiodifusor de servicio público (tipo BBC): independencia editorial, financiación estable, gobernanza plural.
- **Nuevo:** bloque propositivo "cómo se comunica bien", con principios de uso en vez de propaganda: comunicar para servicio, rendición de cuentas, contexto y emergencia; mostrar la prueba y no pedir que crean; mostrar el proceso y no solo el resultado; hablar claro sin frivolizar el cargo; accesibilidad; y comunicación atada al cargo y no a la persona.

## [1.21] Comunicación pública y derecho a la información

- **Nuevo:** sección transversal sobre la comunicación como función de gobierno, escrita con el equilibrio entre el derecho del Estado a informar y el peligro de que ese derecho se vuelva propaganda o censura. Distingue medios públicos (del Estado, leales al ciudadano) de medios gubernamentales (voz del presidente de turno), y propone blindaje por estructura: financiación estable por ley, junta plural y escalonada, directores con periodo desfasado del ciclo presidencial.
- Alocuciones regladas, comunicación por verificabilidad (datos abiertos) en vez de propaganda, y un tratamiento explícito del equilibrio entre combatir la desinformación y la libertad de expresión, con el principio tajante de que el Estado no debe ser árbitro de la verdad y la lista de lo que NO debe hacer (nada de oficina de la verdad ni tipos penales vagos contra la crítica).

## [1.20] La denuncia ciudadana como sensor de los puntos ciegos

- **Nuevo:** subsección en el Frente IV sobre el papel de la denuncia ciudadana. Reconoce los canales que ya existen (línea 122 y Denuncia Fácil de la Fiscalía, PACO, personerías, veedurías), dispersos y desconectados, y plantea que el plan los unifica y los conecta a la plataforma como flujo de entrada.
- **Diseño de triaje corregido:** la denuncia se cruza con los datos para priorizar, nunca para descartar. La denuncia que cae en un vacío de datos no se descarta, se trata como doble alerta (sobre el hecho y sobre el punto ciego) con investigación humana, porque el silencio del dato no es prueba de inocencia. Compuerta humana para lo que la máquina no sabe clasificar, enrutamiento de las quejas de servicio fuera del embudo anticorrupción, y protección al denunciante de buena fe.
- Toque breve en la sección transversal de la plataforma: la denuncia ciudadana queda listada como uno de sus flujos de entrada.

## [1.19] Mecanismos concretos para la confianza pública

- **Nuevo:** la sección de percepción de corrupción aterriza en dos compromisos verificables. Uno, el reporte público del criterio (no del resultado): el operador independiente publica que la regla de detección fue ciega al partido y se aplicó sin excepción, vigilando sobre todo que el oficialismo no aparezca subrepresentado, en vez de prometer un conteo parejo. Dos, el compromiso de primer caso propio: la vara más dura hacia adentro, verificable con hechos. Cada uno con su responsable, su forma de medición y su límite honesto (la asimetría de un criterio ciego es hecho y no sesgo; la paridad forzada sería tan injusta como el sesgo).

## [1.18] La percepción de corrupción y la confianza pública

- **Nuevo:** sección al cierre del Frente IV que distingue combatir la corrupción de combatir su percepción, y trata la segunda como un problema de confianza y no de información. Reconoce el límite de la polarización (parte de la percepción es tribal y no se recupera) y propone cuatro palancas: verificabilidad, simetría demostrada (que la sanción caiga por hechos y no por bando, empezando por los propios), gestos visibles y comunicación honesta que admite errores.

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
