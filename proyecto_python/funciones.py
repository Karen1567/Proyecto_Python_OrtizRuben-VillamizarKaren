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

# Función para crear un nuevo objeto
def crear_camper():
    with open('creacion_de_datos.json','r')as proceso1:
        creacion_de_datos = json.load(proceso1)
    identificacion = int(input("ingresa el numero de identificación")) #Al inicio debes indicar donde quieres ingresar la informacion en  el JSON
    nombre = str(input("ingresa el nombre"))
    apellido1 = str(input("ingresa el primer apellido: "))
    apellido2 = str(input("ingresa el segundo apellido: "))
    direccion = str(input("ingresa la direccion del camper: "))
    telefono1 = int(input("ingresa el telefono celular: "))
    telefono2 = int(input("ingresa el telefono fijo: "))
    edad = int(input("ingresa la edad: "))
    estado = str(input("ingrese el estado actual: "))
    if edad > 16 and edad < 27:
        if edad <18  :
            acudiente = str(input("ingresa el acudiente: "))
        else:
            print ("fuera de rango")
    json_datos = json.dump()
    
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
    nombre_a_actualizar = input("Ingrese el nombre del Camper a actualizar: ")
    data = cargar_datos()

    for act_camper in data:
        if act_camper['nombre'] == nombre_a_actualizar:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nueva_edad = int(input("Ingrese la nueva edad: "))
            act_camper['nombre'] = nuevo_nombre
            act_camper['edad'] = nueva_edad
            guardar_datos(data)
            print("Objeto actualizado con éxito.")
            return
    
    print(f"No se encontró el objeto con el nombre {nombre_a_actualizar}.")

# Función para eliminar un objeto por nombre
def eliminar_objeto():
    nombre_a_eliminar = input("Ingrese el nombre del objeto a eliminar: ")
    data = cargar_datos()

    for obj in data:
        if obj['nombre'] == nombre_a_eliminar:
            data.remove(obj)
            guardar_datos(data)
            print("Objeto eliminado con éxito.")
            return
    
    print(f"No se encontró el objeto con el nombre {nombre_a_eliminar}.")
