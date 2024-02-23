from carpeta_archivos import CarpetaArchivos


class AnalizadorArchivos:
    """
    Clase para analizar archivos de texto en una carpeta dada en busca de una palabra específica.
    """

    def __init__(self, carpeta):
        """
        Inicializa un nuevo analizador de archivos con la carpeta dada.

        Args:
            carpeta (str): La ruta de la carpeta que se va a analizar.
        """
        self.carpeta = CarpetaArchivos(carpeta)

    def analizar(self, palabra):
        """
        Analiza los archivos de la carpeta en busca de una palabra específica y muestra los resultados.

        Args:
            palabra (str): La palabra que se desea buscar.
        """
        self.carpeta.listar_archivos()
        total_palabras = self.carpeta.contar_palabra_en_archivos(palabra)
        self.mostrar_resultados(total_palabras, palabra)

    def mostrar_resultados(self, total, palabra):
        """
        Muestra los resultados del análisis, incluyendo el número de ocurrencias de la palabra en cada archivo y el total.

        Args:
            total (int): El número total de ocurrencias de la palabra en todos los archivos.
        """
        print("Resultados:")
        for archivo in self.carpeta.archivos:
            print(f"{archivo.nombre}: {archivo.contar_palabra(palabra)} veces")
        print(f"Total: {total} veces")
