# Se importan las librerías
import os


class ManejoArchivo:

    def __init__(self):

        # Se obtiene el directorio actual
        directorioActual = os.getcwd()

        # Se define el nombre de la carpeta donde estarán los archivos
        self.carpetaArchivos = directorioActual + "/" + "directorioArchivos"

        # Se crea la carpeta para almacenar los archivos
        # y se controla el error en caso tal de que se intente crear la carpeta
        # sabiendo que ya existe en el sistema
        try:
            os.mkdir(self.carpetaArchivos)
        except OSError as error:
            print("Como la carpeta de archivos ya existe no se creará de nuevo")

    # Esta función permite crear el archivo a partir del nombre ingresado por el usuario
    # en la variable nombreArchivo,
    # no se retorna información.
    def CrearArchivo(self, nombreArchivo):

        # Se añade a la ruta de la carpeta el nombre del archivo donde se almacenará el inventario de libros
        archivoInventario = self.carpetaArchivos + "/" + nombreArchivo

        # Se crea el archivo
        f = open(archivoInventario, "w")

        # Se cierra el archivo
        f.close()

    # Esta función permite añadir texto al archivo,
    # se ingresa el nombre el archivo y el texto a ser escrito en el archivo,
    # no se retorna
    def AnadirContenidoAlArchivo(self, nombreArchivo, texto):

        # Variable con la ruta completa del archivo de inventario
        archivoInventario = self.carpetaArchivos + "/" + nombreArchivo

        # Se abre el archivo
        f = open(archivoInventario, "a")

        # Se escribe en el archivo el texto ingresado como parámetro
        f.write(texto)

        # Se escribe un salto de linea en el archivo para posteriormente escribir en la siguiente linea
        f.write('\n')

        # Se cierra el archivo
        f.close()

    # Esta función permite leer el contenido del archivo a partir del nombre
    # ingresado por el usuario en la variable nombreArchivo,
    # no se retorna información.
    def LeerArchivo(self, nombreArchivo):

        # Variable con la ruta completa del archivo de inventario
        archivoInventario = self.carpetaArchivos + "/" + nombreArchivo

        # Se abre el archivo
        f = open(archivoInventario, "r")

        # Se lee el archivo y se imprime en consola el contenido
        print(f.read())

        # Se cierra el archivo
        f.close()

    # Esta función permite eliminar el archivo del directorio de trabajo actual,
    # se ingresa el nombre el archivo a ser eliminado en los parámetros,
    # no se retorna información
    def EliminarArchivo(self, nombreArchivo):

        # Variable con la ruta completa del archivo de inventario
        archivoInventario = self.carpetaArchivos + "/" + nombreArchivo

        # Se intenta eliminar el archivo, si no existe se controla el error generado por
        # el sistema al no encontrar el archivo
        try:
            os.remove(archivoInventario)
        except OSError as error:
            print("Como el archivo no existe no se borrará y se controla el error")