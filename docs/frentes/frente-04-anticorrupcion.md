> **EJECUCIÓN, abierto a corrección con evidencia.** Cifras, vías jurídicas, plazos y detalles de diseño se discuten vía *issues* y *pull requests*; ver [CONTRIBUTING](../../CONTRIBUTING.md).

# Frente IV: Anticorrupción

**Meta:** subir Colombia del puesto ~92 al ≤70 en el IPC al final del período.

**El reencuadre:** la corrupción alcanzó 94% de impunidad en 2024 no por falta de leyes, sino por tratarla como suma de delitos individuales. La gran corrupción funciona como sistema que captura instituciones. Se investiga como sistema, con metodologías de macrocriminalidad: identificar aparatos y determinadores, develar modus operandi, rastrear lavado y mecanismos de impunidad.

## La estrategia anticorrupción opera en dos escalas y se apoya en una herramienta

La lucha anticorrupción del plan no está toda en este frente, y conviene leerla como un solo cuerpo aunque sus piezas vivan en lugares distintos por una razón de método. Entra por aquí:

- **Escala nacional y sistémica (este Frente IV).** La gran corrupción tratada como red, no como caso suelto: la Unidad de Macrocorrupción en la Fiscalía, la financiación de campañas, la extinción de dominio, el fondo de reparación.
- **Escala territorial y municipal (Frente XIII, secciones 13.9 y 13.10).** La corrupción en alcaldías y gobernaciones, atacada con diseño de mecanismos: interventoría nacional obligatoria, pago directo nación-proveedor, techos de concentración por empresa, rendición en vivo y un protocolo de alertas por niveles. Vive en el XIII porque su método es el diseño de mecanismos, que es el corazón de ese frente.
- **La herramienta que conecta ambas (la plataforma de trazabilidad, el "Sistema Nervioso" del Estado).** La infraestructura de datos que sigue cada peso del gasto público, descrita en su sección transversal propia, [Plataforma de Trazabilidad del Gasto](../transversal/plataforma-trazabilidad.md). Aquí abajo se detalla el motor anticorrupción que corre sobre ella, porque es el hilo que cose la escala territorial con la nacional: la misma alerta que congela un contrato municipal puede revelar la red que opera en nueve departamentos.

| Capa | Medida | Responsable | Plazo | Vía jurídica |
|---|---|---|---|---|
| Origen (gran corrupción) | Financiación pública base de campañas; inhabilidad automática (Cuentas Claras × SECOP); CNE técnico e independiente | CNE + Congreso | Años 1-2 | Ley estatutaria / reforma |
| Investigación sistémica | Unidad de Macrocorrupción en la Fiscalía: investiga cadenas como sistemas. Estructurada como unidad delegada con **presupuesto protegido por vigencias** y modelo de nombramiento por concurso técnico (no pretende autonomía que la Constitución no da dentro de la Fiscalía) | Fiscalía + Congreso | Año 1 | Ley estatutaria |
| Oportunidad | Digitalizar y eliminar contacto humano discrecional: ventanilla única, inspector digital, adjudicación por algoritmo con reglas públicas | Min. TIC + Entidades | Años 1-3 | Decreto + reglamento |
| Certeza | Detección por dato, no por denuncia; proceso máx. 18 meses; mismas reglas para aliados y opositores; reparación a víctimas colectivas | Fiscalía + Consejo Superior | Año 1 | Ley |
| Fondo de Reparación | Todos los bienes recuperados van al Fondo; cuando la corrupción golpea un sector, los recursos reparan ese sector | Fiscalía + SGC + DNP | Años 1-2 | Ley |
| Extinción de dominio | Disparada por datos; plazos máx. 24 meses; tierras al Fondo de Tierras; testaferros con responsabilidad solidaria | Fiscalía + SGC | Años 1-2 | Ley |
| Cultura | Currículo escolar con el costo concreto del robo; PAE honesto como práctica | Min. Educación | Años 2-4 | Reglamento |

## La herramienta tecnológica: detección por dato, no por denuncia

Toda la estrategia descansa en una promesa que hay que volver concreta: detectar la corrupción por los datos y no esperar a que alguien la denuncie. Conviene explicar qué es esa herramienta, cómo funciona y, con la misma honestidad, qué no puede hacer. Porque vendida como una caja mágica, defrauda; entendida como lo que es, una buena, cambia el cálculo del que roba.

### Qué es (y qué no es)

No es una inteligencia artificial que "descubre corruptos". Es un sistema de integración de datos y detección de anomalías que corre sobre la plataforma de trazabilidad del gasto (su sección transversal propia). Su premisa es simple: casi toda corrupción que toca el gasto público deja huella en los datos. Una empresa que gana un contrato grande pero no tiene un solo empleado en planilla. Un precio unitario muy por encima del de la región. Un "concurso" con un solo proponente, o con tres que comparten dirección y dueño. La huella existe; el problema es que hoy vive dispersa en bases que no se hablan entre sí. La herramienta no inventa información nueva, hace visible y comparable la que ya existe.

### De dónde saca los datos

Su valor está en el cruce, no en una base sola. Integra fuentes que hoy están separadas, casi todas ya públicas o estatales:

| Fuente | Qué aporta |
|---|---|
| SECOP I y II | Contratos: objeto, monto, proponentes, adjudicación |
| Cuentas Claras (CNE) | Quién financió cada campaña |
| PILA | Si una empresa tiene empleados reales (o es un cascarón) |
| RUES y cámaras de comercio | Cuándo se creó una empresa y quiénes son sus dueños y representantes |
| DIAN | Facturación y declaraciones (con las reservas legales del caso) |
| Sistema General de Regalías | El gasto de regalías, foco histórico de desvío |
| Catastro e IGAC | Valor real de predios y obras |
| UIAF | Reportes de operaciones sospechosas (capacidad que ya existe) |
| Nómina pública | Nóminas paralelas y contratistas que también son funcionarios |

### El motor de alertas: qué señales dispara

El motor compara, cruza y marca patrones. Cada alerta es una bandera para que un humano revise, no un veredicto.

| Señal | Cómo se detecta |
|---|---|
| Empresa fantasma | Constituida pocas semanas antes de ganar, sin empleados en PILA, gana contrato grande |
| Competencia simulada | Un solo proponente, o "competidores" que comparten dirección, dueños o representante legal (cruce RUES) |
| Fraccionamiento | Muchos contratos del mismo objeto y proveedor, justo por debajo del umbral que obliga a licitar |
| Sobreprecio | Precio unitario muy por encima del acuerdo marco o del histórico de la región |
| Discrepancia físico-financiera | Avance real de la obra (fotos, interventoría) muy por debajo del porcentaje ya desembolsado |
| Concentración | Una empresa, o un grupo de socios comunes, acapara una porción anómala del presupuesto de un municipio |
| Direccionamiento | Pliegos con requisitos hechos a la medida de un proponente |
| Conflicto de interés | Dueños de contratistas que coinciden con funcionarios o con financiadores de campaña (cruce RUES, nómina y Cuentas Claras) |

### Cómo cose las dos escalas

Aquí está lo que hace a la herramienta el hilo de toda la estrategia. La misma alerta sirve en dos direcciones. Hacia abajo, en lo territorial: una alerta roja sin respuesta congela el siguiente desembolso del nodo y dispara la interventoría del Frente XIII, sin necesidad de esperar a un juez. Hacia arriba, en lo sistémico: si la misma empresa, o los mismos socios, o el mismo patrón aparecen en nueve departamentos, eso ya no es un caso, es una red, y ahí entra la Unidad de Macrocorrupción a reconstruir el sistema completo. La herramienta detecta el caso pequeño y, al mismo tiempo, revela el patrón grande del que ese caso era apenas un nodo.

### El mismo motor, otros dominios del gasto

Conviene ver la herramienta por lo que de verdad es. No es "anticorrupción de contratos", es detección de anomalías sobre los flujos de dinero y datos del Estado. La contratación de obra es solo el primer dominio donde se aplica, porque ahí el patrón es más claro. Pero el mismo motor sirve en cualquier parte donde el Estado mueve plata o presta un servicio dejando datos. Es, en rigor, una **plataforma de integridad del gasto público** con un motor común y módulos por sector.

| Dominio | La señal análoga que detecta | Dónde vive |
|---|---|---|
| Contratación de obra | Empresa fantasma, sobreprecio, fraccionamiento, obra desembolsada y no construida | Módulo 1 (este frente) |
| Salud | Facturación de procedimientos no realizados, recobros por encima del precio de referencia, pacientes fantasma o fallecidos que siguen "atendidos" | Frente VI |
| Subsidios y transferencias | Beneficiarios duplicados, fallecidos que cobran, ingresos que no cuadran con el subsidio recibido | Frente XI y programas sociales |
| Nómina pública | Muertos de nómina, una misma persona en dos cargos incompatibles | Frente VIII |
| PAE y compras de bienes | Proveedores y precios anómalos, entregas reales por debajo de lo facturado | Frentes VII y XIII |

La regla que evita el desastre: **no es la misma herramienta repetida, es el mismo motor con reglas distintas por dominio.** La infraestructura (integrar datos, comparar contra un patrón normal, marcar lo anómalo, publicarlo) se reutiliza, y ahí está el ahorro: construir el motor una vez y aplicarlo a cinco sectores rinde mucho más que cinco sistemas sueltos. Pero las reglas de detección las diseña quien conoce cada sector, porque lo anómalo en una obra no es lo anómalo en una factura médica, y un cruce mal calibrado produce miles de falsos positivos.

Y el orden de despliegue lo manda el dato, no el dolor: se empieza por los dominios donde la información ya existe y tiene calidad, no por donde más duele el robo. Salud, por ejemplo, exige que la facturación electrónica del sector esté ordenada antes de que el módulo sirva de algo.

Salud merece una salvedad de fondo, porque sus datos son clínicos y personales, los más sensibles que existen. En contratación, cruzar quién le ganó qué a quién es información que debería ser pública. En salud, cruzar la facturación de un paciente roza su historia clínica, donde el habeas data y la reserva médica no son un trámite sino un derecho. La diferencia entre cazar al cartel de los recobros y vigilar al enfermo está en el diseño: trabajar sobre datos agregados y de facturación, no sobre diagnósticos individuales; anonimizar donde se pueda; y mantener al operador independiente y auditable. El mismo cuidado de los límites de abajo, subido de nivel porque el dato es más íntimo.

![Diagrama de la plataforma de integridad: los módulos por dominio (contratación, salud, subsidios, nómina, PAE) alimentan un motor común de detección, que produce alertas con dos salidas, la territorial que congela el desembolso y la nacional que alimenta la Unidad de Macrocorrupción.](img/herramienta-integridad.png)

### Quién la maneja, para que no se vuelva un arma política

Una plataforma que cruza los datos de todos es poderosa y, por eso mismo, peligrosa. El blindaje es parte del diseño, no un añadido: la opera un ente independiente del que ejecuta el gasto (Contraloría y veeduría, como define la sección de la Plataforma de Trazabilidad), sus datos son abiertos y descargables para que cualquier periodista o ciudadano corra sus propias consultas, las alertas son públicas, y las reglas de detección son auditables, para que nadie las afloje a conveniencia ni las afile contra un opositor. Se construye sobre lo que ya existe (SECOP, UIAF y Cuentas Claras ya son estatales o públicos), así que es sobre todo un trabajo de interoperabilidad (Frente VIII) por decreto y reglamento, no una ley nueva. El uso de datos personales se sujeta al habeas data (Ley 1581 de 2012).

### Límites y qué NO puede hacer

Esta es la parte que un vendedor de humo omite y que aquí se dice de frente:

- **No prueba la corrupción, la señala.** Una alerta es una hipótesis, no una condena. La verifica un humano (auditor, fiscal) con debido proceso. Habrá falsos positivos, y tratarlos como culpa sería injusto y además ilegal.
- **No reemplaza al juez ni a la Fiscalía.** Detecta; la sanción sigue su curso con garantías. Por eso el efecto inmediato se ata a una palanca administrativa que el programa sí controla (congelar el desembolso), no a un castigo automático.
- **Vale lo que valgan los datos de entrada.** Si SECOP está mal diligenciado, si los contratos se suben como PDF escaneado, si un municipio no reporta, la herramienta ve menos. Mejorar la calidad y la obligatoriedad del dato no es un detalle técnico, es una precondición.
- **No ve la corrupción que no deja rastro en el gasto formal.** Sobornos en efectivo, tráfico de influencias sin contrato, o la captura "legal" (una norma hecha a la medida de alguien) se le escapan. Para eso hacen falta otras herramientas.
- **Se puede burlar si las reglas son fijas y conocidas.** Quien las conoce puede diseñar el fraude para no dispararlas (un contrato apenas distinto, un precio apenas bajo el umbral). Por eso las reglas tienen que evolucionar y combinarse con análisis humano; una regla congelada se evade.
- **No perfila personas.** No genera puntajes de riesgo sobre individuos ni vigila gente, se enfoca en transacciones y patrones de gasto. Esa frontera es deliberada: la diferencia entre una herramienta de transparencia y una de vigilancia.

> En una frase: la herramienta no atrapa al corrupto sola, le quita el escondite. Hoy la corrupción se esconde en la dispersión, en que ninguna base habla con la otra y nadie compara. Cuando cada peso es rastreable y comparable en público, robar deja de ser fácil e invisible y pasa a ser arriesgado y visible. Ese cambio en el cálculo, más que cualquier captura espectacular, es la meta.

## El papel de la denuncia ciudadana: el sensor que ve donde el dato no llega

La detección por dato tiene un punto ciego inevitable, ya nombrado en los límites: solo ve lo que está digitalizado. El municipio que no reporta, el contrato subido como PDF escaneado, el gasto en efectivo, la zona donde no llega ni el dato ni el Estado, todo eso escapa a la plataforma. Y esos huecos no son aleatorios, coinciden con los lugares de mayor riesgo, porque la ausencia de dato es muchas veces el escondite. Ahí la denuncia ciudadana deja de ser un complemento y se vuelve indispensable: es el sensor humano que llega adonde el dato no llega, el vecino que ve la obra que no se hizo, el empleado que sabe del sobreprecio.

Colombia ya tiene canales (la línea 122 y Denuncia Fácil de la Fiscalía, el portal PACO de la Presidencia, personerías y contralorías locales, veedurías ciudadanas). El problema no es que falten, es que están dispersos, desconectados entre sí y de los datos, y con protección al denunciante débil. El plan no crea un canal nuevo, unifica los que existen y los conecta a la plataforma como uno de sus flujos de entrada.

La conexión con los datos sirve para priorizar, nunca para descartar, y esa distinción es todo:

- La denuncia que coincide con una anomalía que la plataforma ya veía se escala de inmediato, porque el dato la respalda.
- La denuncia que no encuentra nada en los datos no se descarta. Se trata como doble alerta: sobre el hecho denunciado y sobre el punto ciego que reveló, y va a investigación humana tradicional. Que los datos no muestren nada puede significar que no hay nada o que ahí no hay datos, y el sistema solo no distingue cuál, así que el silencio del dato nunca es prueba de inocencia.
- Lo que el sistema no sabe clasificar pasa por una compuerta humana, precisamente porque lo que no encaja en las categorías de la máquina es lo que más puede tocar lo que ella no ve. El triaje nunca es del todo automático, o los puntos ciegos de la máquina se vuelven ley.

Dos salvaguardas cierran el diseño. La queja por mal servicio o mala atención se enruta al sistema de peticiones y quejas, no al embudo anticorrupción, para no ahogarlo con lo que no es corrupción. Y al denunciante de buena fe se le protege aunque se equivoque: la sanción por denuncia falsa se reserva para la mala fe demostrable, la calumnia deliberada, no el error honesto, porque el mismo garrote que asusta al calumniador silencia al que se atreve a denunciar al poderoso.

## La otra batalla: la percepción de corrupción y la confianza pública

Combatir la corrupción y combatir la percepción de corrupción son dos batallas distintas, y un gobierno puede ganar la primera y perder la segunda. La corrupción real se ataca con detección, pruebas y sanción, y de eso trata el resto de este frente. La percepción es otra cosa: es un problema de confianza, no de información, y por eso no se cura con más datos. Se puede tener el gasto más transparente del mundo y aun así una parte del país seguirá convencida de que el gobierno roba, porque esa convicción no se construyó con datos y no se derriba con datos.

Ignorar esa diferencia sale caro. Un Estado honesto pero percibido como corrupto pierde la legitimidad que necesita para gobernar, y le abre la puerta a quien prometa mano dura contra una corrupción que, real o no, la gente ya da por cierta. La confianza pública no es un adorno de la lucha anticorrupción, es parte de ella.

El plan reconoce, además, un límite incómodo: en un país polarizado, una porción de la percepción de corrupción es en realidad polarización disfrazada. Una parte del país percibirá corrupto al gobierno haga lo que haga, solo por ser del bando contrario, igual que percibirá honesto al suyo pase lo que pase. Esa porción no se recupera con transparencia ni con gestos, porque no depende de la conducta del gobierno sino de la tribu de quien mira. Prometer recuperar la confianza de todos sería deshonesto. La meta realista es merecer la confianza con hechos y ganarse a los que todavía juzgan por lo que ven y no por el carnet.

Con esa honestidad de base, el plan trabaja la confianza pública con cuatro palancas, distintas de la detección técnica:

- **La verificabilidad, para que la sospecha se resuelva mirando.** La plataforma de trazabilidad y los datos abiertos no solo detectan el robo, permiten que cualquiera compruebe. Eso no convence al que ya decidió, pero le quita el terreno a la sospecha de buena fe: cambia "yo creo que robaron" por "míralo tú mismo". La desconfianza infundada crece en el vacío de información, y este lo llena.
- **La simetría demostrada, contra el castigo por bando.** La percepción más tóxica no es "hay corruptos", es "solo persiguen a los del otro lado". El plan la combate haciendo visible que la sanción cae por los hechos y no por el color político: se publica que las alertas y los procesos alcanzan a propios y ajenos en proporción a la evidencia, y el primer gesto de un gobierno honesto es investigar a uno de los suyos con la misma dureza con que investigaría a un rival. Un solo aliado procesado con todas las garantías comunica más integridad que mil tableros de datos.
- **Los gestos visibles, porque la gente no juzga por indicadores.** La percepción se mueve con señales concretas y humanas: austeridad real y visible en quien gobierna, un poderoso que por fin responde, decisiones que se sienten como justicia. El plan trata esos gestos como parte de la política anticorrupción y no como cosmética, porque comunican lo que ninguna cifra comunica.
- **La comunicación honesta, no la propaganda.** Un gobierno mudo, o que se declara impoluto, pierde la batalla del relato frente a cualquier demagogo con buena historia. El plan asume que explicar en lenguaje humano lo que se hace, y sobre todo admitir los errores en público, construye más confianza que fingir perfección. La gente confía más en el que reconoce una falla que en el que jura no tener ninguna. Es la misma lógica con que este documento lleva una bitácora de sus propios errores: la honestidad sobre lo que salió mal es lo que vuelve creíble lo que salió bien.

### Cómo se aterriza: dos compromisos verificables

Las palancas anteriores son principios. Para que no se queden en buenas intenciones, dos se convierten en mecanismos concretos, y son los dos que atacan la percepción más dañina, la de que la justicia persigue por bando y no por hechos.

**Reporte público del criterio, no del resultado.** El ente independiente que opera la plataforma (Contraloría y veeduría) publica de forma periódica no un conteo crudo de "cuántos casos de cada partido", que invitaría a leer sesgo donde hay hechos, sino la evidencia de que el criterio de selección fue ciego al color político. Es decir, publica los umbrales y las reglas de alerta, que son los mismos para todos, y la prueba de que ningún caso que cruzó el umbral se archivó por conveniencia y ninguno se abrió sin cruzarlo. La salud del sistema no se mide por si los números salen parejos, se mide por si la regla fue una sola y se aplicó sin excepción. Y vigila con especial celo la señal más reveladora de captura: no que un partido tenga más casos, sino que el partido en el poder tenga sistemáticamente menos de lo esperado. La vara más dura se aplica hacia adentro.

El límite honesto de este mecanismo hay que decirlo, porque es el corazón del asunto. Un criterio ciego puede producir un resultado asimétrico si un partido de verdad comete más corrupción, y esa asimetría no es sesgo, es información sobre la realidad, blindada por un proceso demostrablemente imparcial. Buscar que el reporte salga parejo sería lo contrario de la justicia: sería perseguir por cuotas, proteger al más corrupto o inventarle casos al menos corrupto para cuadrar la foto. La paridad forzada es tan injusta como el sesgo, solo que disfrazada de equilibrio. Por eso el mecanismo promete criterio uniforme y auditable, no simetría de resultados. Y aun así, el partido más señalado alegará persecución, porque le conviene y porque a sus seguidores la pertenencia les pesa más que cualquier auditoría. El reporte convence al que mira de buena fe y desarma al acusador honesto; no silencia al que necesita sentirse perseguido, y no está diseñado para él, sino para todos los demás.

**Compromiso de primer caso propio.** Un gobierno demuestra imparcialidad no cuando castiga al rival, que es lo que se espera de él, sino cuando es severo con los suyos. El compromiso, explícito y desde el arranque, es que la vara más dura se aplique hacia adentro y que las primeras actuaciones anticorrupción visibles alcancen a aliados o a miembros del propio gobierno con las mismas garantías y la misma firmeza con que alcanzarían a un opositor. Se verifica con hechos, no con discursos: o los primeros casos tocan a los propios, o el compromiso quedó en retórica, y el reporte de criterio de arriba lo deja en evidencia. Su límite también es honesto: es un gesto fundacional, no una prueba permanente, y se puede simular sacrificando a un aliado menor. Por eso no vive solo, se sostiene sobre el reporte de criterio ciego, que vigila la impunidad de los propios más allá del gesto inicial. Un solo aliado procesado con todas las garantías comunica, eso sí, más integridad que cualquier campaña.

Ninguna de estas palancas gana la percepción de una vez, y el plan no lo promete. Lo que hace es lo único honesto y sostenible: merecer la confianza con hechos verificables, tratar igual al amigo y al enemigo a la vista de todos, y hablarle a la gente como a adultos. La parte de la desconfianza que es pura trinchera no se conquista, y perseguirla desgasta al gobierno y lo tienta a tratar a sus críticos como enemigos. Saber qué percepción se puede cambiar y cuál no, es también parte de gobernar con integridad.
