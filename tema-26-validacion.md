# Tema 26 — Checklist de Validación

> **Título oficial**: Sistemas de almacenamiento y su virtualización. Políticas, sistemas y procedimientos de backup y su recuperación. Backup de sistemas físicos y virtuales.
> **Versión**: v1.0 — Pendiente validación
> **Fecha**: 2026-08-20
> **Revisores**: María y Ana (eTrivium) · revisión técnica IAM (Jesús Cuadrado)
> **Instrucciones**: marcar cada ítem. Los cambios no se guardan en la web (imprimir o exportar a PDF si se desea fijarlos).

---

## 1. Cobertura del temario oficial

- [ ] **Arquitecturas de almacenamiento físico**: DAS, SAN y NAS, almacenamiento de objetos y unificado — §1.1
- [ ] **Protocolos y tolerancias**: acceso a bloque (iSCSI, Fibre Channel) y a archivo (NFS, SMB); niveles RAID y técnicas de optimización — §1.2
- [ ] **Conceptos y modelos de virtualización**: basada en host, en red y en array; almacenamiento definido por software — §2.1
- [ ] **Arquitecturas avanzadas**: infraestructuras hiperconvergentes y gestión de pools de recursos — §2.2
- [ ] **Políticas y planificación**: RTO y RPO, retención, ventanas de copia y regla 3-2-1 — §3.1
- [ ] **Tipos y soportes**: completas, incrementales, diferenciales y sintéticas; soportes físicos, lógicos e inmutables en la nube — §3.2
- [ ] **Sistemas y procedimientos de recuperación**: arquitectura del software de copia, verificación, pruebas de restauración y DRP — §3.3
- [ ] **Backup en entornos físicos**: agentes locales y recuperación bare-metal — §4.1
- [ ] **Backup en entornos virtuales**: copias sin agente por API del hipervisor, snapshots y CBT, replicación y recuperación granular — §4.2
- [ ] **Normativa**: ENS (copias y continuidad) y protección de datos (disponibilidad, resiliencia e integridad) — §5.1-5.2

## 2. Contenido teórico

- [ ] El nivel de profundidad (5 secciones, 32 epígrafes, ~17.600 palabras medidas con `wc -w`) es adecuado para C1 (¿hay que ampliar o recortar alguna sección?)
- [ ] La distinción **SAN = bloque / NAS = fichero**, con el criterio de «quién pone el sistema de ficheros», queda suficientemente nítida: es el núcleo conceptual de la primera mitad del tema
- [ ] La distinción **incremental / diferencial** y la de **RPO / RTO** quedan inequívocas: son las dos distinciones centrales de la segunda mitad
- [ ] Las cifras de RAID (capacidad útil n−1 y n−2, penalización de escritura 4 y 6 operaciones) y los puertos (3260, 2049, 445) son correctos
- [ ] La afirmación reiterada de que **RAID ≠ backup**, **snapshot ≠ backup** y **alta disponibilidad ≠ backup** está bien graduada y no resulta repetitiva en exceso
- [ ] Los bloques añadidos más allá del enunciado literal del esqueleto (medios físicos y cinta LTO, NVMe-oF, niveles de consistencia, VSS y LVM, modos de transporte, arquitectura del software de copia, tipos de emplazamiento alternativo, archivo electrónico) aportan valor y no desbordan el nivel C1
- [ ] La frontera con los Temas 11 y 12 (arquitectura y elementos de almacenamiento), 14 (sistemas operativos), 25 (puesto de usuario), 27 (administración del SO), 28 (virtualización de sistemas), 29 (incidencias), 30 (administración de redes), 31 (cloud), 32 (seguridad y criptografía), 34-37 (redes y protocolos) y 39 (ENS/ENI) está clara y sin duplicidades innecesarias
- [ ] Los ejemplos Ayto Madrid (CPD municipal, Padrón, sede electrónica, expedientes, archivo electrónico) son verosímiles y coherentes entre secciones
- [ ] **Vigencia tecnológica**: confirmar que las cifras de capacidad de LTO (LTO-9 18 TB nativos, LTO-10 30 TB nativos en 2025, con cartucho superior anunciado después) siguen siendo las adecuadas en la fecha del examen

## 3. Fuentes

- [ ] Todas las afirmaciones técnicas están respaldadas por fuente Tier 1 (SNIA, INCITS T10/T11, NVM Express, IETF, ISO/IEC, NIST, documentación oficial de plataforma)
- [ ] Las referencias inline se corresponden con `tema-26-fuentes.md`
- [ ] **Verificar la cita normativa exacta**: artículo 26 del RD 311/2022 (continuidad de la actividad), medida `[mp.info.6]` (copias de seguridad) y códigos del grupo `[op.cont]` (op.cont.1 análisis de impacto, op.cont.2 plan de continuidad, op.cont.3 pruebas periódicas, op.cont.4 medios alternativos), así como los niveles a partir de los cuales se exige cada una
- [ ] Atribuciones correctas: RAID formalizado en Berkeley en 1988 (Patterson, Gibson y Katz); iSCSI consolidado en el RFC 7143; NFS 4.1 en el RFC 8881

## 4. Test (60 preguntas)

- [ ] Cada pregunta tiene una sola respuesta correcta e inequívoca
- [ ] Los distractores (A/B/C) son plausibles
- [ ] La distribución de la opción correcta entre A/B/C está equilibrada (**verificada 20/20/20** por el generador)
- [ ] Las explicaciones y referencias de cada respuesta son correctas
- [ ] El reparto por bloques (P1-P16 almacenamiento, P17-P26 virtualización, P27-P48 políticas y procedimientos, P49-P57 físico y virtual, P58-P60 normativa) es el adecuado para el peso de cada parte

## 5. Casos prácticos (3)

- [ ] Realistas y propios del Ayuntamiento (diseño del almacenamiento del CPD; política de copias con cálculo de RTO/RPO y ventana; recuperación ante ransomware)
- [ ] Los cálculos numéricos son correctos (capacidad útil por nivel RAID, caudal de la ventana de copia, RPO y RTO reales)
- [ ] La puntuación de cada caso suma 10 puntos

## 6. Diagramas (14 SVG)

- [ ] Cada diagrama es correcto y legible (también impreso en blanco y negro)
- [ ] Accesibilidad: todos tienen `role="img"` y `aria-label`
- [ ] Sin desbordes de texto ni colisiones de estilo entre SVG (clases con sufijo único, QA de caja contenedora con render en navegador y **pestañas forzadas visibles**)

## 7. Referencias cruzadas a otros temas

- [ ] Validadas contra BOAM 10.032 (T11, T12, T14, T25, T27, T28, T29, T30, T31, T32, T34, T35, T36, T37, T39)
- [ ] Ninguna referencia cruzada cita un enunciado de tema incorrecto

## 8. Calidad editorial

- [ ] Ortografía verificada (tildes y ñ) — sin diacríticos perdidos, también dentro de los `aria-label` de los SVG
- [ ] Coherencia de versión (v1.0) en title, badges, banner y footer del `index.html`
- [ ] El `index.html` abre, navega entre las 8 pestañas y el motor de test funciona
- [ ] Las listas anidadas del Contenido se muestran con sus niveles (sin aplanar)
- [ ] Los bloques de código (`bash`, LVM, `tar`) se muestran correctamente formateados, sin markdown crudo

---

## Observaciones abiertas

_(Espacio para anotaciones de María, Ana y la revisión IAM.)_

- Pendiente confirmar con el IAM si interesa **ampliar la parte normativa** (§5) con el detalle de las medidas del ENS relacionadas con soportes de información (`[mp.si]`) y servicios externos (`[op.ext]`), o si el nivel actual es el adecuado dada la existencia del Tema 39.
- Pendiente decidir si conviene **desarrollar el cálculo económico** del almacenamiento (coste por terabyte por soporte, coste de salida de datos en la nube), que en la parte práctica del examen podría aparecer como problema numérico.
- Este tema comparte frontera especialmente estrecha con el **Tema 28** (virtualización de sistemas y de puestos) y con el **Tema 12** (elementos de almacenamiento): conviene revisar los tres en conjunto cuando estén los tres publicados, para evitar solapamientos y, sobre todo, huecos.
