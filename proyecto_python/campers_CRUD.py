import json
# Función para cargar datos desde el archivo JSON
def cargar_datos():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

# Función para guardar datos en el archivo JSON
def guardar_datos(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)

# Función para crear un nuevo camper
def crear_camper():
    identificacion = int(input("ingresa el numero de identificación: ")) #Al inicio debes indicar donde quieres ingresar la informacion en  el JSON
    nombre = str(input("ingresa el nombre: "))
    apellido1 = str(input("ingresa el primer apellido: "))
    apellido2 = str(input("ingresa el segundo apellido: "))
    direccion = str(input("ingresa la direccion del camper: "))
    telefono1 = int(input("ingresa el telefono celular: "))
    telefono2 = int(input("ingresa el telefono fijo: "))
    edad = int(input("ingresa la edad: "))
    estado = str(input("ingrese el estado actual: "))
    acudiente = str(input("ingresa el acudiente: "))

    data = cargar_datos()
    nuevo_camper = {'identificacoion':identificacion, 'nombre':nombre,'apellido1':apellido1, 'apellido2':apellido2, 'direccion':direccion, 'telefono1':telefono1, 'telefono2':telefono2, 'edad':edad, 'estado':estado, 'acudiente':acudiente}
    data.append(nuevo_camper)
    guardar_datos(data)
    print("Objeto creado con éxito.")

# Función para leer todos los objetos
def leer_camper():
    data = cargar_datos()
    if data:
        print("Lista de Campers:")
        for camper in data:
            print(f"Identificacion:{camper['identificacion']}, Nombre: {camper['nombre']}, Apellido 1:{camper['apellido1']}, Apellido2:{camper['apellido2']}, Direccion:{camper['direccion']}, Telefono1:{camper['telefono1']}, Telefono2:{camper['telefono2']}, Edad: {camper['edad']}, Estado: {camper['estado']}, Acudiente: {camper['acudiente']}")
    else:
        print("No hay Campers para mostrar.")

# Función para actualizar un objeto por nombre
def actualizar_camper():
    camper_a_actualizar = input("Ingrese el nombre del Camper a actualizar: ")
    data = cargar_datos()

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

# Función para eliminar un objeto por nombre
def eliminar_objeto():
    camper_a_eliminar = input("Ingrese el nombre del objeto a eliminar: ")
    data = cargar_datos()

    for elim_camper in data:
        if elim_camper['nombre'] == camper_a_eliminar:
            data.remove(elim_camper)
            guardar_datos(data)
            print("Objeto eliminado con éxito.")
            return
    
    print(f"No se encontró el objeto con el nombre {camper_a_eliminar}.")
