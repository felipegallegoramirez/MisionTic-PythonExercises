# Descripción del Reto

El Departamento de Logística de Corporación Umbrella ha quedado muy contento con tu desarrollo anterior, puesto que ahora puede administrar los despachos de las vacunas con mayor eficiencia, además de la implementación del sistema de planillas para llevar un mejor control y la gestión de la capacidad de sus camiones en el orden de 1000 a 1500 cajas.

**Llegó la hora de implementar! **

Transportes del Norte te ha contactado para desarrollar una interfaz para su Departamento de Logística. Es esta unidad de negocio la encargada de toda la interacción con los clientes de Transporte del Norte. Es aquí donde se registran y se dan de baja clientes, se asignan camiones a cada cliente, se programan sus despachos periódicamente, y se llevan indicadores de desempeño, tanto para Transportes del Norte, como para cada uno de sus clientes.

Como sabes, el nuevo desarrollo está orientado a operadores del Departamento de Logística de Transportes del Norte. Tu desarrollo trabajará a partir de dos archivos (proporcionados para este reto) de una base de datos que son el insumo para poder calcular los parámetros de desempeño. Por tanto, debe:

1.	Leer desde el archivo “ValoresAsignados.csv” los siguientes campos, correspondientes a la programación asignada por Transportes del Norte:

        a.	PuntoDistribución

        b.	CargaEntregada_cajas

        c.	TiempoDespacho_minutos

2.	Leer desde el archivo “ValoresRegistrados.csv” los siguientes campos, correspondientes a la operación registrada por los conductores de Transportes del Norte:

        a.	PuntoDistribución

        b.	CargaEntregada_cajas

        c.	TiempoDespacho_minutos

Debes desarrollar una interfaz de consola que permita mostrar los indicadores de desempeño de cada vehículo, para cada cliente, permitiendo:

  I.	Seleccionar el punto de distribución al que se le calcularán los indicadores de desempeño

  II.	Desplegar los siguientes indicadores de desempeño para cualquier punto de distribución (LAS 3 PRUEBAS AUTOMÁTICAS EN REPLIT SE APLICAN SOLO AQUÍ):
  
    •	Eficiencia en tiempos de despacho (%) = 100 * (Tiempo total de despacho asignado - Tiempo total de despacho registrado) / Tiempo de total despacho asignado 

    •	Tasa de entrega (cajas/min) = Cantidad total de cajas despachadas / Tiempo total de despacho

    •	Nivel de cumplimiento de los despachos (%) = 100 * (Total de cajas despachadas / Total de cajas asignadas) 

    •	Entregas a tiempo (%) = 100 * (No. de entregas a tiempo / No. Total de entregas realizadas).  Nota: este es un resultado que es constante, es decir, es independiente del punto de distribución porque toma en cuenta todos los puntos de distribución.

  III.	ESTO ES UN COMPLEMENTO SIN PRUEBA AUTOMÁTICA: Registrar (escribir) en un archivo CSV *(llamado **'registro_estadisticas.csv'** que debe quedar guardado como los demás archivos que se muestran en Replit)* un informe con los indicadores de desempeño anteriores (todos excepto el último), para cada punto de distribución, que recopile finalmente TODOS los 30 registros, y luzca como sigue (como ejemplo se muestran los datos del punto de distribución 5, 15 y 25):

    PuntoDistribucion,EficienciaTiemposDespacho_%,TasaEntrega_cajas/min, NivelCumplimientoDespachos_%
    …
    5,7.3, 22.3, 83.3
    …
    15,-6.4,25.3,91.9
    …
    25,12.0,31.0,92.6
    …

  IV.	ESTO ES OTRO  COMPLEMENTO SIN PRUEBA AUTOMÁTICA: Realizar 6 gráficas *(nombrarlas como: **'grafica1.png','grafica2.png',...,'grafica6.png'**, y deben quedar guardadas como los demás archivos que se muestran en Replit)* usando **matplotlib**: 3 con los datos del archivo 'ValoresAsignados.csv', y 3 con los datos del archivo 'Valores Registrados.csv' , así:

    i.	Carga_cajas(EjeY) vs PuntoDistribucion(EjeX)

    ii.	Tiempo_minutos(EjeY) vs PuntoDistribucion(EjeX)
    
    iii.	Única gráfica que muestre i y ii 

**Ejemplo (para verificar las 3 pruebas automáticas en Replit):**

    1. En la parte principal (main.py) del programa, el usuario debe ingresar el punto de distribución, del cual se van a obtener los indicadores de desempeño por comparación entre los datos registrados en los archivos (Asignados vs Registrados):

              punto_distribucion = input()  

    2. En la parte del programa que se encarga del control (control.py), está la función de control la cual tiene un parámetro, así:

            def control(punto_distribucion)
                          
Dentro del cuerpo de la función se debe leer el archivo 'ValoresAsignados.csv' y el archivo 'Valores Registrados.csv', y dependiendo del punto de distribución que haya elegido el usuario, se procede a realizar los cálculos correspondientes, mostrando lo que aparece en el siguiente literal (3).

    3. La estructura de salida esperada para el caso donde se escoge el punto de distribución 5, es la siguiente:

    Eficiencia en tiempos de despacho = 7.3 %
    Tasa de entrega = 22.3 cajas/min
    Nivel de cumplimiento de los despachos = 83.3 %
    Entregas a tiempo = 50.0 %

*Sugerencia: como el programa debe funcionar para cualquier punto de distribución escogido por el usuario, entonces probar específicamente con los puntos 15 y 25 que se evaluarán en las pruebas automáticas.*



**Recomendaciones:**
- El ingreso de las planillas será mediante el empleo de archivos
- Mantener el formato de la "salida esperada" (orden, palabras y signos). Para ello se recomienda copiar y pegar del ejemplo
- Redondear los números reales a 1 dígito decimal