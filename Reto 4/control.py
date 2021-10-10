
#=======================================================
#E S P A C I O    D E    T R A B A J O     A L U M N O
#=======================================================
def control_camion(tiempo_entrega, cantidad_cajas):
  if (tiempo_entrega < 15) and (cantidad_cajas >= 10):
    cajas_totales=100
    for r in range (1,11):
      print ("Punto de distribución #",r)
      cajas_camion=0
      for i in range(1,cantidad_cajas+1):
        if i > 10:
          print("Encender alarma")
        print("Caja #",i)
        cajas_totales=cajas_totales-1
        cajas_camion=cajas_camion+1
        if (cajas_totales<=0):
          print("Se ha agotado el inventario en el camión")
          break
      print("El total de cajas en inventario en el camión =",cajas_totales)
      print("Cantidad de cajas despachadas =",cajas_camion)
      print("Tiempo de despacho =",tiempo_entrega)
      if (cajas_totales<=0):
        break
  elif (tiempo_entrega > 15 or tiempo_entrega < 0 ):
    print("Se excede el límite de tiempo")
  elif (cantidad_cajas < 10):
    print("La cantidad de cajas de vacunas a despachar en cada punto de distribución es inferior a la mínima ideal/sugerida (10)")


  # no retorna ningún valor