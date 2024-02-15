
import os 
import json

#FUNCION PARA CARGAR LOS DATOS DE LOS CAMPERS QUE YA ESTAN
def cargar_datos(ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
        
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstPersonal

#FUNCION PARA AGREGAR LOS DATOS DEL NUEVO CAMPER
def guardar_datos(lstPersonal, ruta):
    # Función que guarda los datos de la lista de personal
    # en un arcivo JSON
    # Devuelve True: si los datos fueron guardados correctamente
    # Devuelve False: si los datos no se pudieron guardar
    try:
        fd = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstPersonal, fd, indent=4)
    except Exception as e:
        print("Error al guardar la información del empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla para continuar\n")
        return False
    
    return True

# Función para crear un nuevo objeto
def crear_camper():
    identificacion = str(input("ingresa el numero de identificación: ")) #Al inicio debes indicar donde quieres ingresar la informacion en  el JSON
    nombre = str(input(" ingresa el nombre: "))
    apellido1 = str(input(" ingresa el primer apellido: "))
    apellido2 = str(input(" ingresa el segundo apellido: "))
    direccion = str(input(" ingresa la direccion del camper: "))
    telefono1 = str(input(" ingresa el telefono celular: "))
    telefono2 = str(input(" ingresa el telefono fijo: "))
    edad = str(input(" ingresa la edad: "))
    estado = str(input(" ingrese el estado actual: "))
    acudiente = str(input(" ingresa el acudiente: "))
    data = cargar_datos("proyecto_python/data.json")
    id = len(data) + 1;
    nuevo_objeto = {"id": id, 
                    'identificacion':identificacion,
                    'nombre':nombre,
                    'apellido1':apellido1,
                    'apellido2':apellido2,
                    'direccion':direccion,
                    'telefono1':telefono1,
                    'telefono2':telefono2,
                    'edad':edad,
                    'estado':estado,
                    'acudiente':acudiente}
    data.append(nuevo_objeto)
    guardar_datos(data, 'proyecto_python/data.json')
    
# Función para leer todos los objetos
def leer_camper():
    with open('datos.json', 'r') as archivo:
        data = json.load(archivo)
    if data:
        print("Lista de Campers:")
        for camper in data:
            print(f"Identificacion:{camper['identificacion']}, Nombre: {camper['nombre']}, Apellido 1:{camper['apellido1']}, Apellido2:{camper['apellido2']}, Direccion:{camper['direccion']}, Telefono1:{camper['telefono1']}, Telefono2:{camper['telefono2']}, Edad: {camper['edad']}, Estado: {camper['estado']}")
    else:
        print("No hay Campers para mostrar.")

# Función para actualizar un objeto por nombre
def buscar_y_actualizar_camper(json_data, id_buscado, nuevos_datos):
    for data in json_data:
        if data.get("id") == id_buscado:
            data.update(nuevos_datos)
            return True
    return False    
# PARA LAS RUTAS
    ## AGREGAR RUTA
def agregarRuta(infModulos, nombreRuta):
    ruta = 'proyecto_python/rutas.json'
    rutaNew = {
        nombreRuta: infModulos
    }
    rutas = cargar_datos(ruta);
    rutas.append(rutaNew)
    guardar_datos(rutas, ruta,);


# Funcion para limpiar pantalla
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')