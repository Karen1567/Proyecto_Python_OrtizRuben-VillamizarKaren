import json
# Función para cargar datos desde el archivo JSON
def cargar_datos():
    try:
        with open('campers.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

# Función para guardar datos en el archivo JSON
def guardar_datos(data):
    with open('campers.json', 'w') as file:
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
    nuevo_camper = {'id':id,'identificacoion':identificacion, 'nombre':nombre,'apellido1':apellido1, 'apellido2':apellido2, 'direccion':direccion, 'telefono1':telefono1, 'telefono2':telefono2, 'edad':edad, 'estado':estado, 'acudiente':acudiente}
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
    camper_a_actualizar = input("Ingrese el id del Camper a actualizar: ")
    data = cargar_datos()
    decisiondecamper = str(input("ingresa el id del Camper: "))
    nombre = str(input("ingresa el nombre actualizado: "))
    apellido1 = str(input("ingresa el primer apellido actualizado: "))
    apellido2 = str(input("ingresa el segundo apellido actualizado: "))
    direccion = str(input("ingresa la direccion del camper actualizado: "))
    telefono1 = str(input("ingresa el telefono celular actualizado: "))
    telefono2 = str(input("ingresa el telefono fijo actualizado: "))
    edad = str(input("ingresa la edad actualizado: "))
    acudiente = str(input("ingresa el acudiente: "))
    
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
