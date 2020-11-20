## Programación dinámica = Matemáticas
- Subestructura óptima. Una solución global óptima se puede encontrar al combinar soluciones óptimas de subproblemas locales.

- Problemas empalmados. Una solución óptima que involucra resolver el mismo problema en varias ocasiones.

## Memoization
- La *Memorización* es una técnica para guardar cómputos previos y evitar realizarlos nuevamente.

- Normalmente se utiliza un diccionario, donde las consultas se pueden hacer en O(1).

- Intercambia tiempo por espacio.

## Optimización de Fibonacci con diccionario.
¿Por que usar diccionario y no listas?

El algoritmo que usa Python internamente para buscar un elemento en un diccionario es muy distinto que el que utiliza para buscar en listas.

Para buscar en las listas, se utiliza un algoritmos de comparación que tarda cada vez más a medida que la lista se hace más larga. En cambio, para buscar en diccionarios se utiliza un algoritmo llamado hash, que se basa en realizar un cálculo numérico sobre la clave del elemento, y tiene una propiedad muy interesante: sin importar cuántos elementos tenga el diccionario, el tiempo de búsqueda es siempre aproximadamente igual (O(1)).

Este algoritmo de hash es también la razón por la cual las claves de los diccionarios deben ser inmutables, ya que la operación hecha sobre las claves debe dar siempre el mismo resultado, y si se utilizara una variable mutable esto no sería posible.

## Programas deterministas:
Al mismo input, tenemos el mismo output.

## Programación estocástica
- Un programa es determinístico si cuando se corre con el mismo *input* produce el mismo *output*.

- Los programas determinísticos son muy importantes, pero existen problemas que no pueden resolverse de esa manera.

- La programación estocástica permite introducir aleatoriedad a nuestros programas para crear simulaciones que permiten resolver otro tipo de problemas.

- Los programas estocásticos se aprovechan de que las distribuciones probabilísticas de un problema se conocen o pueden ser estimadas.

*Ejemplos:*
- Determinista:
    Escribir palabras de un mensaje en el celular manualmente.
- Estocastica:
    Usar el autocorrector para predecir las palabras, segun al historial de palabras que usamos habitualmente y predecir cual sera la siguente palabra en el texto.

- Determinista:
    Un programa de ventas de tickets, donde las entradas que de el usuario, deben dar salidas preestablecidas

- Estocástico:
    Un programa de simulación de divisas para trading, utilizando datos históricos para tomar decisiones según probabilidad de escenarios.

## Probabilidades
- La probabilidad es una medida de la certidumbre asociada a un evento o suceso futuro y suele expresarse como un número entre 0 y 1.

- La probadilidad de 0 significa que un suceso jamás sucederá.

- La probailidad de 1 significa que un suceso está garantizado de suceder en el futuro.

- Al hablar de probabilidad preguntamos qué fracción de todos los posibles eventos tiene la propiedad que buscamos.

- Por eso es importante poder calcular todas las posibilidades de un evento para entender su probabilidad.

- La probabilidad de que un evento suceda y de que no suceda es siempre 1. Osea `P(A) + P(~A) = 1`
    - Ley del complemento

- `P(A y B) = P(A) * P(B)`
    - Ley multiplicativa (sólo si ambos eventos son independientes)

- `P(A o B) = P(A) + P(B)` (mutuamente exclusivos)
- `P(A o B) = P(A) + P(B) - P(A y B)`(no exclusivos)
    - Ley aditiva

## Inferencia estadística
- Con las simulaciones podemos calcular las probabilidades de eventos complejos sabiendo las probabilidades de eventos simples.

- ¿Qué pasa cuando no sabemos las probabilidades de los eventos simples?

- Las técnicas de la Inferencia Estadística nos permiten inferir/concluir las propiedades de una población a partir de una muestra aleatoria.

"El principio guía de la Inferencia Estadística es que una muestra aleatoria tiende a exhibir las mismas propiedades que la población de la cual fue extraída." - *John Guttang*

Es decir, podemos extraer a muestras de una población para obtener datos e inferir los resultados de la población.
¡Es importate que esto sea *aleatorio*! No podemos seleccionar datos en específico porque vamos a tener resultados *sesgados*.

## Ley de los grandes números
- En pruebas independientes repetidas con la misma probabilidad p de un resultado, la fracción de desviaciones de p converge a cero conforme la cantidad de pruebas se acerca al infinito.

`P(lim de n cuando tiene a infinito por X testadada(media) sub n = μ) = 1`

## Falacia del apostador
- La falacia del apostador señala que después de un evento extremo, ocurrirán eventos menos extremos para nivelar la media.

- La regresión a la media señala que después de un evento aleatorio extremo, el siguiente evento probablemente será menos extremo.

## Media o Promedio
- Es una medida de tendencia central.
- Comúnmente es conocida como el promedio
- La media de una población se denota con el símbolo μ. La media de una muestra se denota con Χ testada.

Suma de de valores, dividida entre la cantidad de valores.

## Varianza
- La varianza mide qué tan propagados se encuentran un conjunto de valores aleatorios de su media.
- Mientras que la media nos da una idea de dónde se encuentran los valores, la varianza nos dice qué tan dispersos se encuentran.
- La varianza ***siempre*** debe entenderse con respecto a la media, si no, no tiene sentido.

## Desviación estándar
- La desviación estándar es la raíz cuadrada de la varianza.
- Nos permite entender, también, la progagación y se debe entender siempre relacionado a la media.
- La ventaja sobre la varianza es que la desviación estándar está en las mismas unidades que la media.

## Distribución normal
- Es una de las distribuciones más recurrentes en cualquier ámbito.
- Se define completamente por su media y su desviación estándar.
- Permite calcular intervalos de confianza con la regla empírica.

## Regla empírica
- También conocida como la regla 68-95-99.7
- Señala cuál es la disperción de los datos en una distribución normal a uno, dos y tres sigmas.
- Permite calcular probabilidades con la densidad de la distribución normal.
`Pr(µ-1σ ≤ X ≤ µ + 1σ) ≈ 0.6827`
`Pr(µ-2σ ≤ X ≤ µ + 2σ) ≈ 0.9545`
`Pr(µ-3σ ≤ X ≤ µ + 3σ) ≈ 0.9973`

## Simulaciones de Montecarlo
- Permite crear simulaciones para predecir el resultado de un problema.
- Permite convertir problemas determinísticos en problemas estocásticos.
- Es utilizado en una gran diversidad de áreas, desde la ingeniería hasta la biología y el derecho.

## Muestreo
- Hay ocasiones en la que no tenemos acceso a toda la población que queremos explorar.
- Uno de los grandes descubrimientos de la estadística es que las muestras aleatorias tienden a mostrar las mismas propiedades de la población objetivo.
- El tipo de muestreo que hemos hecho hasta ahora es muestro probabilístco.
- En un muestreo aleatorio cualquier miembro de la población tiene la misma probabilidad de ser escogido.
- En un muestreo estratificado tomamos en consideración las características de la población para partirla en subgrupos y luego tomamos muestras de cada subgrupo.
    - Incrementa la probabilidad de que el muestreo sea representativo de la población.

## Teorema del límite central
- Es uno de los teoremas más importantes de la estadística
- Establece que muestras aleatorias de cualquier distribución van a tener una distribución normal
- Permite entender cualquier distribución como la distribución normal de sus medias y eso nos permite aplicar todo lo que sabemos de distribuciones normales
- Mientras más muestras obtengamos, mayor será la similitud con la distribución normal
- Mientras la muestra sea de mayor tamaño, la desviación estándar será menor

## Datos experimentales
- Es la aplicación del método científico
- Es necesario comenzar con una hipótesis sobre el resultado al que se quiere llegar
- Basado en la hipótesis se debe crear un experimento para validar o falsear la hipótesis
- Se valida o falsea una hipótesis midiendo la diferencia entre las mediciones experimentales y aquellas mediciones predichas por la hipótesis

## Regresión lineal
- Permite aproximar una función a un conjunto de datos obtenidos de manera experimental
- No necesariamente permite aproximar funciones lineales, sino que sus variantes permiten aproximar cualquier función polinómica

## Conclusiones
- La programación dinámica permite optimizar problemas que tienen subestructura óptima y subproblemas empalmados
- Las computadoras pueden resolver problemas determinísticos y estocásticos
- Podemos generar simulaciones computacionales para responder preguntas del mundo real
- La inferencia estadística nos permite tener confianza de que nuestras simulaciones arrojan resultados válidos