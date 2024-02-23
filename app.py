from analizador_archivos import AnalizadorArchivos

if __name__ == "__main__":
    carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra = input("Ingrese la palabra que desea buscar: ")

    analizador = AnalizadorArchivos(carpeta)
    analizador.analizar(palabra)
