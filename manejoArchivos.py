# Se importan las librerías
import os


# Esta clase permite definir la implementación del patrón Singleton para tener
# una sola instancia de clase en el proyecto
class SingletonManejoArchivosMeta(type):
    _instancias = {}

    # Este método es el que restringe que solo se pueda crear una instancia del objeto
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            instancia = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instancia
        return cls._instancias[cls]


# Clase para operaciones de crear, agregar, editar y eliminar datos en el archivo usado
class ManejoArchivo(metaclass=SingletonManejoArchivosMeta):

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
    # en la variable nombreArchivo, no se retorna información.
    def CrearArchivo(self, nombreArchivo):

        # Se añade a la ruta de la carpeta el nombre del archivo donde se almacenará
        # el inventario de libros y se guarda en una variable del objeto self.archivoInventario
        # para no tener que pasar el nombre para realizar las operaciones sobre el archivo
        self.archivoInventario = self.carpetaArchivos + "/" + nombreArchivo

        # Se crea el archivo
        f = open(self.archivoInventario, "a")

        # Se cierra el archivo
        f.close()

    # Esta función permite añadir texto al archivo,
    # se ingresa el texto a ser escrito en el archivo,
    # no se retorna
    def AnadirContenidoAlArchivo(self, texto):

        # Se abre el archivo en formato append para añadir texto al final
        # y no empezar con el achivo en blanco cada vez que se vaya a escribir
        f = open(self.archivoInventario, "a")

        # Se escribe en el archivo el texto ingresado como parámetro
        f.write(texto)

        # Se escribe un salto de linea en el archivo para evitar escribir todo en la misma linea
        f.write('\n')

        # Se cierra el archivo
        f.close()

    # Esta función permite leer el contenido del archivo,
    # y se retorna el contenido en la variable mensaje
    def LeerArchivo(self):

        # Se verifica que no exista un error en la lectura del archivo
        try:

            # Se abre el archivo
            f = open(self.archivoInventario, "r")

            # Se lee el archivo y se imprime en consola el contenido
            mensaje = f.read()

            # Se cierra el archivo
            f.close()
        except:
            mensaje = "Error de lectura del archivo"

        return mensaje


    # Esta función permite eliminar el archivo del directorio de trabajo actual,
    # no se retorna información
    def EliminarArchivo(self):

        # Se intenta eliminar el archivo, si no existe se controla el error generado por
        # el sistema al no encontrar el archivo
        try:
            os.remove(self.archivoInventario)
        except OSError as error:
            print("Como el archivo no existe no se borrará y se controla el error")