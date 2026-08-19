# Tema 26 — Fuentes

> **Título oficial**: Sistemas de almacenamiento y su virtualización. Políticas, sistemas y procedimientos de backup y su recuperación. Backup de sistemas físicos y virtuales.
>
> **Criterio**: todo dato del contenido cita un **ID** inline (p. ej. `[SNIA-DICT]`). Tier 1 = especificaciones y normas técnicas de organismos de estandarización (SNIA, INCITS/T10-T11, NVM Express, IETF, ISO/IEC, NIST) y documentación oficial de plataforma; Tier 2 = documentación de productos, motores y servicios concretos, citada para ilustrar sin atar el tema a un único fabricante; Tier 3 = marco normativo y del puesto, no citado como contenido técnico puro.

---

## Tier 1 — Normas técnicas, especificaciones y documentación oficial de plataforma

| ID | Referencia |
|---|---|
| `[SNIA-DICT]` | Storage Networking Industry Association (SNIA). *SNIA Dictionary* — terminología canónica del almacenamiento (DAS, NAS, SAN, LUN, thin provisioning, deduplicación, snapshot). snia.org/education/dictionary. |
| `[SNIA-SSM]` | SNIA. *Shared Storage Model* — modelo de referencia por capas del almacenamiento compartido (dispositivo, agregación por bloque, sistema de ficheros, aplicación). Marco conceptual de §1 y §2. |
| `[SNIA-SDS]` | SNIA. *Software Defined Storage — White Paper* y *Swordfish/SMI-S*: separación del plano de control y el plano de datos, aprovisionamiento por políticas y gestión estandarizada de sistemas de almacenamiento. |
| `[PATTERSON88]` | Patterson, D. A.; Gibson, G.; Katz, R. H. *A Case for Redundant Arrays of Inexpensive Disks (RAID)*. ACM SIGMOD, 1988 (Universidad de California, Berkeley). Artículo fundacional que define y numera los niveles RAID. |
| `[SNIA-DDF]` | SNIA. *Common RAID Disk Data Format (DDF) Specification* — formato común de metadatos de un conjunto RAID, que permite que un grupo de discos sea reconocido por controladoras distintas. |
| `[T10-SCSI]` | INCITS T10. *SCSI Architecture Model (SAM)* y *SCSI Block Commands (SBC)* — modelo de comandos de bloque (LUN, `READ`/`WRITE`, `UNMAP`) sobre el que se construyen FC e iSCSI. |
| `[T11-FC]` | INCITS T11. *Fibre Channel* — *Framing and Signaling (FC-FS)*, *Fibre Channel Protocol for SCSI (FCP)* y *Fibre Channel over Ethernet (FCoE)*. Define WWN, capas FC-0 a FC-4, servicios de fabric y zoning. |
| `[RFC7143]` | IETF. *RFC 7143: Internet Small Computer System Interface (iSCSI) Protocol (Consolidated)* (2014), que actualiza y consolida el RFC 3720 (2004). Transporte de comandos SCSI sobre TCP/IP; puerto **3260**, nomenclatura **IQN**, autenticación CHAP. |
| `[NVME-OF]` | NVM Express, Inc. *NVM Express over Fabrics (NVMe-oF) Specification* — NVMe sobre RDMA, sobre Fibre Channel y sobre TCP. Modelo de colas paralelas frente al modelo SCSI. |
| `[RFC1813]` | IETF. *RFC 1813: NFS Version 3 Protocol Specification* (1995). |
| `[RFC8881]` | IETF. *RFC 8881: Network File System (NFS) Version 4 Minor Version 1 Protocol* (2020) — sesiones, delegaciones y pNFS. Obsoleta el RFC 5661. |
| `[MS-SMB2]` | Microsoft. *[MS-SMB2] Server Message Block (SMB) Protocol Versions 2 and 3* (especificación abierta) y documentación de SMB 3.x: cifrado en tránsito, *multichannel*, puerto **445**. |
| `[RFC9110]` | IETF HTTP Working Group. *RFC 9110: HTTP Semantics* (2022). Base del acceso REST al almacenamiento de objetos. |
| `[ISO27040]` | ISO/IEC 27040. *Information technology — Security techniques — Storage security*. Norma de referencia sobre seguridad del almacenamiento: cifrado en reposo, saneamiento de soportes, seguridad de SAN/NAS y de las copias de seguridad. |
| `[ISO27002]` | ISO/IEC 27002:2022. *Controles de seguridad de la información*. Control **8.13 «Copia de seguridad de la información»**: copias, pruebas de restauración y periodicidad acordes al negocio. |
| `[ISO22301]` | ISO 22301. *Sistemas de gestión de la continuidad del negocio*. Origen normativo del análisis de impacto en el negocio (BIA) y de los objetivos de recuperación. |
| `[ISO27031]` | ISO/IEC 27031. *Directrices para la preparación de las TIC para la continuidad del negocio*. Enlaza el plan de continuidad (BCP) con el plan de recuperación ante desastres (DRP). |
| `[NIST-SP800-34]` | NIST. *SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems*. Define el ciclo del plan de contingencia, los tipos de emplazamiento alternativo (*hot*, *warm*, *cold site*) y la estrategia de copias. |
| `[NIST-SP800-209]` | NIST. *SP 800-209: Security Guidelines for Storage Infrastructure* (2020). Recomendaciones de seguridad para SAN, NAS, almacenamiento de objetos, cifrado y copias de seguridad. |
| `[NIST-SP800-88]` | NIST. *SP 800-88 Rev. 1: Guidelines for Media Sanitization*. Borrado, purgado y destrucción de soportes: aplicable al fin de vida de discos y cintas de copia. |
| `[MS-VSS]` | Microsoft. *Volume Shadow Copy Service (VSS)* — arquitectura de solicitante, escritores y proveedores para obtener instantáneas **consistentes con la aplicación** en Windows. learn.microsoft.com. |
| `[LVM-LINUX]` | Proyecto LVM2 / *device-mapper* del núcleo Linux. *Logical Volume Manager* — grupos de volúmenes, volúmenes lógicos, instantáneas y aprovisionamiento fino (`lvmthin`). Ejemplo canónico de virtualización de almacenamiento **basada en host**. |
| `[SQLITE-WAL]` | Documentación de motores de base de datos sobre *write-ahead logging* y copia en caliente (`pg_basebackup`, *hot backup*, modo `ARCHIVELOG`). Fundamento de la consistencia de la copia de una base de datos en funcionamiento. |

## Tier 2 — Productos, servicios y tecnologías concretas

| ID | Referencia |
|---|---|
| `[VMW-VADP]` | VMware/Broadcom. *vSphere Storage APIs – Data Protection (VADP)* y *Changed Block Tracking (CBT)*. Modos de transporte SAN, HotAdd, NBD/NBDSSL y API de copia sin agente. |
| `[VMW-SNAP]` | VMware/Broadcom. *Understanding virtual machine snapshots* — ficheros delta, cadena de instantáneas y advertencia expresa de que **una instantánea no es una copia de seguridad**. |
| `[HYPERV-RCT]` | Microsoft. *Hyper-V — Resilient Change Tracking (RCT)*, *production checkpoints* e integración con VSS del invitado. learn.microsoft.com/windows-server/virtualization. |
| `[VSAN]` | VMware/Broadcom. *vSAN — Architecture and design*: almacenamiento distribuido por software sobre discos locales de los nodos del clúster. |
| `[S2D]` | Microsoft. *Storage Spaces Direct (S2D)* — almacenamiento definido por software sobre servidores estándar en Windows Server. |
| `[CEPH]` | Ceph Foundation. *Ceph Documentation* — RADOS, algoritmo CRUSH, réplica y **codificación de borrado** (*erasure coding*), pasarelas de bloque (RBD), de fichero (CephFS) y de objeto (RGW). |
| `[NUTANIX]` | Nutanix. *Nutanix Bible / Web-scale HCI architecture* — infraestructura hiperconvergente con capa de almacenamiento distribuida y localidad de datos. |
| `[S3-LOCK]` | Amazon Web Services. *Amazon S3 Object Lock* — inmutabilidad WORM en modos *governance* y *compliance*, y *legal hold*. Modelo de referencia de la copia inmutable en la nube. |
| `[S3-CLASSES]` | Amazon Web Services. *Amazon S3 storage classes* (Standard, Infrequent Access, Glacier) y equivalentes de otros proveedores. Niveles de coste y tiempo de recuperación del archivo en la nube. |
| `[NDMP]` | SNIA. *Network Data Management Protocol (NDMP)* — protocolo para copiar cabinas NAS sin pasar los datos por un servidor intermedio. |
| `[LTO]` | LTO Program (HPE, IBM, Quantum). *LTO Ultrium roadmap and specifications* — capacidades por generación, cartuchos WORM y compatibilidad hacia atrás. lto.org. |
| `[VEEAM-DOC]` | Veeam. *Backup & Replication User Guide* — verificación automatizada de la restauración en entorno aislado, *instant recovery*, cadenas incremental-para-siempre y repositorios inmutables. Citado como ejemplo de arquitectura de producto. |
| `[VTL]` | Documentación de bibliotecas virtuales de cintas (*Virtual Tape Library*) de fabricantes de sistemas de respaldo: emulación de biblioteca de cintas sobre disco con deduplicación. |

## Tier 3 — Marco normativo y del puesto (contexto, no contenido técnico)

| ID | Referencia |
|---|---|
| `[ENS]` | Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad. **Artículo 26** (continuidad de la actividad) y **Anexo II**: medida **`[mp.info.6]` Copias de seguridad** y grupo **`[op.cont]`** (análisis de impacto, plan de continuidad, pruebas periódicas y medios alternativos). |
| `[CCN-STIC]` | Centro Criptológico Nacional. *Guías CCN-STIC serie 800* (desarrollo de las medidas del ENS; perfiles de cumplimiento y guías de configuración). ccn-cert.cni.es. |
| `[ENI]` | Real Decreto 4/2010, Esquema Nacional de Interoperabilidad, y sus **Normas Técnicas de Interoperabilidad** (política de gestión de documentos electrónicos, digitalización, catálogo de estándares). Marco de la conservación del documento electrónico. |
| `[LEY39-2015]` | Ley 39/2015, del Procedimiento Administrativo Común. **Artículo 17**: archivo electrónico único de los documentos que correspondan a procedimientos finalizados, con garantías de autenticidad, integridad y **conservación**. |
| `[RGPD]` | Reglamento (UE) 2016/679. **Artículo 32** (seguridad del tratamiento: confidencialidad, integridad, **disponibilidad y resiliencia**; capacidad de restaurar el acceso a los datos; verificación regular de la eficacia), **artículo 5.1.e** (limitación del plazo de conservación), **artículos 33-34** (notificación de brechas). |
| `[LOPDGDD]` | Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales. **Artículo 32**: bloqueo de los datos. |
| `[AEPD]` | Agencia Española de Protección de Datos. *Guía de medidas de seguridad*, *Guía para la gestión y notificación de brechas de seguridad* y criterios sobre el ejercicio del derecho de supresión frente a las copias de seguridad. aepd.es. |
| `[BOAM10032]` | BOAM 10.032 (23-dic-2025). Bases específicas TIC C1 Ayto. Madrid — temario oficial. |

---

*Las referencias Tier 1 fijan el fundamento del tema: la terminología y los modelos de SNIA, el artículo fundacional del RAID, las especificaciones de los protocolos de acceso a bloque (T10/T11, iSCSI, NVMe-oF) y a fichero (NFS, SMB), las normas ISO/IEC de seguridad del almacenamiento y de copias, y las guías del NIST sobre contingencia e infraestructura de almacenamiento. Tier 2 documenta productos concretos citados como ejemplo (VADP/CBT, RCT, vSAN, S2D, Ceph, S3 Object Lock, LTO) sin que el tema dependa de ningún fabricante. Tier 3 enmarca la normativa —ENS, ENI, Ley 39/2015, RGPD y LOPDGDD— que convierte la copia de seguridad, en el Ayuntamiento de Madrid, en una obligación jurídica y no solo en una buena práctica técnica.*
