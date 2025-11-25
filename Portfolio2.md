Arrays:
Los arrays son una estrucutura estatica con un mismo tipo de variable (int, float, var....).

Listas:
Similares a los Arrays, pero con la diferencia que pueden contener más de un tipo de variable. 

Estas dos estrucuturas de datos son de tipo obejto, alamcenando un conjunto de datos, el índice de estos va en 
el orden de los números naturales, empezando desde el 0 y van ordenados en el orden de inserción.
Eso sí en Python no existe diferenciación de los Arrays y Listas, a diferencia de lenguajes como Java o C#.
Estos se pueden leer mediante índice con un bucle for usando rango o while, pero también se puede usar una
variante del for llamada for-each, está vairante no itera los elementos del Array.

No nos olvidemos de los elementos basicos de los Arrays en Python, como:
1. len(): para leer el array.
2. insert(): inserta una nueva variable
y un largo etc...

Tras eso tenemos dos tipos de busquedas llamadas: secuencial y binaria.
Definidas como:
Búsqueda secuencial → aplica a arrays desordenados
Búsqueda binaria → aplica a arrays ordenados (para este usaremos el metodo .sort() ordenando el Array inicial).
Eso si la comparación de Arrays en Python es con == mientras que en Java se haría con .equals()
La copia de Arrays se puede realizar de cualquier manera, la más común es con .copy(), también se hace con un slicing nnn[:] y maualmente.

Los arrays pueden tener vairas dimensiones, la que se va a ver es la mátriz siendo un array de dos dimensiones, al igual que el unidimensional
se recorre usando los números naturales.
Ej: matriz[0][1]

Ahora con la cadenas, secuencia inmutable de caracteres (letras, números, símbolos), esta sirve para almacenar texto.
Se pueden definir usando la comilla normal '' y las comillas dobles "".
Recordemos que las cadenas son secuencias, lo que significa que podemos acceder a sus elementos por posición.
Mediante el slicing podemos extraer un fragmento de la cadena siendo el formato: cadena[inicio:fin:paso].
Los métodos son funciones específicas que se aplican directamente a un objeto string, como: .lower(), .upper()....
Con f"" podemos dar formato a las cadenas y sí queremos que salga un resultado del código podremos {}.
Y por último tenemos la expresiones regulares, son universales y se encuentran en los patrones de busquedas,
en Python se importa y usando import re, las expresiones que se usan va desde ., \d, \w, \ s (y sus versiones en mayúsculas que son lo opuesto)
y los cuantificadores +, *, {n}....
También es valido expresiones como r'^[A-Z] [0-9] \w{5,20}$'.






