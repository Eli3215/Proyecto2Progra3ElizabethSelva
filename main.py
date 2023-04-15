# Se importan las librerias
import tkinter as tk
from manejoArchivos import ManejoArchivo
from categoriaLibro import FabricaLibros

# Variables y constantes usadas en el programa
nombreArchivo = "datos_libros.txt"

# Variable tipo diccionario para almacenar el precio de venta actual
usuarios = {1: 0.0}

# Esta variable almacena el código del usuario actual con el que se almacenará en la variable usuarios
claveUsuarioActual = 1

# Matriz para almacenar por filas los libros y por columnas las caracteristicas
matrizLibros = []

# Se crea un objeto de la clase ManejoArchivo para manipular el archivo
archivo = ManejoArchivo()

# Se crea el archivo donde se guardarán los datos de la librería usando la función CrearArchivo del objeto archivo
archivo.CrearArchivo(nombreArchivo)


# Funciones que se llaman al presionar los botones en la interfaz

# Esta función permite retornar un mensaje para generar las ventas totales
# del proceso de compra en la librería
def MensajeVentasTotales():
    # Definición de variables que son definidas fuera de la función y que son globales
    global usuarios

    # Variable float para calcular el valor total de libros vendidos
    totalVendido = 0.0

    # Se genera el mensaje a mostrar en la etiqueta
    mensaje = "Ventas Totales\n"
    for usuario, valorFactura in usuarios.items():
        valorFacturaConImpuesto = valorFactura + ((valorFactura * 5.0) / 100.0)
        mensaje += f"{usuario}: {valorFacturaConImpuesto}\n"
        totalVendido += valorFacturaConImpuesto

    mensaje += f"Total: {totalVendido}"
    return mensaje


def ObtenerMatrizDesdeArchivo(texto):
    # Esta variable permite tener una lista con los libros que se encuentran almacenados en el archivo
    listaLibros = []

    # Esta variable permite almacenar los libros del archivo teniendo como filas cada libro
    # y como columnas cada caracteristica: código, nombre, categoria, precio, cantidad
    matriz = []

    # Como deseamos tener los datos de cada libro, primero
    # usamos el método split para obtener los datos de cada linea del archivo
    # y lo almacenamos en forma de lista o vector con las caracteristicas
    listaLibros = texto.split("\n")

    # Recorremos toda la lista de libros para obtener de cada uno las características
    for libro in listaLibros:

        # Usamos nuevamente el método split para buscar cada parámetro del libro
        # que esté separado por ; y lo almacenamos en la lista
        listaCaracteristicasLibro = libro.split(";")

        # Evaluamos si hay una lista de caracteristicas valida
        if len(listaCaracteristicasLibro) > 1:
            matriz.append(listaCaracteristicasLibro)

    return matriz


# Esta función permite retornar un mensaje que actualizará todos los registros de libros en el archivo
# a partir de la matriz ingresada a la función
def ObtenerMensajeDesdeMatriz(matriz):
    # Variable que contendrá el mensaje a ser retornado
    mensaje = ""

    for fila in matriz:
        (codigo, nombre, categora, precio, cantidad) = fila
        mensaje += f"{codigo};{nombre};{categora};{precio};{cantidad}\n"

    return mensaje


# Función para registrar la compra del libro en la factura de venta
def ComprarLibro():
    # Definición de variables que son definidas fuera de la función y que son globales
    global matrizLibros
    global catalogoLibros
    global textoFacturaVenta
    global textoFacturaVentaImpuestos
    global claveUsuarioActual
    global textoVentasTotales

    # Esta variable almacena la matriz modificada en el ciclo para luego actualizar la matriz original
    matrizTemporal = []

    # Se recuperan los libros disponibles de la matriz
    for fila in matrizLibros:

        # Se genera una tupla para obtener cada caracterista de la fila
        (codigo, nombre, categorai, precio, cantidad) = fila

        # Se comprueba primero si el usuario seleccionó un elemento de la lista para evitar errores
        if len(catalogoLibros.curselection()) > 0:
            codigoSelector = catalogoLibros.get(catalogoLibros.curselection())

            # Debido a que se devuelve un texto en la forma 1:quimica, se debe separar el texto y tomar solo el código
            # y para hacer eso usamos las siguientes instrucciones
            codigoSelector = codigoSelector.split(":")  # Obtenemos aqui una lista de la forma [1, quimica]
            codigoSelector = codigoSelector[0]  # Tomamos solo el primer elemento con índice 0

            # Se transforma la variable cantidad a int para comparar si hay libros disponibles
            cantidadLibros = int(cantidad)

            # Luego se compara si el código coincide con alguno de los libros leidos desde el archivo para calcular
            # la factura de venta con y sin impuestos
            if codigo == codigoSelector:

                # Se disminuye en 1 la cantidad de libros disponibles
                cantidadLibros = cantidadLibros - 1

                # Se calculan los valores de la factura
                usuarios[claveUsuarioActual] += float(precio)
                valorImpuestos = usuarios[claveUsuarioActual] + ((usuarios[claveUsuarioActual] * 5.0) / 100.0)

                # Se muestran los valores de la factura con y sin impuestos en la interfaz
                textoFacturaVenta.config(text="Valor factura: " + str(usuarios.get(claveUsuarioActual)))
                textoFacturaVentaImpuestos.config(text="Valor factura con impuestos: " + str(valorImpuestos))

                # Se verifica si hay libros disponibles para actualizar la matriz de libros, pero
                # si no hay se omiten para no guardar libros que no tengan disponibilidad
                if cantidadLibros > 0:
                    # Se actualiza la cantidad de libros para pasarlo a la matriz temporal
                    matrizTemporal.append([codigo, nombre, categorai, precio, cantidadLibros])

            else:
                matrizTemporal.append(fila)
        else:
            matrizTemporal = matrizLibros.copy()

        # Se copia la matriz temporal a la matriz principal para actualizar los registros
        matrizLibros = matrizTemporal.copy()

    # Se obtiene el mensaje para actualizar el archivo
    mensaje = ObtenerMensajeDesdeMatriz(matrizLibros)

    # Se borra el archivo para generarlo de nuevo ya que es más sencillo pasar
    # toda la información de la matriz que actualizar manualmente la posición dentro del
    # archivo
    archivo.EliminarArchivo()

    # Se llama la función AnadirContenidoAlArchivo para guardar la información en el archivo
    archivo.AnadirContenidoAlArchivo(mensaje)

    # Se llama la función para mostrar la cantidad de libros actualizada en la interfaz
    LeerArchivo()


# Esta función permite realizar una nueva venta poniendo la factura en 0
def FinalizarVenta():
    # Definición de variables que son definidas fuera de la función y que son globales
    global textoFacturaVenta
    global textoFacturaVentaImpuestos
    global usuarios
    global claveUsuarioActual

    # Se escriben las ventas totales realizadas por los clientes antes de ingresar uno nuevo
    mensajeVenta = MensajeVentasTotales()
    textoVentasTotales.config(text=mensajeVenta)

    # Se pasa a otro usuario solo si el valor de venta es > 0.0
    if usuarios[claveUsuarioActual] > 0.0:
        claveUsuarioActual += 1
        usuarios[claveUsuarioActual] = 0.0
        textoFacturaVenta.config(text="Valor factura: " + str(usuarios.get(claveUsuarioActual)))
        textoFacturaVentaImpuestos.config(text="Valor factura: " + str(usuarios.get(claveUsuarioActual)))


# Función para leer el contenido del archivo cuando se presiona el botón botonLeerArchivo
def LeerArchivo():
    # Definición de variables que son definidas fuera de la función y que son globales
    global matrizLibros
    global catalogoLibros
    global textoTablaLibros
    global archivo

    # Texto leido del archivo
    contenidoArchivo = archivo.LeerArchivo()

    # Se limpia el contenido de la matriz donde se almacena el contenido completo de los libros
    matrizLibros.clear()

    # Se limpia el selector de libros para agregar solo lo que esté disponible en la lectura del archivo
    catalogoLibros.delete(0, tk.END)

    matrizLibros = ObtenerMatrizDesdeArchivo(contenidoArchivo)

    # Se imprime el contenido del archivo de texto en la pantalla como una tabla
    textoTablaLibros.delete('1.0', tk.END)

    # Se inserta el encabezado de la tabla en pantalla
    textoTablaLibros.insert(tk.END, "codigo | nombre | categoria | precio | cantidad |")
    textoTablaLibros.insert(tk.END, "\n")

    # Se recorre la matriz de libros para mostrarla en pantalla
    for cont, fila in enumerate(matrizLibros):
        # Se genera una tupla para obtener cada caracterista de la fila
        (codigo, nombre, categorai, precio, cantidad) = fila

        catalogoLibros.insert(cont + 1, f"{codigo}:{nombre}")
        for columna in fila:
            textoTablaLibros.insert(tk.END, columna)
            textoTablaLibros.insert(tk.END, " | ")

        # Este comando nos permite pasar a la siguiente linea y no imprimir todo en la misma linea
        textoTablaLibros.insert(tk.END, "\n")


# Función para guardar el contenido del archivo cuando se presiona el botón botonGuardarArchivo
def GuardarDatosLibro():
    # Definición de variables que son definidas fuera de la función y que son globales
    global categoriaLibro
    global archivo
    global ingresoNombre
    global ingresoPrecio
    global ingresoCantidad
    global matrizLibros

    # Llamado a la clase que fabricará los libros de ciencias o humanidades de acuerdo a lo ingresado
    fabrica = FabricaLibros()

    # De la interfaz primero se obtiene la categoría del libro
    if (categoriaLibro.get() == 'LibroCiencias'):
        libro = fabrica.CrearLibro('LibroCiencias')
    elif (categoriaLibro.get() == 'LibroHumanidades'):
        libro = fabrica.CrearLibro('LibroHumanidades')
    else:
        print('Error de ingreso')

    # Se llama a la función LeerArchivo para actualizar la variable matrizLibros
    LeerArchivo()

    # Se crean estos vectores para evitar repetir codigos de las categorias existentes
    listaCodigos = [1]

    for fila in matrizLibros:
        # Se genera una tupla para obtener cada caracterista de la fila
        (codigo, nombre, categorai, precio, cantidad) = fila

        # Se convierte el código a int porque se lee como un str
        codigo = int(codigo)

        # Esta variable booleana permite definir si ya existe el codigo en la lista
        yaExisteElCodigo = False
        codigoMasAlto = 1

        for codigoLista in listaCodigos:

            # Se realiza la comparación para verificar si ya existe el código en la lista
            if codigo == codigoLista:
                yaExisteElCodigo = True
                codigoMasAlto = codigo

                # Se suma 1 al código más alto encontrado en la lista para evitar repetir
        if yaExisteElCodigo == True:
            listaCodigos.append(codigoMasAlto + 1)

    # En esta parte se selecciona el último código de la lista ya que esta se encuentra ordenada
    # y el último es el más actualizado para evitar repetir
    codigo = listaCodigos[-1]

    # Se obtienen los datos de los campos de ingreso y se almacenan en el objeto
    libro.EstablecerCodigo(codigo)
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

    # Se llama a la función LeerArchivo para actualizar la variable matrizLibros
    LeerArchivo()


# Función para borrar la pantalla
def BorrarPantalla():
    # Definición de variables que son definidas fuera de la función y que son globales
    global textoTablaLibros

    # Se usa la función delete para borrar el texto actual en la pantalla
    textoTablaLibros.delete('1.0', tk.END)


# Función para eliminar el archivo cuando se presiona el botón botonBorrarArchivo
def BorrarArchivo():
    # Definición de variables que son definidas fuera de la función y que son globales
    global archivo

    # Se usa el objeto archivo y la función EliminarArchivo para eliminar el archivo del sistema
    archivo.EliminarArchivo()

    # Se lee el archivo para actualizar la pantalla
    LeerArchivo()


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
textoTablaLibros.insert(tk.END, "codigo | nombre | categoria | precio | cantidad |")

# Creación de botones para las diferentes operaciones
botonGuardarArchivo = tk.Button(ventana, text="Guardar Datos", command=GuardarDatosLibro)
botonLeerArchivo = tk.Button(ventana, text="Leer Archivo", command=LeerArchivo)
botonBorrarArchivo = tk.Button(ventana, text="Eliminar Archivo", command=BorrarArchivo)
botonBorrarPantalla = tk.Button(ventana, text="Borrar Pantalla", command=BorrarPantalla)
botonComprar = tk.Button(ventana, text="Comprar Libro", command=ComprarLibro)
botonFinalizarVenta = tk.Button(ventana, text="Finalizar Venta", command=FinalizarVenta)

# Se agrega una etiqueta para definir la compra de libros por parte del cliente
etiquetaParaComprarLibros = tk.Label(ventana,
                                     text="Espacio para comprar libros por parte del cliente,\nseleccione el código para comprar libros y oprimir en el botón de comprar")

# Se presenta el catálogo de libros al cliente
catalogoLibros = tk.Listbox(ventana, height=5)

# Se crea un texto en la interfaz para mostrar el valor de la factura
textoFacturaVenta = tk.Label(ventana, text="Valor factura:")
textoFacturaVentaImpuestos = tk.Label(ventana, text="Valor factura con impuestos:")
textoVentasTotales = tk.Label(ventana, text="Ventas Totales")

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
botonFinalizarVenta.grid(row=numeroFila, column=2)

numeroFila = numeroFila + 1
textoVentasTotales.grid(row=numeroFila, column=0)
botonComprar.grid(row=numeroFila, column=1)
catalogoLibros.grid(row=numeroFila, column=2, pady=10)

numeroFila = numeroFila + 1
textoFacturaVenta.grid(row=numeroFila, column=2)

numeroFila = numeroFila + 1
textoFacturaVentaImpuestos.grid(row=numeroFila, column=2)

# Leer archivo para cargar pantalla con los datos iniciales
LeerArchivo()

# Se inicia el bucle principal de la interfaz
ventana.mainloop()
