# Se importan las librerías
import os


class ManejoArchivo:

    # Esta función permite crear el archivo a partir del nombre ingresado por el usuario
    # en la variable nombreArchivo,
    # no se retorna información.
    def CrearArchivo(self, nombreArchivo):
        # Se crea el archivo
        f = open(nombreArchivo, "w")

        # Se cierra el archivo
        f.close()

    # Esta función permite añadir texto al archivo,
    # se ingresa el nombre el archivo y el texto a ser escrito en el archivo,
    # no se retorna
    def AnadirContenidoAlArchivo(self, nombreArchivo, texto):
        # Se abre el archivo
        f = open(nombreArchivo, "a")

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
        # Se abre el archivo
        f = open(nombreArchivo, "r")

        # Se lee el archivo y se imprime en consola el contenido
        print(f.read())

        # Se cierra el archivo
        f.close()

    # Esta función permite eliminar el archivo del directorio de trabajo actual,
    # se ingresa el nombre el archivo a ser eliminado en los parámetros,
    # no se retorna información
    def EliminarArchivo(self, nombreArchivo):
        # Se elimina el archivo
        os.remove(nombreArchivo)