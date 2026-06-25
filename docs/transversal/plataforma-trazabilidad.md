> **EJECUCIÓN, abierto a corrección con evidencia.** Cifras, vías jurídicas, plazos y detalles de diseño se discuten vía *issues* y *pull requests*; ver [CONTRIBUTING](../../CONTRIBUTING.md).

# Plataforma de Trazabilidad del Gasto Público (el Sistema Nervioso del Estado)

Esta es una sección transversal, no parte de un frente, porque la plataforma no pertenece a ninguno: sirve a todos. Es la infraestructura que sigue cada peso público desde que entra hasta que se gasta en algo real. La cañería de datos sobre la que corren muchas cosas del plan, entre ellas la plataforma de integridad del gasto que se detalla en el Frente IV (su aplicación anticorrupción, con el motor, los módulos por dominio, las dos escalas y los límites).

El reparto es deliberado: aquí vive la infraestructura, en el Frente IV se explica qué corre por ella. Así, cambiar una señal de detección se hace en un solo lugar y no hay que sincronizar dos secciones.

| Componente | Medida | Responsable | Plazo |
|---|---|---|---|
| Integración de bases | Interoperar SECOP, Cuentas Claras, PILA, DIAN, catastro, UIAF y demás fuentes; API pública. Es la base común que alimenta tanto la gestión del gasto como la detección de anomalías | DNP + DIAN + IGAC + UIAF | Año 1 |
| Motor de detección | Corre sobre esta infraestructura. Las señales concretas y los módulos por dominio (contratación, salud, subsidios, nómina) se detallan en el Frente IV, para no duplicarlos aquí | Ente independiente (Contraloría + Veeduría) | Años 1-2 |
| Inteligencia financiera | Uso propio de seguridad, distinto de la detección de corrupción en el gasto: rastreo de flujos financieros de grupos armados, en coordinación con la UIAF | UIAF + Min. Defensa | Años 1-2 |
| Datos abiertos | Toda la plataforma descargable; actualización diaria; API para periodistas y veedores | DNP + Min. TIC | Año 2 |
| Independencia | Administrada por ente independiente del que ejecuta; director por méritos; presupuesto protegido | Contraloría + Veeduría | Año 1 |
| Acople a Fiscalía | Las alertas disparan investigación con respuesta máx. 30 días; se publica la tasa de conversión alerta-imputación | Fiscalía + Contraloría | Año 2 |

**Por qué es transversal y no de un frente.** La plataforma habilita al menos cinco frentes a la vez: es la base de la anticorrupción (Frente IV), el control del gasto en salud (Frente VI), la integridad territorial (Frente XIII), la inteligencia financiera de seguridad (Frente III) y la trazabilidad de la titulación y las obras de los nodos (Frentes II y la Columna Vertebral). No es política industrial, es infraestructura del Estado entero.

**Un buen ejemplo de "primer cliente".** Aunque no pertenece al Frente X, la plataforma sí ilustra su principio de compra pública como jalonador: el Estado se compra a sí mismo una capacidad tecnológica nacional, en vez de importarla. Es un caso de "cómprate lo que predicas", y por eso el Frente X la menciona como ejemplo.

> Un Estado que ve cada peso en tiempo real, con los datos abiertos para que cualquiera mire, cambia el cálculo del que roba: la corrupción deja de esconderse en la dispersión. Esa es la función de la plataforma, y la razón de que sea cimiento y no apéndice.
