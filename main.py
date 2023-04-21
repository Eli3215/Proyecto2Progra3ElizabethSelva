# Se importan las librerias
import tkinter as tk
from manejoArchivos import ManejoArchivo
from categoriaLibro import FabricaLibros
from funciones import GenerarElementosGuardarLibro, BuscarCodigoMasAlto, MensajeVentasTotales, \
    ObtenerMatrizDesdeArchivo, ObtenerMensajeDesdeMatriz, GenerarElementosLeerLibros, GenerarElementosComprarLibros, \
    GenerarElementosMostrarVentasTotales

# Variable tipo diccionario para almacenar numero de usuario como clave y compra total como valor tipo float
usuarios = {1: 0.0}

# Esta variable almacena el código del usuario actual con el que se almacenará en el diccionario de usuarios
claveUsuarioActual = 1

# Matriz para almacenar por filas los libros y por columnas las caracteristicas de los libros
matrizLibros = []

# Se crea un objeto de la clase ManejoArchivo para manipular el archivo
archivo = ManejoArchivo()

# Nombre del archivo
nombreArchivo = "datos_libros.txt"

# Se crea el archivo donde se guardarán los datos de la librería usando la función CrearArchivo del objeto archivo
archivo.CrearArchivo(nombreArchivo)


# Funciones que se llaman al presionar los botones en la interfaz

# Esta función permite actualizar el catálogo para compras en la interfaz
def ActualizarCatalogoParaCompra():
    # Definición de variables que son definidas fuera de la función y que son globales
    global catalogoLibros
    global archivo
    global matrizLibros

    # Se limpia el selector de libros para agregar solo lo que esté disponible en la lectura del archivo
    catalogoLibros.delete(0, tk.END)

    # Texto leido del archivo
    contenidoArchivo = archivo.LeerArchivo()

    # Se limpia el contenido de la matriz donde se almacena el contenido completo de los libros
    matrizLibros.clear()

    # Se llama a la función ObtenerMatrizDesdeArchivo para leer el contenido del archivo y actualizar
    # la matrizLibros que contiene todas las caracteristicas de los libros almacenadas en el archivo
    matrizLibros = ObtenerMatrizDesdeArchivo(contenidoArchivo)

    # Se recorre toda la matriz por filas ya que cada fila corresponde a un libro ingresado
    cont = 1
    for fila in matrizLibros:
        # Se genera una tupla para obtener cada caracterista de la fila
        (codigo, nombre, categorai, precio, cantidad) = fila

        # Se ingresan los códigos, nombre y cantidad de libros al catálogo de libro que luego el usuario seleccionará para comprar
        catalogoLibros.insert(cont, f"{codigo}:{nombre}:{cantidad}")

        # Se incrementa el contador de elementos para ingresar en el catálogo
        cont += 1


# Esta función permite visualizar las ventas totales realizadas
def MostrarInterfazVentasTotales():
    # Definición de variables que son definidas fuera de la función y que son globales
    global contenedorGuardarLibros
    global contenedorMostrarLibros
    global contenedorComprarLibros
    global contenedorVentasTotales
    global textoVentasTotales
    global usuarios

    # Se muestra el contenedor respectivo y se oculta el resto
    contenedorMostrarLibros.pack_forget()
    contenedorComprarLibros.pack_forget()
    contenedorVentasTotales.pack()
    contenedorGuardarLibros.pack_forget()

    # Se escriben las ventas totales de todos los usuarios
    mensajeVenta = MensajeVentasTotales(usuarios)
    textoVentasTotales.config(text=mensajeVenta)


# Esta función permite mostrar solo el contenedor donde están todos los elementos para guardar libros en el inventario
def MostrarInterfazGuardar():
    # Definición de variables que son definidas fuera de la función y que son globales
    global contenedorGuardarLibros
    global contenedorMostrarLibros
    global contenedorComprarLibros
    global contenedorVentasTotales

    # Se muestra el contenedor respectivo y se oculta el resto
    contenedorMostrarLibros.pack_forget()
    contenedorComprarLibros.pack_forget()
    contenedorVentasTotales.pack_forget()
    contenedorGuardarLibros.pack()


# Esta función permite mostrar solo el contenedor donde están todos los elementos para comprar libros
def MostrarInterfazComprar():
    # Definición de variables que son definidas fuera de la función y que son globales
    global contenedorGuardarLibros
    global contenedorMostrarLibros
    global contenedorComprarLibros
    global contenedorVentasTotales

    # Se muestra el contenedor respectivo y se oculta el resto
    contenedorMostrarLibros.pack_forget()
    contenedorGuardarLibros.pack_forget()
    contenedorVentasTotales.pack_forget()
    contenedorComprarLibros.pack()

    # Permite actualizar la vista del catálogo para evitar comprar libros que ya no tengan inventario
    ActualizarCatalogoParaCompra()


# Función para guardar un libro en el inventario
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

    # De la interfaz primero se obtiene la categoría del libro a partir de los botones de radio
    if (categoriaLibro.get() == 'LibroCiencias'):
        libro = fabrica.CrearLibro('LibroCiencias')
    elif (categoriaLibro.get() == 'LibroHumanidades'):
        libro = fabrica.CrearLibro('LibroHumanidades')
    else:
        print('Error de ingreso')

    # Texto leido del archivo usando el objeto que controla el archivo
    contenidoArchivo = archivo.LeerArchivo()

    # Se llama a la función ObtenerMatrizDesdeArchivo para leer el contenido del archivo y actualizar
    # la matrizLibros que contiene todas las caracteristicas de los libros almacenadas en el archivo
    matrizLibros = ObtenerMatrizDesdeArchivo(contenidoArchivo)

    # Se llama a la función BuscarCodigoMasAlto para encontrar el código siguiente en el ingreso
    # y evitar repetir ya que en la compra se pueden generar errores con códigos repetidos
    codigo = BuscarCodigoMasAlto(matrizLibros)

    # Se obtienen los datos de los campos de ingreso y se almacenan en el objeto
    libro.EstablecerCodigo(codigo)
    libro.EstablecerNombre(ingresoNombre.get())
    libro.EstablecerPrecio(ingresoPrecio.get())
    libro.EstablecerCantidad(ingresoCantidad.get())

    # Se retorna el mensaje completo con todas las caracteristicas del libro
    mensaje = libro.RetornarCaracteristicasLibro()

    # Se llama la función AnadirContenidoAlArchivo para guardar la información en el archivo
    archivo.AnadirContenidoAlArchivo(mensaje)

    # Se limpian los campos en la interfaz para agregar nuevos valores
    ingresoNombre.delete(0, tk.END)
    ingresoPrecio.delete(0, tk.END)
    ingresoCantidad.delete(0, tk.END)


# Función para eliminar el archivo del sistema
def BorrarArchivo():
    # Definición de variables que son definidas fuera de la función y que son globales
    global archivo
    global contenedorGuardarLibros
    global contenedorMostrarLibros
    global contenedorComprarLibros
    global contenedorVentasTotales

    # Se ocultan todos los contenedores
    contenedorMostrarLibros.pack_forget()
    contenedorGuardarLibros.pack_forget()
    contenedorComprarLibros.pack_forget()
    contenedorVentasTotales.pack_forget()

    # Se usa el objeto archivo y la función EliminarArchivo para eliminar el archivo del sistema
    archivo.EliminarArchivo()


# Función para leer el contenido del archivo
def LeerArchivo():
    # Definición de variables que son definidas fuera de la función y que son globales
    global matrizLibros
    global textoTablaLibros
    global archivo
    global contenedorGuardarLibros
    global contenedorMostrarLibros
    global contenedorComprarLibros
    global contenedorVentasTotales

    # Se muestra el contenedor respectivo y se oculta el resto
    contenedorMostrarLibros.pack()
    contenedorGuardarLibros.pack_forget()
    contenedorComprarLibros.pack_forget()
    contenedorVentasTotales.pack_forget()

    # Texto leido del archivo
    contenidoArchivo = archivo.LeerArchivo()

    # Se limpia el contenido de la matriz donde se almacena el contenido completo de los libros
    matrizLibros.clear()

    # A partir del texto leido desde el archivo se genera la matriz de libros y caracteristicas
    matrizLibros = ObtenerMatrizDesdeArchivo(contenidoArchivo)

    # Se elimina el contenido inicial del texto donde se imprime la tabla de libros
    textoTablaLibros.delete('1.0', tk.END)

    # Se inserta el encabezado de la tabla en pantalla en el componente de texto
    textoTablaLibros.insert(tk.END, "codigo | nombre | categoria | precio | cantidad |")
    textoTablaLibros.insert(tk.END, "\n")

    # Se recorre la matriz de libros para mostrarla en pantalla en el campo de texto
    # Primero se extraen las filas
    for fila in matrizLibros:
        # Aqui se recorren las columnas
        for columna in fila:
            # Se imprime en el campo de texto cada caracteristica separada por |
            textoTablaLibros.insert(tk.END, columna)
            textoTablaLibros.insert(tk.END, " | ")

        # Este comando nos permite pasar a la siguiente linea y no imprimir todo en la misma linea
        textoTablaLibros.insert(tk.END, "\n")


# Función para registrar la compra del libro
def ComprarLibro():
    # Definición de variables que son definidas fuera de la función y que son globales
    global matrizLibros
    global catalogoLibros
    global textoFacturaVenta
    global textoFacturaVentaImpuestos
    global claveUsuarioActual
    global usuarios

    # Esta variable almacena la matriz modificada en el ciclo para luego actualizar la matriz original
    matrizTemporal = []

    # Se recuperan los libros disponibles de la matriz
    for fila in matrizLibros:

        # Se genera una tupla para obtener cada caracterista del libro
        (codigo, nombre, categorai, precio, cantidad) = fila

        # Se comprueba primero si el usuario seleccionó un elemento de la lista para evitar errores
        if len(catalogoLibros.curselection()) > 0:

            # Se toma del catálogo presentado en la interfaz la opción para comprar libro
            codigoSelector = catalogoLibros.get(catalogoLibros.curselection())

            # Debido a que se devuelve un texto en la forma 1:quimica:2, se debe separar el texto y tomar solo el código
            # y para hacer eso usamos las siguientes instrucciones
            codigoSelector = codigoSelector.split(":")  # Obtenemos aqui una lista de la forma [1, quimica, 2]
            codigoSelector = codigoSelector[0]  # Tomamos solo el primer elemento con índice 0

            # Se transforma la variable cantidad a int para comparar si hay libros disponibles como valores enteros
            cantidadLibros = int(cantidad)

            # Se compara si el código coincide con alguno de los libros leidos desde el archivo para calcular
            # la factura de venta con y sin impuestos
            if codigo == codigoSelector:

                # Se disminuye en 1 la cantidad de libros disponibles
                cantidadLibros = cantidadLibros - 1

                # Se aumenta el valor de pago para la factura para el cliente actual
                usuarios[claveUsuarioActual] += float(precio)

                # Se calcula el valor con impuestos del 5%
                valorImpuestos = usuarios[claveUsuarioActual] + ((usuarios[claveUsuarioActual] * 5.0) / 100.0)

                # Se muestran los valores de la factura con y sin impuestos en la interfaz en las etiquetas
                textoFacturaVenta.config(text="Valor factura: " + str(usuarios.get(claveUsuarioActual)))
                textoFacturaVentaImpuestos.config(text="Valor factura con impuestos: " + str(valorImpuestos))

                # Se verifica si hay libros disponibles para actualizar la matriz de libros, pero
                # si no hay se omiten para no guardar libros que no tengan disponibilidad
                if cantidadLibros > 0:
                    # Se actualiza la cantidad de libros para pasarlo a la matriz temporal
                    matrizTemporal.append([codigo, nombre, categorai, precio, cantidadLibros])
            else:
                matrizTemporal.append(fila)

        # Esta opción evita que se genere un error cuando no se seleccionan libros en el catálogo
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

    # Se llama la función AnadirContenidoAlArchivo para guardar la información en el archivo como texto poniendo cada libro en una nueva linea
    archivo.AnadirContenidoAlArchivo(mensaje)

    # Se llama a la función que actualiza el catálogo de compra
    ActualizarCatalogoParaCompra()


# Esta función permite realizar una nueva venta
def FinalizarVenta():
    # Definición de variables que son definidas fuera de la función y que son globales
    global textoFacturaVenta
    global textoFacturaVentaImpuestos
    global usuarios
    global claveUsuarioActual

    # Se pasa a otro usuario solo si el valor de venta es > 0.0 y se restauran los valores de las etiquetas a su valor inicial
    if usuarios[claveUsuarioActual] > 0.0:
        claveUsuarioActual += 1
        usuarios[claveUsuarioActual] = 0.0
        textoFacturaVenta.config(text="Valor factura: " + str(usuarios.get(claveUsuarioActual)))
        textoFacturaVentaImpuestos.config(text="Valor factura: " + str(usuarios.get(claveUsuarioActual)))


# -----     Inicio del programa     -----#

# Se crea la interfaz gráfica

# Se crea la ventana principal
ventana = tk.Tk()

# Se establece el título de la ventana
ventana.title("Inventario de libros")

# Se establece la geometría de la ventana
ventana.geometry("670x450+20+20")

# Esta etiqueta define el mensaje del menú
etiquetaMensajeMenu = tk.Label(ventana, text="Menú de opciones")

# Pondremos este elemento en la primera fila
etiquetaMensajeMenu.pack()

# Creación de contenedor de botones del menú
contenedorBotonesMenu = tk.Frame(ventana)
contenedorBotonesMenu.pack()

# Se generan los elementos en la interfaz con la función GenerarElementosGuardarLibro y se retornan los
# elementos creados en una tupla para ser usados posteriormente en el programa como variables globales
(contenedorGuardarLibros, categoriaLibro, botonRadio1, botonRadio2, ingresoNombre, ingresoPrecio, ingresoCantidad,
 botonGuardarArchivo) = GenerarElementosGuardarLibro(ventana)

# Se configura la función a ser llamada por el botón de guardar que se encuentra dentro de contenedorGuardarLibros
botonGuardarArchivo.config(command=GuardarDatosLibro)

# Se generan los elementos en la interfaz con la función GenerarElementosLeerLibros para el proceso de mostrar el inventario
#  y se retornan los elementos creados en una tupla para ser usados posteriormente en el programa como variables globales
(contenedorMostrarLibros, textoTablaLibros) = GenerarElementosLeerLibros(ventana)

# Se generan los elementos en la interfaz con la función GenerarElementosComprarLibros para el proceso de compra
#  y se retornan los elementos creados en una tupla para ser usados posteriormente en el programa como variables globales
(contenedorComprarLibros, catalogoLibros, textoFacturaVenta, textoFacturaVentaImpuestos, botonComprar,
 botonFinalizarVenta) = GenerarElementosComprarLibros(ventana)

# Se configuran las funciones a ser llamadas al presionar los botones
botonComprar.config(command=ComprarLibro)
botonFinalizarVenta.config(command=FinalizarVenta)

# Se generan los elementos en la interfaz con la función GenerarElementosMostrarVentasTotales para el proceso de compras
#  y se retornan los elementos creados en una tupla para ser usados posteriormente en el programa como variables globales
(contenedorVentasTotales, textoVentasTotales) = GenerarElementosMostrarVentasTotales(ventana)

# Creación de botones para realizar acciones sobre la interfaz
botonMostrarProcesoGuardar = tk.Button(contenedorBotonesMenu, text="Guardar Libros Inventario",
                                       command=MostrarInterfazGuardar)
botonMostrarProcesoLeer = tk.Button(contenedorBotonesMenu, text="Mostrar Libros Inventario", command=LeerArchivo)
botonMostrarProcesoComprar = tk.Button(contenedorBotonesMenu, text="Comprar Libros", command=MostrarInterfazComprar)
botonComprasTotales = tk.Button(contenedorBotonesMenu, text="Mostrar Ventas Totales",
                                command=MostrarInterfazVentasTotales)
botonBorrarArchivo = tk.Button(contenedorBotonesMenu, text="Eliminar Archivo", command=BorrarArchivo)
botonSalir = tk.Button(contenedorBotonesMenu, text="Salir de la Aplicación", command=ventana.destroy)

# Se organizan los botones en la interfaz
botonMostrarProcesoGuardar.pack()
botonMostrarProcesoLeer.pack()
botonMostrarProcesoComprar.pack()
botonComprasTotales.pack()
botonBorrarArchivo.pack()
botonSalir.pack()

# Se inicia el bucle principal de la interfaz
ventana.mainloop()
