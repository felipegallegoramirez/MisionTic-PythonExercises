## Distribución de vacunas - Corporación Umbrella

Tu cliente, Corporación Umbrella, está preparando todo lo necesario para comenzar distribución de la vacuna contra el Covid-19.

Para dar inicio a la distribución, se desea comenzar el proceso de contratación del personal encargado de manejar los camiones que llevarán las vacunas a diferentes regiones del país. Con lo cual se le pide ingresar la siguiente información a los aspirantes al cargo, para poder registrarlos a la base de datos de la Corporación:

    1. [nombre] Primer nombre.
    2. [ident] Número de identificación (Sin puntos, ni comas).
    3. [correo] Correo electrónico.
    4. [sobrenombre] Sobrenombre elegido.
    5. [clave] Clave de acceso.
    6. [tiempo] Ingrese el tiempo total de experiencia en meses. Si no ha tenido experiencia se debe colocar cero (Valor numérico).
    7. [tratamiento] Está siguiendo algún tratamiento médico en estos momentos?: [Si, No]
    8. [conocimiento] Tiene conocimientos de mecánica de camiones?: [Si, No]

Para asegurar un registro exitoso a la plataforma se deben cumplir ciertos criterios:

* El nombre debe ser de tipo cadena.
* El número de identificación debe estar en el rango: [10’000.000 – 100’000.000].
* El correo electrónico debe tener el caracter  ‘@’ no más de una vez.
* El sobrenombre no debe iniciar con un valor numérico y no debe contener más de 3 veces la letra ‘a’.
* La clave de acceso debe tener al menos uno de los siguientes símbolos [‘_’, ‘&’, ‘?’] 


Una vez que el registro haya sido exitoso (Si lo ha sido),  y después de una ardua jornada de selección, se asignarán las zonas del país donde llevarán los camiones con las vacunas, de acuerdo a la siguiente tabla.

![](Tabla.png)


Si no se cumplieron los criterios saldrá un mensaje que le avisará el **primer parámetro** donde tiene la falla: 

"Registro No Exitoso, [parámetro] incorrecto."


Si se cumplieron los criterios de validación, debe salir un mensaje con la siguiente información:

Nombre: [nombre]

Identificación: [ident]

Registro Exitoso! Bienvenido a la Corporación Umbrella.

Tu zona asignada para la distribución de la vacuna es: [Zona asignada]
Que tenga un Feliz Día!