import json 

class reader:

    def __init__(self):
        pass

    def cargar_datos_desde_json(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
            print("Datos cargados exitosamente desde el archivo JSON.")
            return datos
        except FileNotFoundError:
            print("Archivo no encontrado. Por favor, asegúrate de que el archivo JSON exista.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. Por favor, verifica el formato del archivo.")
        except KeyError:
            print("Clave faltante en el archivo JSON. Por favor, verifica la estructura del archivo.")