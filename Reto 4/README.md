# Descripción del Reto

Tu cliente, Corporación Umbrella, está preparando todo lo necesario para comenzar distribución de la vacuna contra el Covid-19.

Para dar inicio a la distribución, ya se inició el proceso de contratación del personal encargado de manejar los camiones que llevarán las vacunas a diferentes regiones del país (porque tú ya solucionaste el Reto de la semana 3).

Ahora, uno de los clientes de Transportes del Norte es Corporación Umbrella, una empresa de vacunas que requiere mantener un control estricto sobre los tiempos de despacho de sus vacunas en sus 10 puntos de distribución.

Además del control de inventario, Transportes del Norte desea brindarle a Corporación Umbrella la posibilidad de llevar el control de tiempos de despacho que realiza en cada punto de distribución asignado, para garantizar las exigencias del Departamento de Logística de Corporación Umbrella.

Por su parte, Corporación Umbrella ha definido las siguientes **restricciones, prioritariamente**: 

1.	Un tiempo máximo de 15 minutos para la permanencia de cada camión en cada punto de distribución.
2.	Una cantidad mínima ideal/sugerida de 10 cajas de vacunas a despachar en cada punto de distribución.

Teniendo en cuenta que cada camión sale cargado con 100 cajas del centro de despacho de Corporación Umbrella, desarrolla un programa que:

*	Registre el conteo de cajas de vacunas, una a una, a medida que son extraídas del camión en cada punto de despacho.
*	Lleve un conteo del inventario existente en el contenedor del camión. 
*	Emita una alarma si se excede el tiempo de despacho estipulado o si se entregan más productos de los especificados, por punto de despacho. 
*	Genere un reporte al final de cada despacho, indicando el número de cajas entregadas y el tiempo de despacho, por cada uno de los 10 puntos de distribución. 
*	En caso de que se entreguen más cajas de las estipuladas para cada punto de distribución, se debe notificar que “Se ha agotado el inventario” indicando el número del último punto de distribución que recibió la última caja.

### Ejemplo: 
*(los puntos suspensivos . . . indican que la lógica de la solución continua similarmente al proceso descrito, además, la entrega se repite para cada punto de distribución hasta que alcance el inventario en el camión):*

Los parámetros de entrada que recibe la función  **control_camion** son tiempo_entrega y cantidad_cajas, quedando de esta forma: **control_camion**(tiempo_entrega, cantidad_cajas). 

En caso de que el tiempo ingresado sea mayor que el límite establecido, es decir que no se cumpla la restricción número 1, por ejemplo 20 minutos, es decir: **control_camion**(20, 5) o **control_camion**(20, 10) o **control_camion**(20, 15), en cualquiera de tales tres posibles escenarios (independiente del número de cajas de vacunas), como el tiempo de entrega (20) es mayor al tiempo máximo de entrega que son 15 minutos, se debe imprimir este mensaje: 

“Se excede el límite de tiempo”

Para el caso en que no se cumpla con la restricción número 2, por ejemplo **control_camion**(15,5), entonces se debe imprimir en pantalla lo siguiente:

“La cantidad de cajas de vacunas a despachar en cada punto de distribución es inferior a la mínima ideal/sugerida (10)”

Para el caso normal (donde se cumple con las dos restricciones sin excepciones) que se utilice, por ejemplo **control_camion**(10, 10), la salida esperada es la siguiente:

Punto de distribución # 1

Caja # 1

Caja # 2

Caja # 3

Caja # 4

Caja # 5

Caja # 6

Caja # 7

Caja # 8

Caja # 9

Caja # 10

El total de cajas en inventario en el camión = 90

Cantidad de cajas despachadas = 10

Tiempo de despacho = 10


Punto de distribución # 2 

Caja # 1

. . .

Caja # 10

. . .

Punto de distribución # 10

Caja # 1

. . .

Caja # 10

El total de cajas en inventario en el camión = 0

Cantidad de cajas despachadas = 100

Tiempo de despacho = 10

En caso de que la cantidad de cajas a entregar supere el valor de 10 *(se cumple con las dos restricciones pero con excepciones ya que un escenario posible, donde se abastecerán los primeros puntos de distribución con una cantidad superior a 10 cajas de vacunas, quedando probablemente los últimos puntos de distribución sin abastecer, y uno en particular con una excepción a la restricción número 2 porque la cantidad de cajas será inevitablemente inferior a 10, con el fin de cumplir con el objetivo de entregar el inventario de 100 cajas completamente)*, por ejemplo: **control_camion**(10, 13), la salida esperada es la siguiente:

Punto de distribución # 1

Caja # 1

. . .

Caja # 10

Encender alarma


Caja # 11

Encender alarma

Caja # 12

Encender alarma

Caja # 13

El total de cajas en inventario en el camión = 87

Cantidad de cajas despachadas = 13

Tiempo de despacho = 10

Punto de distribución # 2 

. . .

Punto de distribución # 8

Caja # 1

. . .

Caja # 9

Se ha agotado el inventario en el camión

El total de cajas en inventario en el camión = 0

Cantidad de cajas despachadas = 9

Tiempo de despacho = 10