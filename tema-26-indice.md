# Tema 26 — Índice

> **Título oficial**: Sistemas de almacenamiento y su virtualización. Políticas, sistemas y procedimientos de backup y su recuperación. Backup de sistemas físicos y virtuales.
>
> **Bloque**: Parte II — Técnico (Temas 11-40)
> **Nivel**: C1 — Técnico Auxiliar TIC, Ayuntamiento de Madrid

---

## Estructura del tema

1. **Sistemas de almacenamiento de información**
   1.1. Arquitecturas de almacenamiento físico
   1.1.1. Almacenamiento de conexión directa (DAS)
   1.1.2. Redes de área de almacenamiento (SAN) y almacenamiento conectado a red (NAS)
   1.1.3. Almacenamiento de objetos y almacenamiento unificado
   1.2. Protocolos y tolerancias en almacenamiento
   1.2.1. Protocolos de acceso a bloque (iSCSI, Fibre Channel) y archivo (NFS, SMB)
   1.2.2. Niveles RAID y técnicas de optimización (deduplicación, thin provisioning)

2. **Virtualización del almacenamiento**
   2.1. Conceptos y modelos de virtualización
   2.1.1. Virtualización basada en host, en red y en array de almacenamiento
   2.1.2. Almacenamiento definido por software (SDS)
   2.2. Arquitecturas avanzadas de virtualización
   2.2.1. Infraestructuras hiperconvergentes (HCI) y gestión de pools de recursos

3. **Políticas, sistemas y procedimientos de backup y su recuperación**
   3.1. Políticas y planificación de copias de seguridad
   3.1.1. Parámetros RTO y RPO en la planificación de respaldos
   3.1.2. Estrategias de retención, ventanas de backup y regla 3-2-1
   3.2. Tipos y soportes de backup
   3.2.1. Copias completas, incrementales, diferenciales y sintéticas
   3.2.2. Soportes físicos, lógicos y almacenamiento inmutable en la nube
   3.3. Sistemas y procedimientos de recuperación
   3.3.1. Arquitecturas de software de backup (servidores de control, agentes y repositorios)
   3.3.2. Verificación de integridad, pruebas de restauración y planes de recuperación ante desastres (DRP)

4. **Backup de sistemas físicos y virtuales**
   4.1. Backup en entornos físicos
   4.1.1. Copias basadas en agentes locales y recuperación Bare-Metal
   4.2. Backup en entornos virtuales
   4.2.1. Copias sin agentes mediante APIs del hipervisor
   4.2.2. Instantáneas (snapshots) y seguimiento de bloques modificados (CBT)
   4.2.3. Replicación de máquinas virtuales y recuperación granular

5. **Normativa y marco legal en la Administración Pública (material complementario)**
   5.1. Esquema Nacional de Seguridad (ENS)
   5.1.1. Medidas relativas a copias de seguridad y continuidad de la información
   5.2. Protección de datos personales (RGPD y LOPDGDD)
   5.2.1. Principios de disponibilidad, resiliencia e integridad de los respaldos

---

## Conceptos clave para memorizar

| Concepto | Dato clave |
|---|---|
| DAS | Almacenamiento **conectado directamente** a un único servidor por un bus (SAS, SATA, NVMe): sin red de por medio, no se comparte y el sistema de ficheros lo gestiona el servidor |
| NAS | Cabina que sirve **ficheros** por la red IP con NFS o SMB: **el sistema de ficheros vive en la cabina**, y el cliente ve carpetas y ficheros |
| SAN | Red dedicada que sirve **bloques** (LUN) por Fibre Channel, iSCSI o NVMe-oF: **el sistema de ficheros lo pone el servidor**, que ve el LUN como si fuera un disco propio |
| Regla mnemotécnica NAS/SAN | **NAS = fichero** (carpeta compartida) · **SAN = bloque** (disco en bruto). Es la distinción central |
| Almacenamiento de objetos | Espacio de nombres **plano** (contenedores/*buckets*), objeto = dato + **metadatos** + identificador único, acceso por **API REST sobre HTTP**; ideal para archivo y copias, no para bases de datos transaccionales |
| LUN | *Logical Unit Number*: unidad lógica de bloque que una cabina presenta a un servidor; es la unidad de aprovisionamiento en una SAN |
| iSCSI | Comandos SCSI encapsulados en **TCP/IP**, puerto **3260**, nombres **IQN**, autenticación **CHAP**. SAN sobre red Ethernet convencional |
| Fibre Channel | Red de almacenamiento **dedicada** con HBA, conmutadores y **WWN**; el aislamiento lógico se hace con ***zoning*** (en el switch) y ***LUN masking*** (en la cabina) |
| RAID 5 / RAID 6 | Paridad distribuida: RAID 5 tolera **1** disco caído (capacidad útil n−1); RAID 6, **2** discos (capacidad útil n−2). RAID 6 es hoy el mínimo recomendable con discos grandes por el riesgo durante la reconstrucción |
| RAID 0 / 1 / 10 | RAID 0 = *striping* **sin** redundancia (0 tolerancia); RAID 1 = espejo (50 % de capacidad útil); RAID 10 = espejo + *striping*: máximo rendimiento en escritura y mejor reconstrucción |
| RAID ≠ copia de seguridad | El RAID protege del **fallo de un disco**, no del borrado, del cifrado por ransomware ni del error humano: no sustituye al backup |
| Thin provisioning | Se presenta al servidor más capacidad de la asignada físicamente; el espacio se consume **según se escribe**. Exige vigilar el llenado real del pool |
| Deduplicación | Elimina bloques repetidos guardando una sola copia y referencias. **En origen** (menos tráfico de red) o **en destino**; **en línea** (*inline*) o **posproceso** |
| Virtualización de almacenamiento | Tres modelos según dónde se hace: en el **host** (LVM), en la **red** (appliance o switch, típicamente *in-band*) o en la **cabina** (controladora, incluida la virtualización de cabinas de terceros) |
| SDS | Almacenamiento definido por software: separa el **plano de control** (políticas) del **plano de datos**, sobre hardware estándar (Ceph, vSAN, Storage Spaces Direct) |
| HCI | Hiperconvergencia: cómputo + almacenamiento + red **en el mismo nodo**, con una capa de almacenamiento distribuida por software; se crece **añadiendo nodos** (*scale-out*) |
| RPO | *Recovery Point Objective*: **cuántos datos** puedo permitirme perder → determina la **frecuencia** de las copias |
| RTO | *Recovery Time Objective*: **cuánto tiempo** puedo estar caído → determina la **tecnología** de recuperación (réplica, copia en disco, cinta) |
| Regla 3-2-1 | **3** copias de los datos, en **2** soportes distintos, con **1** fuera de la ubicación. Evolución **3-2-1-1-0**: 1 copia **inmutable o desconectada** y **0** errores tras la verificación |
| GFS | *Grandfather-Father-Son*: esquema de retención con copias diarias, semanales, mensuales y anuales de vigencia creciente |
| Copia completa / incremental / diferencial | **Completa**: todo. **Incremental**: lo cambiado desde **la copia anterior** (cadena larga, restauración lenta). **Diferencial**: lo cambiado desde **la última completa** (crece cada día, restauración con solo 2 piezas) |
| Copia sintética | El software **fabrica** una copia completa nueva combinando la completa anterior con los incrementales, **sin volver a leer** el sistema de origen |
| Copia inmutable (WORM) | Escrita una vez y no modificable ni borrable durante un periodo de retención (cinta WORM, *Object Lock*): la defensa principal frente al **ransomware**, que ataca también a las copias |
| VSS | *Volume Shadow Copy Service* de Windows: coordina solicitante, escritores y proveedor para lograr una copia **consistente con la aplicación** (base de datos coherente, no solo los ficheros) |
| Bare-Metal Recovery | Restauración completa de un sistema físico —incluidos sistema operativo, controladores y configuración— sobre hardware vacío, arrancando desde un soporte de rescate |
| Copia sin agente | En entornos virtuales, el software copia el **disco virtual desde el hipervisor** mediante su API (VADP en vSphere, RCT en Hyper-V), sin instalar nada dentro de cada máquina virtual |
| Snapshot vs backup | La instantánea vive en la **misma cabina o el mismo almacén** que el dato original y depende de él: es un punto de retorno rápido, **no una copia de seguridad** |
| CBT | *Changed Block Tracking*: el hipervisor lleva la cuenta de los bloques modificados desde la copia anterior, y el incremental se hace **sin recorrer todo el disco virtual** |
| Réplica de VM | Copia arrancable y actualizada de la máquina virtual en otro emplazamiento: **RTO muy bajo** (encender la réplica), frente a la copia de seguridad, que hay que restaurar |
| ENS | RD 311/2022: **artículo 26** (continuidad de la actividad), medida **`[mp.info.6]` Copias de seguridad** y grupo **`[op.cont]`** (análisis de impacto, plan de continuidad, pruebas periódicas y medios alternativos) |
| RGPD art. 32 | Exige garantizar la **disponibilidad y resiliencia** permanentes, la **capacidad de restaurar** el acceso a los datos rápidamente ante un incidente y la **verificación regular** de la eficacia de las medidas |

---

*Tiempo estimado de estudio: 14-16 horas*
*Extensión del contenido: ~17.600 palabras · 14 diagramas SVG embebidos*
