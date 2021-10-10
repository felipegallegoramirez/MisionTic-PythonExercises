'''
*NOTA:

¡ESTE SCRIPT SOLO CONTIENE LA DESCRIPCIÓN DE LA FUNCIÓN control()!

Usted debe construir su solución dentro de la función control(). 

Cuando usted haya terminado toda la lógica dentro de la función control(), entonces debe proceder a terminar el script main.py 
'''
import csv


##import matplotlib.pyplot as plt
def control(punto_distribucion):
    p = int(punto_distribucion)
    '''
  input: recibe el punto_distribucion
  proceso:
   1. lee los dos archivos proporcionados para este reto: 
   'ValoresAsignados.csv'
   'ValoresReportados.csv'
   2. muestra las estadísticas de cada punto de distribución,comparando cada fila de ValoresAsignados.csv vs ValoresReportados.csv
   3. Si usted desea puede seguir trabajado dentro de esta función o crear otras funciones o segmentos de codigo en este script control.py o en el sccript main.py para resolver todo lo que el Reto6 solicita.
  output: puede retornar o no valores (eso se deja a criterio del programador)
  '''
    #=================================================
    #E S P A C I O   D E   T R A B A J O   A L U M N O
    #=================================================
    asig = open('ValoresAsignados.csv', 'r')
    list_asig = []
    read_asig = csv.reader(asig)

    for row in read_asig:
        list_asig.append(row)
    asig.close()

    reg = open('ValoresRegistrados.csv', 'r')
    list_reg = []
    read_reg = csv.reader(reg)

    for row in read_reg:
        list_reg.append(row)
    reg.close()

    entregas = 0
    result = open('registro_estadisticas.csv', 'w')
    list_resultados = [[
        'PuntoDistribucion', 'EficienciaTiemposDespacho_', 'TasaEntrega_cajas',
        'NivelCumplimientoDespachos_%'
    ]]
    result.write(str(list_resultados[0]))
    result.write('\n')

    for i in range(1, len(list_asig)):
        efi = round(
            100 * (int(list_asig[i][2]) - int(list_reg[i][2])) /
            int(list_asig[i][2]), 1)
        tasa = round(int(list_reg[i][1]) / int(list_reg[i][2]), 1)
        cumplimiento = round(
            100 * (int(list_reg[i][1]) / int(list_asig[i][1])), 1)
        cant = i
        list_resultados.append([i, efi, tasa, cumplimiento])
        result.write(str(list_resultados[i]))
        result.write('\n')
        if (int(list_asig[i][2]) >= int(list_reg[i][2])):
            entregas += 1
    entregas = (entregas / cant) * 100
    print(f'Eficiencia en tiempos de despacho = {list_resultados[p][1]} %')
    print(f'Tasa de entrega = {list_resultados[p][2]} cajas/min')
    print(
        f'Nivel de cumplimiento de los despachos = {list_resultados[p][3]} %')
    print(f'Entregas a tiempo = {entregas} %')


'''
  eje_x=[]
  eje_y=[]
  for i in range(1,cant):
    eje_x.append(int(list_asig[i][0]))
    eje_y.append(int(list_asig[i][1]))
  plt.title('Asignado Carga_cajas(EjeY) vs PuntoDistribucion(EjeX)', size = 15)
  plt.xlabel('PuntoDistribucion', size = 20)
  plt.ylabel('Carga_cajas', size = 20)

  plt.plot(eje_x, eje_y, 'r',label = 'Cajas')
  plt.legend()
  plt.show()
  
  eje_x2=[]
  eje_y2=[]

  for i in range(1,cant):
    eje_x2.append(int(list_asig[i][0]))
    eje_y2.append(int(list_asig[i][2]))
  plt.title('Asignado Tiempo_minutos(EjeY) vs PuntoDistribucion(EjeX)', size = 15)
  plt.xlabel('PuntoDistribucion', size = 20)
  plt.ylabel('Tiempo_minutos', size = 20)

  plt.plot(eje_x2, eje_y2, 'r', label = 'Tiempo')
  plt.legend()
  plt.show()
  
  plt.title('Asignado i y ii ', size = 15)
  plt.xlabel('PuntoDistribucion', size = 20)
  plt.ylabel('Tiempo_minutos', size = 20)

  plt.plot(eje_x2, eje_y2, 'r', label = 'Tiempo')
  plt.plot(eje_x, eje_y, 'b', label = 'Cajas')
  plt.legend()
  plt.show()

  eje_x=[]
  eje_y=[]
  for i in range(1,cant):
    eje_x.append(int(list_reg[i][0]))
    eje_y.append(int(list_reg[i][1]))
  plt.title('Registrado Carga_cajas(EjeY) vs PuntoDistribucion(EjeX)', size = 15)
  plt.xlabel('PuntoDistribucion', size = 20)
  plt.ylabel('Carga_cajas', size = 20)

  plt.plot(eje_x, eje_y, 'r',label = 'Cajas')
  plt.legend()
  plt.show()
  
  eje_x2=[]
  eje_y2=[]

  for i in range(1,cant):
    eje_x2.append(int(list_reg[i][0]))
    eje_y2.append(int(list_reg[i][2]))
  plt.title('Registrado Tiempo_minutos(EjeY) vs PuntoDistribucion(EjeX)', size = 15)
  plt.xlabel('PuntoDistribucion', size = 20)
  plt.ylabel('Tiempo_minutos', size = 20)

  plt.plot(eje_x2, eje_y2, 'r', label = 'Tiempo')
  plt.legend()
  plt.show()
  
  plt.title('Registrado i y ii ', size = 15)
  plt.xlabel('PuntoDistribucion', size = 20)
  plt.ylabel('Tiempo_minutos', size = 20)

  plt.plot(eje_x2, eje_y2, 'r', label = 'Tiempo')
  plt.plot(eje_x, eje_y, 'b', label = 'Cajas')
  plt.legend()
  plt.show()
  '''
