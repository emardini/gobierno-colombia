> **EJECUCIÓN — abierto a corrección con evidencia.** Cifras, vías jurídicas, plazos y detalles de diseño se discuten vía *issues* y *pull requests*; ver [CONTRIBUTING](../../CONTRIBUTING.md).

# Frente II — Reforma Agraria Integral

**Metas:** titular 3 millones de ha en 4 años; Gini de tierras de ~0.89 a ≤0.82; cero entregas sin paquete habilitador.

| Paso | Medida concreta | Responsable | Plazo |
|---|---|---|---|
| 1. Catastro | Mapear para titular, cobrar predial y planear. Misma inversión que Frente I. | IGAC + SNR | Años 1–8 |
| 2. Titulación masiva | Proceso administrativo simplificado; 750.000 ha/año; prioridad mujeres y jóvenes rurales | ANT | Años 1–4 |
| 3. Redistribución | Fondo de Tierras + extinción de dominio + compra subsidiada; siempre con paquete habilitador | ANT + SGC + Min. Agricultura | Años 2–8 |
| 4. Paquete habilitador | Ninguna tierra sin crédito + asistencia técnica + acceso a mercado + vía | Min. Agricultura + Finagro + SENA | Por entrega |
| 5. Blindaje | No-enajenación 10 años; registro cruzado IGAC–ANT–PILA; informes semestrales públicos | ANT + IGAC | Permanente |

## Jurisdicción Agraria y Rural — ya creada, falta implementarla

La titulación masiva genera conflictos (traslapes, ocupaciones superpuestas, disputas de linderos). Sin un mecanismo judicial ágil y territorialmente presente, esos conflictos bloquean la titulación o producen títulos impugnables. La buena noticia es que la jurisdicción especializada **ya existe**: el Acto Legislativo 03 de 2023 la incorporó a la Constitución y la Ley Estatutaria 2570 de 2026 definió su estructura. El trabajo del programa no es crearla — es **implementarla, financiarla y conectarla a los nodos**, además de empujar la ley ordinaria de competencias y procedimiento que aún está en trámite.

| Componente | Qué hace | Responsable | Plazo |
|---|---|---|---|
| Despliegue de jueces y tribunales en los nodos | El Consejo Superior de la Judicatura crea los despachos agrarios priorizando zonas de nodos y PDET; el Gobierno garantiza los recursos | Consejo Superior de la Judicatura + Min. Justicia + MinHacienda | Años 1–2 |
| Ley ordinaria de competencias y procedimiento | Apoyar el trámite de la ley que define el procedimiento especial agrario (audiencias ágiles, plazos máximos, acceso sin abogado para casos pequeños) | Congreso + Min. Justicia | En curso |
| Articulación con ANT y catastro | El juez accede en tiempo real a la base catastral y a títulos de la ANT; los fallos se registran en IGAC | ANT + IGAC + Rama Judicial | Año 2 |
| Prioridad étnica | Procedimientos diferenciados que respetan la consulta previa y las formas propias de resolución | Min. Interior + Rama Judicial | Año 1 |

**Vía jurídica (verificado):** la jurisdicción ya está constitucionalmente creada (AL 03/2023) y tiene su ley estatutaria de estructura (Ley 2570/2026). Lo pendiente es la ley ordinaria de procedimiento y, sobre todo, la implementación operativa y presupuestal — que depende del Consejo Superior de la Judicatura y del Gobierno, no de un nuevo trámite estatutario. Es, por tanto, mucho más factible de lo que parecía: el plan acelera y financia algo que el ordenamiento ya decidió.

## Tecnología de punta para el catastro — el multiplicador de velocidad

La meta de 750.000 ha/año exige duplicar la velocidad histórica del IGAC. Con detección automática de linderos por IA, drones y registro digital integrado, la productividad por técnico se multiplica de 3 a 5 veces. La tecnología no es adorno — es la condición de posibilidad de la meta.

**Base ya existente en Colombia:** el IGAC tiene contrato activo con Planet Labs (monitoreo satelital diario con IA). En enero de 2026, investigadores colombianos validaron extracción automática de linderos por fusión SAR + óptica con el modelo Segment Anything (SAM), desarrollada para la Reforma Rural Integral. **Referente:** Ruanda registró 10,3 millones de parcelas en menos de cinco años, con costo por título de ~$7 USD, escalando de 15.000 a 376.686 archivos/año (×25) con levantamiento comunitario + verificación tecnológica.

| Capa tecnológica | Cómo se usa | Estado en Colombia | Impacto |
|---|---|---|---|
| IA + imágenes satelitales | Borrador catastral automático (SAR + óptica, SAM reentrenado) que el técnico verifica en campo en vez de levantar desde cero | Metodología validada ene-2026; contrato Planet Labs activo | El técnico verifica, no mide. Productividad ×3–5. |
| Drones UAV ala fija + LiDAR | Levantamiento fotogramétrico (500–2.000 ha/vuelo); LiDAR para dosel denso (Caquetá, Chocó) | CIAC certifica pilotos; SENA incorpora operación en el Servicio (modalidad ambiental) | Cubre zonas inaccesibles; jóvenes del Servicio como operadores |
| Registro digital integrado (modelo Estonia) | El lindero verificado entra una vez y fluye a IGAC, ANT y SNR; sin reentrada manual | Requiere integración IGAC–ANT–SNR; articulado con la plataforma de trazabilidad | Elimina el principal cuello de botella administrativo |
| Inteligencia ambiental en tiempo real | Detección de deforestación, minería ilegal y cambio de uso post-catastro | IGAC ya usa Planet Labs para detección de cambios | Protege la inversión del catastro; alerta antes del daño irreversible |

> El cuello de botella del catastro no es la tecnología — es la integración. Hacer que IA-satelital, drones y registro operen como un sistema único articulado con ANT y SNR, con un solo ingreso de dato, es una decisión de arquitectura institucional, no una inversión tecnológica nueva.
