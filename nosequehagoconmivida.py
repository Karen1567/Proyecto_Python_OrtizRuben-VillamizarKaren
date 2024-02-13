#x = int(input("elige"))
 #   if(x==1):
  #      nombre=str(input("ingresa el nombre:"))
   #     categoria[nombre] =nombre
    #    print("")
    data = cargar_datos()
    nuevo_objeto = {'identificacoion':identificacion, 'nombre':nombre,'apellido1':apellido1, 'apellido2':apellido2, 'direccion':direccion, 'telefono1':telefono1, 'telefono2':telefono2, 'edad':edad, 'estado':estado, 'acudiente':acudiente}
    data.append(nuevo_objeto)
    guardar_datos(data)
    print("Objeto creado con éxito.")
