# Tema 26 — Casos Prácticos

> **Título oficial**: Sistemas de almacenamiento y su virtualización. Políticas, sistemas y procedimientos de backup y su recuperación. Backup de sistemas físicos y virtuales.
>
> **Formato**: 3 casos prácticos sobre supuestos reales del Ayuntamiento de Madrid. Cada caso suma **10 puntos**.
> **Nivel**: C1 — Técnico Auxiliar TIC, Ayuntamiento de Madrid

Los tres casos recorren la plataforma de almacenamiento y respaldo del CPD municipal (ver tema-26-contenido.md, «Convenciones»): el **Caso 1** trabaja el **diseño del almacenamiento y su virtualización**; el **Caso 2**, la **política de copias, el cálculo de RTO/RPO y la ventana de respaldo**; y el **Caso 3**, la **recuperación real ante un incidente de ransomware** y sus obligaciones normativas.

---

## Caso 1 — Diseño del almacenamiento para el nuevo CPD municipal

### Enunciado

El CPD municipal renueva su plataforma de almacenamiento. Debe dar servicio a cuatro cargas de trabajo:

1. La **base de datos del Padrón municipal**, con escritura intensa y exigencia de latencia mínima.
2. Los discos de **120 máquinas virtuales** (sede electrónica, gestor de expedientes y servicios internos), casi todas con la misma imagen base del sistema operativo.
3. Las **carpetas departamentales** de 1.200 empleados, con documentos ofimáticos y permisos por unidad administrativa.
4. El **archivo electrónico**: documentos de expedientes finalizados, que se escriben una vez, se consultan raramente y deben conservarse muchos años con sus metadatos.

Además, conviven en el CPD una cabina antigua todavía en garantía y la nueva, de fabricante distinto, y se pretende migrar los datos **sin ventana de parada**.

### Cuestiones

**Cuestión 1 — Modo de acceso por carga (3 puntos).** Indique, para cada una de las cuatro cargas, si conviene acceso por **bloque**, por **fichero** o por **objeto**, y justifíquelo en una línea.

**Cuestión 2 — Protocolos y nivel RAID (3 puntos).** Concrete el protocolo de acceso adecuado para las cargas 1, 2 y 3, y proponga el nivel RAID (o esquema de protección) de las cargas 1 y 4, razonando la elección.

**Cuestión 3 — Migración sin parada (2 puntos).** Indique qué modelo de virtualización del almacenamiento permite migrar los datos de la cabina antigua a la nueva sin detener el servicio, y cuál es su inconveniente característico.

**Cuestión 4 — Optimización y su riesgo (2 puntos).** Señale las dos técnicas de optimización que más espacio ahorrarán en la carga 2 y el riesgo operativo que introducen.

### Solución orientativa

- **C1**: (§1.1)

| Carga | Modo de acceso | Justificación |
|---|---|---|
| **Padrón (base de datos)** | **Bloque** | Necesita latencia mínima y modificación parcial de bloques; el motor pone su propio sistema de ficheros |
| **120 máquinas virtuales** | **Bloque** (LUN de almacén de datos; también es válido NFS) | El hipervisor exige acceso de bloque de baja latencia y que varios anfitriones vean el mismo volumen a la vez |
| **Carpetas departamentales** | **Fichero** | 1.200 usuarios concurrentes sobre las mismas carpetas, con permisos y bloqueo de ficheros gestionados por la cabina |
| **Archivo electrónico** | **Objeto** | Se escribe una vez y se lee raramente; necesita metadatos ricos (expediente, retención) y encaja con el versionado y la inmutabilidad |

- **C2**: (§1.2) Protocolos: Padrón y máquinas virtuales, **Fibre Channel** (o **iSCSI** sobre red segregada de 10/25 Gbit/s si el presupuesto lo aconseja; **NVMe-oF** si se busca la latencia mínima); carpetas departamentales, **SMB 3.x** por ser entorno Windows con autenticación de dominio (NFS si fuera Unix). Protección: para el **Padrón**, **RAID 10**, porque su penalización de escritura es de solo dos operaciones frente a las cuatro de RAID 5 y las seis de RAID 6, y la carga es de escritura intensa; para el **archivo electrónico**, **RAID 6** o **codificación de borrado**, porque la carga es de lectura, prima la capacidad y con discos de gran tamaño el riesgo durante la reconstrucción desaconseja RAID 5.

- **C3**: (§2.1.1) Virtualización **basada en red** (appliance o conmutador virtualizador en el fabric) o **virtualización de cabina externa** desde la cabina nueva, que adopta los volúmenes de la antigua y migra los bloques en segundo plano. Inconveniente característico: al operar **en banda**, **añade latencia** y se convierte en un punto crítico que obliga a desplegarla en pareja; además introduce dependencia de ese elemento intermedio.

- **C4**: (§1.2.2) **Deduplicación** (120 máquinas con la misma imagen base ofrecen ratios muy altos, del orden de 5:1 a 20:1) y **thin provisioning** (cada máquina declara mucho más espacio del que consume). Riesgo: el **sobreaprovisionamiento** hace que la suma de lo declarado supere lo físico, de modo que **si el pool se llena de verdad, todos los volúmenes fallan a la vez**; exige umbrales de alerta, vigilancia del llenado real y un procedimiento de ampliación. Sería válido añadir la compresión y el *tiering* automático.

### Criterios de evaluación

| Criterio | Puntos |
|---|---|
| Las cuatro cargas asignadas al modo de acceso correcto, con justificación | 3 |
| Protocolos coherentes y niveles RAID correctamente razonados (RAID 10 por escritura, RAID 6 por capacidad y reconstrucción) | 3 |
| Modelo de virtualización adecuado para la migración sin parada, con su inconveniente | 2 |
| Deduplicación y aprovisionamiento fino, con el riesgo de llenado del pool | 2 |

---

## Caso 2 — Política de copias, RTO/RPO y ventana de respaldo

### Enunciado

La actual política de copias del CPD municipal es única para todos los servicios: **copia completa diaria a las 02:00** al repositorio de disco de la misma sala, con **retención de 14 días**. En la última revisión se detecta que:

1. El responsable del **Padrón** exige un **RPO de 15 minutos** y un **RTO de 1 hora**; restaurar sus 2 TB tarda actualmente unas 3 horas.
2. El volumen total copiado ha crecido hasta **20 TB** y la ventana nocturna disponible es de **8 horas**, con una red de 10 Gbit/s.
3. No existe ninguna copia fuera del edificio y el repositorio está integrado en el dominio corporativo con las mismas credenciales de administración.
4. Nunca se ha realizado una prueba de restauración documentada.

### Cuestiones

**Cuestión 1 — Diagnóstico del Padrón (2 puntos).** Calcule el RPO y el RTO reales del Padrón con la política actual y proponga una corrección para cada uno, explicando por qué son problemas distintos.

**Cuestión 2 — Ventana de copia (3 puntos).** Determine si los 20 TB caben en la ventana de 8 horas y proponga tres medidas para resolver el problema de forma sostenible.

**Cuestión 3 — Regla 3-2-1 (3 puntos).** Enumere los incumplimientos de la regla 3-2-1-1-0 en la situación descrita y proponga el diseño de destinos que la satisfaga.

**Cuestión 4 — Verificación y retención (2 puntos).** Indique qué exige la normativa respecto de las pruebas de restauración y qué esquema de retención propondría, señalando su límite legal.

### Solución orientativa

- **C1**: (§3.1.1) **RPO real: hasta 24 horas** —si el incidente ocurre a las 01:30, se pierden casi un día de altas, bajas y cambios de domicilio—, frente a los 15 minutos comprometidos. **RTO real: al menos 3 horas**, frente a 1 hora. Correcciones: para el **RPO**, añadir **copia del registro de transacciones cada 15 minutos**, que además habilita la recuperación a un instante concreto; para el **RTO**, disponer de una **réplica** de la base de datos en el segundo emplazamiento a la que conmutar, o de una **restauración instantánea** desde el repositorio. Son problemas distintos porque **el RPO se corrige copiando con más frecuencia y el RTO cambiando la tecnología de recuperación**: copiar más a menudo no acelera ni un minuto la restauración.

- **C2**: (§3.1.2) Cálculo: 10 Gbit/s ≈ 1,25 GB/s teóricos; con una eficiencia realista del 60 %, unos **0,75 GB/s**, que en 28.800 segundos dan ≈ **21,6 TB**. Cabe **muy justo**, y solo si el origen y el destino sostienen ese caudal, cosa improbable con muchos ficheros pequeños; en la práctica, la limitación suele ser **la lectura del origen**, no la red. Tres medidas: (a) pasar a **copia completa semanal e incrementales diarios**, o directamente a **incremental para siempre con completas sintéticas**, moviendo solo el 2-5 % diario; (b) **deduplicar y comprimir en origen** y copiar desde **instantáneas** en lugar de desde el sistema vivo; (c) **paralelizar** con varios proxies o servidores de medios y escalonar los trabajos. En entornos virtuales, activar **CBT** para que los incrementales lean solo los bloques cambiados.

- **C3**: (§3.1.2) Incumplimientos: solo hay **dos copias** (original y repositorio) en lugar de tres; **un solo tipo de destino** (disco) en lugar de dos; **ninguna copia fuera de la ubicación** —el repositorio está en la misma sala, expuesto al mismo incendio o inundación—; **ninguna copia inmutable o fuera de línea**, agravado porque el repositorio comparte credenciales del dominio, de modo que **un atacante que comprometa el directorio destruye también las copias**; y **cero verificación**. Diseño propuesto: (1) dato en producción; (2) repositorio de disco con deduplicación en la sala para restauración rápida; (3) **réplica del repositorio al segundo CPD**; (4) **copia inmutable** en objetos con bloqueo WORM y retención de 30 días, más **cinta LTO extraída** y custodiada para el archivo; (5) credenciales separadas y autenticación multifactor en la consola de copias.

- **C4**: (§3.3.2 y §5) Normativa: el **ENS** exige verificar las copias y, en categoría **ALTA**, **probar periódicamente el plan de continuidad** (`[op.cont.3]`); el **RGPD**, en su **artículo 32.1.d**, exige un proceso de **verificación, evaluación y valoración regulares** de la eficacia de las medidas. Por tanto, procede establecer una **prueba de restauración documentada y cronometrada**, de periodicidad al menos trimestral para los servicios críticos, con acta y medición del RTO real. Retención: esquema **GFS** —diarias 14 días, semanales 8 semanas, mensuales 12 meses y anuales según la obligación aplicable—, con el límite del **artículo 5.1.e del RGPD**: la retención debe estar justificada y documentada, y su vencimiento ejecutarse con destrucción segura del soporte.

### Criterios de evaluación

| Criterio | Puntos |
|---|---|
| RPO y RTO reales bien calculados, con corrección diferenciada de cada uno | 2 |
| Cálculo razonado de la ventana y tres medidas técnicamente correctas | 3 |
| Incumplimientos del 3-2-1-1-0 identificados y diseño de destinos que los resuelve | 3 |
| Obligación de prueba de restauración (ENS y RGPD) y esquema de retención con su límite legal | 2 |

---

## Caso 3 — Recuperación ante un incidente de ransomware

### Enunciado

Un sábado por la noche, un código dañino cifra el servidor de ficheros departamental, el gestor de expedientes y **el propio servidor de copias**, cuyo catálogo queda inutilizable. El lunes se comprueba que:

- La **réplica** de las máquinas virtuales al segundo CPD también está cifrada, porque replicó fielmente los bloques ya cifrados.
- La **copia inmutable** en objetos, con retención WORM de 30 días, está intacta.
- Los indicadores del análisis forense sitúan la **primera actividad anómala nueve días antes** del cifrado.
- Entre los datos afectados hay documentos con datos personales de ciudadanos.

### Cuestiones

**Cuestión 1 — Por qué falló la réplica (2 puntos).** Explique por qué la réplica no sirvió y qué papel corresponde a cada mecanismo (réplica, instantánea y copia de seguridad) frente a este incidente.

**Cuestión 2 — Orden de recuperación (3 puntos).** Establezca el orden de las actuaciones de recuperación y justifique cuál debe ser la primera tarea técnica.

**Cuestión 3 — Punto de restauración (2 puntos).** Indique de qué fecha debe restaurarse y qué consecuencia tiene sobre la retención mínima que debe exigir la política.

**Cuestión 4 — Obligaciones normativas (3 puntos).** Enumere las obligaciones derivadas del ENS y del RGPD que activa este incidente, con sus plazos y referencias.

### Solución orientativa

- **C1**: (§4.2.3 y §3.1) La réplica **no protege frente a la corrupción del contenido**: mantiene una copia fiel y actualizada de la máquina virtual, de modo que **replicó el cifrado casi al instante**. Su función es reducir el **RTO** ante el desastre del emplazamiento —se enciende y el servicio vuelve en minutos—, no conservar estados anteriores. La **instantánea** tampoco sirve si vive en el mismo almacén de datos comprometido, y en todo caso su horizonte es de horas. Solo la **copia de seguridad** conserva **profundidad histórica**, y solo la **copia inmutable o fuera de línea** resiste a un atacante con credenciales de administrador. Conclusión: réplica y copia son **complementarias**, y la arquitectura correcta tiene las dos.

- **C2**: (§3.3.2) Orden: (1) **contener** el incidente —aislar la red, detener la propagación, preservar evidencias— y **declarar el desastre** conforme al DRP; (2) **verificar la integridad de la copia inmutable** y determinar el último punto limpio; (3) **reconstruir la infraestructura base**: directorio, DNS, red y, muy señaladamente, el **servidor de copia y su catálogo**, que es la primera tarea técnica ineludible, porque **sin catálogo no hay restauración granular** y no se puede recuperar nada más de forma ordenada; (4) restaurar los servicios **por orden de criticidad** conforme a sus RTO, sobre sistemas reconstruidos desde cero y parcheados, nunca sobre los comprometidos; (5) validar funcionalmente cada servicio antes de reabrirlo; (6) **notificar** y documentar; (7) revisar y actualizar el DRP con las lecciones aprendidas.

- **C3**: (§3.1.2) Debe restaurarse de un punto **anterior a la primera actividad anómala**, es decir, de **más de nueve días atrás**, porque las copias posteriores pueden contener ya las herramientas del atacante o datos comprometidos. Consecuencia: una retención de pocos días **habría dejado a la organización sin ningún punto limpio**. Por tanto, la política debe garantizar una retención escalonada (GFS) que cubra **semanas y meses**, y la copia inmutable debe tener un periodo de retención superior al tiempo típico de permanencia no detectada del atacante. Es la justificación práctica de la retención larga.

- **C4**: (§5) Obligaciones: **ENS** [ENS] — cumplimiento del **artículo 26** (continuidad de la actividad) y de la medida **`[mp.info.6]`**, incluida la exigencia de que las copias no puedan alterarse ni destruirse de forma no autorizada y de que se **autorice y registre** cada restauración; activación de las medidas del grupo **`[op.cont]`** (plan de continuidad, medios alternativos) y del **registro de la actividad** `[op.exp.8]`; notificación del incidente al **CCN-CERT** conforme a los procedimientos de notificación de incidentes del ENS. **RGPD** [RGPD] — la pérdida de **disponibilidad** de datos personales es una **violación de la seguridad**: procede **notificarla a la AEPD en el plazo de 72 horas** desde que se tuvo constancia (art. 33) y, si el riesgo para los derechos y libertades es alto, **comunicarla a los interesados** (art. 34); debe además documentarse el incidente en el registro interno de brechas y revisarse la eficacia de las medidas del **artículo 32**, que exige garantizar la disponibilidad y la resiliencia y **la capacidad de restaurar** el acceso a los datos con rapidez. Sería válido añadir la revisión del análisis de riesgos y la comunicación al delegado de protección de datos.

### Criterios de evaluación

| Criterio | Puntos |
|---|---|
| Explicación correcta de por qué la réplica no protege frente al cifrado, y papel de cada mecanismo | 2 |
| Orden de recuperación coherente, con la reconstrucción del servidor de copia y su catálogo como primera tarea técnica | 3 |
| Punto de restauración anterior a la intrusión y su consecuencia sobre la retención | 2 |
| Obligaciones del ENS (art. 26, mp.info.6, op.cont, notificación) y del RGPD (arts. 32, 33 y 34, con el plazo de 72 horas) | 3 |
