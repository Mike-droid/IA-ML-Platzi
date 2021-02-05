# Fundamentos matemáticos para la Inteligencia Artificial
## 1. Motivación
### Bases de la IA
"(IA) es la ciencia e ingenio de hacer máquinas inteligentes." - John McCarthy, 1956
Imitar funciones cognitivas humanas.
- Aprender
- Adaptarse
- Tomar decisiones

#### Aprendizaje estadístico
Datos (entrada) => Datos recogidos junto con algoritmo => Procesamiento => Resultado (salida)

#### Aprendizaje supervisado
Necesita que un humano esté supervisando los datos que entran
Supervisión => Datos de entrenamiento   => Algoritmo => Procesamiento => Resultado
Datos de entrada  -------------------------⤴

#### Aprendizaje no supervisado
Datos de entrada => Interpretación => Algoritmo => Procesamiento => Resultado

#### Aprendizaje por refuerzo
El algoritmo aprende de manera automática, es cíclica. Si el resultado es bueno, se le "recompensa", si no, se le "regaña".
- DeepFake: Mostrar la cara de una persona importante en un vídeo, diciendo cosas que nunca ha dicho.

Algunas aplicaciones:
- Internet
- Agricultura
- Marketing
- Transporte
- Finanzas
- Defensa
- Medicina
- Videojuegos
- Atención al cliente
- Industria

## Vectores
Operaciones:
- Suma y Resta => Resultado, 2 números de coordenadas (x,y)
- Multiplicación => Resultado, producto escalar o producto vectorial **(combinación lineal)**
    - Producto escalar: Multiplicar coordenada X con X, Y con Y, Z con Z y al final sumarlo todo.
    - Producto vectorial: Método de Gauss o Gauss Jordan

***¿Para qué sirve todo esto?
Machile learning requeire de muchas matemáticas y debemos optimizar las operaciones para no saturar a la computadora.***

## Matrices
Organización bidimensional de números, de orden mxn (filas y columnas).
- Matriz identidad: Tiene 1 en la diagonal principal y 0 en el resto de los espacios.
- Matriz fila y matriz columna: son vectores

## Álgebra lineal
Necesitamos encontrar un vector que nos dé el resultado que buscamos.
En el proceso obtendremos un sistema de ecuaciones lineales.
Las soluciones que puede tener un sistema de ecuaciones lineales son:
- Sistema compatible determinado (única solución)
- Sistema compatbile indeterminado (infinitas soluciones)
- Sistema incompatabile (No tiene soluciones)

## Método de Gauss
Este método sirve para mátrices cuadradas y NO cuadradas.

## Función
Entrada (x): se le llama variable independiente.

Salida f(x): se le llama variable dependiente, porque su resultado depende de x.

Toda función lleva asociada una gráfica y nos muestra su comportamiento
- Función cuadrática: x^2
- Función lineal: mx + n donde 'm'  es la pendiente
- Función cúbica x^3
- Función exponencial e^x
- Función de raíz de x
- Función de logaritmo de x `log(x)`
- Funciones trigonométricas
  - sen(x)
  - cos(x)
  - tan(x)
  - cot(x)
  - sec(x)
  - cosec(x)
- Funciones hiperbólicas
  - senh(x)
  - cosh(x)
  - tanh(x)
  - ctgh(x)
  - sech(x)
  - csech(x)

### Límites, Infinito y asíntotas. Teoremas
¿Cómo podemos saber lo que hace una función con solo ver su expresión?
Con el  límite, evaluando una función en un punto dado.

Para la matemática, un límite es una magnitud a la que se acercan progresivamente los términos de una secuencia infinita de magnitudes. Un límite matemático, por lo tanto, expresa la tendencia de una función o de una sucesión mientras sus parámetros se aproximan a un cierto valor.

Hay funciones que van mucho más rápido que otras hacia el infinito.

¿Qué pasa con la función f(x)=1/x? Que tiene una asíntota vertical en 0. Es decir, ese valor es indefinido, porque 1/0 = ????

Podemos aplicar límites en las sucesiones para conocer sus comportamientos.

Si obtenemos un ♾ como resultado, quiere decir que la función diverge.

Si obtenemos un número real como resultado, quiere decir que la función converge.

### Zoo de derivadas
f'(x) = df/df
- La derivada de una constante es 0
- f(x) = sen(x) => f'(x) = cos(x)
- f(x) = cos(x) => f'(x) = -sen(x)
- f(x) = Ln(x) => f'(x) = 1/x

### Útiles de la derivada

#### Regla de la cadena
df/dx = (df/dg)(dg/dx)

#### Derivadas parciales
Derivadas de funciones con varias variables.
f(x)
f(x,y)
f(x,y,z)

### Integrales
La integral es el proceso inverso a la derivada.
Cuando derivamos perdemos información.

### Teorema de Bolzano
Si una función f(x) es continua en un intervalo [a,b], cuyos valores extremos f(a) y f(b) tienen distinto signo, la función cortará al eje (y por tanto devolverá el valor 0) en algún punto del intervalo.
![](https://static.platzi.com/media/user_upload/cod1-347e2f56-60a2-400d-ab92-0791ebf1b829.jpg)
![](https://static.platzi.com/media/user_upload/cod2-b2c586e5-73db-44ae-bd69-9f0b79acd7f5.jpg)
![](https://static.platzi.com/media/user_upload/cod3-587258fc-62a4-46b1-8487-1dd868d6d276.jpg)

### Teorema de los Valores Intermedios
En el mismo caso y condiciones explicitadas en el teorema de Bolzano, la función alcanzará cualquier valor intermedio comprendido entre f(a) y f(b)]. Como puedes ver, no es más que una generalización del teorema de Bolzano.
![](https://static.platzi.com/media/user_upload/cod4-6c7d83a0-5db6-4ab1-b7a6-86b308c0edb1.jpg)

### Representación gráfica de funciones
1. Dominio
2. Puntos de corte
3. Asintotas
4. Crecimiento y decrecimiento
5. Máximos y mínimos
6. Concavidad y convexidad

- f'(x)>0 entonces ↗
- f'(x)<0 entonces ↘
- f''(x)>0 MÍNIMO
- f''(x)<0 MÁXIMO

## Optimización
Resumen procedimiento:

1. Plantear la función a maximiar o minimizar.
2. Plantear una ecuación que relacione las distints variables del caso, cuanod exista más de una variable.
3. Reemplazar las varaibles de las ecuaciones en la función, de tal forma que queden en términos de una sola variable.
4. Derivar la función e igualarla a cero, para hallar los máximos y mínimos.
5. Calcular la segunda derivada para comprobar los resultados obtenidos.

## Matemática avanzada
### Combinatoria
n! = n (n-1)(n-2)(n-3)... x 1

A esto se le llama factorial

***Esto se usa en el aprendizaje por refuerzo.***

![Tabla de combinaciones](tabla_combinaciones.png)

#### Pequeño teorma de Fermat
a^p - a  es divisible entre p si p es primo.

### No repetición
- Permutaciones: Posibles ordenaciones de un conjunto de n elementos distintos. (Esto es el factorial).
- Variaciones:Posibles muestras **ordenadas** de r elementos dinstintos extraídos de un conjunto de n elementos. ¡n no puede ser menor que r!
- Combinaciones: Posibles muestras **no ordenadas** de r elementos distintos extraídos de un conjunto de n elementos.

### Repetición
- Permutaciones: Posibles ordenaciones de una secuencia de n signos entre los que hay algunos repetidos. Uno se repite x veces, otro se repite y veces, otro z ...
- Variaciones: Posibles muestras ordenadas de r elementos no necesariamente distintos que se puedan extraer de un conjunto de n elementos. ¡Aquí r puede ser mayor que n!
- Combinaciones: Posibles muestras no ordenadas de r elementos no necesariamente distintos que se pueden extraer de un conjunto de n elementos.¡Aquí r puede ser mayor que n!

Resumen:
![resumen](resumen.png)

### Conjuntos
Es una agrupación de elementos que tienen características en común.
#### Subconjunto
Un conjunto que tiene menos elementos que el conjunto universo y pertenece a este.

### Grafos
Diagramas, vértices unidos con aristas. Una serie de elementos conectados entre sí. Estructura de datos no lineales de naturaleza dinámica. G=(V,A).
![Tipos de grafos](tiposDeGrafos.jpg)

#### Subgrafos
Es una porción de un grafo.

***Los grafos son usados en el Deep Learning*** de aquí salen las neuronas artificiales y redes neuronales.

#### Grafo bipartito
Relación de los elementos de un conjunto con otros elementos de otro conjunto.

#### Teorema de Hall
Que sea necesario para la completitud que no haya más correspondencias que subconjunto.
*'Dado un conjunto de “m” chicas y “n” chicos, sabiendo que cada chica conoce un determinado número de chicos, ¿bajo qué condiciones es posible que todas las chicas puedan casarse / emparejarse / citarse simultáneamente con uno de los chicos entre sus conocidos?'*

Philip Hall (1904 – 1982)

*El propio enunciado ya obliga a que el número de chicos “n” sea mayor o igual al de chicas “m”.* Es fácil encontrar algunos ejemplos sencillos donde no es posible la situación pedida: si dos chicas conocen a un solo chico, y se trata de la misma persona, una de las chicas quedará sin pareja; si tres chicas conocen solo a dos chicos, y son los mismos, tampoco podrán hacerse tres parejas; y así sucesivamente.


### Árboles 1
Un árbol es un tipo de grafo direccionado y enraizado. Quiere decir que un nodo es "el origen". Entonces los demás nodos que salgan de aquí serán las ramas. Los nodos finales se llaman hojas. Estas ramas y hojas serán **decisiones** que la máquina tomará.
Por ejemplo se usa cuando compras cosas en amazon y te recomiendan otros productos, o terminas una película en netflix y te recomiendan otras. Esto se hace por haber una relación.

Es común que en los árboles se realicen una serie de operaciones como:

1. Enumerar los nodos.
2. Buscar un vértice.
3. Dado un nodo, listar sus hijos o sucesores.
4. Borrar un elemento.
5. Eliminar un subárbol (podar una rama).
6. Añadir un subárbol (injertar una rama).
7. Encontrar la raíz de un nodo cualquiera.
8. Recorrer el árbol:
  - Azar.
  - Primero a lo ancho.
  - Primero en profundidad.
9. De manera infija: hijo-padre-hijo.


### Lógica 1
Tablas de verdad
Conectivo|Significado|Proposición compuesta|Nombre en lógica
---|---|---|---
^|Y|P^Q|Conjunción
v|O|PvQ|Disyunción
¬|No|¬P|Negación
->|Si... entonces|P->Q|Condicional
<->|Si y sólo si|P<->Q|Bicondicional

### Lógica 2
Las similitudes entre las matemáticas y la lógica son más que evidentes. Si te centras en la lógica proposicional, como estás haciendo en el presente curso, encontrarás que está constituida por un sistema formal cuyos elementos representan proposiciones (oraciones) y cuyas constantes (conectores) lógicas representan operaciones entre las proposiciones, combinándose para formar proposiciones más complejas. Ya conoces el alfabeto de la lógica y su forma de funcionar. Conoces los operadores lógicos. También conoces la sintaxis y las tablas de verdad. Ahora tienes la preparación necesaria para aprender sobre la teoría axiomática.

Un sistema axiomático formal consta de los siguientes elementos:

Un alfabeto S para que puedas construir expresiones formales, esto incluye:
- Un conjunto de símbolos para conectivas lógicas, cuantificadores. Ya los conoces.
- Un conjunto de símbolos para designar las variables. También los conoces.
- Un conjunto de símbolos para constantes: esto dependera de cada modelo.
- Un conjunto de símbolos que serán interpretados como funciones.
- Un conjunto de símbolos que serán interpretados como relaciones.


Una gramática formal que incluirá:
- Reglas de buena formación, que reproducen la “morfología” del lenguaje formal: igual que el análisis morfológico de una frase.
- Reglas de inferencia que permitirán deducir unas proposiciones de otras, estas reglas reproducen la “sintaxis” del lenguaje formal.
- Un conjunto de axiomas inicial, o expresiones bien formadas son el punto de partida de cualquier deducción.

### Estadística
La estadística descriptiva es el estudio de los métodos de recogida y descripción de datos, así como en análisis de esta información.
- Grupo de elementos: Población
- Elementos: individuos

La estadística es la ciencia que se ocupa de la recogida y obtención de datos y de su posterior tratamiento para poder expresarlos numéricamente y así poder extraer conclusiones.

Los primeros estudios estadísticos eran demográficos así que se ha conservado gran parte del vocabulario.

1. Población: Es el conjunto sobre el que se realizará el estudio estadístico.
Individuo o Unidad Estadística: Cada uno de los elementos que componen la población.

2. Muestra: Conjunto representativo de la población pero más pequeño que esta.

3. Muestreo: Es la reunión de los datos sobre una muestra que serán el objeto de nuestro estudio estadístico.

4. Valor: Son todos los resultados que podemos obtener. En el caso de una moneda serían cara y cruz.

5. Dato: Los distintos valores que obtenemos para cada individuo. Si lanzamos la moneda al aire tres veces obtendríamos 3 datos; por ejemplo: cruz, cara, cruz.

***La estadística en ML se usa para el aprendizaje estadístico.***

#### Data mining
Esto se relaciona con los árboles de decisión y es la base de cómo se aplica la estadística a la IA.

- Moda: valor más repetido
- Mediana: valor intermedio
- Media: valor promedio
- Varianza: medida de dispersión

### Probabilidad
El Cálculo de Probabilidades nos permite calcular el grado de fiabilidad o error de las conclusiones obtenidas mediante inferencia estadística. La probabilidad mide o cuantifica la incertidumbre que tenemos sobre el resultado de un experimento aleatorio. Todo comienza con la caracterización de la Ley de Laplace:
![](https://static.platzi.com/media/user_upload/estadistica1-e623567b-36c8-4b3f-8947-3a8d67324f06.jpg)

Ten en cuenta que P(A)≥0

La probabilidad que engloba todas las probabilidades es igual a la unidad: P(E)=1
Y la probabilidad contraria es uno menos la probabilidad favorable: ![](https://static.platzi.com/media/user_upload/estadistica%202-656f9a81-a754-407f-a0cc-9aa29cb2b15d.jpg)

Probabilidad condicionada: Probabilidad de que ocurra el suceso A, condicionado
a que el suceso B haya ocurrido ya: ![](https://static.platzi.com/media/user_upload/estadistica3-cf92a3d9-1aed-47b9-b28c-cb4c301f537a.jpg)

El Teorema de Bayes nos expresa la probabilidad de que ocurra un suceso determinado, Ai , condicionado a que el suceso B ya ha ocurrido: ![](https://static.platzi.com/media/user_upload/estadistica4-87b5e2c9-ac9e-4d38-8755-18991e6b8135.jpg)

![](https://static.platzi.com/media/user_upload/estadistica5-a08f762b-b9f1-4f98-896c-2d935f31680c.jpg)
Si S es el espacio muestral asociado, una v.a. es discreta si toma un número finito o infinito numerable de valores, y se denota por X. Hallemos la función de probabilidad puntual de la v.a. X : número de caras pares al arrojar dos veces un dado equilibrado.
![](https://static.platzi.com/media/user_upload/estadistica6-738cb330-d25a-4623-aadb-e2518260f151.jpg)
![](https://static.platzi.com/media/user_upload/estadistica7-ef4430d8-5fa2-4930-8eb8-a7e263111ef3.jpg)

El valor esperado: ![](https://static.platzi.com/media/user_upload/estadistica8-752eaf95-5512-48aa-99b7-ed9395f2014c.jpg)
La varianza: ![](https://static.platzi.com/media/user_upload/estadistica9-aeebee07-8d7d-4cd3-a147-cb12c57719e3.jpg)
El valor esperado o esperanza es el número que formaliza la idea de valor medio de un fenómeno aleatorio. Cuando la variable aleatoria es discreta, la esperanza es igual a la suma de la probabilidad de cada posible suceso aleatorio multiplicado por el valor de dicho suceso.
En el caso de una distribución binomial:
P(A) = p ![](https://static.platzi.com/media/user_upload/estadistica10-d1b9c1d5-9ff3-4fb4-993b-115fbb66cd09.jpg) ![](https://static.platzi.com/media/user_upload/estadistica11-b2ef969b-1066-495b-abb1-6c2f3594a88d.jpg) ![](https://static.platzi.com/media/user_upload/estadistica12-8a0fcb46-06ea-41f3-a5b4-5750dfd13251.jpg) ![](https://static.platzi.com/media/user_upload/estadistica13-1de6c8ac-51aa-494d-bb45-7b47c942f097.jpg)

Se denomina variable aleatoria continua aquella puede tomar un número infinito de valores entre un intervalo dado, no valores discretos. Por ejemplo, la densidad de una sustancia o la altura de un árbol.
![](https://static.platzi.com/media/user_upload/estadistica14-74bb76a1-e9e3-436d-854d-81ac817bd7e3.jpg) ![](https://static.platzi.com/media/user_upload/estadistica15-f32b40a2-5799-4bc8-bfc5-d6ac8ca5697a.jpg)

Entonces:
![](https://static.platzi.com/media/user_upload/estadistica16-6082a166-0532-44fb-bfc8-f9c4300b6e68.jpg) ![](https://static.platzi.com/media/user_upload/estadistica17-274e4eff-f91b-4b6f-a1f2-9bc410e21325.jpg) ![](https://static.platzi.com/media/user_upload/estadistica18-a01f0500-0981-404c-bf81-243ef0909e22.jpg)
![](https://static.platzi.com/media/user_upload/estadistica19-9e259843-87f3-4fad-ad0c-edf242ca8557.jpg)

También puede ser uniforme:
![](https://static.platzi.com/media/user_upload/estadistica20-eed2bd87-3fe4-4f4b-ab0f-2d2be4562e52.jpg) ![](https://static.platzi.com/media/user_upload/estadistica21-d196d0b7-89f1-4d42-9352-8d175f73e8cb.jpg) ![](https://static.platzi.com/media/user_upload/estadistica22-8925a36e-c5c8-4787-b231-d2b9ca513b4f.jpg)
![](https://static.platzi.com/media/user_upload/estadistica23-1b075e47-9f0a-4fb0-8d7a-655651bd9978.jpg)

O normal:
![](https://static.platzi.com/media/user_upload/estadistica24-da15dbf0-9e10-4f97-b16a-8e7e3fa42a4b.jpg) ![](https://static.platzi.com/media/user_upload/estadistica25-5223741c-fac7-488b-932f-fb372b06cf27.jpg)
![](https://static.platzi.com/media/user_upload/estadistica26-e07d0469-8fbf-41d5-a8c9-5293aa533ae9.jpg)

Si se trata de una distribución de Poisson:
![](https://static.platzi.com/media/user_upload/estadistica27-36e3f698-bef0-4a0b-8f43-29bb1b18a4c4.jpg) ![](https://static.platzi.com/media/user_upload/estadistica28-544f0288-a40f-44a0-a8fc-611b2418eda1.jpg) ![](https://static.platzi.com/media/user_upload/estadistica29-01d3738e-9f64-4ad3-be21-7fedeea5c261.jpg)

## Algoritmos
### Clasificación
Una serie de procesos que la máquina seguirá para tomar decisiones.
La clasificación se usa en ***aprendizaje no supervisado***

La clasificación es: Predecir etiquetas de clase categóricas de un grupo de instancias nuevas a partir de observaciones pasadas.

Hay 2 tipos de clasificación:
- Binaria (2 clases), 1,0
  - Correo deseado, correo no deseado
  - Valores linealmente separables
- Multiclase (varias clases), 0,1,2,3,4,5,6,7,8,9, [az-AZ]
  - Cifras
  - Valores linealmente no separables

Tu algorito podrá clasificar, separ cuantizadamente los datos de un tipo de otro.
Algunos ejemplos de estos algoritmos de clasificación son:
- Regresión logística
- Support Vector Machines
- Árboles y bosques
- KNN

### Regresión
- Regresión logística: Algoritmo de clasificación
- Regresión lineal: Algoritmo de regresión

#### Diferencias entre Regresión Lineal y Regresión Logística

La Regresión Lineal proporciona una salida continua, pero la Regresión Logística proporciona una salida discreta. Un ejemplo de una salida continua es conocer el porcentaje de probabilidad de lluvia o el precio de una acción. Un ejemplo de una salida discreta, por su parte, es conocer si va a llover o no, o si el precio de una acción subirá o no.
![Diferencia entre regresión lineal y regresión logística](regresion%20lineal%20y%20regresion%20logistica.jpeg)

#### Tipos de Regresión Logística

1. Regresión Logística Binaria: la variable objetivo tiene solo dos resultados posible, Llueve o NO Llueve, Sube o Baja.

2. Regresión Logística Multinomial: la variable objetivo tiene tres o más categorías nominales, como predecir el tipo de vino.

3. Regresión Logística Ordinal: la variable objetivo tiene tres o más categorías ordinales, como clasificar un restaurante o un producto del 1 al 5.

### Support Vector Machines
Consiste en separar los datos en clases.

Si la manera de separar los datos es muy difícil, podemos usar la *kernelización*. Esto se refiere a que; tenemos la información desplegada en 2D, podemos pasar a 3D o incluso más dimensiones con el fin de lograr separar está información.

Para bien entender lo que hace este algoritmo de SVM:

1. Definimos nuestra dimension n, en este caso tenemos una dimension 2D, y confirmamos que nuestro dataset es linealmente separable.

2. Se tiene que hallar un hiperplano que separe nuestros datos, es decir un subespacio de dimension n-1, en este caso sera 1D, una recta, la cual debe estar lo mas alejada posible de nuestros datos, para que pase esto tenemos que indicarle: kernel=“linear”, si nuestro dataset no fuera linealmente separable tendriamos que usar otro tipo de kernel como una funcion polinomial, entre otras.

3. Esto es lo mas importante del SVM: se tienen que hallar los vectores de soporte(de ahi viene el nombre), los cuales tienen que ser paralelos al hiperplano y tienen que establecer un margen de tal forma que el hiperplano este lo mas separado posible de nuestros datos.

En caso de que nuestros datos no se puedan separar linealmente o polinomicamente, lo que tenemos que hacer es aumentar nuestra dimension en n+1(3D) y conseguir una funcion f(x,y) que clasifique bien nuestros datos. Ejemplo:
![svm](https://static.platzi.com/media/user_upload/svm-8a504101-ab7d-485e-a6bd-1e52cd7fb82c.jpg)

### Árboles 2
Árboles de decisión. Existen 2 tipos:
- Árboles de regresión
  - Estadística
  - Números
  - Media
- Árboles de clasificación
  - Minado de datos
  - Clases
  - Moda

### Aprendizaje basado en Kernels
KNN : K-nearest neighbours

¿Cómo funciona kNN?

Calcular la distancia entre el item a clasificar y el resto de items del dataset de entrenamiento.
Seleccionar los «k» elementos más cercanos (con menor distancia, según la función que se use)
Realizar una «votación de mayoría» entre los k puntos: los de una clase/etiqueta que dominen decidirán su clasificación final.

![KNN](knn.jpg)

El algoritmo KNN es uno de los algoritmos de clasificación más simples, incluso con tal simplicidad puede dar resultados altamente competitivos. Pertenece al dominio de ***aprendizaje supervisado y puede ser utilizado para el reconocimiento de patrones, extracción de datos y detección de intrusos.***

### Clustering
Este se usa en ***aprendizaje no supervisado***.

K-Means. Calcula el centroide en cada iteración.

El Clustering es una técnica de aprendizaje no supervisado (es decir sólo se dispone de los datos de entrada sin conocerse la etiqueta de salida).

El proceso consiste en agrupar un conjunto de objetos (no etiquetados) en subconjuntos de objetos llamados Clusters. Cada Cluster está formado por una colección de objetos que son similares (o se consideran similares) entre sí, pero que son distintos respecto a los objetos de otros Clusters.

##### Características del clustering
![característicasClustering](caracteristicasClustering.jpeg)

### Aprendizaje de dependencias
#### Redes bayesianas
Esto está relacionado con la probabilidad y (obviamente) con el teorema de Bayes.
La máquina tiene que interpretar cuáles son las probabilidades de que algo suceda.

#### Reglas de asociación
Esto está más apegado al tema del comercio y del marketing. Obtenemos números e información a tráves de probabilidades y de hechos.
- Soporte
- Confianza

Las reglas de asociación permiten descubrir hechos que ocurren en común dentro de un conjunto grande de datos, y con esto definir “reglas” o *patrones de interés*.

Para seleccionar una “regla” útil entre el conjunto que podamos definir, se tienen los conceptos de soporte y confianza.

El *soporte* de un conjunto de elementos, por ejemplo, (Leche y pan) tiene que ver con el número de veces que aparece este conjunto en el total de transacciones. En el ejemplo, se tiene que en el supermercado se efectuaron 5 transacciones y entre esas, en 2 las personas incluyeron al menos la leche y el pan juntos.

*Soporte (Leche, pan)* = Número de transacciones donde se compraron juntos leche y pan / total de transacciones.

La *confianza* de una regla, nos dice la probabilidad calculada a partir del conjunto de datos de que se compre la mantequilla dado que se compraron la leche y el pan, es decir, entre las transacciones que compraron leche y pan, cuantas también compraron la mantequilla.

*Confianza (regla):* Número de transacciones que contienen al menos leche, pan y mantequilla / Número de transacciones que contienen al menos leche y pan.

### Programación lógica inductiva
La PLI es una **intersección** entre Aprendizaje automático y lógica.

`PLI = Aprendizaje automático ⋂ Lógica`

Esto tiene muchísimas aplicaciones:
- Ecología
- Tecnologoía
- Biotecnología
- Procesamiento del lenguaje natural
- Coordinación de tráfico

Lo que hace la PLI es enseñarle una serie de cosas a la máquina y que esta sea capaz de inducir una ley. En el sentido de que no hay que decírselo directamente porque está en una serie de normas, en un lenguaje que se traducirá a lenguaje máquina para que la máquina saque sus propias conclusiones de manera natural.

Establecemos un **entrenamiento** con normas que la máquina tiene que entender.

**Conocimiento base**.

Con todo el entrenamiento y el conocimiento base, la máquina podrá hacer una **hipótesis inducida**.

El objetivo de la programación lógica inductiva es construir un programa lógico que, junto al conocimiento que se tenga del dominio, tenga como consecuencia lógica el conjunto de entrenamiento del sistema.

### Optimización 2
2 algoritmos:
- Algoritmo genético: es, a fin de cuentas, cómo funciona la población humana o una población animal.
  1. Generar población
  2. Calcular aptitud de individuos
  3. Seleccionar aptos
  4. Aplicar reproducción, cruce y mutación
  5. Volver al paso 2
- Ant colony: se trata de usar los caminos más cortos para recolectar la mayor cantidad de cosas. Hay que considerar todos los caminos posibles.

![algoritmoGenetico](algoritmoGenetico.jpeg)
![algoritmoDeHormigas](algoritmoDeHormigas.jpeg)

### Q-learning
Este es usado en ***aprendizaje por refuerzo***.

Q -> Quality

```python
import numpy as np
#Iniciar desde 0 los valores de la tabla q
 Q = np.zeros((state_size, action_size))

import random
#Establece el porcentaje a explorar
epsilon = 0.2

if random.uniform(0,1) < epsilon:
  """
  Explora: selecciona una acción aleatoria
  """
else:
  """
  Explota: selecciona acción de máximo valor (recompensa)
  """

Q[state, action] = Q[state, action] + lr * (reward + gama * np.max(Q[new_state,:]) - Q[state, action])
```

### Redes neuronales
Estas se usan en ***deep learning***.

'Deep' hace referencia a muchas capas interconectadas entre sí.

Las redes neuronales son grafos dirigidos.

Una neurona es una célula que está en el cerebro y teniendo muchas de estas conectadas se forma una red, que por medio de impulsos eléctricos consiguen procesar pensamientos. Esto se trata de replicar con neuronas artificiales.
- Función suma
La neurona artificial está en un entorno donde tiene una entrada de datos que serán procesados. El peso sináptico regula la cantidad de información que entra a la neurona.

- Función de activación
Lo que hace es reunir toda la información y prepararla para la salida.

Ejemplo de una red neuronal profunda:
![ejemploDeepLearning](deep-learning-proceso.png)