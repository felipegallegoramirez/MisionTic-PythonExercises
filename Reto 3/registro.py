

def validar_nombre(nombre):
  #retorna un booleano
  paso=nombre.isalpha()

  return paso

def validar_ident(identificacion):
  #retorna un booleano
  paso=False
  if 10000000<identificacion<100000000:
    paso=True
  return paso

def validar_correo(correo):
  #retorna un booleano
  cant=correo.count("@")
  paso=False
  if cant==1:
    paso=True
  return paso

def validar_sobrenombre(sobrenombre):
  #retorna un booleano
  cant=sobrenombre.count("a")
  
  num=sobrenombre[0].isdigit()
  paso=False
  if cant<=3 and num==False:
    paso=True
  return paso 

def validar_clave(clave):
  #retorna un booleano
  cant=clave.count("_")
  cant=cant+clave.count("&")
  cant=cant+clave.count("?")
  paso=False
  if cant>0:
    paso=True
  return paso
  
def asignar_zona(tiempo, tratamiento, conocimiento):
  tiempo=tiempo/12
  if (1<tiempo<=5) and (tratamiento=="No") and (conocimiento=="No"):
    zona="Sur"
  
  elif (1<tiempo<=5) and (tratamiento=="Si") and (conocimiento=="No"):
    zona="Norte"

  elif (tiempo >5) and (tratamiento=="No") and (conocimiento=="Si"):
    zona="Oriente"

  elif (tiempo >5) and (tratamiento=="Si") and (conocimiento=="Si"):
    zona="Occidente"

  elif (tiempo >5) and (tratamiento=="No") and (conocimiento=="No"):
    zona="Sur Occidente"
  else:
    zona="Central"

  #retorna un string con la zona
  return zona


def validar_informacion(val_nombre, val_ident, val_correo, val_sobrenombre, val_clave):
  paso=False
  if val_nombre==False:
    mensaje="Registro No Exitoso, nombre incorrecto."
  elif val_ident==False:
    mensaje="Registro No Exitoso, ident incorrecto."
  elif val_correo==False:
    mensaje="Registro No Exitoso, correo incorrecto."
  elif val_sobrenombre==False:
    mensaje="Registro No Exitoso, sobrenombre incorrecto."
  elif val_clave==False:
    mensaje="Registro No Exitoso, clave incorrecto."
  else:
    paso=True
    mensaje=""

  #retorna dos valores: booleano, parámetro(string)
  return paso,mensaje
