# Tema 26 — Test de Autoevaluación

> **Título**: Sistemas de almacenamiento y su virtualización. Políticas, sistemas y procedimientos de backup y su recuperación. Backup de sistemas físicos y virtuales.
> **Formato**: 60 preguntas tipo test A/B/C (formato oficial oposición)
> **Nivel**: C1 — Técnico Auxiliar TIC, Ayuntamiento de Madrid
> **Versión**: v1.0 — Pendiente validación
> **Fecha**: 2026-08-20
> **Fuentes**: ver tema-26-fuentes.md

---

## Instrucciones

- Cada pregunta tiene **3 opciones** (A, B, C). Solo una es correcta.
- Penalización en examen real: respuesta incorrecta descuenta **1/3** del valor de una correcta.
- Tiempo orientativo: 1 minuto por pregunta.
- Distribución: Sistemas de almacenamiento (P1-P16), Virtualización del almacenamiento (P17-P26), Políticas y procedimientos de backup (P27-P48), Backup de sistemas físicos y virtuales (P49-P57), Normativa y marco legal (P58-P60).

---

### Pregunta 1

**¿Qué caracteriza al almacenamiento de conexión directa (DAS)?**

A) Está conectado directamente a un servidor por un bus local y no se comparte con otros servidores
B) Sirve ficheros por la red IP mediante NFS o SMB a muchos clientes simultáneos
C) Requiere una red dedicada de Fibre Channel con conmutadores y zoning

<details><summary>Respuesta</summary>

**Correcta: A) Está conectado directamente a un servidor por un bus local y no se comparte con otros servidores** El DAS emplea interfaces SAS, SATA o NVMe sin red de almacenamiento de por medio; su limitación esencial no es el rendimiento, que es excelente, sino la imposibilidad de compartirlo.

*Referencia: §1.1.1 [SNIA-DICT]*
</details>

---

### Pregunta 2

**En una cabina NAS, ¿quién gestiona el sistema de ficheros?**

A) El servidor cliente, que formatea el volumen recibido
B) La propia cabina, que publica carpetas y ficheros a los clientes
C) El conmutador de la red de almacenamiento

<details><summary>Respuesta</summary>

**Correcta: B) La propia cabina, que publica carpetas y ficheros a los clientes** Es la diferencia estructural con la SAN: si se sirven ficheros, el sistema de ficheros vive en la cabina; si se sirven bloques, lo pone el servidor.

*Referencia: §1.1.2 [SNIA-DICT]*
</details>

---

### Pregunta 3

**¿Qué unidad presenta una SAN a los servidores?**

A) Una carpeta compartida con permisos por usuario
B) Un contenedor de objetos accesible por HTTP
C) Un LUN, que el servidor ve como si fuera un disco propio

<details><summary>Respuesta</summary>

**Correcta: C) Un LUN, que el servidor ve como si fuera un disco propio** El LUN (*Logical Unit Number*) es la unidad lógica de bloque que la cabina presenta; el servidor le aplica su tabla de particiones y su sistema de ficheros.

*Referencia: §1.1.2 [SNIA-DICT] [T10-SCSI]*
</details>

---

### Pregunta 4

**¿Dónde se configura el zoning en una red de almacenamiento Fibre Channel?**

A) En la controladora RAID del servidor
B) En el conmutador de la SAN
C) En el sistema operativo invitado de cada máquina virtual

<details><summary>Respuesta</summary>

**Correcta: B) En el conmutador de la SAN** El zoning se configura en el conmutador y decide qué iniciador ve qué objetivo; el LUN masking, que es complementario, se configura en la cabina y decide qué unidad lógica ve cada servidor.

*Referencia: §1.1.2 [T11-FC] [NIST-SP800-209]*
</details>

---

### Pregunta 5

**¿Cuál de estos rasgos define al almacenamiento de objetos?**

A) Un árbol jerárquico de directorios con permisos heredados
B) Acceso mediante comandos SCSI encapsulados en TCP
C) Espacio de nombres plano, metadatos ricos y acceso por API REST sobre HTTP

<details><summary>Respuesta</summary>

**Correcta: C) Espacio de nombres plano, metadatos ricos y acceso por API REST sobre HTTP** El objeto se compone de contenido, metadatos extensibles e identificador único, y se guarda en contenedores sin jerarquía real de carpetas.

*Referencia: §1.1.3 [SNIA-DICT] [RFC9110]*
</details>

---

### Pregunta 6

**¿Para cuál de estos usos NO es adecuado el almacenamiento de objetos?**

A) Alojar el disco de una base de datos transaccional en producción
B) Guardar copias de seguridad inmutables con retención WORM
C) Conservar documentos digitalizados del archivo electrónico

<details><summary>Respuesta</summary>

**Correcta: A) Alojar el disco de una base de datos transaccional en producción** El objeto no admite modificación parcial —se escribe una versión nueva— y su latencia es la de una petición HTTP, lo que lo descarta para cargas transaccionales.

*Referencia: §1.1.3 [SNIA-DICT] [S3-LOCK]*
</details>

---

### Pregunta 7

**¿Qué es una cabina de almacenamiento unificado?**

A) Una cabina que solo admite un protocolo, elegido en la instalación
B) Un conjunto de cabinas idénticas replicadas entre dos centros de proceso de datos
C) Una cabina que ofrece simultáneamente acceso por bloque, por fichero y, en muchos casos, por objeto sobre el mismo pool

<details><summary>Respuesta</summary>

**Correcta: C) Una cabina que ofrece simultáneamente acceso por bloque, por fichero y, en muchos casos, por objeto sobre el mismo pool** Su ventaja es la consolidación; su riesgo, convertirse en un punto único de fallo de servicios muy distintos, lo que obliga a que las copias no residan en ella.

*Referencia: §1.1.3 [SNIA-DICT]*
</details>

---

### Pregunta 8

**¿Qué puerto TCP utiliza iSCSI de forma estándar?**

A) 3260
B) 2049
C) 445

<details><summary>Respuesta</summary>

**Correcta: A) 3260** El 2049 corresponde a NFS y el 445 a SMB. Los extremos iSCSI se nombran con IQN y la autenticación estándar es CHAP.

*Referencia: §1.2.1 [RFC7143]*
</details>

---

### Pregunta 9

**¿Qué identificador emplea Fibre Channel para nombrar sus puertos?**

A) IQN
B) WWN
C) NQN

<details><summary>Respuesta</summary>

**Correcta: B) WWN** El WWN (*World Wide Name*) es un identificador único de 64 bits, análogo funcional de la dirección MAC. El IQN identifica extremos iSCSI y el NQN, extremos NVMe over Fabrics.

*Referencia: §1.2.1 [T11-FC]*
</details>

---

### Pregunta 10

**¿Qué aporta NVMe over Fabrics frente a iSCSI?**

A) Permite servir ficheros además de bloques
B) Elimina la necesidad de red, al ser una conexión directa
C) Transporta el juego de comandos NVMe, con colas paralelas y menor latencia, sobre RDMA, Fibre Channel o TCP

<details><summary>Respuesta</summary>

**Correcta: C) Transporta el juego de comandos NVMe, con colas paralelas y menor latencia, sobre RDMA, Fibre Channel o TCP** Sustituye el modelo de cola única de SCSI por miles de colas paralelas, diseñado para memoria flash.

*Referencia: §1.2.1 [NVME-OF]*
</details>

---

### Pregunta 11

**¿Qué versión de NFS incorpora sesiones con estado, seguridad Kerberos integrada y pNFS?**

A) NFS versión 2
B) NFS versión 4.1
C) NFS versión 3

<details><summary>Respuesta</summary>

**Correcta: B) NFS versión 4.1** Definida en el RFC 8881, unifica montaje y bloqueo en un solo protocolo sobre el puerto 2049, frente a la versión 3, sin estado y dependiente de protocolos auxiliares.

*Referencia: §1.2.1 [RFC8881] [RFC1813]*
</details>

---

### Pregunta 12

**¿Cuál de estas funciones es propia de SMB 3.x?**

A) Cifrado en tránsito, multichannel y continuidad transparente ante la caída de un nodo
B) Encapsular comandos SCSI para presentar LUN a los servidores
C) Calcular la ubicación de los objetos mediante el algoritmo CRUSH

<details><summary>Respuesta</summary>

**Correcta: A) Cifrado en tránsito, multichannel y continuidad transparente ante la caída de un nodo** SMB 3.x opera sobre el puerto 445 y se integra con la autenticación de dominio y las listas de control de acceso.

*Referencia: §1.2.1 [MS-SMB2]*
</details>

---

### Pregunta 13

**En un conjunto RAID 5 de 8 discos de 4 TB, ¿cuál es la capacidad útil aproximada y cuántos discos tolera?**

A) 32 TB y tolera 1 disco
B) 16 TB y tolera 2 discos
C) 28 TB y tolera 1 disco

<details><summary>Respuesta</summary>

**Correcta: C) 28 TB y tolera 1 disco** RAID 5 ofrece una capacidad útil de n−1 discos: (8−1) × 4 = 28 TB, con tolerancia al fallo de un solo disco.

*Referencia: §1.2.2 [PATTERSON88]*
</details>

---

### Pregunta 14

**¿Qué nivel RAID ofrece doble paridad distribuida?**

A) RAID 6
B) RAID 5
C) RAID 10

<details><summary>Respuesta</summary>

**Correcta: A) RAID 6** RAID 6 tolera el fallo simultáneo de dos discos y ofrece una capacidad útil de n−2, lo que lo ha convertido en el mínimo razonable con discos de gran capacidad por el riesgo durante la reconstrucción.

*Referencia: §1.2.2 [PATTERSON88]*
</details>

---

### Pregunta 15

**¿Qué nivel RAID conviene a una base de datos con escritura muy intensa?**

A) RAID 5, porque desperdicia menos capacidad
B) RAID 10, porque su penalización de escritura es de solo dos operaciones
C) RAID 0, porque es el más rápido en todos los escenarios

<details><summary>Respuesta</summary>

**Correcta: B) RAID 10, porque su penalización de escritura es de solo dos operaciones** RAID 5 exige cuatro operaciones físicas por escritura y RAID 6 seis; además, RAID 0 carece por completo de tolerancia a fallos.

*Referencia: §1.2.2 [PATTERSON88]*
</details>

---

### Pregunta 16

**¿Cuál es el riesgo característico del aprovisionamiento fino (thin provisioning)?**

A) Que el servidor no pueda ampliar el volumen en caliente
B) Que obligue a reservar toda la capacidad desde el primer momento
C) Que, si el pool se llena físicamente, fallen a la vez todos los volúmenes que dependen de él

<details><summary>Respuesta</summary>

**Correcta: C) Que, si el pool se llena físicamente, fallen a la vez todos los volúmenes que dependen de él** El sobreaprovisionamiento exige umbrales de alerta y un procedimiento de ampliación; la orden UNMAP permite devolver al pool el espacio liberado.

*Referencia: §1.2.2 [SNIA-DICT] [T10-SCSI]*
</details>

---

### Pregunta 17

**¿Qué diferencia hay entre deduplicación en origen y en destino?**

A) En origen se ejecuta en el cliente, con lo que se reduce también el tráfico de red; en destino, en la cabina o el repositorio
B) En origen se ejecuta después de escribir y en destino antes de escribir
C) En origen solo se aplica a ficheros y en destino solo a bloques

<details><summary>Respuesta</summary>

**Correcta: A) En origen se ejecuta en el cliente, con lo que se reduce también el tráfico de red; en destino, en la cabina o el repositorio** La distinción entre antes o después de escribir es la de deduplicación en línea (inline) frente a posproceso, que es un eje diferente.

*Referencia: §1.2.2 [SNIA-DICT]*
</details>

---

### Pregunta 18

**¿En qué consiste la virtualización del almacenamiento?**

A) En ejecutar varios sistemas operativos sobre un mismo servidor mediante un hipervisor
B) En sustituir los discos magnéticos por unidades de estado sólido
C) En interponer una capa de abstracción que presenta volúmenes lógicos independientes del hardware físico que los soporta

<details><summary>Respuesta</summary>

**Correcta: C) En interponer una capa de abstracción que presenta volúmenes lógicos independientes del hardware físico que los soporta** No debe confundirse con la virtualización de servidores, que es su principal consumidor pero una disciplina distinta.

*Referencia: §2.1 [SNIA-DICT]*
</details>

---

### Pregunta 19

**LVM en Linux es un ejemplo canónico de virtualización de almacenamiento…**

A) Basada en la cabina
B) Basada en el host
C) Basada en la red

<details><summary>Respuesta</summary>

**Correcta: B) Basada en el host** El gestor de volúmenes lógicos se ejecuta en el sistema operativo del servidor y agrupa volúmenes físicos en grupos de volúmenes de los que talla volúmenes lógicos ampliables en caliente.

*Referencia: §2.1.1 [LVM-LINUX]*
</details>

---

### Pregunta 20

**Se quiere unificar cabinas de fabricantes distintos y migrar los datos sin parar el servicio. ¿Qué modelo de virtualización encaja mejor?**

A) Basada en la red, mediante un appliance o conmutador virtualizador situado en el fabric
B) Basada en el host, instalando un gestor de volúmenes en cada servidor
C) Basada en la cabina, activando los pools de una de ellas

<details><summary>Respuesta</summary>

**Correcta: A) Basada en la red, mediante un appliance o conmutador virtualizador situado en el fabric** Es el modelo que mejor resuelve la heterogeneidad; su precio es la latencia añadida al operar en banda y la necesidad de duplicar el dispositivo.

*Referencia: §2.1.1 [SNIA-DICT]*
</details>

---

### Pregunta 21

**En una capa de virtualización que trabaja «fuera de banda» (out-of-band)…**

A) Todas las lecturas y escrituras atraviesan la capa de virtualización
B) La capa se ejecuta necesariamente dentro de la cabina de almacenamiento
C) La capa gestiona solo los metadatos y los datos van directamente del servidor a la cabina

<details><summary>Respuesta</summary>

**Correcta: C) La capa gestiona solo los metadatos y los datos van directamente del servidor a la cabina** Por eso no añade latencia, a costa de exigir software específico en cada servidor. El modelo en banda es el contrario.

*Referencia: §2.1 [SNIA-DICT]*
</details>

---

### Pregunta 22

**¿Cuál es el rasgo definitorio del almacenamiento definido por software (SDS)?**

A) Que se gestiona mediante una consola gráfica en lugar de por línea de órdenes
B) Que separa el plano de control, basado en políticas, del plano de datos, y se ejecuta sobre hardware estándar
C) Que sustituye el RAID por una controladora propietaria de doble paridad

<details><summary>Respuesta</summary>

**Correcta: B) Que separa el plano de control, basado en políticas, del plano de datos, y se ejecuta sobre hardware estándar** No basta con que un producto se gobierne por software: lo distintivo es que la inteligencia deja de residir en hardware propietario y el crecimiento es horizontal.

*Referencia: §2.1.2 [SNIA-SDS]*
</details>

---

### Pregunta 23

**¿Cómo protege el dato una solución SDS típica?**

A) Mediante réplica de varias copias entre nodos o codificación de borrado (erasure coding)
B) Mediante una única controladora RAID compartida por todos los nodos
C) Mediante cintas WORM insertadas en cada nodo

<details><summary>Respuesta</summary>

**Correcta: A) Mediante réplica de varias copias entre nodos o codificación de borrado (erasure coding)** La protección se hace por software y puede tolerar la caída de discos, de nodos o incluso de armarios completos, según la política definida.

*Referencia: §2.1.2 [CEPH] [SNIA-SDS]*
</details>

---

### Pregunta 24

**¿Qué elimina una infraestructura hiperconvergente (HCI) respecto de la arquitectura clásica de tres capas?**

A) La necesidad de hipervisor, al ejecutar las aplicaciones directamente sobre el hardware
B) La necesidad de copias de seguridad, al replicar los bloques entre nodos
C) La cabina de almacenamiento dedicada, sustituida por los discos locales de los nodos agregados por software

<details><summary>Respuesta</summary>

**Correcta: C) La cabina de almacenamiento dedicada, sustituida por los discos locales de los nodos agregados por software** Con ella desaparecen también el fabric Fibre Channel, el zoning y el LUN masking, y la gestión se unifica en una sola consola.

*Referencia: §2.2.1 [VSAN] [NUTANIX]*
</details>

---

### Pregunta 25

**¿Cuál es la unidad de crecimiento de una infraestructura hiperconvergente?**

A) El nodo, que aporta a la vez cómputo, memoria y capacidad
B) La bandeja de discos de la cabina
C) El conmutador de la red de almacenamiento

<details><summary>Respuesta</summary>

**Correcta: A) El nodo, que aporta a la vez cómputo, memoria y capacidad** Es su virtud —crecimiento incremental y predecible— y su limitación, porque ambos recursos crecen acoplados, algo que se mitiga con nodos solo de almacenamiento.

*Referencia: §2.2.1 [VSAN] [S2D]*
</details>

---

### Pregunta 26

**¿Por qué debe reservarse espacio libre sin usar en el pool de un clúster hiperconvergente?**

A) Porque el aprovisionamiento fino lo exige para poder crear volúmenes nuevos
B) Porque el sistema necesita sitio para reconstruir los datos cuando cae un disco o un nodo
C) Porque el hipervisor guarda ahí los ficheros de configuración del clúster

<details><summary>Respuesta</summary>

**Correcta: B) Porque el sistema necesita sitio para reconstruir los datos cuando cae un disco o un nodo** Llenar el pool al límite deja al clúster sin capacidad de autorrepararse; es el error de dimensionado más frecuente en estas arquitecturas.

*Referencia: §2.2.1 [VSAN] [NUTANIX]*
</details>

---

### Pregunta 27

**¿Cuál de estas causas de pérdida de datos NO queda cubierta por un RAID 6?**

A) El fallo simultáneo de dos discos del conjunto
B) El borrado accidental de una carpeta por un usuario
C) El fallo de un único disco durante la reconstrucción de otro

<details><summary>Respuesta</summary>

**Correcta: B) El borrado accidental de una carpeta por un usuario** El RAID protege del fallo físico del disco, pero replica al instante el borrado, la corrupción lógica y el cifrado por ransomware: no es una copia de seguridad.

*Referencia: §3.1 [ISO27002] [NIST-SP800-209]*
</details>

---

### Pregunta 28

**¿Qué determina el RPO en una política de copias?**

A) La tecnología de recuperación que hay que emplear
B) El número de emplazamientos alternativos necesarios
C) La frecuencia con que hay que realizar las copias

<details><summary>Respuesta</summary>

**Correcta: C) La frecuencia con que hay que realizar las copias** El RPO expresa cuántos datos, medidos en tiempo, se acepta perder; si es de 4 horas, no puede copiarse una sola vez al día.

*Referencia: §3.1.1 [ISO22301] [NIST-SP800-34]*
</details>

---

### Pregunta 29

**Un servicio tiene un RTO de 15 minutos. ¿Qué solución es coherente?**

A) Disponer de una réplica encendible en el emplazamiento alternativo
B) Realizar una copia completa diaria en cinta y custodiarla fuera del edificio
C) Ampliar la retención de las copias diarias a 30 días

<details><summary>Respuesta</summary>

**Correcta: A) Disponer de una réplica encendible en el emplazamiento alternativo** El RTO determina la tecnología de recuperación: restaurar volúmenes grandes desde cinta se mide en horas, no en minutos. La retención no influye en el tiempo de recuperación.

*Referencia: §3.1.1 [NIST-SP800-34]*
</details>

---

### Pregunta 30

**¿Qué significa MTD (o MTPD) en la planificación de la continuidad?**

A) El tiempo medio de reparación de un componente averiado
B) El tiempo máximo que el servicio puede estar interrumpido antes de que el daño sea inasumible
C) El intervalo disponible para ejecutar la copia sin degradar el servicio

<details><summary>Respuesta</summary>

**Correcta: B) El tiempo máximo que el servicio puede estar interrumpido antes de que el daño sea inasumible** El RTO debe fijarse siempre por debajo del MTD. El tiempo medio de reparación es el MTTR y el intervalo de ejecución es la ventana de copia.

*Referencia: §3.1.1 [ISO22301]*
</details>

---
### Pregunta 31

**¿En qué consiste la regla 3-2-1?**

A) Tres copias de los datos, en dos soportes distintos, con una fuera de la ubicación
B) Tres copias diarias, dos semanales y una mensual
C) Tres emplazamientos, dos redes y un único administrador responsable

<details><summary>Respuesta</summary>

**Correcta: A) Tres copias de los datos, en dos soportes distintos, con una fuera de la ubicación** Las tres copias incluyen el propio original más dos copias adicionales; su extensión 3-2-1-1-0 añade una copia inmutable o fuera de línea y cero errores de verificación.

*Referencia: §3.1.2 [ISO27002] [NIST-SP800-209]*
</details>

---

### Pregunta 32

**¿Qué añade la regla 3-2-1-1-0 respecto de la clásica 3-2-1?**

A) Una copia adicional en la misma cabina y un informe mensual
B) Un servidor de copia adicional y cero agentes instalados
C) Una copia inmutable o fuera de línea y la exigencia de cero errores tras la verificación

<details><summary>Respuesta</summary>

**Correcta: C) Una copia inmutable o fuera de línea y la exigencia de cero errores tras la verificación** El añadido responde al ransomware moderno, que busca y cifra primero las copias y el catálogo para impedir la recuperación.

*Referencia: §3.1.2 [NIST-SP800-209]*
</details>

---

### Pregunta 33

**¿Cumple la regla 3-2-1 una copia guardada en la misma cabina que aloja los datos originales?**

A) Sí, siempre que se guarde en un pool distinto del original
B) No, porque comparte el fallo de la cabina, el incendio de la sala y el alcance de un atacante
C) Sí, siempre que la copia esté cifrada

<details><summary>Respuesta</summary>

**Correcta: B) No, porque comparte el fallo de la cabina, el incendio de la sala y el alcance de un atacante** La independencia respecto del original es justamente lo que distingue una copia de seguridad de una instantánea.

*Referencia: §3.1.2 [ISO27002]*
</details>

---

### Pregunta 34

**En el esquema de retención GFS, ¿qué representa el nivel «abuelo»?**

A) La copia mensual, conservada típicamente durante doce meses
B) La copia diaria, conservada entre siete y catorce días
C) La copia inmutable custodiada por un tercero

<details><summary>Respuesta</summary>

**Correcta: A) La copia mensual, conservada típicamente durante doce meses** El «hijo» es la copia diaria, el «padre» la semanal y el «abuelo» la mensual, con vigencia creciente; por encima suele añadirse una copia anual.

*Referencia: §3.1.2 [ISO27002]*
</details>

---

### Pregunta 35

**¿Por qué la retención de las copias no puede ser indefinida cuando contienen datos personales?**

A) Porque el software de copia no admite retenciones superiores a un año
B) Porque el catálogo perdería la referencia de las copias antiguas
C) Porque el artículo 5.1.e del RGPD impone la limitación del plazo de conservación

<details><summary>Respuesta</summary>

**Correcta: C) Porque el artículo 5.1.e del RGPD impone la limitación del plazo de conservación** La retención debe estar justificada y documentada, y su vencimiento debe ejecutarse con destrucción segura del soporte.

*Referencia: §3.1.2 [RGPD] [NIST-SP800-88]*
</details>

---

### Pregunta 36

**Una copia incremental guarda…**

A) Todo lo que ha cambiado desde la última copia completa
B) Todo lo que ha cambiado desde la copia anterior, sea del tipo que sea
C) Todos los datos seleccionados, con independencia de si han cambiado

<details><summary>Respuesta</summary>

**Correcta: B) Todo lo que ha cambiado desde la copia anterior, sea del tipo que sea** Es la más rápida y la que menos ocupa, pero la restauración exige la completa y toda la cadena de incrementales posteriores en orden.

*Referencia: §3.2.1 [NIST-SP800-34]*
</details>

---

### Pregunta 37

**Se hace copia completa el domingo y diferenciales de lunes a sábado. ¿Cuántas piezas hacen falta para restaurar el estado del jueves?**

A) Cinco: la completa y las cuatro diferenciales
B) Una: solo la diferencial del jueves
C) Dos: la completa del domingo y la diferencial del jueves

<details><summary>Respuesta</summary>

**Correcta: C) Dos: la completa del domingo y la diferencial del jueves** La diferencial acumula todos los cambios desde la última completa, de modo que basta con la última. Con incrementales harían falta cinco piezas encadenadas.

*Referencia: §3.2.1 [NIST-SP800-34]*
</details>

---

### Pregunta 38

**¿Qué es una copia completa sintética?**

A) Una completa que el software fabrica en el repositorio combinando la completa anterior con los incrementales, sin leer el sistema de origen
B) Una completa que se realiza con el servicio detenido para garantizar la consistencia
C) Una completa cifrada y firmada digitalmente antes de enviarla a la nube

<details><summary>Respuesta</summary>

**Correcta: A) Una completa que el software fabrica en el repositorio combinando la completa anterior con los incrementales, sin leer el sistema de origen** Es la base del modelo incremental para siempre: no consume ventana ni carga la producción y deja un punto de restauración de una sola pieza.

*Referencia: §3.2.1 [VEEAM-DOC]*
</details>

---

### Pregunta 39

**¿Qué técnica ofrece el RPO más bajo posible?**

A) La copia diferencial cada seis horas
B) La protección continua de datos (CDP), que registra cada escritura según se produce
C) La copia completa sintética diaria

<details><summary>Respuesta</summary>

**Correcta: B) La protección continua de datos (CDP), que registra cada escritura según se produce** Permite volver a prácticamente cualquier instante, con un RPO de segundos, a costa de un consumo de recursos considerablemente mayor.

*Referencia: §3.2.1 [NIST-SP800-34]*
</details>

---

### Pregunta 40

**¿Qué nivel de consistencia obtiene una copia realizada sin coordinación alguna con la aplicación?**

A) Consistente con la aplicación
B) Consistente con el sistema de ficheros
C) Consistente con el bloque (crash-consistent), equivalente a haber desenchufado el servidor

<details><summary>Respuesta</summary>

**Correcta: C) Consistente con el bloque (crash-consistent), equivalente a haber desenchufado el servidor** Los bloques están, pero puede faltar lo que había en memoria, de modo que la base de datos restaurada podría necesitar recuperación o no abrir.

*Referencia: §4.1 [MS-VSS] [VMW-VADP]*
</details>

---

### Pregunta 41

**¿Qué caracteriza a una copia inmutable con bloqueo de objetos en modo de cumplimiento?**

A) Que solo puede leerla el usuario que la creó
B) Que no puede modificarse ni borrarse por nadie, ni siquiera por la cuenta administradora, hasta que expire la retención
C) Que se guarda automáticamente en un soporte extraíble

<details><summary>Respuesta</summary>

**Correcta: B) Que no puede modificarse ni borrarse por nadie, ni siquiera por la cuenta administradora, hasta que expire la retención** En el modo de gobernanza, en cambio, un usuario con un permiso especial sí puede levantar la retención antes de tiempo.

*Referencia: §3.2.2 [S3-LOCK]*
</details>

---

### Pregunta 42

**¿Cuál es la ventaja distintiva de la cinta LTO como soporte de copia?**

A) Que un cartucho extraído de la biblioteca queda físicamente inalcanzable por la red, con coste por terabyte mínimo
B) Que ofrece la restauración más rápida de todos los soportes
C) Que permite modificar los datos ya escritos sin reescribir el cartucho

<details><summary>Respuesta</summary>

**Correcta: A) Que un cartucho extraído de la biblioteca queda físicamente inalcanzable por la red, con coste por terabyte mínimo** Su acceso es secuencial, por lo que la restauración es lenta; existen además cartuchos WORM que impiden por hardware la reescritura.

*Referencia: §3.2.2 [LTO]*
</details>

---

### Pregunta 43

**¿Qué diferencia hay entre una copia inmutable y una copia fuera de línea?**

A) Ninguna: son dos nombres del mismo mecanismo
B) La inmutable se guarda en cinta y la fuera de línea, en disco
C) La inmutable está conectada pero no puede modificarse durante la retención; la fuera de línea es inalcanzable porque no existe camino hasta ella

<details><summary>Respuesta</summary>

**Correcta: C) La inmutable está conectada pero no puede modificarse durante la retención; la fuera de línea es inalcanzable porque no existe camino hasta ella** Ambas persiguen el mismo fin: que un atacante con credenciales de administrador no pueda destruir la copia.

*Referencia: §3.2.2 [S3-LOCK] [NIST-SP800-209]*
</details>

---

### Pregunta 44

**¿Cuál es la pieza más crítica de la arquitectura de una solución de copias de seguridad?**

A) El agente instalado en cada sistema de origen
B) El catálogo del servidor de control, que indexa qué hay en cada copia
C) La consola gráfica de administración

<details><summary>Respuesta</summary>

**Correcta: B) El catálogo del servidor de control, que indexa qué hay en cada copia** Sin catálogo la restauración granular es casi imposible, por lo que debe copiarse aparte y todo plan de recuperación debe contemplar su reconstrucción como primer paso.

*Referencia: §3.3.1 [NIST-SP800-34]*
</details>

---

### Pregunta 45

**¿Para qué sirve el protocolo NDMP?**

A) Para copiar una cabina NAS enviando sus datos directamente al destino sin pasar por un servidor intermedio
B) Para cifrar el tráfico entre el agente y el servidor de copia
C) Para deduplicar los bloques en el cliente antes de enviarlos

<details><summary>Respuesta</summary>

**Correcta: A) Para copiar una cabina NAS enviando sus datos directamente al destino sin pasar por un servidor intermedio** Preserva además los atributos y permisos propios del sistema de ficheros de la cabina.

*Referencia: §3.3.1 [NDMP]*
</details>

---

### Pregunta 46

**¿Cuál es la única verificación que mide el RTO real de un servicio?**

A) La comprobación de que el trabajo de copia ha terminado sin errores
B) El cálculo de la suma de verificación de los bloques escritos
C) La prueba de restauración real, documentada y cronometrada

<details><summary>Respuesta</summary>

**Correcta: C) La prueba de restauración real, documentada y cronometrada** Que un trabajo termine «con éxito» no significa que la copia sirva; el ENS exige probar el plan y el RGPD, en su artículo 32.1.d, la verificación regular de la eficacia.

*Referencia: §3.3.2 [ENS] [RGPD]*
</details>

---

### Pregunta 47

**¿Qué relación hay entre el plan de recuperación ante desastres (DRP) y el plan de continuidad del negocio (BCP)?**

A) El DRP es la parte TIC del BCP, que es más amplio y abarca personas, sedes, procesos y proveedores
B) Son sinónimos y la norma emplea ambos términos indistintamente
C) El BCP es la parte técnica y el DRP el documento de gestión

<details><summary>Respuesta</summary>

**Correcta: A) El DRP es la parte TIC del BCP, que es más amplio y abarca personas, sedes, procesos y proveedores** Su articulación se describe en la norma ISO/IEC 27031 y en la guía NIST SP 800-34.

*Referencia: §3.3.2 [ISO27031] [NIST-SP800-34]*
</details>

---

### Pregunta 48

**Un emplazamiento alternativo que dispone de espacio, energía y comunicaciones, pero sin equipos ni datos, se denomina…**

A) Emplazamiento caliente (hot site)
B) Emplazamiento frío (cold site)
C) Emplazamiento templado (warm site)

<details><summary>Respuesta</summary>

**Correcta: B) Emplazamiento frío (cold site)** Su activación se mide en días o semanas y su coste es bajo; el templado tiene el equipamiento instalado y datos parcialmente actualizados, y el caliente permite conmutar en minutos u horas.

*Referencia: §3.3.2 [NIST-SP800-34]*
</details>

---

### Pregunta 49

**En Windows, ¿qué papel desempeña el Servicio de instantáneas de volumen (VSS)?**

A) Deduplicar los bloques del volumen antes de enviarlos al repositorio
B) Cifrar la copia en tránsito hacia el servidor de control
C) Coordinar solicitante, escritores y proveedor para lograr una copia consistente con la aplicación

<details><summary>Respuesta</summary>

**Correcta: C) Coordinar solicitante, escritores y proveedor para lograr una copia consistente con la aplicación** Los escritores —SQL Server, Exchange, Active Directory— vacían sus búferes y congelan sus escrituras unos segundos mientras se crea la instantánea.

*Referencia: §4.1 [MS-VSS]*
</details>

---

### Pregunta 50

**¿Qué requisitos exige una recuperación bare-metal sobre hardware distinto del original?**

A) Una copia de imagen o volumen, un soporte de arranque de rescate y la inyección de controladores de almacenamiento y red
B) Una copia de ficheros y la reinstalación previa del sistema operativo
C) Una réplica síncrona del volumen y un sistema de ficheros de clúster

<details><summary>Respuesta</summary>

**Correcta: A) Una copia de imagen o volumen, un soporte de arranque de rescate y la inyección de controladores de almacenamiento y red** Sin esos controladores el sistema restaurado no arranca; restaurar una copia de ficheros sobre un equipo vacío no reconstruye un sistema arrancable.

*Referencia: §4.1.1 [NIST-SP800-34]*
</details>

---

### Pregunta 51

**En la copia sin agente de una máquina virtual, ¿de dónde obtiene los datos el software de copia?**

A) De un agente ligero instalado temporalmente en el sistema invitado
B) Del registro de transacciones de la aplicación
C) Del hipervisor, a través de su API de protección de datos, leyendo los discos virtuales

<details><summary>Respuesta</summary>

**Correcta: C) Del hipervisor, a través de su API de protección de datos, leyendo los discos virtuales** En vSphere ese conjunto de interfaces se conoce como VADP; en Hyper-V se apoya en los escritores VSS del anfitrión y en RCT.

*Referencia: §4.2.1 [VMW-VADP] [HYPERV-RCT]*
</details>

---

### Pregunta 52

**¿Qué modo de transporte de la copia sin agente lee directamente el LUN de la cabina sin cargar la red IP?**

A) NBDSSL
B) SAN, también llamado LAN-free
C) HotAdd

<details><summary>Respuesta</summary>

**Correcta: B) SAN, también llamado LAN-free** Exige un proxy con acceso a la red de almacenamiento. HotAdd conecta en caliente los discos al proxy virtual y NBD/NBDSSL usa la red de gestión del anfitrión, más lenta pero siempre disponible.

*Referencia: §4.2.1 [VMW-VADP]*
</details>

---

### Pregunta 53

**Una instantánea de máquina virtual mantenida durante meses provoca principalmente…**

A) Crecimiento incontrolado del fichero delta, degradación del rendimiento y una consolidación muy costosa
B) La pérdida del seguimiento de bloques modificados del hipervisor
C) La imposibilidad de migrar la máquina virtual entre anfitriones

<details><summary>Respuesta</summary>

**Correcta: A) Crecimiento incontrolado del fichero delta, degradación del rendimiento y una consolidación muy costosa** El delta puede llegar a llenar el almacén de datos, y cada lectura debe recorrer la cadena de instantáneas encadenadas.

*Referencia: §4.2.2 [VMW-SNAP]*
</details>

---

### Pregunta 54

**¿Por qué una instantánea no es una copia de seguridad?**

A) Porque no captura el estado de la memoria de la máquina virtual
B) Porque vive en el mismo almacén que el dato original y depende de él
C) Porque no puede crearse con la máquina encendida

<details><summary>Respuesta</summary>

**Correcta: B) Porque vive en el mismo almacén que el dato original y depende de él** Si se pierde o se corrompe el almacén de datos, se pierden ambos; la copia de seguridad, en cambio, es independiente y reside en otro sitio.

*Referencia: §4.2.2 [VMW-SNAP] [ISO27002]*
</details>

---

### Pregunta 55

**¿Qué aporta el seguimiento de bloques modificados (CBT) a la copia de una máquina virtual?**

A) Cifra los bloques antes de enviarlos al repositorio
B) Garantiza la consistencia de la base de datos alojada en la máquina virtual
C) Permite que el incremental lea solo los bloques cambiados, sin recorrer todo el disco virtual

<details><summary>Respuesta</summary>

**Correcta: C) Permite que el incremental lea solo los bloques cambiados, sin recorrer todo el disco virtual** Es una función del hipervisor —RCT en Hyper-V—, reduce drásticamente la ventana de copia y hace viable el modelo incremental para siempre.

*Referencia: §4.2.2 [VMW-VADP] [HYPERV-RCT]*
</details>

---

### Pregunta 56

**¿Cuál es la diferencia esencial entre replicar una máquina virtual y hacer su copia de seguridad?**

A) La réplica está lista para arrancar en el destino, mientras que la copia hay que restaurarla antes de poder usarla
B) La réplica conserva más puntos de restauración históricos que la copia
C) La réplica protege mejor frente a la corrupción lógica y el ransomware

<details><summary>Respuesta</summary>

**Correcta: A) La réplica está lista para arrancar en el destino, mientras que la copia hay que restaurarla antes de poder usarla** Precisamente por eso la réplica da un RTO de minutos, pero guarda pocos puntos en el tiempo y replica la corrupción casi al instante: ambas son complementarias.

*Referencia: §4.2.3 [NIST-SP800-34]*
</details>

---

### Pregunta 57

**¿En qué consiste la restauración instantánea (instant recovery) de una máquina virtual?**

A) En restaurar únicamente los ficheros seleccionados por el usuario
B) En arrancar la máquina directamente desde el repositorio de copias mientras sus datos se migran en segundo plano
C) En conmutar el servicio a la réplica del emplazamiento alternativo

<details><summary>Respuesta</summary>

**Correcta: B) En arrancar la máquina directamente desde el repositorio de copias mientras sus datos se migran en segundo plano** El servicio vuelve en minutos aunque la restauración completa tarde horas; es la técnica que más ha reducido el RTO en la última década.

*Referencia: §4.2.3 [VEEAM-DOC]*
</details>

---

### Pregunta 58

**¿Qué artículo del Real Decreto 311/2022 (ENS) establece que los sistemas dispondrán de copias de seguridad y de mecanismos que garanticen la continuidad de las operaciones?**

A) El artículo 26, sobre continuidad de la actividad
B) El artículo 5, sobre categorización de los sistemas
C) El artículo 44, sobre auditoría de la seguridad

<details><summary>Respuesta</summary>

**Correcta: A) El artículo 26, sobre continuidad de la actividad** Ese mandato se desarrolla en el Anexo II mediante la medida mp.info.6, de copias de seguridad, y el grupo op.cont, de continuidad del servicio.

*Referencia: §5.1.1 [ENS]*
</details>

---

### Pregunta 59

**Según el ENS, ¿qué nivel de protección debe aplicarse a las copias de seguridad?**

A) Un nivel inferior al de los datos originales, por tratarse de información ya consolidada
B) Únicamente la protección física del soporte donde residen
C) El mismo nivel de seguridad que a los datos originales, en control de acceso, cifrado y protección física

<details><summary>Respuesta</summary>

**Correcta: C) El mismo nivel de seguridad que a los datos originales, en control de acceso, cifrado y protección física** Es la exigencia menos intuitiva y la más incumplida: una copia mal custodiada es una fuga de datos esperando a ocurrir.

*Referencia: §5.1.1 [ENS] [CCN-STIC]*
</details>

---

### Pregunta 60

**Un ciudadano ejerce su derecho de supresión y los datos figuran también en las copias de seguridad. ¿Cuál es la actuación correcta?**

A) Restaurar cada copia, borrar el dato y volver a generar la copia
B) Suprimir el dato en producción, bloquear el tratamiento en las copias y volver a aplicar la supresión si alguna se restaura
C) Destruir de inmediato todas las copias que contengan ese dato

<details><summary>Respuesta</summary>

**Correcta: B) Suprimir el dato en producción, bloquear el tratamiento en las copias y volver a aplicar la supresión si alguna se restaura** Editar una copia consolidada es inviable y destruiría su integridad; la supresión efectiva llega cuando la copia vence conforme a la política de retención.

*Referencia: §5.2.1 [RGPD] [LOPDGDD] [AEPD]*
</details>
