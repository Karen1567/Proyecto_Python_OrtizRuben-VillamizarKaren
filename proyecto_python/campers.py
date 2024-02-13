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
            json.dump(self.campers_data, file, indent=2)

    def create_camper(self, name, age):
        new_camper = {'name': name, 'age': age}
        self.campers_data['campers'].append(new_camper)
        self.save_data()
        print(f"Camper {name} creado con éxito.")

    def read_campers(self):
        campers = self.campers_data['campers']
        for camper in campers:
            print(f"Nombre: {camper['name']}, Edad: {camper['age']}")

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
app.create_camper('Juan', 25)

# Mostrar todos los campers
app.read_campers()

# Actualizar la edad de un camper
app.update_camper('Juan', 26)

# Eliminar un camper
app.delete_camper('Juan')

# Mostrar campers después de eliminar
app.read_campers()