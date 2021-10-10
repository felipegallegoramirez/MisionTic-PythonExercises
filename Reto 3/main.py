import registro as reg


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

nombre=input()
ident=int(input())
correo=input()
sobrenombre=input()
clave=input()
tiempo=int(input())
tratamiento=input()
conocimiento=input()


val_nombre=reg.validar_nombre(nombre)
val_ident=reg.validar_ident(ident)
val_correo=reg.validar_correo(correo)
val_sobrenombre=reg.validar_sobrenombre(sobrenombre)
val_clave=reg.validar_clave(clave)

est,mensaje=reg.validar_informacion(val_nombre, val_ident, val_correo, val_sobrenombre, val_clave)

if est==True:
  print("Nombre:",nombre)
  print("Identificación:",ident)
  print("Registro Exitoso!, Bienvenido a la Corporación Umbrella.")
  zona=reg.asignar_zona(tiempo,tratamiento,conocimiento)
  print(f"Tu zona asignada para la distribución de la vacuna es: {zona}")
  print("Que tenga un Feliz Día!")
else:
  print (mensaje)