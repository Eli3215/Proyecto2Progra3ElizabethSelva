# Se importan las librerias

import tkinter as tk

from manejoArchivos import ManejoArchivo
from categoriaLibro import FabricaLibros

# Variables y constantes usadas en el programa
nombreArchivo = "datos_libros.txt"

# Variable tipo diccionario para almacenar el precio de venta actual
usuarios = {1: 0.0}

# Matriz para almacenar por filas los libros y por columnas las caracteristicas
matrizLibros = []

# Se crea un objeto de la clase ManejoArchivo para manipular el archivo
archivo = ManejoArchivo()

# Se crea el archivo donde se guardarán los datos de la librería usando la función CrearArchivo del objeto archivo
archivo.CrearArchivo(nombreArchivo)


# Funciones que se llaman al presionar los botones en la interfaz

# Función para registrar la compra del libro en la factura de venta
def ComprarLibro():
    # Se recuperan los libros disponibles de la matriz
    for fila in matrizLibros:

        # Se genera una tupla para obtener cada caracterista de la fila
        (codigo, nombre, categorai, precio, cantidad) = fila

        # Se comprueba primero si el usuario seleccionó un elemento de la lista para evitar errores
        if len(catalogoLibros.curselection()) > 0:
            codigoSelector = catalogoLibros.get(catalogoLibros.curselection())

            # Luego se compara si el código coincide con alguno de los libros leidos desde el archivo para calcular
            # la factura de venta con y sin impuestos
            if codigo == codigoSelector:
                # Se calculan los valores de la factura
                usuarios[1] += float(precio)
                valorImpuestos = usuarios[1] + ((usuarios[1] * 5.0) / 100.0)

                # Se muestran los valores de la factura con y sin impuestos en la interfaz
                textoFacturaVenta.config(text="Valor factura: " + str(usuarios.get(1)))
                textoFacturaVentaImpuestos.config(text="Valor factura con impuestos: " + str(valorImpuestos))


# Esta función permite realizar una nueva venta poniendo la factura en 0
def NuevaVenta():
    # Se reinicia el valor de factura
    usuarios[1] = 0.0
    textoFacturaVenta.config(text="Valor factura: " + str(usuarios.get(1)))
    textoFacturaVentaImpuestos.config(text="Valor factura: " + str(usuarios.get(1)))


# Función para leer el contenido del archivo cuando se presiona el botón botonLeerArchivo
def LeerArchivo():
    # Texto leido del archivo
    mensaje = archivo.LeerArchivo()

    # Se limpia el contenido de la matriz donde se almacena el contenido completo de los libros
    matrizLibros.clear()

    # Se limpia el selector de libros para agregar solo lo que esté disponible en la lectura del archivo
    catalogoLibros.delete(0, tk.END)

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
    textoTablaLibros.delete('1.0', tk.END)

    # Se inserta el encabezado de la tabla en pantalla
    textoTablaLibros.insert(tk.END, "codigo | nombre | categoria | precio | cantidad |")
    textoTablaLibros.insert(tk.END, "\n")

    # Se recorre la matriz de libros para mostrarla en pantalla
    for cont, fila in enumerate(matrizLibros):
        catalogoLibros.insert(cont + 1, fila[0])
        for columna in fila:
            textoTablaLibros.insert(tk.END, columna)
            textoTablaLibros.insert(tk.END, " | ")

        # Este comando nos permite pasar a la siguiente linea y no imprimir todo en la misma linea
        textoTablaLibros.insert(tk.END, "\n")


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

    # Se retorna el mensaje completo con todas las caracteristicas del libro
    mensaje = libro.RetornarCaracteristicasLibro()

    # Se llama la función AnadirContenidoAlArchivo para guardar la información en el archivo
    archivo.AnadirContenidoAlArchivo(mensaje)

    # Se limpian los campos en la interfaz
    ingresoNombre.delete(0, tk.END)
    ingresoPrecio.delete(0, tk.END)
    ingresoCantidad.delete(0, tk.END)


# Función para borrar la pantalla
def BorrarPantalla():
    # Se usa la función delete para borrar el texto actual en la pantalla
    textoTablaLibros.delete('1.0', tk.END)


# Función para eliminar el archivo cuando se presiona el botón botonBorrarArchivo
def BorrarArchivo():
    # Se usa el objeto archivo y la función EliminarArchivo para eliminar el archivo del sistema
    archivo.EliminarArchivo()


# -----     Inicio del programa     -----#

# Se crea la interfaz gráfica

# Crear una nueva ventana
ventana = tk.Tk()

# Se establece el título de la ventana
ventana.title("Inventario de libros")

# Se establece la geometría de la ventana
ventana.geometry("670x580+20+20")

# Esta etiqueta define el encabezado en la primera sección donde el administrador
# ingresará los libros en el archivo
etiquetaMensajeAdministrador = tk.Label(ventana, text="Espacio del administrador para ingresar libros")

# Se crean etiquetas para cada campo de ingreso

# Esta variable permite leer la categoria del libro a ingresar
categoriaLibro = tk.StringVar()

# Se crean las etiquetas y botones de radio para seleccionar el tipo de libro a ingresar
etiquetaCategoriaLibro1 = tk.Label(ventana, text="Categoria 1:")
botonRadio1 = tk.Radiobutton(ventana, text="Ciencias", variable=categoriaLibro, value='LibroCiencias')
botonRadio1.select()

etiquetaCategoriaLibro2 = tk.Label(ventana, text="Categoria 2:")
botonRadio2 = tk.Radiobutton(ventana, text="Humanidades", variable=categoriaLibro, value='LibroHumanidades')

# Se crean etiquetas para ingresar nombre, precio y cantidad de libros
etiquetaNombre = tk.Label(ventana, text="Nombre:")
etiquetaPrecio = tk.Label(ventana, text="Precio:")
etiquetaCantidad = tk.Label(ventana, text="Cantidad:")

# Se crean campos de entrada para cada característica de los libros
ingresoNombre = tk.Entry(ventana)
ingresoPrecio = tk.Entry(ventana)
ingresoCantidad = tk.Entry(ventana)

# Se crea un texto en la interfaz para mostrar la información del archivo
textoTablaLibros = tk.Text(ventana, height=5)

# Creación de botones para las diferentes operaciones
botonGuardarArchivo = tk.Button(ventana, text="Guardar Datos", command=GuardarDatosLibro)
botonLeerArchivo = tk.Button(ventana, text="Leer Archivo", command=LeerArchivo)
botonBorrarArchivo = tk.Button(ventana, text="Eliminar Archivo", command=BorrarArchivo)
botonBorrarPantalla = tk.Button(ventana, text="Borrar Pantalla", command=BorrarPantalla)
botonComprar = tk.Button(ventana, text="Comprar Libro", command=ComprarLibro)
botonNuevaVenta = tk.Button(ventana, text="Nueva Venta", command=NuevaVenta)

# Se agrega una etiqueta para definir la compra de libros por parte del cliente
etiquetaParaComprarLibros = tk.Label(ventana,
                                     text="Espacio para comprar libros por parte del cliente,\nseleccione el código para comprar libros y oprimir en el botón de comprar")

# Se presenta el catálogo de libros al cliente
catalogoLibros = tk.Listbox(ventana, height=5)

# Se crea un texto en la interfaz para mostrar el valor de la factura
textoFacturaVenta = tk.Label(ventana, text="Valor factura:")
textoFacturaVentaImpuestos = tk.Label(ventana, text="Valor factura con impuestos:")

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
botonRadio1.grid(row=numeroFila, column=columnaEntradasTexto, sticky="W")

numeroFila = numeroFila + 1
etiquetaCategoriaLibro2.grid(row=numeroFila, column=columnaEtiquetas, sticky="E")
botonRadio2.grid(row=numeroFila, column=columnaEntradasTexto, sticky="W")

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
botonGuardarArchivo.grid(row=numeroFila, column=1, sticky="E")
botonBorrarArchivo.grid(row=numeroFila, column=2, sticky="W")

numeroFila = numeroFila + 1
etiquetaParaComprarLibros.grid(row=numeroFila, column=0, columnspan=4, pady=5)

numeroFila = numeroFila + 1
textoTablaLibros.grid(row=numeroFila, column=0, columnspan=4, padx=5, pady=5)

numeroFila = numeroFila + 1
botonLeerArchivo.grid(row=numeroFila, column=0, sticky="E")
botonBorrarPantalla.grid(row=numeroFila, column=1, sticky="W")
botonNuevaVenta.grid(row=numeroFila, column=2)

numeroFila = numeroFila + 1
botonComprar.grid(row=numeroFila, column=1)
catalogoLibros.grid(row=numeroFila, column=2, pady=10)

numeroFila = numeroFila + 1
textoFacturaVenta.grid(row=numeroFila, column=2)

numeroFila = numeroFila + 1
textoFacturaVentaImpuestos.grid(row=numeroFila, column=2)

# Se inicia el bucle principal de la interfaz
ventana.mainloop()
