# Tema 26 — Changelog

> **Título oficial**: Sistemas de almacenamiento y su virtualización. Políticas, sistemas y procedimientos de backup y su recuperación. Backup de sistemas físicos y virtuales.

---

## v1.0 — 2026-08-20 — Primera versión

**Estado**: pendiente de validación por María y Ana, y de revisión técnica del IAM (Jesús Cuadrado).

**Motivo**: desarrollo del Tema 26, dentro de la serie de temas técnicos generados desde cero, replicando la estructura y el formato de los Temas 1, 11, 17-24 ya consolidados. El bloque técnico queda con **T11-T24 y T26 publicados**, con el **hueco pendiente del T25**.

### Alcance de la v1.0

| Entregable | Cantidad |
|---|---|
| Contenido teórico | ~17.600 palabras · 5 secciones (fieles al esqueleto oficial) con 32 epígrafes numerados |
| Diagramas SVG inline | 14 (accesibles con `role`/`aria-label`, clases con sufijo único anti-colisión) |
| Banco de preguntas tipo test | 60 preguntas A/B/C con explicación y referencia, balanceadas **20/20/20** (verificado por el generador) |
| Casos prácticos | 3 (diseño del almacenamiento del CPD; política de copias con RTO/RPO y ventana; recuperación ante ransomware) · 10 puntos cada uno |
| Fuentes Tier 1 | 23 referencias canónicas (SNIA, INCITS T10/T11, NVM Express, IETF, ISO/IEC, NIST, documentación de plataforma) |

### Decisiones de generación

1. **Sin material de cliente**: solo el esqueleto `Test_Prompting/temas agosto/26.md`. Desarrollado desde fuentes canónicas (diccionario y modelos de SNIA, artículo fundacional del RAID, RFC de iSCSI y NFS, especificación NVMe-oF, normas ISO/IEC 27040, 27002, 22301 y 27031, guías NIST SP 800-34, 800-209 y 800-88), todas referenciadas.
2. **Estructura fiel al esqueleto oficial**, con numeración jerárquica de hasta tres niveles (H2 > H3 > H4), respetando sus 5 secciones —incluida la quinta, «Normativa y marco legal en la Administración Pública», que el esqueleto añade sobre el enunciado literal del BOAM— sin crear secciones nuevas de primer nivel.
3. **Ampliaciones dentro de los epígrafes existentes** (decisión de generación, no del esqueleto): medios físicos y generaciones de cinta LTO, NVMe over Fabrics, *zoning* y *LUN masking*, niveles de consistencia de la copia, VSS y LVM con órdenes reales, modos de transporte de la copia sin agente, arquitectura de cinco piezas del software de copia, tipos de emplazamiento alternativo y delimitación entre copia de seguridad y archivo electrónico. Todas encajan en epígrafes ya previstos y cubren huecos que en examen se preguntan con frecuencia.
4. **Órdenes y ficheros reales** (`pvcreate`/`vgcreate`/`lvcreate`, instantánea LVM + `tar`) en lugar de pseudocódigo, mismo criterio que T21 con Java/Jakarta, T23 con HTML/JS/PHP y T24 con Kotlin/Swift/Dart: la parte práctica del examen pregunta por herramientas concretas.
5. **Caso de referencia único para todo el tema**: el **CPD municipal** con cuatro cargas de exigencias distintas (Padrón, sede electrónica, gestor de expedientes y archivo electrónico) y un segundo emplazamiento, planteado como **supuesto simplificado** y no como descripción de la infraestructura real del IAM. Concentra las dificultades del tema: convivencia de bloque y fichero, virtualización, RTO y RPO diferenciados, copias de sistemas físicos y virtuales, conservación a largo plazo y obligaciones del ENS y del RGPD.
6. **Tres negaciones como eje pedagógico**: **RAID ≠ copia de seguridad**, **snapshot ≠ copia de seguridad** y **alta disponibilidad o réplica ≠ copia de seguridad**. Son las tres confusiones que más rinden en examen y las tres que más daño hacen en la práctica profesional; se refuerzan con diagramas dedicados (D4, D13, D14) y con varias preguntas de test.
7. **Datos normativos verificados**: se confirmó en fuentes oficiales que la medida de copias de seguridad del RD 311/2022 es **`[mp.info.6]`** (renumerada respecto del RD 3/2010, donde era mp.info.9) y el texto del **artículo 26**. Las capacidades de cinta se contrastaron con el programa LTO: **LTO-9 = 18 TB nativos**, **LTO-10 = 30 TB nativos (2025)**, con un cartucho de mayor capacidad anunciado con posterioridad; el texto se redactó con esa cautela por ser un dato volátil.
8. **Frontera con temas vecinos** cuidada: los dispositivos de almacenamiento en cuanto tales a los Temas 11 y 12; los sistemas operativos al Tema 14; el puesto de usuario final al Tema 25; la administración del sistema operativo al Tema 27; la **virtualización de sistemas y de puestos al Tema 28** (frontera más delicada del tema); la gestión de incidencias al Tema 29; la administración y monitorización de redes al Tema 30; la nube al Tema 31; criptografía y firma al Tema 32; TCP/IP, HTTP/TLS, seguridad de redes y redes locales a los Temas 34-37; y ENS/ENI al Tema 39.
9. **Referencias cruzadas validadas contra BOAM 10.032**: T11, T12, T14, T25, T27, T28, T29, T30, T31, T32, T34, T35, T36, T37, T39. Todas comprobadas contra el enunciado oficial de cada tema.
10. **Anti-colisión de SVG**: las clases CSS de cada diagrama llevan **sufijo numérico único** (`.t1`…`.t14`), evitando el fallo sistémico de estilos que se filtran de un SVG a otro al estar todos embebidos en la misma página (lección de T5).
11. **Distribución A/B/C fijada antes de redactar** y verificada con el generador (lección de T23 y práctica ya consolidada en T24): la secuencia de letras correctas se determinó de antemano y `build_t26.py` confirma **20/20/20**.
12. **QA de diagramas con las pestañas forzadas visibles** (lección de T24): el script de comprobación de desbordes activa todas las `.tab-content` antes de medir y deja una sonda de control, porque `getBBox()` devuelve 0×0 en un subárbol con `display:none` y produce un «0 desbordes» falso.
13. **Cómputo de extensión medido, no estimado**: la cifra de ~17.600 palabras procede de `wc -w` sobre el `.md`. Con el mismo criterio, T24 —hasta ahora el más extenso de la serie— arroja ≈ 12.300, de modo que **este pasa a ser el tema más extenso del bloque técnico**. La diferencia se explica en buena parte por la densidad de tablas comparativas, que el tema pide de forma natural (RAID, protocolos, tipos de copia, soportes, modelos de virtualización).

### Pendientes para QA / próxima iteración

- Validación de profundidad por María/Ana/IAM (¿alguna sección a ampliar o recortar?).
- **Confirmar con el IAM la cita exacta de los códigos `[op.cont.1]` a `[op.cont.4]`** y los niveles del ENS a partir de los cuales se exige cada medida, contra el Anexo II del RD 311/2022.
- Decidir si conviene añadir un tratamiento numérico del **coste** del almacenamiento y de la salida de datos en la nube, de cara a la parte práctica.
- Revisión conjunta con los **Temas 12, 25 y 28** cuando estén los cuatro disponibles, para cerrar solapamientos y huecos.
- **Tema 25 pendiente**: su esqueleto (`Test_Prompting/temas agosto/25.md`) sigue sin desarrollar; conviene abordarlo antes de continuar con T27-T29 para no dejar el hueco abierto.
- Verificación ortográfica con corrector es_ES (cuidado con falsos positivos por términos técnicos en inglés: *striping*, *mirroring*, *thin provisioning*, *snapshot*, *bare-metal*, *air gap*, *failover*, *bucket*, *scale-out*, *hot site*…).

### Origen

Generado el 2026-08-20 en el flujo de trabajo de eTrivium, replicando el patrón de los Temas 1 (v2.1), 11 (v3.2), 17-24 (v1.0). `build_t26.py` y `_build_css.txt` persistidos en el repo.
