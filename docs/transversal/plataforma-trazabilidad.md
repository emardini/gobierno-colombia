> **EJECUCIÓN, abierto a corrección con evidencia.** Cifras, vías jurídicas, plazos y detalles de diseño se discuten vía *issues* y *pull requests*; ver [CONTRIBUTING](../../CONTRIBUTING.md).

# Plataforma de Trazabilidad del Gasto Público (el Sistema Nervioso del Estado)

Esta es una sección transversal, no parte de un frente, porque la plataforma no pertenece a ninguno: sirve a todos. Es la infraestructura que sigue cada peso público desde que entra hasta que se gasta en algo real. La cañería de datos sobre la que corren muchas cosas del plan, entre ellas la plataforma de integridad del gasto que se detalla en el Frente IV (su aplicación anticorrupción, con el motor, los módulos por dominio, las dos escalas y los límites).

El reparto es deliberado: aquí vive la infraestructura, en el Frente IV se explica qué corre por ella. Así, cambiar una señal de detección se hace en un solo lugar y no hay que sincronizar dos secciones.

| Componente | Medida | Responsable | Plazo |
|---|---|---|---|
| Integración de bases | Interoperar SECOP, Cuentas Claras, PILA, DIAN, catastro, UIAF y demás fuentes; API pública. Es la base común que alimenta tanto la gestión del gasto como la detección de anomalías | DNP + DIAN + IGAC + UIAF | Año 1 |
| Motor de detección | Corre sobre esta infraestructura. Las señales concretas y los módulos por dominio (contratación, salud, subsidios, nómina) se detallan en el Frente IV, para no duplicarlos aquí | Ente independiente (Contraloría + Veeduría) | Años 1-2 |
| Inteligencia financiera | Uso propio de seguridad, distinto de la detección de corrupción en el gasto: rastreo de flujos financieros de grupos armados, en coordinación con la UIAF | UIAF + Min. Defensa | Años 1-2 |
| Denuncia ciudadana | Canal unificado (integra los que ya existen) como flujo de entrada; es el sensor humano que cubre los puntos ciegos del dato. Su triaje (cruzar para priorizar, nunca para descartar) y sus salvaguardas se detallan en el Frente IV | Secretaría de Transparencia + entes de control | Años 1-2 |
| Vetting de proveedores con historial global | Cruce automático de todo oferente en SECOP contra las listas de inhabilitación del Banco Mundial, el BID, la CAF y las agencias anticorrupción de otros países, antes de adjudicar. La corrupción no es solo doméstica: una empresa sancionada por sobornar en un país entra a Colombia como si nada hubiera pasado, porque hoy nada cruza esa información | Colombia Compra Eficiente + plataforma | Año 1 |
| Datos abiertos | Toda la plataforma descargable; actualización diaria; API para periodistas y veedores | DNP + Min. TIC | Año 2 |
| Independencia | Administrada por ente independiente del que ejecuta; director por méritos; presupuesto protegido | Contraloría + Veeduría | Año 1 |
| Acople a Fiscalía | Las alertas disparan investigación con respuesta máx. 30 días; se publica la tasa de conversión alerta-imputación | Fiscalía + Contraloría | Año 2 |

**Por qué es transversal y no de un frente.** La plataforma habilita al menos cinco frentes a la vez: es la base de la anticorrupción (Frente IV), el control del gasto en salud (Frente VI), la integridad territorial (Frente XIII), la inteligencia financiera de seguridad (Frente III) y la trazabilidad de la titulación y las obras de los nodos (Frentes II y la Columna Vertebral). No es política industrial, es infraestructura del Estado entero.

**Un buen ejemplo de "primer cliente".** Aunque no pertenece al Frente X, la plataforma sí ilustra su principio de compra pública como jalonador: el Estado se compra a sí mismo una capacidad tecnológica nacional, en vez de importarla. Es un caso de "cómprate lo que predicas", y por eso el Frente X la menciona como ejemplo.

## Vetting de proveedores con historial de corrupción global

La corrupción no es solo un problema de contratistas locales. Una empresa sancionada por el Banco Mundial por sobornar funcionarios en África, o inhabilitada por el BID por fraude en una obra en otro país de la región, puede hoy presentarse a un contrato en Colombia sin que nada la detecte, porque las listas de inhabilitación de los organismos multilaterales y de las agencias anticorrupción de otros países no cruzan con SECOP. El plan cierra esa puerta con un mecanismo simple: antes de adjudicar, todo oferente se cruza automáticamente contra las listas de inhabilitación del Banco Mundial, el BID, la CAF y los registros públicos de sanciones de otros países, y el resultado del cruce queda como parte del expediente público del contrato. No es un tribunal nuevo ni un juicio propio, es hacer visible un historial que ya existe en otro lado y que hoy nadie consulta. El costo es bajo, porque las listas son públicas; lo único que faltaba era la costumbre de mirarlas.

## Lo que cuesta y lo que genera

Desarrollar y operar la plataforma exige inversión, pero esa inversión no es solo gasto: es empleo formal de alta calificación (ingeniería de datos, análisis, auditoría), es capacidad estatal que hoy no existe y que queda instalada, y es la clase de activo que, maduro, se puede ofrecer como conocimiento anticorrupción a otros países de la región. Construirla es, en sí mismo, una de las apuestas productivas y de soberanía tecnológica del plan, no un costo administrativo.

## El riesgo de la ruta crítica, y cómo se evita

Aquí hay que ser honestos, porque es el reverso de lo anterior. Si la plataforma habilita cinco frentes a la vez, entonces todo cuelga de ella, y eso la mete en la ruta crítica: si se atrasa, se cae o sale mal hecha, no falla una cosa, fallan todas las que dependían de ella. Y el software estatal de gran escala es, en Colombia y en casi todo el mundo, el tipo de proyecto que llega tarde, cuesta más de lo previsto y a veces no funciona. Poner un megaproyecto de integración de datos como precondición de todo lo demás sería una receta para paralizar el plan.

La salida no es renunciar a la plataforma, es **desacoplarla del arranque**. El plan no espera a que el software esté listo:

- **El arranque opera con control tradicional reforzado.** Antes de cualquier plataforma, el Estado ya controla con interventoría, auditoría de la Contraloría y supervisión de contratos. Para los pocos nodos del inicio (tres, no trescientos), una interventoría intensiva y una auditoría reforzada hechas a mano son perfectamente viables. La plataforma no inventa el control, lo vuelve masivo y barato.
- **La plataforma se construye en paralelo y habilita el escalamiento, no el arranque.** Su función es permitir hacer en cien municipios, de forma automática y difícil de capturar, lo que al principio se hace a mano en tres. Por eso su criticidad vive en el escalamiento, no en el inicio, y ese es un lugar mucho más seguro: el escalamiento sí puede esperar a que la herramienta madure; el arranque no.
- **Se construye por módulos y desde la experiencia, no en abstracto.** Operar manualmente los primeros nodos enseña qué señales importan, dónde está el fraude real y qué datos sirven. La plataforma se diseña a partir de eso, módulo por módulo y por madurez del dato, en vez de diseñarse a ciegas en una oficina. Es la misma lógica del nodo de aprendizaje: probar en pequeño, entender, y solo entonces automatizar.

El costo honesto de este camino: durante el período manual, el control es más caro por peso vigilado, más lento y más vulnerable a la captura local, que es justo lo que la plataforma viene a resolver. Es un sobrecosto temporal de control a cambio de no detener el arranque esperando un software. Es un trueque sensato: mejor pagar control manual en tres nodos por un tiempo que congelar el plan entero hasta que un sistema esté perfecto.

> Un Estado que ve cada peso en tiempo real, con los datos abiertos para que cualquiera mire, cambia el cálculo del que roba: la corrupción deja de esconderse en la dispersión. Esa es la función de la plataforma, y la razón de que sea cimiento y no apéndice. Pero el cimiento no detiene la obra: el arranque se controla a mano, y la plataforma llega para que el control crezca a escala de país.
