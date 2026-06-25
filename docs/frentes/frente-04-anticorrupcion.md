> **EJECUCIÓN, abierto a corrección con evidencia.** Cifras, vías jurídicas, plazos y detalles de diseño se discuten vía *issues* y *pull requests*; ver [CONTRIBUTING](../../CONTRIBUTING.md).

# Frente IV: Anticorrupción

**Meta:** subir Colombia del puesto ~92 al ≤70 en el IPC al final del período.

**El reencuadre:** la corrupción alcanzó 94% de impunidad en 2024 no por falta de leyes, sino por tratarla como suma de delitos individuales. La gran corrupción funciona como sistema que captura instituciones. Se investiga como sistema, con metodologías de macrocriminalidad: identificar aparatos y determinadores, develar modus operandi, rastrear lavado y mecanismos de impunidad.

## La estrategia anticorrupción opera en dos escalas y se apoya en una herramienta

La lucha anticorrupción del plan no está toda en este frente, y conviene leerla como un solo cuerpo aunque sus piezas vivan en lugares distintos por una razón de método. Entra por aquí:

- **Escala nacional y sistémica (este Frente IV).** La gran corrupción tratada como red, no como caso suelto: la Unidad de Macrocorrupción en la Fiscalía, la financiación de campañas, la extinción de dominio, el fondo de reparación.
- **Escala territorial y municipal (Frente XIII, secciones 13.9 y 13.10).** La corrupción en alcaldías y gobernaciones, atacada con diseño de mecanismos: interventoría nacional obligatoria, pago directo nación-proveedor, techos de concentración por empresa, rendición en vivo y un protocolo de alertas por niveles. Vive en el XIII porque su método es el diseño de mecanismos, que es el corazón de ese frente.
- **La herramienta que conecta ambas (la plataforma de trazabilidad, "Sistema Nervioso", Frente X).** La infraestructura de datos que sigue cada peso del gasto público. Aquí abajo se detalla el motor anticorrupción que corre sobre ella, porque es el hilo que cose la escala territorial con la nacional: la misma alerta que congela un contrato municipal puede revelar la red que opera en nueve departamentos.

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

No es una inteligencia artificial que "descubre corruptos". Es un sistema de integración de datos y detección de anomalías que corre sobre la plataforma de trazabilidad del gasto (Frente X). Su premisa es simple: casi toda corrupción que toca el gasto público deja huella en los datos. Una empresa que gana un contrato grande pero no tiene un solo empleado en planilla. Un precio unitario muy por encima del de la región. Un "concurso" con un solo proponente, o con tres que comparten dirección y dueño. La huella existe; el problema es que hoy vive dispersa en bases que no se hablan entre sí. La herramienta no inventa información nueva, hace visible y comparable la que ya existe.

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

Una plataforma que cruza los datos de todos es poderosa y, por eso mismo, peligrosa. El blindaje es parte del diseño, no un añadido: la opera un ente independiente del que ejecuta el gasto (Contraloría y veeduría, como define el Frente X), sus datos son abiertos y descargables para que cualquier periodista o ciudadano corra sus propias consultas, las alertas son públicas, y las reglas de detección son auditables, para que nadie las afloje a conveniencia ni las afile contra un opositor. Se construye sobre lo que ya existe (SECOP, UIAF y Cuentas Claras ya son estatales o públicos), así que es sobre todo un trabajo de interoperabilidad (Frente VIII) por decreto y reglamento, no una ley nueva. El uso de datos personales se sujeta al habeas data (Ley 1581 de 2012).

### Límites y qué NO puede hacer

Esta es la parte que un vendedor de humo omite y que aquí se dice de frente:

- **No prueba la corrupción, la señala.** Una alerta es una hipótesis, no una condena. La verifica un humano (auditor, fiscal) con debido proceso. Habrá falsos positivos, y tratarlos como culpa sería injusto y además ilegal.
- **No reemplaza al juez ni a la Fiscalía.** Detecta; la sanción sigue su curso con garantías. Por eso el efecto inmediato se ata a una palanca administrativa que el programa sí controla (congelar el desembolso), no a un castigo automático.
- **Vale lo que valgan los datos de entrada.** Si SECOP está mal diligenciado, si los contratos se suben como PDF escaneado, si un municipio no reporta, la herramienta ve menos. Mejorar la calidad y la obligatoriedad del dato no es un detalle técnico, es una precondición.
- **No ve la corrupción que no deja rastro en el gasto formal.** Sobornos en efectivo, tráfico de influencias sin contrato, o la captura "legal" (una norma hecha a la medida de alguien) se le escapan. Para eso hacen falta otras herramientas.
- **Se puede burlar si las reglas son fijas y conocidas.** Quien las conoce puede diseñar el fraude para no dispararlas (un contrato apenas distinto, un precio apenas bajo el umbral). Por eso las reglas tienen que evolucionar y combinarse con análisis humano; una regla congelada se evade.
- **No perfila personas.** No genera puntajes de riesgo sobre individuos ni vigila gente, se enfoca en transacciones y patrones de gasto. Esa frontera es deliberada: la diferencia entre una herramienta de transparencia y una de vigilancia.

> En una frase: la herramienta no atrapa al corrupto sola, le quita el escondite. Hoy la corrupción se esconde en la dispersión, en que ninguna base habla con la otra y nadie compara. Cuando cada peso es rastreable y comparable en público, robar deja de ser fácil e invisible y pasa a ser arriesgado y visible. Ese cambio en el cálculo, más que cualquier captura espectacular, es la meta.
