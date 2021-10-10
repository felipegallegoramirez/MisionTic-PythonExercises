'''
*NOTA:

¡ESTE SCRIPT SOLO CONTIENE LA DESCRIPCIÓN DE LA FUNCIÓN control()!

Usted debe construir su solución dentro de la función control(). 

Cuando usted haya terminado toda la lógica dentro de la función control(), entonces debe proceder a terminar el script main.py 
'''

def control(empresa_transp, id_camion):
  '''
  input: recibe el nombre de la Empresa transportadora y el Id del camión
  proceso:
   1. Lee los dos archivos proporcionados para este reto: 
   'Valores_Asignados.csv'
   'Valores_Reportados.csv'
   2. Muestra las estadísticas solicitadas,comparando cada fila de ValoresAsignados.csv vs ValoresReportados.csv
   3. Si usted desea puede seguir trabajado dentro de esta función o crear otras funciones o segmentos de codigo en este script control.py para resolver todo lo que el Reto 7 solicita.
  output: puede retornar o no valores (eso se deja a criterio del programador)
  '''
  #=================================================
  #E S P A C I O   D E   T R A B A J O   A L U M N O
  #=================================================

  list_asig = Archivo('Valores_Asignados.csv')
  list_reg = Archivo('Valores_Registrados.csv')
  asig=[0,0,0,0,0]
  reg=[0,0,0,0,0]

  if len(list_asig) == len(list_reg):
    tamaño=len(list_asig)
  else:
    if len(list_asig) > len(list_reg):
      tamaño=len(list_asig)
    else:
      tamaño=len(list_reg)
  porcent=0
  cant=0

  for i in range (1,tamaño):
    try:
      if list_asig[i][0] == empresa_transp and  list_asig[i][2] == id_camion:
        for l in range(1,5):
          asig[l]=asig[l]+int(list_asig[i][l])
    except:
      print("Fin asignados")
    try:
      if list_reg[i][0] == empresa_transp and list_reg[i][2] == id_camion:
        for l in range(1,5):
          reg[l]=reg[l]+int(list_reg[i][l])
    except:
      print("Fin Registrados")
    if list_asig[i][2]==list_reg[i][2] and list_asig[i][2] == id_camion and list_asig[i][0] == empresa_transp:
      cant+=1
      if int(list_asig[i][4])>=int(list_reg[i][4]):
        porcent+=1

  Desempeño=[0,0,0,0]
  Desempeño[0]=round(100*(int(asig[4])-int(reg[4]))/int(asig[4]),1)
  Desempeño[1]=round(int(reg[3])/int(reg[4]),1)
  Desempeño[2]=round(100*int(reg[3])/int(asig[3]),1)
  Desempeño[3]=round(porcent/cant*100,1)
  print(f"Eficiencia en tiempo de Despacho = {Desempeño[0]} %")
  print(f"Tasa de entrega = {Desempeño[1]} cajas/min")
  print(f"Nivel de cumplimiento = {Desempeño[2]} %")
  print(f"Entregas a tiempo = {Desempeño[3]} %")
def Archivo (nombre):
  import csv
  with open(nombre, 'r') as reg:
    arreglo = []
    read_reg = csv.reader(reg)
    for row in read_reg:
        arreglo.append(row)
    reg.close()
  return arreglo