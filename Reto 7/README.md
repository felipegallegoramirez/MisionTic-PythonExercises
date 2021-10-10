# Descripción del Reto

El Departamento de Logística de Corporación Umbrella ha quedado muy contento con tus
desarrollos anteriores, puesto que ahora puede administrar los despachos de las vacunas
con mayor eficiencia. Por lo tanto a decidido administrar los envíos de las vacunas
mediante 2 empresas de transporte: Transportes del Norte y Transportes Monky, con sus
respectivos camiones.

**Llegó la hora de implementar! **

Corporación Umbrella te ha contactado para desarrollar una interfaz para su Departamento de Logística. Es esta unidad de negocio la encargada de toda la interacción con las empresas transportadoras. Es aquí donde se registran y se dan de baja clientes, se asignan camiones, se programan sus despachos periódicamente, y se llevan indicadores de desempeño.

Tu desarrollo trabajará a partir de dos archivos (proporcionados para este reto) de una
base de datos que son el insumo para poder calcular los parámetros de desempeño. Por
tanto, debe:

Leer desde el archivo “Valores_Asignados.csv” los siguientes campos, correspondientes a
la programación asignada:

        a. Nombre de la empresa transportadora: Empresa_transp
        b. Punto de Distribución: Punto_dist
        c. ID del Camión: Id_camion
        d. Cajas a entregar: cajas_entrega
        e. Tiempo de despacho (minutos): Tiempo_despacho

Leer desde el archivo “Valores_Registrados.csv” los siguientes campos, correspondientes a
la programación regitrada:

        a. Nombre de la empresa transportadora: Empresa_transp
        b. Punto de Distribución: Punto_dist
        c. ID del Camión: Id_camion
        d. Cajas a entregar: cajas_entrega
        e. Tiempo de despacho (minutos): Tiempo_despacho


Debes desarrollar una interfaz de consola que permita mostrar los indicadores de
desempeño de cada camión correspondiente a la empresa transportadora, permitiendo:

1. Seleccionar la empresa transportadora: Transporte_Norte ó Transporte_Monky.
2. Seleccionar el camión al que se le calcularán los indicadores de desempeño.
3. Desplegar los siguientes indicadores de desempeño para la empresa transportadora y camión seleccionado:
  

    •	Eficiencia en tiempos de despacho (%) = 100 * (Tiempo total de despacho asignado - Tiempo total de despacho registrado) / Tiempo de total despacho asignado 

    •	Tasa de entrega (cajas/min) = Cantidad total de cajas despachadas / Tiempo total de despacho

    •	Nivel de cumplimiento de los despachos (%) = 100 * (Total de cajas despachadas / Total de cajas asignadas) 

    •	Porcentaje de entregas a tiempo = No. de entregas a tiempo / No. Total de entregas realizadas



**Ejemplo:**

  En la parte principal (main.py) del programa, el usuario debe ingresar el nombre de la empresa transportadora y el id del camión, del cual se van a obtener los indicadores de desempeño por comparación entre los datos registrados en los archivos (Asignados vs Registrados):

              empresa_transp = input()
              id_camion = input()  

  En la parte del programa que se encarga del control (control.py), está la función de control la cual tiene 2 parámetros, así:

            def control(empresa_transp, id_camion)
                          
Dentro del cuerpo de la función se debe leer el archivo 'Valores_Asignados.csv' y el archivo 'Valores_Registrados.csv', y dependiendo de la empresa transportadora y del camión que haya elegido el usuario, se procede a realizar los cálculos correspondientes, mostrando lo que aparece en el siguiente literal.

La estructura de salida esperada para el caso donde se escoge el cliente Transporte_Norte y el Id del camión 2, es la siguiente:

    Eficiencia en tiempos de despacho = -11.8 %
    Tasa de entrega = 25.6 cajas/min
    Nivel de cumplimiento = 90.0 %
    Entregas a tiempo = 33.3 %



**Recomendaciones:**
- El ingreso de las planillas será mediante el empleo de archivos
- Mantener el formato de la "salida esperada" (orden, palabras y signos). Para ello se recomienda copiar y pegar del ejemplo
- Redondear los números reales a 1 dígito decimal