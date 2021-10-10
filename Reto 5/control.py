
def estadistica(lista_tuplas_asignado, lista_tuplas_registrado):
#=======================================================
#E S P A C I O    D E    T R A B A J O     A L U M N O
#======================================================= 
  tiempos=[[99999,99999,99999],[0,0,0]]
  sobre=[[99999,99999,99999],[0,0,0]]
  s=0
  cant=[]
  for i in range(0,10):
   print ("Punto #",i+1)
   Diferencia=lista_tuplas_asignado[i][1]-lista_tuplas_registrado[i][1]
   if (Diferencia<sobre[1][0]):
    sobre[0][2]=sobre[0][1]
    sobre[1][2]=sobre[1][1]
    sobre[0][1]=sobre[0][0]
    sobre[1][1]=sobre[1][0]
    sobre[0][0]=i+1
    sobre[1][0]=Diferencia
   elif Diferencia<sobre[1][1]:
    sobre[0][2]=sobre[0][1]
    sobre[1][2]=sobre[1][1]
    sobre[0][1]=i+1
    sobre[1][1]=Diferencia
   elif Diferencia<sobre[1][2]:
    sobre[0][2]=i+1
    sobre[1][2]=Diferencia
   if Diferencia < 0:
     s+=1
   print ("Diferencia de cajas =",Diferencia)
   Diferencia=lista_tuplas_asignado[i][2]-lista_tuplas_registrado[i][2]
   if (Diferencia<tiempos[1][0]):
    tiempos[0][2]=tiempos[0][1]
    tiempos[1][2]=tiempos[1][1]
    tiempos[0][1]=tiempos[0][0]
    tiempos[1][1]=tiempos[1][0]
    tiempos[0][0]=i+1
    tiempos[1][0]=Diferencia
   elif Diferencia<tiempos[1][1]:
    tiempos[0][2]=tiempos[0][1]
    tiempos[1][2]=tiempos[1][1]
    tiempos[0][1]=i+1
    tiempos[1][1]=Diferencia
   elif Diferencia<tiempos[1][2]:
    tiempos[0][2]=i+1
    tiempos[1][2]=Diferencia
   if Diferencia < 0:
    s+=1
   print("Diferencia de tiempos =",Diferencia)
   Diferencia=round(((lista_tuplas_asignado[i][2]-lista_tuplas_registrado[i][2])/lista_tuplas_asignado[i][2])*100,1)
   print(f"Eficiencia = {Diferencia}%")
   if s==2:
     cant.append(i+1)
   else:
     s=0
  print("Los puntos con mayores demoras de tiempo:")
  for i in range(3):
    print(f"Punto {tiempos[0][i]}: {tiempos[1][i]}")
  print("Los puntos con mayores sobre-entregas:")
  for i in range(3):
    print(f"Punto {sobre[0][i]}: {sobre[1][i]}")
  print("Puntos con los dos criterios negativos:")
  for i in cant:
    print("Punto",i)

   
# No retorna valor