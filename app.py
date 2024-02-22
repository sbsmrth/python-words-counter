import os

class ContadorPalabras:
    def __init__(self, carpeta, palabra):
        self.carpeta = carpeta
        self.palabra = palabra

    def contar_en_archivo(self, archivo):
        try:
            with open(archivo, 'r') as file:
                contenido = file.read()
                veces = contenido.count(self.palabra)
                print(f"{archivo}: {veces} veces")
                return veces
        except FileNotFoundError:
            print(f"Error: No se pudo abrir el archivo {archivo}")
            return 0

    def contar_en_carpeta(self):
        if not os.path.exists(self.carpeta):
            print("Error: La carpeta indicada no existe.")
            return

        total_veces = 0
        for archivo in os.listdir(self.carpeta):
            if archivo.endswith(".txt"):
                archivo_path = os.path.join(self.carpeta, archivo)
                total_veces += self.contar_en_archivo(archivo_path)

        if total_veces == 0:
            print("No se encontraron archivos de texto en la carpeta.")
        else:
            print(f"Total: {total_veces} veces")


if __name__ == "__main__":
    carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra = input("Ingrese la palabra que desea buscar: ")

    contador = ContadorPalabras(carpeta, palabra)
    contador.contar_en_carpeta()
