# Curso de pensamiento probabilístico
La diferencia entre la programación estocástica y probabilística es que en la primera usamos aleatoriedad a nuestros programas, en la segunda usamos las distribuciones de estadística.
Ejemplos:
- ¡Uber usa programación estadística!
- Un ejemplo de machine learning es para filtrar spam del email, ¡esto es estadística!
- Medicina, obvio.

Cada vez que usamos "Y", "AND" => la probabilidad se reduce.

## Programación probabilística

Probabilidad es cuántas veces sucede un evento dentro de la totalidad de eventos posibles.
### Probabilidad condicional
Probabilidad condicionada es la probabilidad de que ocurra un evento A, sabiendo que también sucede otro evento B. Depende de otro evento.

P(A|B) => Probabilidad de A, sabiendo que ha sucedido B.

P(A and B) = P(A)*P(B)
PERO, supongamos que ya pasó A
P(A and B) = P(A) * P(B|A) => Quiere decir que multiplicamos probabilidad de A por probabilidad de B, dado que ya pasó A.

| -> Significa "dado que"
¬ -> Significa "no suceda o negativo"

P(B) = P(A) * P(B|A) + P(¬A) * P(B|¬A)
P(cancer) = P(positivo) * P(cancer|positivo) + P(negativo) * P(cancer|negativo)
P(drogas) = P(musico) * P(drogas|musico) + P(¬musico) P(drogas|¬musico)

### Teorema de Bayes
No podemos saltar a conclusiones tan rápidamente.

P(A|B) = [P(B|A)P(A)] / P(B)
Probabilidad de una hipótesis A dada una evidencia B, es igual a la probabilidad de A y B entre la probabilidad de B.

P(H|E)=[P(H and E)]/P(E)

H = hipótesis
E = Evento
P(H) = Prior = hipótesis antes de la evidencia
P(H|E) = Posterior = Ya teniendo evidencia como actualizamos cierta creencia.
P(E|H) = Likelihood = Certeza de que esta situación es correcta.

**La probabilidad es la matemática de las proporciones**

## Aplicaciones del Teorema de Bayes
​
El Teorema de Bayes es uno de los mecanismos matemáticos más importantes en la actualidad. A grandes rasgos, nos permite medir nuestra certidumbre con respecto a un suceso tomando en cuenta nuestro conocimiento previo y la evidencia que tenemos a nuestra disposición. El Teorema de Bayes permea en tu vida diaria, desde descubrimientos científicos hasta coches autónomos, el Teorema de Bayes es el motor conceptual que alimenta mucho de nuestro mundo moderno.
​
En esta lectura me gustaría darte ejemplos de cómo se utiliza en la vida moderna para que puedas comenzar a implementarlo en tus proyectos, análisis y hasta en
tu vida personal.
​

### Turing y el código enigma de los Nazis
​
Casi todos sabemos que Alan Turing es uno de los padres del cómputo moderno; pocos saben que fue gracias a él que los aliados pudieron tener una ventaja decisiva cuando Turing logró descifrar el código enigma que encriptaba todas las comunicaciones nazis; pero aún menos saben que para romper este código utilizó el Teorema de Bayes.
​
Lo que hizo Turing fue aplicar el Teorema para descifrar un segmento de un mensaje, calcular las probabilidades iniciales y actualizar las probabilidades
de que el mensaje era correcto cuando nueva evidencia (pistas) era presentada.
​

### Finanzas
​
Una de las decisiones más difíciles cuando estás manejando un portafolio de inversión es determinar si un instrumento financiero (acciones, valores, bonos, etc.) se va a apreciar en el futuro y por cuánto, o si, por el contrario se debe vender el instrumento. Los portafolios managers más exitosos utilizan el Teorema de Bayes para analizar sus portafolios.
​
En pocas palabras, puedes determinar las probabilidades iniciales basándote en el rendimiento previo de tu portafolio o en el rendimiento de toda la bolsa y
luego añadir evidencia (estados financieros, proyecciones del mercado, etc.) para tener una mayor confianza en las decisiones de venta o compra.
​

### Derecho
​
El Derecho es uno de los campos más fértiles para aplicar pensamiento bayesiano. Cuando un abogado quiere defender a su cliente, puede comenzar a evaluar una probabilidad de ganar (basada en su experiencia previa, o en estadísticas sobre el número de juicios y condenados con respecto del tema legal que competa) y actualiza su probabilidad conforme vayan sucediendo los eventos del proceso jurisdiccional.
​
Cada nueva notificación, cada prueba y evidencia que encuentre, etc. sirve para actualizar la confianza del abogado.
​

### Inteligencia artificial
​
El Teorema de Bayes es central en el desarrollo de sistemas modernos de inteligencia artificial. Cuando un coche autónomo se encuentra navegando en las calles, tiene que identificar todos los objetos que se encuentran en su “campo de visión” y determinar cuál es la probabilidad de tener una colisión. Esta probabilidad se actualiza con cada movimiento de cada objeto y con el propio movimiento del vehículo autónomo. Esta constante actualización de probabilidades es lo que permite que los vehículos autónomos tomen decisiones
acertadas que eviten accidentes.
​
En esta rama existen muchos ejemplos como para cubrirlos todos, pero quiero por lo menos mencionar algunos casos de uso: filtros de spam, reconocimiento de voz, motores de búsqueda, análisis de riesgo crediticio, ofertas automáticas, y un largo etcétera.
​
Para terminar, me gustaría compartir una cita del famoso economista John Maynard Keynes que resume perfectamente el tipo de pensamiento que quiero que desarrolles: “Cuando los hechos cambian, yo cambio mi opinión. ¿Qué hace usted, señor?”

## Mentiras estadísticas

### Garbage in, garbage out (GIGO)
Esto significa que si le avientas basura, recibirás basura.
La calidad de nuestros datos es igual de importante que la precisión de nuestros cómputos.

### Imágenes engañosas
Nunca se debe confiar en una gráfica sin escala o sin etiquetas.
Las escalas normalmente deben empezar en 0, con ciertas excepciones.

### Cum Hoc Ergo Propter Hoc
Es decir, *La correlación entre 2 variables **no** significa causalidad.*
`Después de esto, eso; entonces a consecuencia de esto, eso.`
Correlación quiere decir que 2 variables se mueven en el mismo sentido.
- Positiva: Van al mismo lugar.
- Negativa: Van en sentidos contrarios.
La correlación de mide de -1 a 1.

### Prejuicio en el muestreo
Si no tenemos aleatoriedad en nuestro muestreo, el resultado no puede generalizarce a toda la población.

### Falacia de francotirador de Texas
Se da cuando no se toma la aleatoriedad en consideración.
También sucede cuando se enfoca en las similitudes y se ignoran las diferencias.
Esto pasa cuando la hipotesis se adecuan a los datos *MUY MAL*.

### Porcentajes confusos
¡Necesitamos la cuenta y contexto para entender los porcentajes!

### Falacia de regresión
Por ejemplo, a un atleta le va muy mal por una semana y decide cambiar su alimentación y él le atribuye su mejora a su alimentación *(error)* cuando realmente es la regresión a la media.
`Cuando algo fluctua y se aplican medidas correctivas se puede creer que existe un vínculo de casualidad en lugar de una regresión a la media.`

## Introducción a Machine Learning
¿Qué es machine learning?
"Es el campo de estudio que le da a las computadoras la habilidad de aprender sin ser explícitamente programadas." - Arthur Samuel, 1959

- Machine learning se utiliza cuando:
    - Programar un algoritmo es imposible
    - El problema es muy complejo o no se conocen algoritmos para resolverlo
    - Ayuda a los humanos a entender patrones (data mining)

- Aprendizaje supervisado vs no supervisado vs semisupervisado

- Batch vs online learning

### Feature vectors
Se refiere a una forma de tomar aspectos de objetos del mundo real y representarlos numéricamente para que ML pueda trabajar con ellos.
- Un ejemplo común de estos es la representación de colores = [R,G,B]
- Procesamiento de imágenes
- Reconocimiento de voz
- Spam
Tenemos que saber identifiar qué SÍ importa y qué no importa.

### Métricas de distancia
Muchos algortimos de ML pueden clasificarse como algoritmos de optimización.
Lo que se desea optimizar es una función que en muchas ocasiones se refiere a la distancia entre features.

## Agrupamiento (clustering)
Es un proceso mediante el cual se agrupan objetos similares en clusters que los identifican. Se clasifica como aprendizaje no supervisado ya que no requiere de la utilización de etiquetas. Permite entender la estructura de los datos y la similitud entre los mismos.

### Agrupamiento jerárquico

### K means
Es un algoritmo que agrupa utilizando centroides.

## ¿Qué son las técnicas de agrupamiento?
​
El agrupamiento es una técnica de Machine Learning que consiste, en pocas palabras, en dividir cierta población en grupos con la consecuencia de que los datos en un grupo sean más similares entre ellos que comparado con los otros grupos.
​
Imagina que eres el dueño de una startup que hace e-commerce y quieres tener estrategias de venta para tus clientes. Es casi imposible diseñar una estrategia por cada individuo, pero se puede utilizar el agrupamiento para dividir a los clientes en grupos que tengan similitudes relevantes y así reducir el problema a unas cuantas estrategias.
​

## Tipos de agrupamiento
Existen dos tipos de agrupamiento:
​

- Agrupamiento estricto (hard clustering): cada dato pertenece a un grupo u otro, no hay puntos medios.
- Agrupamiento laxo (soft clustering): en lugar de asignar un dato a un grupo, se asignan probabilidades a cada dato de pertenecer o no a un grupo.
​
Un punto muy importante que debes considerar cuando ejecutas técnicas de agrupamiento es que debes definir muy claro a qué te refieres cuando hablas de similitud entre puntos, porque esto puede ayudarte a definir el algoritmo correcto para tus necesidades particulares.
​
## Modelos para determinar similitudes
A grandes rasgos, existen cuatro aproximaciones para definir similitud:
​

- Modelos conectivos: asumen que los puntos más similares son los que se encuentran más cercanos en el espacio de búsqueda. Recuerda que este espacio puede ser altamente dimensional cuando tus feature vectors definen muchas características a analizar. Una desventaja de este tipo de modelos es que no escalan para conjuntos de datos grandes, aunque es posible utilizar una muestra y aplicar técnicas de estadística inferencial para obtener resultados.
- Modelos de centroide: definen similitud en términos de cercanía con el centroide del grupo. Los datos se agrupan al determinar cuál es el centroide más cercano.
- Modelos de distribución: trata de asignar probabilidades a cada dato para determinar si pertenecen a una distribución específica o no (por
ejemplo, normal, binomial, Poisson, etc.).
- Modelos de densidad: analizan la densidad de los datos en diferentes regiones y dividen el conjunto en grupos, luego asignan los puntos de acuerdo a las áreas de densidad en las que se haya dividido el dataset.
​
Acuérdate de no casarte con un modelo específico. Muchas de las mejores Ingenieras de Machine Learning y Científicas de Datos utilizan varios modelos con el mismo conjunto de datos para analizar el rendimiento de los diversos algoritmos que tienen a su disposición. Así que experimenta y siempre compara tus resultados antes de tomar una decisión.

## Introducción a la clasificación
- Es el proceso mediante el cual se predice la clase de cierto dato.
- Es un tipo de aprendizaje supervisado ya que para que funcione, se necesitan etiquetas (labels) con los datos.
- Sigue dos pasos: aprendizaje (creación del modelo) y clasificación.


### Clasificación K-nearest neighbors
- Parte del supuesto de que ya tenemos un conjunto de datos clasificados.
- Trata de encontrar los "vecinos más cercanos".
- K se refiere a la cantidad de vecinos que se utilizarán para clasificar un ejemplo que aún no ha sido clasificado.
- Es sencillo de implementar y tiene aplicaciones en medicina, finanzas, agricultura, etc.
- Es computacionalmente muy costoso y no sirve con datos de alta dimensionalidad.

### Otras técnicas de clasificación

### Técnicas de clasificación
​
La clasificación es un tipo de Machine Learning supervisado. Esto significa que para entrenar un modelo necesitamos un conjunto de datos (dataset) que ya tenga etiquetas (labels) para poder entrenar nuestros modelos.
​
La mejor forma de pensar en algoritmos de clasificación es pensar en el sombrero clasificador de Harry Potter. Cuando un nuevo alumno de Hogwarts entra a la escuela es necesario asignarlo/clasificarlo en una de las 4 casas. El sombrero obtiene los datos cuando se lo coloca el alumno y define cuál es el mejor match para su caso particular. Aquí estamos asumiendo que el sombrero es un algoritmo que ya ha sido entrenado y que los alumnos son nuevos data points que tienen que ser clasificados.
​

### Clasificadores lineales
​
Estos tipos de clasificadores se distinguen porque dividen el conjunto de datos con una línea (que puede ser multidimensional dependiendo de la cantidad de features que hemos utilizado para definir a nuestros datos). Esto genera áreas dentro de nuestro espacio de búsqueda para que cuando coloquemos un nuevo dato podamos clasificarlo fácilmente.
​
El problema con este tipo de modelos es que son pocos flexibles cuando el conjunto de datos no puede ser separado fácilmente con una simple línea; por ejemplo, cuando necesitáramos una figura más compleja para dividirlo (como un polígono).
​

### Regresión logística
​
Estos algoritmos se parecen mucho a los clasificadores lineales, con la diferencia de que no se divide simplemente con una línea, sino con un gradiente que determina la probabilidad de que un punto pertenezca a una categoría u otra. Es decir, la gradiente determina la probabilidad de que un punto sea asignado a una categoría y mientras un dato se aleje más en una dirección será mayor la probabilidad de que pertenezca a una categoría.
​
Imagina que estos algoritmos generan un área difusa en la que no estamos seguros de la clasificación y un área clara en la que tenemos un alto grado de certeza
en cuanto a la categoría que pertenece un punto.
​

### Nearest neighbor
​
Los modelos que utilizan nearest neighbor se apoyan de los datos que ya han sido clasificados para determinar la distancia entre sus “vecinos más cercanos.” El algoritmo más común que utiliza esta técnica se llama K-nearest neighbors y la K representa el número de vecinos que se utilizarán para clasificar los datos. En pocas palabras, se identifican los datos más cercanos y en el caso más sencillo se hace una votación simple (por ejemplo, 5 azules, 2 rojos, por lo tanto azul).
​
Una característica de estos modelos es que “dibujan” una línea que se asemeja a una costa para clasificar los datos. Mientras K sea más grande la “línea costera” se alisa y se asemeja más y más a una línea simple. Por lo tanto, la definición de K tiene un impacto importante en el desempeño de nuestro algoritmo de clasificación.
​

### Support Vector Machines
​
Estos algoritmos se diferencian por tener la habilidad de generar figuras complejas (polígonos) que pueden agrupar datos. Si la figura que tendríamos que dibujar para dividir nuestros datos es diferente a una línea (círculos, polígonos, etc.), entonces estos modelos son una buena opción.
​

### Árboles de decisión
​
Este tipo de algoritmos nos permiten generar una árbol que tenemos que recorrer y tomar decisiones cada vez que avanzamos en un nivel. Por ejemplo:
​

- Si un feature en análisis es mayor a 5, dibuja la línea y=2x+3, de lo contrario dibuja y=-3x+5
- Si el feature siguiente es menor a 2, dibuja otra línea y así sucesivamente.
​
## Conclusiones
- El pensamiento probabilístico permite evaluar un mundo que es por su propia naturaleza no determinístico.
- Los números no mienten pero la gente los puede usar para mentir y manipular.
- Estas herramientas sirven para fortalecer la capacidad de razonamiento lógico.

# examen
¿A qué categoría de machine learning pertenece la clasificación?:a
¿Qué parámetro controla K dentro del algoritmo de K-nearest neighbors?:d
Antes de que se realice un examen médico, ¿cuál es tu probabilidad (sin mayor información) de padecer una enfermedad?:d
¿Cuál NO es un algoritmo de agrupamiento?:Regresión logística
¿Cuántos grupos deben existir para que el algoritmo de agrupamiento jerárquico termine?:dca❌
¿Cómo se lee la siguiente expresión?: P(H | E):e
La regresión logística modela la probabilidad de que un tipo de evento suceda. ¿Es un enunciado?:a
Se puede leer un gráfico, ¿aún si no existen etiquetas?:e
¿Puede la matemática convertir datos malos en buenos resultados?:a
Dado que se obtuvo una muestra de los alumnos de Platzi, ¿se pueden realizar conclusiones sobre toda la población de estudiantes en línea?:a
¿Se corre el riesgo de caer en la Falacia del Francotirador de Texas cuando realizan experimentos sin una hipótesis?:b
¿A qué categoría de machine learning pertenece el agrupamiento K-means?:b
¿Para qué nos sirven las métricas de distancia en Machine Learning?:a
Un aumento del 10% o del 30%, ¿Qué es mejor?:c
¿Cuál de las siguientes NO es una aplicación del Teorema de Bayes?:e
El centroide, dentro del agrupamiento de K-means, ¿es estático?:c
¿Cuál fue el programa que le ganó en 1997 a Kaspárov en Ajedrez?:b
¿Cuál de los siguientes no es un algoritmo de clasificación?:c
El teorema de Bayes nos permite:a
Siempre que existe un evento extremo, ¿el siguiente evento tenderá a regresar a la media?:e
La correlación y la causalidad es lo mismo. ¿Es un enunciado?:a