# Se importan las librerias
from manejoArchivos import ManejoArchivo

# Variables
nombreArchivo = "datos_libros.txt"

# Inicio del programa
archivo = ManejoArchivo()

# Se ingresa en un bucle infinito hasta que el usuario ingrese 0
opcion = '1'

while opcion != '0':

    # Se despliega el menú al usuario
    print('Seleccione la operación que desea realizar sobre el archivo:')
    print('1. Crear el archivo desde cero')
    print('2. Añadir contenido al archivo ya creado')
    print('3. Leer el contenido del archivo')
    print('4. Eliminar el archivo')
    print('0. Salir del sistema')

    # Se lee la opción ingresada por el usuario
    opcion = input('Ingrese la opción que desea realizar -> ')

    if opcion == '1':
        archivo.CrearArchivo(nombreArchivo)

    elif opcion == '2':

        texto = "m1,matematicas 1, matematicas, 10"

        archivo.AnadirContenidoAlArchivo(nombreArchivo, texto)

    elif opcion == '3':
        archivo.LeerArchivo(nombreArchivo)

    elif opcion == '4':
        archivo.EliminarArchivo(nombreArchivo)

    elif opcion == '0':
        print('Gracias por usar el sistema!')

    else:
        print('Error de ingreso')
