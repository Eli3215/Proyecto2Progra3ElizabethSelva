# Se importan las librerias

import tkinter as tk
from manejoArchivos import ManejoArchivo

# Variables y constantes
nombreArchivo = "datos_libros.txt"

# Matriz para almacenar por filas los libros y por columnas las caracteristicas
matrizLibros = []


# Funciones que se activan al presionar los botones en la interfaz

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

    for fila in matrizLibros:
        for columna in fila:
            info_text.insert(tk.END, columna)
            info_text.insert(tk.END, " | ")

        info_text.insert(tk.END, "\n")


# Función para guardar el contenido del archivo cuando se presiona el botón botonGuardarArchivo
def GuardarDatosLibro():
    # Se obtienen los datos de los campos de ingreso
    codigo = ingresoCodigo.get()
    nombre = ingresoNombre.get()
    categoria = ingresoCategoria.get()
    precio = ingresoPrecio.get()
    cantidad = ingresoCantidad.get()

    # Se genera el texto a ser guardado en el archivo
    mensaje = f"{codigo};{nombre};{categoria};{precio};{cantidad}"

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
etiquetaMensajeAdministrador = tk.Label(ventana, text="Espacio para el administrador")

# Se crean etiquetas para cada campo de ingreso
etiquetaCodigo = tk.Label(ventana, text="Código:")
etiquetaNombre = tk.Label(ventana, text="Nombre:")
etiquetaCategoria = tk.Label(ventana, text="Categoría:")
etiquetaPrecio = tk.Label(ventana, text="Precio:")
etiquetaCantidad = tk.Label(ventana, text="Cantidad:")

# Se crean campos de entrada para cada característica de los libros
ingresoCodigo = tk.Entry(ventana)
ingresoNombre = tk.Entry(ventana)
ingresoCategoria = tk.Entry(ventana)
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

# Pondremos este elemento en la primera fila con indice 0
etiquetaMensajeAdministrador.grid(row=numeroFila, column=0, columnspan=4, pady=5)

# Se usa el componente grid para colocar las etiquetas y campos de entrada de forma ordenada
numeroFila = numeroFila + 1  # Pondremos estos elementos en la fila 2 con indice 1
etiquetaCodigo.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
ingresoCodigo.grid(row=numeroFila, column=columnaEntradasTexto)

numeroFila = numeroFila + 1  # Pondremos estos elementos en la fila 3 con indice 2
etiquetaNombre.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
ingresoNombre.grid(row=numeroFila, column=columnaEntradasTexto)

numeroFila = numeroFila + 1  # Pondremos estos elementos en la fila 4 con indice 3
etiquetaCategoria.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
ingresoCategoria.grid(row=numeroFila, column=columnaEntradasTexto)

numeroFila = numeroFila + 1  # Pondremos estos elementos en la fila 5 con indice 4
etiquetaPrecio.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
ingresoPrecio.grid(row=numeroFila, column=columnaEntradasTexto)

numeroFila = numeroFila + 1  # Pondremos estos elementos en la fila 6 con indice 5
etiquetaCantidad.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
ingresoCantidad.grid(row=numeroFila, column=columnaEntradasTexto)

numeroFila = numeroFila + 1  # Pondremos estos elementos en la fila 7 con indice 6
info_text.grid(row=numeroFila, column=0, columnspan=4, padx=5, pady=5)

numeroFila = numeroFila + 1  # Pondremos estos elementos en la fila 8 con indice 7
botonGuardarArchivo.grid(row=numeroFila, column=0)
botonLeerArchivo.grid(row=numeroFila, column=1)
botonBorrarPantalla.grid(row=numeroFila, column=2)
botonBorrarArchivo.grid(row=numeroFila, column=3)

numeroFila = numeroFila + 1  # Pondremos estos elementos en la fila 9 con indice 8
etiquetaParaComprarLibros.grid(row=numeroFila, column=0, columnspan=4, pady=5)

# Se inicia el bucle principal
ventana.mainloop()