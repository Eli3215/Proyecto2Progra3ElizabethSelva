# Se importan las librerias
import tkinter as tk
from manejoArchivos import ManejoArchivo
from categoriaLibro import FabricaLibros


# Funciones que se llaman al presionar los botones en la interfaz

# Función para leer el contenido del archivo cuando se presiona el botón botonLeerArchivo
def LeerArchivo():
    # Texto leido del archivo
    mensaje = archivo.LeerArchivo()

    # Se limpia el contenido de la matriz donde se almacena el contenido completo de los libros
    matrizLibros.clear()

    # Como deseamos tener los datos de cada libro, primero
    # usamos el método split para obtener los datos de cada linea del archivo
    # y lo almacenamos en forma de lista o vector con las caracteristicas
    listaLibros = []
    listaLibros = mensaje.split("\n")

    # Recorremos toda la lista de libros para obtener de cada uno las características
    for libro in listaLibros:

        # Usamos nuevamente el método split para buscar cada parámetro del libro
        # que esté separado por ; y lo almacenamos en la lista
        listaCaracteristicasLibro = libro.split(";")

        # Evaluamos si hay una lista de caracteristicas valida
        if len(listaCaracteristicasLibro) > 1:
            matrizLibros.append(listaCaracteristicasLibro)

    # Se imprime el contenido del archivo de texto en la pantalla como una tabla
    info_text.delete('1.0', tk.END)

    # Se inserta el encabezado de la tabla en pantalla
    info_text.insert(tk.END, "codigo | nombre | categoria | precio | cantidad |")
    info_text.insert(tk.END, "\n")

    # Se recorre la matriz de libros para mostrarla en pantalla
    for fila in matrizLibros:
        for columna in fila:
            info_text.insert(tk.END, columna)
            info_text.insert(tk.END, " | ")

        info_text.insert(tk.END, "\n")


# Función para guardar el contenido del archivo cuando se presiona el botón botonGuardarArchivo
def GuardarDatosLibro():
    # Llamado a la clase que fabricará los libros de ciencias o humanidades de acuerdo a lo ingresado
    fabrica = FabricaLibros()

    # De la interfaz primero se obtiene la categoría del libro
    if (categoriaLibro.get() == 'LibroCiencias'):
        libro = fabrica.CrearLibro('LibroCiencias')
    elif (categoriaLibro.get() == 'LibroHumanidades'):
        libro = fabrica.CrearLibro('LibroHumanidades')
    else:
        print('Error de ingreso')

    # Se obtienen los datos de los campos de ingreso y se almacenan en el objeto
    libro.EstablecerCodigo()
    libro.EstablecerNombre(ingresoNombre.get())
    libro.EstablecerPrecio(ingresoPrecio.get())
    libro.EstablecerCantidad(ingresoCantidad.get())

    mensaje = libro.RetornarCaracteristicasLibro()

    # Se llama la función AnadirContenidoAlArchivo para guardar la información en el archivo
    archivo.AnadirContenidoAlArchivo(mensaje)


# Función para borrar la pantalla
def BorrarPantalla():
    # Se usa la función delete para borrar el texto actual en la pantalla
    info_text.delete('1.0', tk.END)


# Función para eliminar el archivo cuando se presiona el botón botonBorrarArchivo
def BorrarArchivo():
    # Se usa el objeto archivo y la función EliminarArchivo para eliminar el archivo del sistema
    archivo.EliminarArchivo()


# -----     Inicio del programa     -----#

# Variables y constantes
nombreArchivo = "datos_libros.txt"

# Matriz para almacenar por filas los libros y por columnas las caracteristicas
matrizLibros = []

# Se crea un objeto de la clase ManejoArchivo para manipular el archivo
archivo = ManejoArchivo()

# Se crea el archivo donde se guardarán los datos de la librería usando la función CrearArchivo del objeto archivo
archivo.CrearArchivo(nombreArchivo)

# Se crea la interfaz gráfica

# Crear una nueva ventana
ventana = tk.Tk()

# Se establece el título de la ventana
ventana.title("Inventario de libros")

# Se establece la geometría de la ventana
ventana.geometry("670x450+20+20")

# Esta etiqueta define el encabezado en la primera sección donde el administrador
# ingresará los libros en el archivo
etiquetaMensajeAdministrador = tk.Label(ventana, text="Espacio del administrador para ingresar libros")

# Se crean etiquetas para cada campo de ingreso

# Esta variable permite leer la categoria del libro a ingresar
categoriaLibro = tk.StringVar()

# Se crean las etiquetas y botones de radio para seleccionar el tipo de libro a ingresar
etiquetaCategoriaLibro1 = tk.Label(ventana, text="Categoria 1:")
botonesRadio1 = tk.Radiobutton(ventana, text="Ciencias", variable=categoriaLibro, value='LibroCiencias')

etiquetaCategoriaLibro2 = tk.Label(ventana, text="Categoria 2:")
botonesRadio2 = tk.Radiobutton(ventana, text="Humanidades", variable=categoriaLibro, value='LibroHumanidades')

etiquetaNombre = tk.Label(ventana, text="Nombre:")
etiquetaPrecio = tk.Label(ventana, text="Precio:")
etiquetaCantidad = tk.Label(ventana, text="Cantidad:")

# Se crean campos de entrada para cada característica de los libros
ingresoNombre = tk.Entry(ventana)
ingresoPrecio = tk.Entry(ventana)
ingresoCantidad = tk.Entry(ventana)

# Se crea un texto en la interfaz para mostrar la información del archivo
info_text = tk.Text(ventana, height=5)

# Creación de botones para las diferentes operaciones
botonGuardarArchivo = tk.Button(ventana, text="Guardar Datos", command=GuardarDatosLibro)
botonLeerArchivo = tk.Button(ventana, text="Leer Archivo", command=LeerArchivo)
botonBorrarArchivo = tk.Button(ventana, text="Eliminar Archivo", command=BorrarArchivo)
botonBorrarPantalla = tk.Button(ventana, text="Borrar Pantalla", command=BorrarPantalla)

# Se agrega una etiqueta para definir la compra de libros por parte del cliente
etiquetaParaComprarLibros = tk.Label(ventana, text="Espacio para comprar libros por parte del cliente")

# En esta sección ubicaremos los elementos en la interfaz de manera ordenada
# Estas variables nos permitirán definir la fila y columna donde pondremos los elementos en la interfaz
numeroFila = 0
columnaEtiquetas = 1
columnaEntradasTexto = 2

# Pondremos este elemento en la fila 1 con indice 0
etiquetaMensajeAdministrador.grid(row=numeroFila, column=0, columnspan=4, pady=5)

# Se usa el componente grid para colocar las etiquetas y campos de entrada de forma ordenada
numeroFila = numeroFila + 1
etiquetaCategoriaLibro1.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
botonesRadio1.grid(row=numeroFila, column=columnaEntradasTexto, sticky="W")

numeroFila = numeroFila + 1
etiquetaCategoriaLibro2.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
botonesRadio2.grid(row=numeroFila, column=columnaEntradasTexto, sticky="W")

numeroFila = numeroFila + 1
etiquetaNombre.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
ingresoNombre.grid(row=numeroFila, column=columnaEntradasTexto)

numeroFila = numeroFila + 1
etiquetaPrecio.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
ingresoPrecio.grid(row=numeroFila, column=columnaEntradasTexto)

numeroFila = numeroFila + 1
etiquetaCantidad.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
ingresoCantidad.grid(row=numeroFila, column=columnaEntradasTexto)

numeroFila = numeroFila + 1
info_text.grid(row=numeroFila, column=0, columnspan=4, padx=5, pady=5)

numeroFila = numeroFila + 1
botonGuardarArchivo.grid(row=numeroFila, column=0)
botonLeerArchivo.grid(row=numeroFila, column=1)
botonBorrarPantalla.grid(row=numeroFila, column=2)
botonBorrarArchivo.grid(row=numeroFila, column=3)

numeroFila = numeroFila + 1
etiquetaParaComprarLibros.grid(row=numeroFila, column=0, columnspan=4, pady=5)

# Se inicia el bucle principal
ventana.mainloop()
