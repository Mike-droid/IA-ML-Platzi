# Álgebra lineal
## Sistemas de ecuaciones
Un sistema lineal es una ecuación con:
- Coeficientes
- Incógnitas
- Constante
a1x1 + a2x2 + ... anxn = b
Si b = 0 el sistema es homogeneo. Un conjunto de estas ecuaciones formarán un sistema lineal.
Podemos representar el sistema de ecuaciones en una matriz con sus coeficientes.

## Soluciones
### Método de eliminación
Se trata de eliminar una de las variables del sistema.
- Por ejemplo sumando dos ecuaciones para tener una tercera ecuación.
- También podemos multiplicar ecuaciones para tener una nueva ecuación.
- Por último, podemos intercambiar ecuaciones para hacer la cosa más sencilla.
Estos 3 métodos son usados para al final dejar una variable sola y despejarla para obtener su valor.

### Método de Gauss
- Eliminación -> Aquí podemos tomar una ecuación E1, sumarla con un escalar de una ecuación E2 y volver a tener E1.
- Escalamiento -> Multiplicar una ecuación E1 por un escalar y tener una nueva E1.
- Intercambio -> Intercambiar una ecuación E1 por una ecuación E2.

Tendremos una matriz aumentada con los coeficientes del sistema de ecuaciones y deberemos lograr tener coeficientes de 0 debajo de la diagonal principal, haciendo uso de las opereaciones mencionadas arriba.
Se recomienda hacer esto por columnas.
Este método se soluciona de manera ascendente una vez que llegamos a obtenere el valor de una variable.

### Método de Gauss Jordan
- Eliminación -> E1 + cE2 => E1
- Escalamiento -> cE1 => E1
- Intercambio -> E2 => E3
En este método buscamos que tanto los coeficientes por arriba y por debajo de la diagonal principal sean ceros, además de que los coeficientes de la diagonal principal sean todos 1.
Proceso recomendado:    |100| Conseguir el 1 aquí
                        |010| Conseguir 0 a la izquierda y después el 1
                        |001| Conseguir 0 0 y después el 1


## Vectores
Es un ente matemático que tiene magnitud y sentido (o también llamada dirección).
A=|4| Vector de 2 dimensiones
  |3|

V=|2| Vector de 3 dimensiones
  |1|
  |3|

W=|4 | Vector de 4 dimensiones
  |2 |
  |-1|
  |-4|

Podemos pasar de cooredenadas cartesianas a coordenadas polares.

### Vector de valor unitario
En 2 dimensiones encontraremos i,j.
En 3 dimensiones encontraremos i,j,k.
A=|4|
  |3|

A = 4i,3j
A = (4,36.8°) => Representación polar
A = (5, 36.8/180 * π) => Representación en radianes

### Suma de vectores
U=|3|
  |1|

V=|4|
  |2|

U + V = |7|
        |3|

### Resta de vectores
U=|3|
  |1|

V=|4|
  |2|

U - V = |-1|
        |-1|

### Multiplicación de vector por escalar
2 * |3| = |6|
    |2|   |4|

### Producto punto
|a1| * |b1| = (a1b1 + a2b2)
|a2|   |b2|

|a1| * |b1| = (a1b1 + a2b2 + a3b3)
|a2|   |b2|
|a3|   |b3|

vector A * vector B = |a||b|cos(θ) [No es valor absoluto, es la suma de los componentes, cada uno al cuadrado y al final sacamos raíz cuadrada de la suma].

Si:
- vector A * vector B > 0, el ángulo será agudo, menor a 90°
- vector A * vector B < 0, el ángulo será obtuso, mayor a 90°
- vector A * vector B = 0, el ángulo será recto 90°

### Producto cruz
vector A X vector B != vector B X vector A

### Ecuación de un plano
Los vectores normales son aquellos que forman un ángulo de 90 grados respecto a la superficie.

## Matrices
Es una representación de datos. W = m x n (m son filas y n son columnas).
- Matriz renglón: 1 fila x n
- Matriz columna: m x 1 columna
- Matriz cuadrada: m = n
- Matriz rectangular: m != n
- Matriz transpuesta: |2   5 -1| => |2  -1|
                      |-1 -7 -3|    |-5 -7|
                                    |-1 -3|
- Matriz simétrica: los números fuera de la diagonal principal son iguales => |2  *-4* *-5*|
                                                                              |*-4* -7 *-3*|
                                                                              |*-5* *-3* 10|
- Matriz diagonal: Los elementos fuera de la diagonal principal son todos 0.
- Matriz identidad: Los elementos fuera de la diagonal principal son todos 0 y en la diagonal principal todos son 1.
- Matriz triagular superior: Todos los elementos debajo de la digonal principal, son 0.
- Matriz triagular inferior: Todos los elementos arriba de la digonal principal, son 0.

### Suma y multiplicación de matrices
Es requisito que ambas matrices sean del mismo tamaño.
-Para sumar las matrices sumaremos componente por componente
-La multiplicación de una escalar por una matriz, la realizaremos multiplicando el escalar por cada uno de los componentes de la matriz
-La suma de matrices y multiplicación por escalar la podemos utilizar para resolver ecuaciones como por ejemplo : 2x - 4B = 3A, siendo A y B matrices, aislaremos la (x) y resolveremos las operaciones de las matrices

### Multiplicación matricial
Para poder efectuar esta operación, es requisito que el número de columnas de la primera matriz sea igual al número de filas de la segunda matriz.
Entonces: 3X3 * 3x2 => Sí se puede
El resultado será una matriz de 3 filas y 2 columnas, número de filas de la primera matriz y número de columnas de la segunda matriz.
Se recomienda enumerar las filas de la primera matriz y las columnas de la segunda matriz.
A = mxn, B = mxn, entonces AB = AmBn

### Matriz inversa
Se denota por A^(-1)
Sirve para que se cumpla esto: A*A^(-1) = Matriz identidad
¿Cómo hayar la matriz inversa?
- Gauss-Jordan
- A^(-1) = (1/|A|)Adj(A^t) => 1 dividido por el determinante y esto multiplicado por la adjunta de la transpuesta.

## Factorización LU (Lower, Upper)
Ax = b
A = LU
LUx = b
Ux = y
Ly = b
Suma de múltiplos con otras filas
*NO* multiplicación por escalar o renglón

## Transformaciones lineales
La transformación lineal consiste en que tenemos un conjunto de vectores y al aplicarles una función obtenemos otro conjunto de vectores, lo que se le denomina como transformación “T”

Tendremos nuestro vectores en el espacio “V” y le aplicaremos una transformación “T” que nos dará como resultado su imagen en el espacio “W” = T : V -> W

El conjunto inicial del que partimos es el “dominio” y el conjunto en que se convierte sera el “contradominio”, se puede pasara de un vector en R3 a R2

Habrán algunos puntos para los que la función no sea válida, pero para los puntos que la función si sea válida lo llamaremos el contradominio de la función

También puede ocurrir que dos vectores del espacio “V” den la misma imagen en el espacio “W”

### Reflexiones
Las reflexiones son transformaciones lineales de un punto de un a espacio R2 a un espacio R2, para obtener esta reflexiones multiplicamos los puntos por su matriz de transfomación.

Reflexión en el eje Y : P(x,y) = Ry(-x,y)

Reflexión en el eje X : P(x,y) = Rx(x,-y)

Reflexión de la diagonal : P(x,y) = Rd(x,y)

Reflexión respecto al origen : P(x,y) = Ro(-x,-y)

### Compresiones y expansiones
Las comprensiones y expansiones consisten en comprimir o expandir planos a lo largo de los ejes de coordenadas a trabes de la matriz de transformación de cada eje

Podemos obtener una expansión en el eje X o en el eje Y, también podemos obtener una expansión en ambos ejes a la vez

Para hacer la matriz de transformación del eje X, lo que hacemos es multiplicar el eje X por un valor escalar, tenemos nuestro punto (x,y) y al aplicar la matriz de transformación obtenemos el punto (cx,y), donde “c” representa el escalar por le que multiplicamos al eje X

De la misma manera hacemos lo mismo en el eje Y, le aplicamos la matriz de transformación al punto (x,y) y obtendremos el punto (x,dy), esto nos dará una expansión únicamente en el eje Y

Siempre que c/d > 0 obtendremos una expansión

Siempre que c/d < 0 obtendremos una compresión

### Cortes o desplazamientos
Con las transformaciones lineales podemos utilizar una sola gráfica y obtener una serie de imágenes a trabes de las matrices de transformación de caja eje (X,Y), que alteraran la imagen principal obteniendo cortes o desplazamientos en la imagen.

### Rotaciones
Para obtener una rotación de nuestra figura en el plano cartesiano, utilizaremos la matriz de transformación lineal con los ángulos theta de los vectores.

Multiplicaremos esta matriz por los puntos de coordenadas de nuestra figura, solo necesitaremos sustituir el angulo de rotación que queremos aplicar en la matriz de transformación lineal y realizar la multiplicación.

## Determinantes
Los determinantes son muy importantes, porque si el determinante de una matriz es cero, signifca que la matriz no tiene solución
Resolver las matrices a partir de determinantes solo es posible para las matrices cuadradas
El diagrama de Sarrus es un método de determinantes para resolver la matriz:
1. Para el caso de una matriz 3x3 le añadiremos otra vez su 1r y 2n columna
2. Después multiplicaremos la diagonales que van hacia abajo y las sumaremos
3. multiplicaremos las diagonales que van hacia arriba y las restaremos
4. Restaremos el resultado de la segunda multiplicación al de la primera multiplicación de las diagonales

### Determinantes por cofactores
Para resolver los determinantes de una matriz 3x3 a trabes del método de Cofactores
1. Creamos una matriz donde alternamos entre signos positivos (+) y negativos (-) de cada componente de la matriz principal.
2. Para cada componente de la matriz principal hallaremos su matriz 2x2 eliminado la fila y la columna del componente seleccionado.
3. Obtendremos una matriz 3x3 pero que estará compuesta por matrices de 2x2 de cada componente.
4. Para resolver solo hará falta seleccionar una fila o columna y seleccionar los componente de esa fila, cambiarle el signo por el que le corresponda y multiplicarlo por el determinante de la matriz 2X2 que se encuentre en la posición del componente seleccionado.

### Geometría y propiedades del determinante
Cuando a una figura en el plano le aplicamos una matriz de transformación, obtendremos un corte, desplazamiento, rotación, expansión… y el área de la nueva figura que obtenemos de la transformación será igual al determinante de la matriz de transformación.