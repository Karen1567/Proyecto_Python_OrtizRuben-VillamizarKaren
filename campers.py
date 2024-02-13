import json

class CampersApp:
    def __init__(self, data_file):
        self.data_file = data_file
        self.campers_data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {'campers': []}
        return data

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.campers_data, file, indent=10)

    def create_camper(self, identificacion, nombre, apellido1, apellido2, direccion, telefono1, telefono2, edad, estado,acudiente):
        new_camper = {'identificacoion':identificacion, 'nombre':nombre,'apellido1':apellido1, 'apellido2':apellido2, 'direccion':direccion, 'telefono1':telefono1, 'telefono2':telefono2, 'edad':edad, 'estado':estado, 'acudiente':acudiente}
        self.campers_data['campers'].append(new_camper)
        self.save_data()    
        print(f"Camper {identificacion, nombre, apellido1, apellido2, direccion, telefono1, telefono2, edad, estado, acudiente}creado con éxito.")

    def read_campers(self):
        campers = self.campers_data['campers']
        for camper in campers:
            print(f"Identificacion:{camper['identificacion']}, Nombre: {camper['nombre']}, Apellido 1:{camper['apellido1']}, Apellido2:{camper['apellido2']}, Direccion:{camper['direccion']}, Telefono1:{camper['telefono1']}, Telefono2:{camper['telefono2']}, Edad: {camper['edad']}, Estado: {camper['estado']}, Acudiente: {camper['acudiente']}")

    def update_camper(self, name, new_age):
        campers = self.campers_data['campers']
        for camper in campers:
            if camper['name'] == name:
                camper['age'] = new_age
                self.save_data()
                print(f"Edad de {name} actualizada a {new_age}.")
                return
        print(f"No se encontró al camper {name}.")

    def delete_camper(self, name):
        campers = self.campers_data['campers']
        for camper in campers:
            if camper['name'] == name:
                campers.remove(camper)
                self.save_data()
                print(f"Camper {name} eliminado con éxito.")
                return
        print(f"No se encontró al camper {name}.")

# Uso de la aplicación
app = CampersApp('campers_data.json')

# Crear un nuevo camper
app.create_camper()

# Mostrar todos los campers
app.read_campers()

# Actualizar la edad de un camper
app.update_camper()

# Eliminar un camper
app.delete_camper()

# Mostrar campers después de eliminar
app.read_campers()