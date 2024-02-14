
                        
                        
                        
                        
for act_camper in data:
        if act_camper['nombre'] == camper_a_actualizar:
        
            nuevo_nombre = str(input("ingresa el nombre: "))
            nuevo_identificacion = int(input("ingresa el numero de identificación: "))
            nuevo_apellido1 = str(input("ingresa el primer apellido: "))
            nuevo_apellido2 = str(input("ingresa el segundo apellido: "))
            nueva_direccion = str(input("ingresa la direccion del camper: "))
            nuevo_telefono1 = int(input("ingresa el telefono celular: "))
            nuevo_telefono2 = int(input("ingresa el telefono fijo: "))
            nueva_edad = int(input("ingresa la edad: "))
            nuevo_estado = str(input("ingrese el estado actual: "))
            
            act_camper['identificacion'] = nuevo_identificacion
            act_camper['nombre'] = nueva_edad
            act_camper['apellido1'] = nuevo_apellido1
            act_camper['apellido2'] = nuevo_apellido2
            act_camper['direccion'] = nueva_direccion
            act_camper['telefono1'] = nuevo_telefono1
            act_camper['telefono2'] = nuevo_telefono2           
            act_camper['edad'] = nueva_edad
            act_camper['estado'] = nuevo_estado
            
            guardar_datos(data)
            print("Objeto actualizado con éxito.")
            return
    
    print(f"No se encontró el objeto con el nombre {camper_a_actualizar}.")
