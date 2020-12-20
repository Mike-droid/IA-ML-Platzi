# Análisis de negocios para ciencia de datos

## 1. El mundo de los datos: data science y machine learning

### ¿Qué es y qué hace el Científico de datos o Data Scientist?
Científico de datos: Persona que sabe más de estadística que cualquier programador y que a la vez sabe más de programación que cualquier estadístico.
Profesional dedicado a analizar e interpretar grandes bases de datos.

- Recopilar grandes cantidades de datos revueltos y transformarlos a un formato más utilizable.
- Resolver problemas relacionados con negocios empleando técnicas basadas en datos.
- Trabajar con diversos lenguajes de programación, incluidos SAS, R y Python.
- Dominar técnicas analíticas como el machine learning, deep learning y analítica de texto.
- Buscar orden y patrones en datos, además de detectar tendencias que puedan ayudar a la base de
operación de una empresa.

¿A qué se dedica un data scientist?
"A brindar soluciones matemáticas y estadísticas para resolver problemas del negocio".

### ¿Qué tipos de datos se pueden generar?
- Personas: Esto se ve reflejado en redes sociales, por ejemplo.
- Transacciones: Monetarias y no monetarias. Tarjetas de débito y crédito, compras online.
- Navegación web: Cookies 🍪
- Machine 2 Machine: Conexión de máquinas, por ejemplo GPS.
- Biométricos: Información para identificarte como ser único, tus genes, sangre, saliva, huella dactilar, etc.

### Cómo crear un cultura data-driven
1. Crear una **cultura** de datos: Entenderlo, hacer que los empleados tomen decisiones basadas en datos.
2. **Recolectar** información.
3. Medir **todo**.
4. Datos **relevantes** y **precisos**.
5. Testear y crear **hipótessis**: Tienes que pensar en preguntas *específicas*.
6. Desde los **insights** de datos a las **acciones**: Por ejemplo campañas de marketing **personalizadas**.
7. Cumplir las **regulaciones** de datos: ¡No puedes tomar decisiones sesgadas ni que no sean éticas!
8. **Automatizar**

### ¿Qué es inteligencia artificial y machine learning?
La IA se automatiza. Nosotros como humano tenemos emociones, sentimientos, nos sesgamos, eso no pasa con las computadoras.
- AI = Máquinas inteligentes.
- ML = Aprendizaje automatizado (por ejemplo eliminación de SPAM).
- DL = Transformar un punto de imagen en un dato útil.

### Machine learning
- Detección de fraudes: Se pueden bloquear tarjetas por comportamientos sospechosos.
- Búsquedas web: Buscas algo en internet y te salen anuncios relacionados a tu búsqueda.
- Anuncios a tiempo real: Adquieres un producto e inmediatamente te recomiendan otro para que compres más.
- Análisis de textos: Información categórica.
- Next best action: Saber qué está haciendo tu cliente, en qué fase de vida se encuentra y cuál será su siguiente movimiento.

### ¿Qué es deep learning? Análisis de imagen, audio y video
Una máquina acierta el 99% de las ocasiones. Nosotros el 95% pero va bajando conforme pasa el tiempo por el cansansio.
- Shazam convierte el sonido en código binomial: ¿es agudo, es grave? Con la base de datos encuentra la canción.
- Tesla (carro) convierte la información que reciben las cámaras para detener o avanzar.


## 2. Herramientas y roles de trabajo en ciencia de datos

### Flujo de trabajo en ciencia de datos: fases, roles y oportunidades laborales
1. Ingeniero/Arquitecto de datos: Bases de datos, ETLs/APIs, SQL y NoSQL
2. Analista business intelligence: Extración y dashboards, Automatización, SQL y Excel [Nos habla del pasado y presente]
3. Data scientist: Machine learning, Modelos estadísticos, R y Python [Predice el futuro con R]
4. Data translator: Deta scientist- decision makers, Destiladores de data, Expertos en necesidad de negocio [No necesariamente es una persona técnica]

### Herramientas para cada etapa del análisis de datos
- Extración de información con SQL: Encontrar información con una BBDD pequeña o gigante.
- Análisis y visualización con R y Python: Gráficos y visualización. R tiene un enfoque más estadístico. Python está más basado en la ingeniería.

### ¿Qué es y cómo usar una base de datos relacional con SQL?
#### Comandos
- Select : Selección de los campos (columnas) para hacer el análisis o para sintetizar la tabla de origen.
#### Claúsulas
- From: Tabla donde se almacena la información.
- Where: Especificar las condiciones.
- Group by: Campos (Columnas) de agrupación.
- Order by: Campos (columnas) de ordenación.
#### Operadores lógicos
- And: Une varias condiciones que tienen que ser cumplidas para obtener resultados.
- Or: Evalúa dos o más condiciones y obtienes resultados si una de ellas se cumple.
- Not: Excluye un valor de la información a obtener.
#### Funciones agregadas
- Avg: Promedio (average) de un campo (columna).
- Count: Recuento de valores de una columna.
- Distintct: Encontrar valores únicos.
- Sum: Suma de valores de una columna.
- Max: Valor más alto de una columna.
- Min: Valor más bajo de una columna.

#### ¿Qué tipos de comandos hay dentro del SQL?
Los comandos del lenguaje SQL se dividen según su función en estos 5 tipos:

- DDL (Data Definition Language): definen el esquema o estructura de la base de datos. Ejemplos: CREATE (crear); ALTER (alterar); DROP (eliminar objetos); RENAME (renombrar); TRUNCATE (quita todos los registros de una tabla, incluidos los espacios de los registros eliminados); COMMENT (comentar); entre otros.
- DQL (Data Query Language): sirven para hacer consultas sobre los datos en el esquema de objetos. Un objeto puede ser desde un resultado de búsqueda a una tabla. El propósito del comando es el de establecer una relación, basada en la consulta, dentro de la estructura de la base de datos, como la función de búsqueda. Ejemplo: SELECT (recuperar registros de la base de datos).
- DML (Data Manipulation Language): tratan la manipulación de los datos presentes en la base de datos. La mayoría de los comandos pertenecen a este tipo. Ejemplo: INSERT (insertar un objeto); DELETE (eliminar registros); UPDATE (actualizar); CALL; MERGE (3 en 1, inserta, elimina y actualiza); LOCK TABLE (bloquear tabla); EXPLAIN PLAN (determina el plan de acceso); …
- DCL (Data Control Language): se encargan de los derechos, los permisos y otros controles del sistema de la base de datos. Ejemplos: GRANT (proporcionar privilegios acceso a un usuario); REVOKE (revocar el derecho de accceso dado a un usuario); etc.
- TCL (Transaction Control Language): sirve para las transacciones con la base de datos. Es decir, con estos comandos se puede llevar un control sobre otros comandos y cómo afectan a la base de datos. Ejemplos: COMMIT (llevar a cabo una transacción); ROLLBACK (revertir una transacción en caso de que ocurra algún error); SAVEPOINT (establecer un punto de rescate dentro de una transacción.).

### Cómo estructurar queries en SQL
`CREATE TABLE VENTAS_2020 (
	Dia int not null,
	Mes int not null,
	Anio int not null,
	Producto varchar (25) not null,
	id int PRIMARY KEY,
	valor int not null
);`

`INSERT INTO VENTAS_2020 (Dia, Mes, Anio, Producto, id, valor)
values (1,2,1998,'Bocina',24,528),
	   (12,4,2004, 'Auriculares',31,240),
	   (14,8,2016,'Auriculares',14, 315),
	   (16,10,2019,'Bocina',200,1050),
	   (21,12,2020,'Bocina',304,680);`

#### Objetivo: Saber CUÁNTAS bocinas hemos vendido por más de 600 MXN desde 2019
`SELECT COUNT(DISTINCT id)
FROM ventas_2020
WHERE Producto='Bocina'
AND valor > 600
AND anio >= 2019`
Resultado: 2

#### Objetivo: Saber el promedio del valor de bocinas desde 1998 hasta 2020
`SELECT AVG(valor)
FROM ventas_2020
WHERE Producto='Bocina'`
Resultado: 752.66

## 3. Problema de negocio: análisis
### Aplica técnicas de storytelling para convertir problemas de datos en historias
Extraer un problema en una estructura lógica.
#### Estructura del problema
- Problema
- Solución
- Alcance

### Cómo estructurar un caso de negocio
Hipótesis / Storytelling
- Qué
- Por qué
- Cómo: Estrategia de cómo vamos a diseñar nuestro análisis.

1. Identificar
2. Encontrar las categorías
3. Poner en conjunto esta información
4. Crear acciones con esta información
5. Validar que todo nuestro estudio esté sirviendo

### Análisis cuantitativo en un caso de negocio
- Descargar información con SQL. Encontrar clientes que (en este caso) hayan hecho por lo menos 1 queja. Detectar esto por mes.
- Identificar: Debemos encontrar patrones de comportamientos y variables significativas.
- Definir.

### Análisis cualitativo en un caso de negocio
- Clusterizar: causas de contacto.
- Clasificar: cuases de los TO(top offenders) identificados.
- Profundizar: motivos de contacto geolocalización.

### Fusión cuanti-cualitativa
Resolver de manera conjunta la información cuantitativa y cualitativa para sacar conclusiones.

### Minería de texto
Entender los mensajes, encontrar información nueva. Twitter hace esto constantemente.
La minería de textos es una rama específica de la minería de datos que se refiere al proceso de analizar y derivar información nueva de textos. Por medio de la identificación de patrones o correlaciones entre los términos se logra encontrar información que no está explícita dentro del texto. Los textos que se usan como recursos pueden ser páginas web, libros, correos electrónicos, reseñas de clientes, artículos, entre otros.

La minería de textos es un área multidisciplinaria basada en la recuperación de información, aprendizaje automático, estadísticas y la lingüística computacional. Como la mayor parte de la información (más de un 80%) se encuentra actualmente almacenada como texto, se cree que la minería de textos tiene un gran valor comercial.

### Variación de comportamientos a partir de la geolocalización
Podemos observar diferentes comportamientos o comportamientos similares dependiendo de la ubicación de nuestros clientes.

## Problema de negocio: implementación

### Acciones, algoritmos y toma de decisiones según los resultados del análisis

Algoritmos usados:
- Minería de datos para clasificación de motivos de contacto.
- Correlaciones y patrones de comportamiento.
- Árboles de decisión y teoría de juegos para predecir y tomar decisiones.
- Validación con bayesianos y MCMC.

Acciones:
- Taggear a los TO identificados mensualmente.
- Advertilos.
- Llamar usuarios.
- Bloquear usuarios (Este no es ideal pero a veces es necesario).
- Validación con A/B Tests (Necesitamos saber si funciona).