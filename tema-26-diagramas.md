# Tema 26 — Catálogo de Diagramas

> **Título oficial**: Sistemas de almacenamiento y su virtualización. Políticas, sistemas y procedimientos de backup y su recuperación. Backup de sistemas físicos y virtuales.
>
> **Versión**: v1.0
> **Fecha**: 2026-08-20
> **Autor**: ETRIVIUM
> **Formato**: SVG inline (zero-dependencias, escalable, imprimible, accesible con role/aria-label)
> **Paleta**: Ayuntamiento de Madrid #0055a0 (primario) + #d13c3c (alertas) + #2d8659 (ventajas) + #e89822 (callouts)
> **Nota técnica**: las clases CSS de cada SVG llevan sufijo numérico único (`.t1`, `.h1`…) para evitar colisiones de estilos entre los 14 diagramas embebidos en la misma página.

---

## Índice de diagramas

| ID | Título | Sección | Tipo | Formato |
|---|---|---|---|---|
| D1 | DAS, SAN y NAS: dónde se traza la frontera de la red | §1.1 | Comparativa de capas | 680×330 |
| D2 | Bloque, fichero y objeto: los tres modos de acceso | §1.1.3 | Comparativa | 680×330 |
| D3 | Protocolos de almacenamiento, transporte y puertos | §1.2.1 | Tabla visual | 680×340 |
| D4 | Niveles RAID: distribución, capacidad útil y tolerancia | §1.2.2 | Esquema anotado | 680×370 |
| D5 | Thin provisioning y deduplicación sobre un pool | §1.2.2 | Esquema | 680×310 |
| D6 | Los tres modelos de virtualización del almacenamiento | §2.1.1 | Capas comparadas | 680×340 |
| D7 | SDS: separación del plano de control y el plano de datos | §2.1.2 | Bloques | 680×310 |
| D8 | Tres capas frente a hiperconvergencia (HCI) | §2.2.1 | Comparativa | 680×330 |
| D9 | RTO y RPO en la línea de tiempo del incidente | §3.1.1 | Línea temporal | 680×300 |
| D10 | Regla 3-2-1-1-0 y retención GFS | §3.1.2 | Esquema + escalera | 680×340 |
| D11 | Completa, incremental, diferencial y sintética | §3.2.1 | Flujo comparado | 680×370 |
| D12 | Arquitectura de una solución de copias de seguridad | §3.3.1 | Bloques | 680×340 |
| D13 | Copia con agente frente a copia sin agente con CBT | §4.2 | Flujo comparado | 680×350 |
| D14 | Escalera de recuperación y anclaje normativo | §4.2.3 y §5 | Escalera + normativa | 680×380 |

---

## D1 · DAS, SAN y NAS: dónde se traza la frontera de la red

**Sección**: §1.1 — Arquitecturas de almacenamiento físico
**Propósito**: Fijar la distinción fundamental del tema: qué se sirve (bloque o fichero), por dónde y, sobre todo, **quién pone el sistema de ficheros**.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 330" role="img" aria-label="Comparación de DAS, SAN y NAS indicando en cada caso qué se sirve (bloque o fichero), por qué medio viaja y si el sistema de ficheros lo gestiona el servidor o la cabina">
  <style>.t1{font:700 11px system-ui,sans-serif;fill:#fff}.s1{font:9px system-ui,sans-serif;fill:#fff}.d1{font:9px system-ui,sans-serif;fill:#333}.h1{font:700 13px system-ui,sans-serif;fill:#0055a0}.k1{font:700 9px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h1">DAS, SAN y NAS: dónde está la frontera de la red</text>
  <rect x="20" y="34" width="200" height="30" rx="5" fill="#0055a0"/><text x="120" y="54" text-anchor="middle" class="t1">DAS</text>
  <rect x="240" y="34" width="200" height="30" rx="5" fill="#2d8659"/><text x="340" y="54" text-anchor="middle" class="t1">SAN</text>
  <rect x="460" y="34" width="200" height="30" rx="5" fill="#e89822"/><text x="560" y="54" text-anchor="middle" class="t1">NAS</text>
  <text x="20" y="82" class="k1">SERVIDOR / CLIENTE</text>
  <rect x="20" y="88" width="200" height="34" rx="4" fill="#eef3f8"/><text x="120" y="103" text-anchor="middle" class="d1">Aplicación</text><text x="120" y="116" text-anchor="middle" class="d1">+ sistema de ficheros</text>
  <rect x="240" y="88" width="200" height="34" rx="4" fill="#eef3f8"/><text x="340" y="103" text-anchor="middle" class="d1">Aplicación</text><text x="340" y="116" text-anchor="middle" class="d1">+ sistema de ficheros</text>
  <rect x="460" y="88" width="200" height="34" rx="4" fill="#eef3f8"/><text x="560" y="105" text-anchor="middle" class="d1">Aplicación</text><text x="560" y="118" text-anchor="middle" class="d1">(pide ficheros)</text>
  <text x="20" y="142" class="k1">POR DÓNDE VIAJA</text>
  <rect x="20" y="148" width="200" height="30" rx="4" fill="#666"/><text x="120" y="167" text-anchor="middle" class="s1">Bus local SAS / SATA / NVMe</text>
  <rect x="240" y="148" width="200" height="30" rx="4" fill="#666"/><text x="340" y="167" text-anchor="middle" class="s1">Red dedicada: FC o iSCSI</text>
  <rect x="460" y="148" width="200" height="30" rx="4" fill="#666"/><text x="560" y="167" text-anchor="middle" class="s1">Red IP: NFS o SMB</text>
  <text x="20" y="198" class="k1">QUÉ SE SIRVE</text>
  <rect x="20" y="204" width="200" height="26" rx="4" fill="#0055a0"/><text x="120" y="221" text-anchor="middle" class="s1">BLOQUE (disco en bruto)</text>
  <rect x="240" y="204" width="200" height="26" rx="4" fill="#2d8659"/><text x="340" y="221" text-anchor="middle" class="s1">BLOQUE (LUN)</text>
  <rect x="460" y="204" width="200" height="26" rx="4" fill="#e89822"/><text x="560" y="221" text-anchor="middle" class="s1">FICHERO (carpeta compartida)</text>
  <text x="20" y="250" class="k1">CABINA / ALMACENAMIENTO</text>
  <rect x="20" y="256" width="200" height="30" rx="4" fill="#eef3f8"/><text x="120" y="275" text-anchor="middle" class="d1">Discos de un solo servidor</text>
  <rect x="240" y="256" width="200" height="30" rx="4" fill="#eef3f8"/><text x="340" y="275" text-anchor="middle" class="d1">Cabina: pools y LUN</text>
  <rect x="460" y="256" width="200" height="30" rx="4" fill="#eef3f8"/><text x="560" y="269" text-anchor="middle" class="d1">Cabina: aquí vive el</text><text x="560" y="281" text-anchor="middle" class="d1">sistema de ficheros</text>
  <rect x="60" y="294" width="560" height="26" rx="5" fill="none" stroke="#0055a0" stroke-width="2"/>
  <text x="340" y="311" text-anchor="middle" class="k1">Sirve bloques → el sistema de ficheros lo pone el SERVIDOR · Sirve ficheros → lo pone la CABINA</text>
  <text x="670" y="328" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: SNIA-DICT; SNIA-SSM]</text>
</svg>
```

---

## D2 · Bloque, fichero y objeto: los tres modos de acceso

**Sección**: §1.1.3 — Almacenamiento de objetos y almacenamiento unificado
**Propósito**: Comparar los tres modos de acceso en sus rasgos decisivos y delimitar para qué sirve —y para qué no— el almacenamiento de objetos.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 330" role="img" aria-label="Comparativa de los tres modos de acceso al almacenamiento: bloque, fichero y objeto, con su unidad, protocolo, metadatos, escalabilidad y uso idóneo">
  <style>.t2{font:700 11px system-ui,sans-serif;fill:#fff}.s2{font:9px system-ui,sans-serif;fill:#fff}.d2{font:9px system-ui,sans-serif;fill:#333}.h2{font:700 13px system-ui,sans-serif;fill:#0055a0}.k2{font:700 9px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h2">Bloque, fichero y objeto</text>
  <rect x="20" y="34" width="200" height="32" rx="5" fill="#0055a0"/><text x="120" y="47" text-anchor="middle" class="t2">BLOQUE</text><text x="120" y="61" text-anchor="middle" class="s2">SAN · DAS</text>
  <rect x="240" y="34" width="200" height="32" rx="5" fill="#e89822"/><text x="340" y="47" text-anchor="middle" class="t2">FICHERO</text><text x="340" y="61" text-anchor="middle" class="s2">NAS</text>
  <rect x="460" y="34" width="200" height="32" rx="5" fill="#2d8659"/><text x="560" y="47" text-anchor="middle" class="t2">OBJETO</text><text x="560" y="61" text-anchor="middle" class="s2">API REST sobre HTTP</text>
  <text x="20" y="84" class="k2">UNIDAD Y ORGANIZACIÓN</text>
  <rect x="20" y="90" width="200" height="34" rx="4" fill="#eef3f8"/><text x="120" y="105" text-anchor="middle" class="d2">Bloque de un LUN</text><text x="120" y="118" text-anchor="middle" class="d2">sin estructura propia</text>
  <rect x="240" y="90" width="200" height="34" rx="4" fill="#eef3f8"/><text x="340" y="105" text-anchor="middle" class="d2">Fichero en un árbol</text><text x="340" y="118" text-anchor="middle" class="d2">jerárquico de carpetas</text>
  <rect x="460" y="90" width="200" height="34" rx="4" fill="#eef3f8"/><text x="560" y="105" text-anchor="middle" class="d2">Objeto en contenedor</text><text x="560" y="118" text-anchor="middle" class="d2">de espacio plano</text>
  <text x="20" y="144" class="k2">METADATOS</text>
  <rect x="20" y="150" width="200" height="26" rx="4" fill="#eef3f8"/><text x="120" y="167" text-anchor="middle" class="d2">Ninguno</text>
  <rect x="240" y="150" width="200" height="26" rx="4" fill="#eef3f8"/><text x="340" y="167" text-anchor="middle" class="d2">Fijos: nombre, fechas, ACL</text>
  <rect x="460" y="150" width="200" height="26" rx="4" fill="#2d8659"/><text x="560" y="167" text-anchor="middle" class="s2">Ricos y extensibles</text>
  <text x="20" y="196" class="k2">MODIFICACIÓN PARCIAL Y LATENCIA</text>
  <rect x="20" y="202" width="200" height="34" rx="4" fill="#2d8659"/><text x="120" y="217" text-anchor="middle" class="s2">Sí · latencia mínima</text><text x="120" y="230" text-anchor="middle" class="s2">(microsegundos)</text>
  <rect x="240" y="202" width="200" height="34" rx="4" fill="#2d8659"/><text x="340" y="217" text-anchor="middle" class="s2">Sí · latencia baja</text><text x="340" y="230" text-anchor="middle" class="s2">(red IP)</text>
  <rect x="460" y="202" width="200" height="34" rx="4" fill="#d13c3c"/><text x="560" y="217" text-anchor="middle" class="s2">No: se escribe una</text><text x="560" y="230" text-anchor="middle" class="s2">versión nueva · HTTP</text>
  <text x="20" y="256" class="k2">USO IDÓNEO</text>
  <rect x="20" y="262" width="200" height="34" rx="4" fill="#eef3f8"/><text x="120" y="277" text-anchor="middle" class="d2">Bases de datos y discos</text><text x="120" y="290" text-anchor="middle" class="d2">de máquinas virtuales</text>
  <rect x="240" y="262" width="200" height="34" rx="4" fill="#eef3f8"/><text x="340" y="277" text-anchor="middle" class="d2">Carpetas compartidas</text><text x="340" y="290" text-anchor="middle" class="d2">y directorios de usuario</text>
  <rect x="460" y="262" width="200" height="34" rx="4" fill="#eef3f8"/><text x="560" y="277" text-anchor="middle" class="d2">Archivo, contenidos y</text><text x="560" y="290" text-anchor="middle" class="d2">copias inmutables</text>
  <text x="340" y="316" text-anchor="middle" class="k2">Escalabilidad creciente de izquierda a derecha · latencia también creciente</text>
  <text x="670" y="328" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: SNIA-DICT; RFC9110; S3-LOCK]</text>
</svg>
```

---

## D3 · Protocolos de almacenamiento, transporte y puertos

**Sección**: §1.2.1 — Protocolos de acceso a bloque y archivo
**Propósito**: Reunir en una sola imagen los protocolos, su tipo de acceso, su transporte y los identificadores y puertos que se preguntan en examen.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 340" role="img" aria-label="Tabla visual de protocolos de almacenamiento: Fibre Channel, FCoE, iSCSI, NVMe over Fabrics, NFS, SMB y HTTP para objetos, con su tipo de acceso, transporte, puerto o identificador y nota característica">
  <style>.t3{font:700 10px system-ui,sans-serif;fill:#fff}.s3{font:9px system-ui,sans-serif;fill:#fff}.d3{font:9px system-ui,sans-serif;fill:#333}.h3{font:700 13px system-ui,sans-serif;fill:#0055a0}.k3{font:700 9px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h3">Protocolos de almacenamiento: acceso, transporte e identificador</text>
  <rect x="20" y="32" width="150" height="22" rx="3" fill="#0055a0"/><text x="95" y="47" text-anchor="middle" class="t3">PROTOCOLO</text>
  <rect x="174" y="32" width="110" height="22" rx="3" fill="#0055a0"/><text x="229" y="47" text-anchor="middle" class="t3">ACCESO</text>
  <rect x="288" y="32" width="180" height="22" rx="3" fill="#0055a0"/><text x="378" y="47" text-anchor="middle" class="t3">TRANSPORTE</text>
  <rect x="472" y="32" width="188" height="22" rx="3" fill="#0055a0"/><text x="566" y="47" text-anchor="middle" class="t3">PUERTO / IDENTIFICADOR</text>
  <rect x="20" y="58" width="150" height="24" rx="3" fill="#eef3f8"/><text x="30" y="74" class="d3">FCP (Fibre Channel)</text>
  <rect x="174" y="58" width="110" height="24" rx="3" fill="#2d8659"/><text x="229" y="74" text-anchor="middle" class="s3">Bloque</text>
  <rect x="288" y="58" width="180" height="24" rx="3" fill="#eef3f8"/><text x="298" y="74" class="d3">Red FC dedicada</text>
  <rect x="472" y="58" width="188" height="24" rx="3" fill="#eef3f8"/><text x="482" y="74" class="d3">WWN · zoning en el switch</text>
  <rect x="20" y="86" width="150" height="24" rx="3" fill="#eef3f8"/><text x="30" y="102" class="d3">FCoE</text>
  <rect x="174" y="86" width="110" height="24" rx="3" fill="#2d8659"/><text x="229" y="102" text-anchor="middle" class="s3">Bloque</text>
  <rect x="288" y="86" width="180" height="24" rx="3" fill="#eef3f8"/><text x="298" y="102" class="d3">Ethernet sin pérdidas</text>
  <rect x="472" y="86" width="188" height="24" rx="3" fill="#eef3f8"/><text x="482" y="102" class="d3">WWN sobre MAC</text>
  <rect x="20" y="114" width="150" height="24" rx="3" fill="#eef3f8"/><text x="30" y="130" class="d3">iSCSI</text>
  <rect x="174" y="114" width="110" height="24" rx="3" fill="#2d8659"/><text x="229" y="130" text-anchor="middle" class="s3">Bloque</text>
  <rect x="288" y="114" width="180" height="24" rx="3" fill="#eef3f8"/><text x="298" y="130" class="d3">TCP/IP (Ethernet)</text>
  <rect x="472" y="114" width="188" height="24" rx="3" fill="#e89822"/><text x="482" y="130" class="s3">3260 · IQN · CHAP</text>
  <rect x="20" y="142" width="150" height="24" rx="3" fill="#eef3f8"/><text x="30" y="158" class="d3">NVMe-oF</text>
  <rect x="174" y="142" width="110" height="24" rx="3" fill="#2d8659"/><text x="229" y="158" text-anchor="middle" class="s3">Bloque</text>
  <rect x="288" y="142" width="180" height="24" rx="3" fill="#eef3f8"/><text x="298" y="158" class="d3">RDMA, FC o TCP</text>
  <rect x="472" y="142" width="188" height="24" rx="3" fill="#eef3f8"/><text x="482" y="158" class="d3">NQN · colas paralelas</text>
  <rect x="20" y="170" width="150" height="24" rx="3" fill="#eef3f8"/><text x="30" y="186" class="d3">NFS (v3 / v4.1)</text>
  <rect x="174" y="170" width="110" height="24" rx="3" fill="#0055a0"/><text x="229" y="186" text-anchor="middle" class="s3">Fichero</text>
  <rect x="288" y="170" width="180" height="24" rx="3" fill="#eef3f8"/><text x="298" y="186" class="d3">TCP/IP · mundo Unix</text>
  <rect x="472" y="170" width="188" height="24" rx="3" fill="#e89822"/><text x="482" y="186" class="s3">2049 · Kerberos · pNFS</text>
  <rect x="20" y="198" width="150" height="24" rx="3" fill="#eef3f8"/><text x="30" y="214" class="d3">SMB 3.x</text>
  <rect x="174" y="198" width="110" height="24" rx="3" fill="#0055a0"/><text x="229" y="214" text-anchor="middle" class="s3">Fichero</text>
  <rect x="288" y="198" width="180" height="24" rx="3" fill="#eef3f8"/><text x="298" y="214" class="d3">TCP/IP · mundo Windows</text>
  <rect x="472" y="198" width="188" height="24" rx="3" fill="#e89822"/><text x="482" y="214" class="s3">445 · cifrado · multichannel</text>
  <rect x="20" y="226" width="150" height="24" rx="3" fill="#eef3f8"/><text x="30" y="242" class="d3">HTTP/S (tipo S3)</text>
  <rect x="174" y="226" width="110" height="24" rx="3" fill="#d13c3c"/><text x="229" y="242" text-anchor="middle" class="s3">Objeto</text>
  <rect x="288" y="226" width="180" height="24" rx="3" fill="#eef3f8"/><text x="298" y="242" class="d3">TCP/IP · REST</text>
  <rect x="472" y="226" width="188" height="24" rx="3" fill="#e89822"/><text x="482" y="242" class="s3">443 · versionado · WORM</text>
  <rect x="20" y="262" width="640" height="30" rx="5" fill="none" stroke="#0055a0" stroke-width="2"/>
  <text x="340" y="281" text-anchor="middle" class="k3">Los cuatro números de examen: iSCSI 3260 · NFS 2049 · SMB 445 · objeto 443 (HTTPS)</text>
  <text x="340" y="312" text-anchor="middle" class="d3">Identificadores: IQN en iSCSI · WWN en Fibre Channel · NQN en NVMe over Fabrics</text>
  <text x="670" y="332" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: RFC7143; T11-FC; RFC8881; MS-SMB2; NVME-OF]</text>
</svg>
```

---

## D4 · Niveles RAID: distribución, capacidad útil y tolerancia

**Sección**: §1.2.2 — Niveles RAID y técnicas de optimización
**Propósito**: Visualizar cómo se reparten datos y paridad en cada nivel y fijar las dos cifras que se preguntan: capacidad útil y número de discos que se toleran.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 370" role="img" aria-label="Esquema de los niveles RAID 0, 1, 5, 6 y 10, mostrando el reparto de datos y paridad entre discos, la capacidad útil y el número de discos cuyo fallo se tolera en cada nivel">
  <style>.t4{font:700 10px system-ui,sans-serif;fill:#fff}.s4{font:8.5px system-ui,sans-serif;fill:#fff}.d4{font:9px system-ui,sans-serif;fill:#333}.h4{font:700 13px system-ui,sans-serif;fill:#0055a0}.k4{font:700 10px system-ui,sans-serif;fill:#0055a0}.n4{font:700 9px system-ui,sans-serif;fill:#fff}</style>
  <text x="340" y="20" text-anchor="middle" class="h4">Niveles RAID: reparto, capacidad útil y tolerancia</text>
  <text x="20" y="44" class="k4">RAID 0 · striping</text>
  <rect x="200" y="32" width="70" height="22" rx="3" fill="#0055a0"/><text x="235" y="47" text-anchor="middle" class="n4">A1</text>
  <rect x="276" y="32" width="70" height="22" rx="3" fill="#0055a0"/><text x="311" y="47" text-anchor="middle" class="n4">A2</text>
  <rect x="352" y="32" width="70" height="22" rx="3" fill="#0055a0"/><text x="387" y="47" text-anchor="middle" class="n4">A3</text>
  <rect x="428" y="32" width="70" height="22" rx="3" fill="#0055a0"/><text x="463" y="47" text-anchor="middle" class="n4">A4</text>
  <text x="510" y="42" class="d4">Útil: 100 %</text><text x="510" y="53" style="font:700 9px system-ui;fill:#d13c3c">Tolera 0 discos</text>
  <text x="20" y="86" class="k4">RAID 1 · espejo</text>
  <rect x="200" y="74" width="146" height="22" rx="3" fill="#2d8659"/><text x="273" y="89" text-anchor="middle" class="n4">A1 A2</text>
  <rect x="352" y="74" width="146" height="22" rx="3" fill="#888"/><text x="425" y="89" text-anchor="middle" class="n4">copia de A1 A2</text>
  <text x="510" y="84" class="d4">Útil: 50 %</text><text x="510" y="95" style="font:700 9px system-ui;fill:#2d8659">Tolera 1 por espejo</text>
  <text x="20" y="128" class="k4">RAID 5 · paridad</text>
  <rect x="200" y="116" width="70" height="22" rx="3" fill="#0055a0"/><text x="235" y="131" text-anchor="middle" class="n4">A1</text>
  <rect x="276" y="116" width="70" height="22" rx="3" fill="#0055a0"/><text x="311" y="131" text-anchor="middle" class="n4">A2</text>
  <rect x="352" y="116" width="70" height="22" rx="3" fill="#0055a0"/><text x="387" y="131" text-anchor="middle" class="n4">A3</text>
  <rect x="428" y="116" width="70" height="22" rx="3" fill="#e89822"/><text x="463" y="131" text-anchor="middle" class="n4">Paridad P</text>
  <text x="510" y="126" class="d4">Útil: n−1</text><text x="510" y="137" style="font:700 9px system-ui;fill:#e89822">Tolera 1 disco</text>
  <text x="20" y="170" class="k4">RAID 6 · doble paridad</text>
  <rect x="200" y="158" width="70" height="22" rx="3" fill="#0055a0"/><text x="235" y="173" text-anchor="middle" class="n4">A1</text>
  <rect x="276" y="158" width="70" height="22" rx="3" fill="#0055a0"/><text x="311" y="173" text-anchor="middle" class="n4">A2</text>
  <rect x="352" y="158" width="70" height="22" rx="3" fill="#e89822"/><text x="387" y="173" text-anchor="middle" class="n4">Paridad P</text>
  <rect x="428" y="158" width="70" height="22" rx="3" fill="#e89822"/><text x="463" y="173" text-anchor="middle" class="n4">Paridad Q</text>
  <text x="510" y="168" class="d4">Útil: n−2</text><text x="510" y="179" style="font:700 9px system-ui;fill:#2d8659">Tolera 2 discos</text>
  <text x="20" y="212" class="k4">RAID 10 · espejo + striping</text>
  <rect x="200" y="200" width="70" height="22" rx="3" fill="#2d8659"/><text x="235" y="215" text-anchor="middle" class="n4">A1</text>
  <rect x="276" y="200" width="70" height="22" rx="3" fill="#888"/><text x="311" y="215" text-anchor="middle" class="n4">copia A1</text>
  <rect x="352" y="200" width="70" height="22" rx="3" fill="#2d8659"/><text x="387" y="215" text-anchor="middle" class="n4">A2</text>
  <rect x="428" y="200" width="70" height="22" rx="3" fill="#888"/><text x="463" y="215" text-anchor="middle" class="n4">copia A2</text>
  <text x="510" y="210" class="d4">Útil: 50 %</text><text x="510" y="221" style="font:700 9px system-ui;fill:#2d8659">Mejor en escritura</text>
  <line x1="20" y1="236" x2="660" y2="236" stroke="#ccc" stroke-width="1"/>
  <rect x="20" y="248" width="205" height="52" rx="5" fill="#d13c3c"/>
  <text x="122" y="266" text-anchor="middle" class="t4">PENALIZACIÓN DE ESCRITURA</text>
  <text x="122" y="282" text-anchor="middle" class="s4">RAID 5: 4 E/S · RAID 6: 6 E/S</text>
  <text x="122" y="295" text-anchor="middle" class="s4">RAID 1 y 10: solo 2 E/S</text>
  <rect x="237" y="248" width="206" height="52" rx="5" fill="#e89822"/>
  <text x="340" y="266" text-anchor="middle" class="t4">RECONSTRUCCIÓN</text>
  <text x="340" y="282" text-anchor="middle" class="s4">Con discos grandes dura horas</text>
  <text x="340" y="295" text-anchor="middle" class="s4">o días: un 2.º fallo lo destruye</text>
  <rect x="455" y="248" width="205" height="52" rx="5" fill="#2d8659"/>
  <text x="557" y="266" text-anchor="middle" class="t4">ELECCIÓN HABITUAL</text>
  <text x="557" y="282" text-anchor="middle" class="s4">Escritura intensa: RAID 10</text>
  <text x="557" y="295" text-anchor="middle" class="s4">Capacidad y lectura: RAID 6</text>
  <rect x="60" y="312" width="560" height="30" rx="5" fill="none" stroke="#d13c3c" stroke-width="2"/>
  <text x="340" y="331" text-anchor="middle" style="font:700 11px system-ui;fill:#d13c3c">El RAID NO es una copia de seguridad: no protege del borrado, la corrupción ni el ransomware</text>
  <text x="670" y="362" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: PATTERSON88; SNIA-DDF]</text>
</svg>
```

---

## D5 · Thin provisioning y deduplicación sobre un pool

**Sección**: §1.2.2 — Técnicas de optimización
**Propósito**: Mostrar cómo el aprovisionamiento fino y la deduplicación desacoplan lo que ve el servidor de lo que se consume físicamente, y cuál es el riesgo asociado.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 310" role="img" aria-label="Esquema del aprovisionamiento fino y la deduplicación: los volúmenes que ven los servidores suman más capacidad de la que existe físicamente en el pool, que solo consume el espacio realmente escrito">
  <style>.t5{font:700 10.5px system-ui,sans-serif;fill:#fff}.s5{font:9px system-ui,sans-serif;fill:#fff}.d5{font:9px system-ui,sans-serif;fill:#333}.h5{font:700 13px system-ui,sans-serif;fill:#0055a0}.k5{font:700 10px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h5">Thin provisioning y deduplicación</text>
  <text x="20" y="44" class="k5">LO QUE VEN LOS SERVIDORES (capacidad declarada: 6 TB)</text>
  <rect x="20" y="52" width="150" height="40" rx="4" fill="#0055a0"/><text x="95" y="70" text-anchor="middle" class="t5">VM Padrón</text><text x="95" y="85" text-anchor="middle" class="s5">declara 2 TB</text>
  <rect x="178" y="52" width="150" height="40" rx="4" fill="#0055a0"/><text x="253" y="70" text-anchor="middle" class="t5">VM Sede</text><text x="253" y="85" text-anchor="middle" class="s5">declara 2 TB</text>
  <rect x="336" y="52" width="150" height="40" rx="4" fill="#0055a0"/><text x="411" y="70" text-anchor="middle" class="t5">VM Expedientes</text><text x="411" y="85" text-anchor="middle" class="s5">declara 1 TB</text>
  <rect x="494" y="52" width="150" height="40" rx="4" fill="#0055a0"/><text x="569" y="70" text-anchor="middle" class="t5">VM Pruebas</text><text x="569" y="85" text-anchor="middle" class="s5">declara 1 TB</text>
  <path d="M340 96 L340 118" stroke="#0055a0" stroke-width="2" marker-end="url(#a5)"/>
  <defs><marker id="a5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#0055a0"/></marker></defs>
  <rect x="20" y="122" width="624" height="26" rx="4" fill="#e89822"/>
  <text x="332" y="139" text-anchor="middle" class="s5">CAPA DE VIRTUALIZACIÓN: thin provisioning (solo se consume lo escrito) + deduplicación + compresión</text>
  <text x="20" y="172" class="k5">LO QUE SE CONSUME DE VERDAD (pool físico: 4 TB)</text>
  <rect x="20" y="180" width="624" height="42" rx="4" fill="#eef3f8" stroke="#888"/>
  <rect x="22" y="182" width="230" height="38" rx="3" fill="#2d8659"/><text x="137" y="199" text-anchor="middle" class="s5">Datos únicos escritos</text><text x="137" y="213" text-anchor="middle" class="s5">1,5 TB</text>
  <rect x="254" y="182" width="120" height="38" rx="3" fill="#888"/><text x="314" y="199" text-anchor="middle" class="s5">Bloques repetidos</text><text x="314" y="213" text-anchor="middle" class="s5">deduplicados</text>
  <rect x="376" y="182" width="266" height="38" rx="3" fill="#fff" stroke="#2d8659" stroke-dasharray="4,3"/><text x="509" y="205" text-anchor="middle" style="font:9px system-ui;fill:#2d8659">Espacio libre real del pool: hay que vigilarlo</text>
  <rect x="20" y="234" width="310" height="42" rx="5" fill="#2d8659"/>
  <text x="175" y="252" text-anchor="middle" class="t5">VENTAJA</text>
  <text x="175" y="268" text-anchor="middle" class="s5">Se aplaza la compra de discos; 6 TB declarados sobre 4 TB reales</text>
  <rect x="342" y="234" width="302" height="42" rx="5" fill="#d13c3c"/>
  <text x="493" y="252" text-anchor="middle" class="t5">RIESGO</text>
  <text x="493" y="268" text-anchor="middle" class="s5">Si el pool se llena de verdad, TODOS los volúmenes fallan a la vez</text>
  <text x="340" y="294" text-anchor="middle" class="k5">Deduplicación: en origen o en destino · en línea (inline) o posproceso</text>
  <text x="670" y="306" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: SNIA-DICT; T10-SCSI]</text>
</svg>
```

---

## D6 · Los tres modelos de virtualización del almacenamiento

**Sección**: §2.1.1 — Virtualización basada en host, en red y en array
**Propósito**: Situar visualmente dónde se ejecuta la capa de virtualización en cada modelo y qué ventaja e inconveniente característicos tiene.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 340" role="img" aria-label="Los tres modelos de virtualización del almacenamiento: basada en host con LVM, basada en red con un appliance en el fabric y basada en cabina con las controladoras, indicando la ventaja y el inconveniente de cada uno">
  <style>.t6{font:700 10.5px system-ui,sans-serif;fill:#fff}.s6{font:9px system-ui,sans-serif;fill:#fff}.d6{font:9px system-ui,sans-serif;fill:#333}.h6{font:700 13px system-ui,sans-serif;fill:#0055a0}.k6{font:700 9px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h6">¿Dónde se ejecuta la capa de virtualización?</text>
  <rect x="20" y="34" width="200" height="26" rx="5" fill="#0055a0"/><text x="120" y="52" text-anchor="middle" class="t6">1 · EN EL HOST</text>
  <rect x="240" y="34" width="200" height="26" rx="5" fill="#e89822"/><text x="340" y="52" text-anchor="middle" class="t6">2 · EN LA RED</text>
  <rect x="460" y="34" width="200" height="26" rx="5" fill="#2d8659"/><text x="560" y="52" text-anchor="middle" class="t6">3 · EN LA CABINA</text>
  <rect x="20" y="70" width="200" height="30" rx="4" fill="#eef3f8" stroke="#0055a0" stroke-width="2"/><text x="120" y="89" text-anchor="middle" class="d6">Servidor + LVM / hipervisor</text>
  <rect x="240" y="70" width="200" height="30" rx="4" fill="#eef3f8"/><text x="340" y="89" text-anchor="middle" class="d6">Servidores</text>
  <rect x="460" y="70" width="200" height="30" rx="4" fill="#eef3f8"/><text x="560" y="89" text-anchor="middle" class="d6">Servidores</text>
  <rect x="20" y="106" width="200" height="30" rx="4" fill="#eef3f8"/><text x="120" y="125" text-anchor="middle" class="d6">Red o bus</text>
  <rect x="240" y="106" width="200" height="30" rx="4" fill="#eef3f8" stroke="#e89822" stroke-width="2"/><text x="340" y="125" text-anchor="middle" class="d6">Appliance o switch virtualizador</text>
  <rect x="460" y="106" width="200" height="30" rx="4" fill="#eef3f8"/><text x="560" y="125" text-anchor="middle" class="d6">Red SAN</text>
  <rect x="20" y="142" width="200" height="30" rx="4" fill="#eef3f8"/><text x="120" y="161" text-anchor="middle" class="d6">Discos o cabina</text>
  <rect x="240" y="142" width="200" height="30" rx="4" fill="#eef3f8"/><text x="340" y="155" text-anchor="middle" class="d6">Cabina A + cabina B</text><text x="340" y="167" text-anchor="middle" class="d6">(fabricantes distintos)</text>
  <rect x="460" y="142" width="200" height="30" rx="4" fill="#eef3f8" stroke="#2d8659" stroke-width="2"/><text x="560" y="161" text-anchor="middle" class="d6">Controladoras: pools y LUN</text>
  <text x="20" y="192" class="k6">VENTAJA</text>
  <rect x="20" y="198" width="200" height="34" rx="4" fill="#2d8659"/><text x="120" y="213" text-anchor="middle" class="s6">Coste nulo e independiente</text><text x="120" y="226" text-anchor="middle" class="s6">del fabricante</text>
  <rect x="240" y="198" width="200" height="34" rx="4" fill="#2d8659"/><text x="340" y="213" text-anchor="middle" class="s6">Unifica cabinas distintas</text><text x="340" y="226" text-anchor="middle" class="s6">y migra sin parar</text>
  <rect x="460" y="198" width="200" height="34" rx="4" fill="#2d8659"/><text x="560" y="213" text-anchor="middle" class="s6">Máximo rendimiento</text><text x="560" y="226" text-anchor="middle" class="s6">y funciones integradas</text>
  <text x="20" y="252" class="k6">INCONVENIENTE</text>
  <rect x="20" y="258" width="200" height="34" rx="4" fill="#d13c3c"/><text x="120" y="273" text-anchor="middle" class="s6">No se comparte entre</text><text x="120" y="286" text-anchor="middle" class="s6">servidores; usa su CPU</text>
  <rect x="240" y="258" width="200" height="34" rx="4" fill="#d13c3c"/><text x="340" y="273" text-anchor="middle" class="s6">Latencia añadida (in-band)</text><text x="340" y="286" text-anchor="middle" class="s6">y punto crítico a duplicar</text>
  <rect x="460" y="258" width="200" height="34" rx="4" fill="#d13c3c"/><text x="560" y="273" text-anchor="middle" class="s6">Atado al fabricante y</text><text x="560" y="286" text-anchor="middle" class="s6">limitado a esa cabina</text>
  <text x="340" y="312" text-anchor="middle" class="k6">In-band: los datos atraviesan la capa · Out-of-band: solo la atraviesan los metadatos</text>
  <text x="670" y="332" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: SNIA-DICT; SNIA-SSM; LVM-LINUX]</text>
</svg>
```

---

## D7 · SDS: separación del plano de control y el plano de datos

**Sección**: §2.1.2 — Almacenamiento definido por software
**Propósito**: Explicar el rasgo que define al SDS y en qué se diferencia de una cabina tradicional.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 310" role="img" aria-label="Esquema del almacenamiento definido por software: un plano de control que aplica políticas sobre un plano de datos formado por servidores estándar con discos locales, frente al modelo de cabina tradicional">
  <style>.t7{font:700 11px system-ui,sans-serif;fill:#fff}.s7{font:9px system-ui,sans-serif;fill:#fff}.d7{font:9px system-ui,sans-serif;fill:#333}.h7{font:700 13px system-ui,sans-serif;fill:#0055a0}.k7{font:700 9px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h7">Almacenamiento definido por software (SDS)</text>
  <rect x="20" y="34" width="640" height="46" rx="5" fill="#0055a0"/>
  <text x="340" y="52" text-anchor="middle" class="t7">PLANO DE CONTROL — políticas, no cables</text>
  <text x="340" y="70" text-anchor="middle" class="s7">«3 réplicas · cifrado · mínimo 5.000 IOPS · tolerar la caída de un nodo» · API y automatización</text>
  <path d="M340 84 L340 104" stroke="#0055a0" stroke-width="2" marker-end="url(#a7)"/>
  <defs><marker id="a7" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#0055a0"/></marker></defs>
  <text x="20" y="120" class="k7">PLANO DE DATOS — servidores estándar con discos locales</text>
  <rect x="20" y="126" width="150" height="56" rx="4" fill="#2d8659"/><text x="95" y="146" text-anchor="middle" class="s7">Nodo 1</text><text x="95" y="162" text-anchor="middle" class="s7">discos SAS/NVMe</text><text x="95" y="176" text-anchor="middle" class="s7">réplica de bloques</text>
  <rect x="178" y="126" width="150" height="56" rx="4" fill="#2d8659"/><text x="253" y="146" text-anchor="middle" class="s7">Nodo 2</text><text x="253" y="162" text-anchor="middle" class="s7">discos SAS/NVMe</text><text x="253" y="176" text-anchor="middle" class="s7">réplica de bloques</text>
  <rect x="336" y="126" width="150" height="56" rx="4" fill="#2d8659"/><text x="411" y="146" text-anchor="middle" class="s7">Nodo 3</text><text x="411" y="162" text-anchor="middle" class="s7">discos SAS/NVMe</text><text x="411" y="176" text-anchor="middle" class="s7">réplica de bloques</text>
  <rect x="494" y="126" width="150" height="56" rx="4" fill="#888"/><text x="569" y="146" text-anchor="middle" class="s7">Nodo N…</text><text x="569" y="162" text-anchor="middle" class="s7">se crece añadiendo</text><text x="569" y="176" text-anchor="middle" class="s7">nodos (scale-out)</text>
  <rect x="20" y="190" width="624" height="24" rx="4" fill="#e89822"/>
  <text x="332" y="206" text-anchor="middle" class="s7">Red interna de 10/25 Gbit/s redundante: en SDS y HCI la red FORMA PARTE del almacenamiento</text>
  <rect x="20" y="226" width="310" height="56" rx="5" fill="#eef3f8" stroke="#888"/>
  <text x="175" y="244" text-anchor="middle" class="k7">CABINA TRADICIONAL</text>
  <text x="175" y="260" text-anchor="middle" class="d7">Hardware propietario · RAID en la</text>
  <text x="175" y="274" text-anchor="middle" class="d7">controladora · crecimiento vertical</text>
  <rect x="342" y="226" width="302" height="56" rx="5" fill="#eef3f8" stroke="#0055a0" stroke-width="2"/>
  <text x="493" y="244" text-anchor="middle" class="k7">SDS</text>
  <text x="493" y="260" text-anchor="middle" class="d7">Hardware estándar · réplica o erasure coding</text>
  <text x="493" y="274" text-anchor="middle" class="d7">por software · crecimiento horizontal</text>
  <text x="340" y="298" text-anchor="middle" class="k7">Ejemplos: Ceph (CRUSH) · vSAN · Storage Spaces Direct</text>
  <text x="670" y="306" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: SNIA-SDS; CEPH; VSAN; S2D]</text>
</svg>
```

---

## D8 · Tres capas frente a hiperconvergencia (HCI)

**Sección**: §2.2.1 — Infraestructuras hiperconvergentes y gestión de pools
**Propósito**: Contraponer la arquitectura clásica de tres capas con la hiperconvergente y hacer visible que en HCI desaparece la cabina y se crece por nodos.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 330" role="img" aria-label="Comparación entre la arquitectura de tres capas, con servidores, red de almacenamiento y cabina separados, y la arquitectura hiperconvergente, en la que cada nodo aporta cómputo y discos locales agregados por software">
  <style>.t8{font:700 10.5px system-ui,sans-serif;fill:#fff}.s8{font:9px system-ui,sans-serif;fill:#fff}.d8{font:9px system-ui,sans-serif;fill:#333}.h8{font:700 13px system-ui,sans-serif;fill:#0055a0}.k8{font:700 9.5px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h8">Tres capas frente a hiperconvergencia</text>
  <rect x="20" y="32" width="310" height="24" rx="5" fill="#888"/><text x="175" y="49" text-anchor="middle" class="t8">ARQUITECTURA DE TRES CAPAS</text>
  <rect x="350" y="32" width="310" height="24" rx="5" fill="#0055a0"/><text x="505" y="49" text-anchor="middle" class="t8">HIPERCONVERGENCIA (HCI)</text>
  <rect x="20" y="64" width="310" height="34" rx="4" fill="#eef3f8" stroke="#888"/><text x="175" y="78" text-anchor="middle" class="d8">Servidores de cómputo</text><text x="175" y="91" text-anchor="middle" class="d8">(se compran y crecen por separado)</text>
  <rect x="20" y="104" width="310" height="34" rx="4" fill="#eef3f8" stroke="#888"/><text x="175" y="118" text-anchor="middle" class="d8">Red de almacenamiento FC o iSCSI</text><text x="175" y="131" text-anchor="middle" class="d8">(zoning, LUN masking, multipathing)</text>
  <rect x="20" y="144" width="310" height="34" rx="4" fill="#eef3f8" stroke="#888"/><text x="175" y="158" text-anchor="middle" class="d8">Cabina de almacenamiento</text><text x="175" y="171" text-anchor="middle" class="d8">(consola y equipo propios)</text>
  <rect x="350" y="64" width="150" height="56" rx="4" fill="#2d8659"/><text x="425" y="82" text-anchor="middle" class="s8">NODO 1</text><text x="425" y="98" text-anchor="middle" class="s8">CPU + RAM</text><text x="425" y="112" text-anchor="middle" class="s8">+ discos locales</text>
  <rect x="510" y="64" width="150" height="56" rx="4" fill="#2d8659"/><text x="585" y="82" text-anchor="middle" class="s8">NODO 2</text><text x="585" y="98" text-anchor="middle" class="s8">CPU + RAM</text><text x="585" y="112" text-anchor="middle" class="s8">+ discos locales</text>
  <rect x="350" y="126" width="150" height="52" rx="4" fill="#2d8659"/><text x="425" y="144" text-anchor="middle" class="s8">NODO 3</text><text x="425" y="160" text-anchor="middle" class="s8">CPU + RAM</text><text x="425" y="173" text-anchor="middle" class="s8">+ discos locales</text>
  <rect x="510" y="126" width="150" height="52" rx="4" fill="#888"/><text x="585" y="144" text-anchor="middle" class="s8">NODO 4…</text><text x="585" y="160" text-anchor="middle" class="s8">se crece</text><text x="585" y="173" text-anchor="middle" class="s8">añadiendo nodos</text>
  <rect x="350" y="184" width="310" height="24" rx="4" fill="#e89822"/><text x="505" y="200" text-anchor="middle" class="s8">Capa SDS distribuida: un pool único con todos los discos</text>
  <rect x="20" y="184" width="310" height="24" rx="4" fill="#eef3f8"/><text x="175" y="200" text-anchor="middle" class="d8">Tres equipos, tres consolas, tres ciclos de compra</text>
  <line x1="20" y1="220" x2="660" y2="220" stroke="#ccc" stroke-width="1"/>
  <rect x="20" y="230" width="310" height="34" rx="4" fill="#2d8659"/><text x="175" y="245" text-anchor="middle" class="s8">A favor: control y ajuste fino de cada capa;</text><text x="175" y="258" text-anchor="middle" class="s8">se dimensiona cada recurso por separado</text>
  <rect x="350" y="230" width="310" height="34" rx="4" fill="#2d8659"/><text x="505" y="245" text-anchor="middle" class="s8">A favor: una sola consola y crecimiento</text><text x="505" y="258" text-anchor="middle" class="s8">incremental por nodos, sin fabric FC</text>
  <rect x="20" y="268" width="310" height="34" rx="4" fill="#d13c3c"/><text x="175" y="283" text-anchor="middle" class="s8">En contra: complejidad y silos de</text><text x="175" y="296" text-anchor="middle" class="s8">administración entre equipos distintos</text>
  <rect x="350" y="268" width="310" height="34" rx="4" fill="#d13c3c"/><text x="505" y="283" text-anchor="middle" class="s8">En contra: cómputo y capacidad crecen</text><text x="505" y="296" text-anchor="middle" class="s8">juntos; la red entre nodos es crítica</text>
  <text x="340" y="318" text-anchor="middle" class="k8">Regla de dimensionado: reservar espacio libre para que el pool pueda reconstruirse si cae un nodo</text>
  <text x="670" y="328" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: VSAN; NUTANIX; S2D]</text>
</svg>
```

---

## D9 · RTO y RPO en la línea de tiempo del incidente

**Sección**: §3.1.1 — Parámetros RTO y RPO
**Propósito**: Fijar de una vez la diferencia entre los dos parámetros, situándolos a un lado y otro del incidente.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" role="img" aria-label="Línea de tiempo de un incidente que sitúa el RPO hacia atrás, como cantidad de datos que se pierden desde la última copia, y el RTO hacia delante, como tiempo de interrupción hasta que el servicio vuelve a estar operativo">
  <style>.t9{font:700 10.5px system-ui,sans-serif;fill:#fff}.s9{font:9px system-ui,sans-serif;fill:#fff}.d9{font:9px system-ui,sans-serif;fill:#333}.h9{font:700 13px system-ui,sans-serif;fill:#0055a0}.k9{font:700 10px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h9">RPO mira al pasado · RTO mira al futuro</text>
  <line x1="30" y1="120" x2="650" y2="120" stroke="#333" stroke-width="2"/>
  <circle cx="150" cy="120" r="6" fill="#0055a0"/><circle cx="340" cy="120" r="8" fill="#d13c3c"/><circle cx="560" cy="120" r="6" fill="#2d8659"/>
  <text x="150" y="142" text-anchor="middle" class="d9">Última copia válida</text>
  <text x="340" y="142" text-anchor="middle" style="font:700 10px system-ui;fill:#d13c3c">INCIDENTE</text>
  <text x="560" y="142" text-anchor="middle" class="d9">Servicio restablecido</text>
  <text x="150" y="155" text-anchor="middle" class="d9">02:00</text>
  <text x="340" y="155" text-anchor="middle" class="d9">06:00</text>
  <text x="560" y="155" text-anchor="middle" class="d9">08:00</text>
  <rect x="150" y="76" width="190" height="30" rx="4" fill="#e89822"/>
  <text x="245" y="95" text-anchor="middle" class="s9">RPO = datos perdidos (4 h)</text>
  <rect x="340" y="76" width="220" height="30" rx="4" fill="#2d8659"/>
  <text x="450" y="95" text-anchor="middle" class="s9">RTO = tiempo de parada (2 h)</text>
  <path d="M338 66 L152 66" stroke="#e89822" stroke-width="2" marker-end="url(#a9)"/>
  <path d="M342 66 L558 66" stroke="#2d8659" stroke-width="2" marker-end="url(#b9)"/>
  <defs>
    <marker id="a9" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#e89822"/></marker>
    <marker id="b9" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2d8659"/></marker>
  </defs>
  <rect x="20" y="176" width="310" height="60" rx="5" fill="#e89822"/>
  <text x="175" y="195" text-anchor="middle" class="t9">RPO · Recovery Point Objective</text>
  <text x="175" y="212" text-anchor="middle" class="s9">Cuántos DATOS puedo perder</text>
  <text x="175" y="228" text-anchor="middle" class="s9">→ determina la FRECUENCIA de la copia</text>
  <rect x="350" y="176" width="310" height="60" rx="5" fill="#2d8659"/>
  <text x="505" y="195" text-anchor="middle" class="t9">RTO · Recovery Time Objective</text>
  <text x="505" y="212" text-anchor="middle" class="s9">Cuánto TIEMPO puedo estar caído</text>
  <text x="505" y="228" text-anchor="middle" class="s9">→ determina la TECNOLOGÍA de recuperación</text>
  <rect x="60" y="248" width="560" height="30" rx="5" fill="none" stroke="#0055a0" stroke-width="2"/>
  <text x="340" y="267" text-anchor="middle" class="k9">Ambos salen del análisis de impacto (BIA) y se fijan servicio por servicio · RTO &lt; MTD</text>
  <text x="670" y="294" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: ISO22301; NIST-SP800-34]</text>
</svg>
```

---

## D10 · Regla 3-2-1-1-0 y retención GFS

**Sección**: §3.1.2 — Estrategias de retención, ventanas y regla 3-2-1
**Propósito**: Fijar la regla de oro del respaldo, su extensión frente al ransomware y el esquema de retención escalonada.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 340" role="img" aria-label="Esquema de la regla 3-2-1 ampliada a 3-2-1-1-0, con tres copias en dos soportes, una fuera de la ubicación, una copia inmutable o fuera de línea y cero errores de verificación, junto al esquema de retención abuelo-padre-hijo">
  <style>.t10{font:700 11px system-ui,sans-serif;fill:#fff}.s10{font:9px system-ui,sans-serif;fill:#fff}.d10{font:9px system-ui,sans-serif;fill:#333}.h10{font:700 13px system-ui,sans-serif;fill:#0055a0}.k10{font:700 9.5px system-ui,sans-serif;fill:#0055a0}.n10{font:700 20px system-ui,sans-serif;fill:#fff}</style>
  <text x="340" y="20" text-anchor="middle" class="h10">La regla 3-2-1-1-0</text>
  <rect x="20" y="32" width="124" height="76" rx="5" fill="#0055a0"/><text x="82" y="60" text-anchor="middle" class="n10">3</text><text x="82" y="80" text-anchor="middle" class="s10">copias de los datos</text><text x="82" y="95" text-anchor="middle" class="s10">(original + 2)</text>
  <rect x="150" y="32" width="124" height="76" rx="5" fill="#0055a0"/><text x="212" y="60" text-anchor="middle" class="n10">2</text><text x="212" y="80" text-anchor="middle" class="s10">soportes o sistemas</text><text x="212" y="95" text-anchor="middle" class="s10">distintos</text>
  <rect x="280" y="32" width="124" height="76" rx="5" fill="#0055a0"/><text x="342" y="60" text-anchor="middle" class="n10">1</text><text x="342" y="80" text-anchor="middle" class="s10">fuera de la ubicación</text><text x="342" y="95" text-anchor="middle" class="s10">(otro CPD o proveedor)</text>
  <rect x="410" y="32" width="124" height="76" rx="5" fill="#d13c3c"/><text x="472" y="60" text-anchor="middle" class="n10">1</text><text x="472" y="80" text-anchor="middle" class="s10">inmutable o fuera</text><text x="472" y="95" text-anchor="middle" class="s10">de línea (air gap)</text>
  <rect x="540" y="32" width="120" height="76" rx="5" fill="#2d8659"/><text x="600" y="60" text-anchor="middle" class="n10">0</text><text x="600" y="80" text-anchor="middle" class="s10">errores tras la</text><text x="600" y="95" text-anchor="middle" class="s10">verificación</text>
  <rect x="20" y="118" width="640" height="26" rx="4" fill="#e89822"/>
  <text x="340" y="135" text-anchor="middle" class="s10">Los dos últimos dígitos los añade el ransomware: ataca primero las copias y el catálogo para impedir la recuperación</text>
  <text x="20" y="166" class="k10">RETENCIÓN ESCALONADA — GFS (abuelo, padre, hijo)</text>
  <rect x="20" y="174" width="155" height="56" rx="4" fill="#eef3f8" stroke="#0055a0"/><text x="97" y="192" text-anchor="middle" class="k10">HIJO · diaria</text><text x="97" y="208" text-anchor="middle" class="d10">Se conserva 7-14 días</text><text x="97" y="222" text-anchor="middle" class="d10">Errores del día a día</text>
  <rect x="183" y="174" width="155" height="56" rx="4" fill="#eef3f8" stroke="#0055a0"/><text x="260" y="192" text-anchor="middle" class="k10">PADRE · semanal</text><text x="260" y="208" text-anchor="middle" class="d10">Se conserva 4-8 semanas</text><text x="260" y="222" text-anchor="middle" class="d10">Incidentes vistos tarde</text>
  <rect x="346" y="174" width="155" height="56" rx="4" fill="#eef3f8" stroke="#0055a0"/><text x="423" y="192" text-anchor="middle" class="k10">ABUELO · mensual</text><text x="423" y="208" text-anchor="middle" class="d10">Se conserva 12 meses</text><text x="423" y="222" text-anchor="middle" class="d10">Referencia y auditoría</text>
  <rect x="509" y="174" width="151" height="56" rx="4" fill="#eef3f8" stroke="#0055a0"/><text x="584" y="192" text-anchor="middle" class="k10">ANUAL</text><text x="584" y="208" text-anchor="middle" class="d10">5-10 años o lo que</text><text x="584" y="222" text-anchor="middle" class="d10">exija la norma</text>
  <rect x="20" y="242" width="315" height="50" rx="5" fill="#d13c3c"/>
  <text x="177" y="260" text-anchor="middle" class="t10">NO CUMPLE EL 3-2-1</text>
  <text x="177" y="277" text-anchor="middle" class="s10">Guardar la copia en la MISMA cabina que el dato</text>
  <rect x="345" y="242" width="315" height="50" rx="5" fill="#2d8659"/>
  <text x="502" y="260" text-anchor="middle" class="t10">SÍ CUMPLE</text>
  <text x="502" y="277" text-anchor="middle" class="s10">Repositorio local + réplica al 2.º CPD + objeto WORM</text>
  <text x="340" y="312" text-anchor="middle" class="k10">Límite legal: el artículo 5.1.e del RGPD prohíbe conservar datos personales indefinidamente</text>
  <text x="670" y="334" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: ISO27002; NIST-SP800-209; RGPD]</text>
</svg>
```

---

## D11 · Completa, incremental, diferencial y sintética

**Sección**: §3.2.1 — Tipos de copia
**Propósito**: Hacer visual la diferencia que más se pregunta: qué copia cada tipo y cuántas piezas hacen falta para restaurar.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 370" role="img" aria-label="Comparación de los tipos de copia a lo largo de una semana: completa el domingo y después incrementales, diferenciales o sintéticas, indicando cuántas piezas se necesitan para restaurar el jueves">
  <style>.t11{font:700 10.5px system-ui,sans-serif;fill:#fff}.s11{font:9px system-ui,sans-serif;fill:#fff}.d11{font:9px system-ui,sans-serif;fill:#333}.h11{font:700 13px system-ui,sans-serif;fill:#0055a0}.k11{font:700 9.5px system-ui,sans-serif;fill:#0055a0}.l11{font:700 8.5px system-ui,sans-serif;fill:#0055a0}.n11{font:700 9px system-ui,sans-serif;fill:#fff}</style>
  <text x="340" y="20" text-anchor="middle" class="h11">Tipos de copia: qué se copia y qué hace falta para restaurar</text>
  <text x="118" y="42" text-anchor="middle" class="k11">DOM</text><text x="196" y="42" text-anchor="middle" class="k11">LUN</text><text x="274" y="42" text-anchor="middle" class="k11">MAR</text><text x="352" y="42" text-anchor="middle" class="k11">MIÉ</text><text x="430" y="42" text-anchor="middle" class="k11">JUE</text>
  <text x="20" y="66" class="l11">INCREMENTAL</text>
  <rect x="86" y="50" width="64" height="26" rx="3" fill="#0055a0"/><text x="118" y="67" text-anchor="middle" class="n11">COMPLETA</text>
  <rect x="164" y="50" width="64" height="26" rx="3" fill="#2d8659"/><text x="196" y="67" text-anchor="middle" class="n11">inc</text>
  <rect x="242" y="50" width="64" height="26" rx="3" fill="#2d8659"/><text x="274" y="67" text-anchor="middle" class="n11">inc</text>
  <rect x="320" y="50" width="64" height="26" rx="3" fill="#2d8659"/><text x="352" y="67" text-anchor="middle" class="n11">inc</text>
  <rect x="398" y="50" width="64" height="26" rx="3" fill="#2d8659"/><text x="430" y="67" text-anchor="middle" class="n11">inc</text>
  <text x="474" y="61" class="d11">Cada uno guarda lo cambiado</text><text x="474" y="72" class="d11">desde la copia ANTERIOR</text>
  <rect x="86" y="80" width="376" height="18" rx="3" fill="#d13c3c"/><text x="274" y="93" text-anchor="middle" class="n11">Restaurar el jueves: 5 piezas encadenadas</text>
  <text x="20" y="126" class="l11">DIFERENCIAL</text>
  <rect x="86" y="110" width="64" height="26" rx="3" fill="#0055a0"/><text x="118" y="127" text-anchor="middle" class="n11">COMPLETA</text>
  <rect x="164" y="110" width="64" height="26" rx="3" fill="#e89822"/><text x="196" y="127" text-anchor="middle" class="n11">dif</text>
  <rect x="242" y="110" width="64" height="26" rx="3" fill="#e89822"/><text x="274" y="127" text-anchor="middle" class="n11">dif +</text>
  <rect x="320" y="110" width="64" height="26" rx="3" fill="#e89822"/><text x="352" y="127" text-anchor="middle" class="n11">dif ++</text>
  <rect x="398" y="110" width="64" height="26" rx="3" fill="#e89822"/><text x="430" y="127" text-anchor="middle" class="n11">dif +++</text>
  <text x="474" y="121" class="d11">Cada una guarda lo cambiado</text><text x="474" y="132" class="d11">desde la última COMPLETA</text>
  <rect x="86" y="140" width="376" height="18" rx="3" fill="#2d8659"/><text x="274" y="153" text-anchor="middle" class="n11">Restaurar el jueves: solo 2 piezas (completa + diferencial del jueves)</text>
  <text x="20" y="186" class="l11">SINTÉTICA</text>
  <rect x="86" y="170" width="64" height="26" rx="3" fill="#0055a0"/><text x="118" y="187" text-anchor="middle" class="n11">COMPLETA</text>
  <rect x="164" y="170" width="64" height="26" rx="3" fill="#2d8659"/><text x="196" y="187" text-anchor="middle" class="n11">inc</text>
  <rect x="242" y="170" width="64" height="26" rx="3" fill="#2d8659"/><text x="274" y="187" text-anchor="middle" class="n11">inc</text>
  <rect x="320" y="170" width="64" height="26" rx="3" fill="#2d8659"/><text x="352" y="187" text-anchor="middle" class="n11">inc</text>
  <rect x="398" y="170" width="64" height="26" rx="3" fill="#0055a0"/><text x="430" y="187" text-anchor="middle" class="n11">SINTÉTICA</text>
  <text x="474" y="181" class="d11">El repositorio fabrica la completa</text><text x="474" y="192" class="d11">sin leer el sistema de origen</text>
  <rect x="86" y="200" width="376" height="18" rx="3" fill="#2d8659"/><text x="274" y="213" text-anchor="middle" class="n11">Restaurar el jueves: 1 pieza, y sin consumir ventana en producción</text>
  <line x1="20" y1="230" x2="660" y2="230" stroke="#ccc" stroke-width="1"/>
  <rect x="20" y="240" width="205" height="66" rx="5" fill="#2d8659"/>
  <text x="122" y="258" text-anchor="middle" class="t11">INCREMENTAL</text>
  <text x="122" y="275" text-anchor="middle" class="s11">Mínimo espacio y ventana</text>
  <text x="122" y="290" text-anchor="middle" class="s11">Restauración lenta; si se rompe</text>
  <text x="122" y="302" text-anchor="middle" class="s11">un eslabón, se pierde lo posterior</text>
  <rect x="237" y="240" width="206" height="66" rx="5" fill="#e89822"/>
  <text x="340" y="258" text-anchor="middle" class="t11">DIFERENCIAL</text>
  <text x="340" y="275" text-anchor="middle" class="s11">Crece cada día que pasa</text>
  <text x="340" y="290" text-anchor="middle" class="s11">Restauración rápida y robusta:</text>
  <text x="340" y="302" text-anchor="middle" class="s11">solo dos piezas</text>
  <rect x="455" y="240" width="205" height="66" rx="5" fill="#0055a0"/>
  <text x="557" y="258" text-anchor="middle" class="t11">SINTÉTICA</text>
  <text x="557" y="275" text-anchor="middle" class="s11">Consolida en el repositorio</text>
  <text x="557" y="290" text-anchor="middle" class="s11">Base del modelo incremental</text>
  <text x="557" y="302" text-anchor="middle" class="s11">para siempre</text>
  <text x="340" y="326" text-anchor="middle" class="k11">Incremental = desde la última copia · Diferencial = desde la última completa</text>
  <text x="340" y="344" text-anchor="middle" class="d11">Copia en frío: servicio parado · Copia en caliente: exige un mecanismo de consistencia (VSS, instantánea)</text>
  <text x="670" y="362" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: NIST-SP800-34; ISO27002; VEEAM-DOC]</text>
</svg>
```

---

## D12 · Arquitectura de una solución de copias de seguridad

**Sección**: §3.3.1 — Arquitecturas de software de backup
**Propósito**: Presentar las cinco piezas funcionales comunes a casi cualquier producto y señalar cuál es la crítica.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 340" role="img" aria-label="Arquitectura de una solución de copias de seguridad: servidor de control con catálogo, agentes en los sistemas de origen, proxies o servidores de medios, repositorios en disco, cinta y nube, y consola de administración">
  <style>.t12{font:700 10.5px system-ui,sans-serif;fill:#fff}.s12{font:9px system-ui,sans-serif;fill:#fff}.d12{font:9px system-ui,sans-serif;fill:#333}.h12{font:700 13px system-ui,sans-serif;fill:#0055a0}.k12{font:700 9.5px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h12">Arquitectura de una solución de copias de seguridad</text>
  <text x="20" y="44" class="k12">ORIGEN</text>
  <rect x="20" y="52" width="140" height="34" rx="4" fill="#eef3f8" stroke="#888"/><text x="90" y="66" text-anchor="middle" class="d12">Servidores físicos</text><text x="90" y="79" text-anchor="middle" class="d12">(con AGENTE)</text>
  <rect x="20" y="92" width="140" height="34" rx="4" fill="#eef3f8" stroke="#888"/><text x="90" y="106" text-anchor="middle" class="d12">Hipervisor y VM</text><text x="90" y="119" text-anchor="middle" class="d12">(SIN agente, por API)</text>
  <rect x="20" y="132" width="140" height="34" rx="4" fill="#eef3f8" stroke="#888"/><text x="90" y="146" text-anchor="middle" class="d12">Cabina NAS</text><text x="90" y="159" text-anchor="middle" class="d12">(NDMP)</text>
  <path d="M164 109 L206 109" stroke="#0055a0" stroke-width="2" marker-end="url(#a12)"/>
  <defs><marker id="a12" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#0055a0"/></marker></defs>
  <rect x="210" y="76" width="150" height="66" rx="5" fill="#0055a0"/>
  <text x="285" y="96" text-anchor="middle" class="t12">PROXY / SERVIDOR</text>
  <text x="285" y="110" text-anchor="middle" class="t12">DE MEDIOS</text>
  <text x="285" y="126" text-anchor="middle" class="s12">Mueve los datos y</text>
  <text x="285" y="138" text-anchor="middle" class="s12">permite paralelizar</text>
  <path d="M364 109 L406 109" stroke="#0055a0" stroke-width="2" marker-end="url(#a12)"/>
  <text x="410" y="44" class="k12">REPOSITORIOS</text>
  <rect x="410" y="52" width="250" height="30" rx="4" fill="#2d8659"/><text x="535" y="71" text-anchor="middle" class="s12">Disco con deduplicación — restauración rápida</text>
  <rect x="410" y="88" width="250" height="30" rx="4" fill="#e89822"/><text x="535" y="107" text-anchor="middle" class="s12">Objeto en nube con WORM — copia inmutable</text>
  <rect x="410" y="124" width="250" height="30" rx="4" fill="#888"/><text x="535" y="143" text-anchor="middle" class="s12">Cinta LTO extraída — copia fuera de línea</text>
  <rect x="210" y="168" width="450" height="46" rx="5" fill="#d13c3c"/>
  <text x="435" y="187" text-anchor="middle" class="t12">SERVIDOR DE CONTROL + CATÁLOGO</text>
  <text x="435" y="204" text-anchor="middle" class="s12">Configuración, planificación, retención e índice de qué hay en cada copia</text>
  <path d="M285 166 L285 146" stroke="#d13c3c" stroke-width="2" marker-end="url(#b12)"/>
  <defs><marker id="b12" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#d13c3c"/></marker></defs>
  <rect x="20" y="176" width="180" height="38" rx="4" fill="#eef3f8" stroke="#0055a0"/><text x="110" y="191" text-anchor="middle" class="d12">Consola e informes</text><text x="110" y="204" text-anchor="middle" class="d12">(evidencia para auditoría)</text>
  <rect x="20" y="226" width="640" height="34" rx="5" fill="none" stroke="#d13c3c" stroke-width="2"/>
  <text x="340" y="247" text-anchor="middle" style="font:700 10.5px system-ui;fill:#d13c3c">Sin catálogo no hay restauración granular: hay que copiarlo aparte y saber reconstruirlo el primero</text>
  <text x="20" y="282" class="k12">CAMINO DE LOS DATOS</text>
  <rect x="20" y="288" width="205" height="30" rx="4" fill="#eef3f8"/><text x="122" y="307" text-anchor="middle" class="d12">Por la LAN: sencillo, compite con usuarios</text>
  <rect x="237" y="288" width="206" height="30" rx="4" fill="#eef3f8"/><text x="340" y="307" text-anchor="middle" class="d12">LAN-free: el proxy lee el LUN por la SAN</text>
  <rect x="455" y="288" width="205" height="30" rx="4" fill="#eef3f8"/><text x="557" y="307" text-anchor="middle" class="d12">Sin servidor: copia desde la cabina</text>
  <text x="670" y="334" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: NIST-SP800-34; NDMP; VEEAM-DOC]</text>
</svg>
```

---

## D13 · Copia con agente frente a copia sin agente con CBT

**Sección**: §4.2 — Backup en entornos virtuales
**Propósito**: Contraponer las dos formas de copiar y mostrar el flujo completo de la copia sin agente, con el papel de la instantánea y del seguimiento de bloques modificados.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 350" role="img" aria-label="Comparación entre la copia basada en agente instalado en el sistema operativo y la copia sin agente mediante la API del hipervisor, con el flujo de instantánea, congelación con VSS, lectura de bloques cambiados mediante CBT y consolidación">
  <style>.t13{font:700 10.5px system-ui,sans-serif;fill:#fff}.s13{font:9px system-ui,sans-serif;fill:#fff}.d13{font:9px system-ui,sans-serif;fill:#333}.h13{font:700 13px system-ui,sans-serif;fill:#0055a0}.k13{font:700 9.5px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h13">Con agente (desde dentro) frente a sin agente (desde el hipervisor)</text>
  <rect x="20" y="32" width="310" height="24" rx="5" fill="#e89822"/><text x="175" y="49" text-anchor="middle" class="t13">CON AGENTE · sistema físico o virtual</text>
  <rect x="350" y="32" width="310" height="24" rx="5" fill="#2d8659"/><text x="505" y="49" text-anchor="middle" class="t13">SIN AGENTE · solo entornos virtuales</text>
  <rect x="20" y="64" width="310" height="30" rx="4" fill="#eef3f8" stroke="#888"/><text x="175" y="83" text-anchor="middle" class="d13">Aplicación y sistema operativo</text>
  <rect x="20" y="100" width="310" height="30" rx="4" fill="#e89822"/><text x="175" y="119" text-anchor="middle" class="s13">AGENTE instalado: lee, congela con VSS y envía</text>
  <rect x="20" y="136" width="310" height="30" rx="4" fill="#eef3f8" stroke="#888"/><text x="175" y="155" text-anchor="middle" class="d13">Disco (físico o virtual)</text>
  <rect x="350" y="64" width="310" height="30" rx="4" fill="#eef3f8" stroke="#888"/><text x="505" y="83" text-anchor="middle" class="d13">Máquina virtual: sin nada instalado</text>
  <rect x="350" y="100" width="310" height="30" rx="4" fill="#2d8659"/><text x="505" y="119" text-anchor="middle" class="s13">HIPERVISOR: API de protección de datos + CBT</text>
  <rect x="350" y="136" width="310" height="30" rx="4" fill="#eef3f8" stroke="#888"/><text x="505" y="155" text-anchor="middle" class="d13">Almacén de datos con los discos virtuales</text>
  <text x="20" y="188" class="k13">FLUJO DE LA COPIA SIN AGENTE</text>
  <rect x="20" y="196" width="122" height="46" rx="4" fill="#0055a0"/><text x="81" y="213" text-anchor="middle" class="s13">1 · Instantánea</text><text x="81" y="228" text-anchor="middle" class="s13">de la VM</text>
  <rect x="150" y="196" width="122" height="46" rx="4" fill="#0055a0"/><text x="211" y="213" text-anchor="middle" class="s13">2 · VSS congela</text><text x="211" y="228" text-anchor="middle" class="s13">la aplicación</text>
  <rect x="280" y="196" width="122" height="46" rx="4" fill="#0055a0"/><text x="341" y="213" text-anchor="middle" class="s13">3 · Escrituras</text><text x="341" y="228" text-anchor="middle" class="s13">nuevas al delta</text>
  <rect x="410" y="196" width="122" height="46" rx="4" fill="#0055a0"/><text x="471" y="213" text-anchor="middle" class="s13">4 · Se leen SOLO</text><text x="471" y="228" text-anchor="middle" class="s13">bloques cambiados</text>
  <rect x="540" y="196" width="120" height="46" rx="4" fill="#0055a0"/><text x="600" y="213" text-anchor="middle" class="s13">5 · Consolidar</text><text x="600" y="228" text-anchor="middle" class="s13">y borrar el delta</text>
  <rect x="20" y="252" width="310" height="44" rx="5" fill="#eef3f8" stroke="#e89822" stroke-width="2"/>
  <text x="175" y="269" text-anchor="middle" class="k13">CUÁNDO SIGUE HACIENDO FALTA EL AGENTE</text>
  <text x="175" y="286" text-anchor="middle" class="d13">Bases de datos con registro de transacciones, puestos, nube</text>
  <rect x="350" y="252" width="310" height="44" rx="5" fill="#eef3f8" stroke="#2d8659" stroke-width="2"/>
  <text x="505" y="269" text-anchor="middle" class="k13">QUÉ APORTA EL CBT</text>
  <text x="505" y="286" text-anchor="middle" class="d13">Incrementales en minutos e incremental para siempre</text>
  <rect x="60" y="304" width="560" height="26" rx="5" fill="none" stroke="#d13c3c" stroke-width="2"/>
  <text x="340" y="321" text-anchor="middle" style="font:700 10px system-ui;fill:#d13c3c">Sin agente NO significa sin consistencia: el hipervisor sigue llamando a VSS dentro del invitado</text>
  <text x="670" y="344" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: VMW-VADP; HYPERV-RCT; MS-VSS]</text>
</svg>
```

---

## D14 · Escalera de recuperación y anclaje normativo

**Sección**: §4.2.3 y §5 — Replicación, recuperación granular y marco normativo
**Propósito**: Ordenar los mecanismos de recuperación por RTO creciente y unir cada capa con la obligación jurídica que la respalda.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 380" role="img" aria-label="Escalera de mecanismos de recuperación ordenados por tiempo de recuperación, desde la instantánea y la réplica hasta la restauración desde cinta y el plan de recuperación ante desastres, con el anclaje normativo del Esquema Nacional de Seguridad y del Reglamento General de Protección de Datos">
  <style>.t14{font:700 10.5px system-ui,sans-serif;fill:#fff}.s14{font:9px system-ui,sans-serif;fill:#fff}.d14{font:9px system-ui,sans-serif;fill:#333}.h14{font:700 13px system-ui,sans-serif;fill:#0055a0}.k14{font:700 9.5px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="340" y="20" text-anchor="middle" class="h14">Escalera de recuperación: de segundos a días</text>
  <rect x="20" y="32" width="500" height="28" rx="4" fill="#2d8659"/><text x="30" y="51" class="s14">Instantánea de cabina o de VM — deshacer un cambio reciente</text>
  <text x="530" y="51" class="d14">Segundos · depende del original</text>
  <rect x="20" y="66" width="500" height="28" rx="4" fill="#2d8659"/><text x="30" y="85" class="s14">Réplica en el segundo CPD — se enciende (failover)</text>
  <text x="530" y="85" class="d14">Minutos · RPO de minutos</text>
  <rect x="20" y="100" width="500" height="28" rx="4" fill="#0055a0"/><text x="30" y="119" class="s14">Restauración instantánea desde el repositorio de disco</text>
  <text x="530" y="119" class="d14">Minutos · arranca y migra</text>
  <rect x="20" y="134" width="500" height="28" rx="4" fill="#0055a0"/><text x="30" y="153" class="s14">Recuperación granular: un fichero, un correo, una tabla</text>
  <text x="530" y="153" class="d14">Minutos · sin restaurar la VM</text>
  <rect x="20" y="168" width="500" height="28" rx="4" fill="#e89822"/><text x="30" y="187" class="s14">Restauración completa desde el repositorio de disco</text>
  <text x="530" y="187" class="d14">Horas · según volumen</text>
  <rect x="20" y="202" width="500" height="28" rx="4" fill="#e89822"/><text x="30" y="221" class="s14">Recuperación bare-metal de un sistema físico</text>
  <text x="530" y="221" class="d14">Horas · medio de arranque</text>
  <rect x="20" y="236" width="500" height="28" rx="4" fill="#d13c3c"/><text x="30" y="255" class="s14">Restauración desde cinta o archivo profundo en nube</text>
  <text x="530" y="255" class="d14">Horas o días · secuencial</text>
  <rect x="20" y="270" width="500" height="28" rx="4" fill="#d13c3c"/><text x="30" y="289" class="s14">Activación del DRP en el emplazamiento alternativo</text>
  <text x="530" y="289" class="d14">Frío, templado o caliente</text>
  <line x1="20" y1="308" x2="660" y2="308" stroke="#ccc" stroke-width="1"/>
  <rect x="20" y="316" width="310" height="46" rx="5" fill="#0055a0"/>
  <text x="175" y="334" text-anchor="middle" class="t14">ENS · RD 311/2022</text>
  <text x="175" y="351" text-anchor="middle" class="s14">Art. 26 · [mp.info.6] copias · [op.cont] continuidad</text>
  <rect x="350" y="316" width="310" height="46" rx="5" fill="#2d8659"/>
  <text x="505" y="334" text-anchor="middle" class="t14">RGPD · art. 32</text>
  <text x="505" y="351" text-anchor="middle" class="s14">Disponibilidad, resiliencia, restaurar y verificar</text>
  <text x="670" y="374" text-anchor="end" style="font:9px system-ui;fill:#666">[Fuente: NIST-SP800-34; ENS; RGPD]</text>
</svg>
```
