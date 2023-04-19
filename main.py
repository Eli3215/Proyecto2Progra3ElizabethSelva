# Se importan las librerias
import tkinter as tk
from manejoArchivos import ManejoArchivo
from categoriaLibro import FabricaLibros
from funciones import GenerarElementosGuardarLibro, BuscarCodigoMasAlto, MensajeVentasTotales, \
    ObtenerMatrizDesdeArchivo, ObtenerMensajeDesdeMatriz, GenerarElementosLeerLibros, GenerarElementosComprarLibros

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

# Esta función permite actualizar el catálogo para compras en la interfaz
def ActualizarCatalogoParaCompra():
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

    cont = 0
    for fila in matrizLibros:
        cont += 1
        # Se genera una tupla para obtener cada caracterista de la fila
        (codigo, nombre, categorai, precio, cantidad) = fila
        catalogoLibros.insert(cont, f"{codigo}:{nombre}:{cantidad}")


# Esta función permite mostrar solo el contenedor donde están todos los elementos para guardar libros en el inventario
def MostrarInterfazGuardar():
    # Definición de variables que son definidas fuera de la función y que son globales
    global contenedorGuardarLibros
    global contenedorMostrarLibros
    global contenedorComprarLibros

    # Se muestra el contenedor respectivo y se oculta el resto
    contenedorMostrarLibros.pack_forget()
    contenedorComprarLibros.pack_forget()
    contenedorGuardarLibros.pack()


# Esta función permite mostrar solo el contenedor donde están todos los elementos para comprar libros
def MostrarInterfazComprar():
    # Definición de variables que son definidas fuera de la función y que son globales
    global contenedorGuardarLibros
    global contenedorMostrarLibros
    global contenedorComprarLibros

    # Se muestra el contenedor respectivo y se oculta el resto
    contenedorMostrarLibros.pack_forget()
    contenedorGuardarLibros.pack_forget()
    contenedorComprarLibros.pack()

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

    # De la interfaz primero se obtiene la categoría del libro
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
    # y evitar repetir
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

    # Se limpian los campos en la interfaz
    ingresoNombre.delete(0, tk.END)
    ingresoPrecio.delete(0, tk.END)
    ingresoCantidad.delete(0, tk.END)


# Función para eliminar el archivo cuando se presiona el botón botonBorrarArchivo
def BorrarArchivo():
    # Definición de variables que son definidas fuera de la función y que son globales
    global archivo
    global contenedorGuardarLibros
    global contenedorMostrarLibros
    global contenedorComprarLibros

    # Se muestra el contenedor respectivo y se oculta el resto
    contenedorMostrarLibros.pack_forget()
    contenedorGuardarLibros.pack_forget()
    contenedorComprarLibros.pack_forget()

    # Se usa el objeto archivo y la función EliminarArchivo para eliminar el archivo del sistema
    archivo.EliminarArchivo()


# Función para leer el contenido del archivo cuando se presiona el botón botonLeerArchivo
def LeerArchivo():
    # Definición de variables que son definidas fuera de la función y que son globales
    global matrizLibros
    global textoTablaLibros
    global archivo
    global contenedorGuardarLibros
    global contenedorMostrarLibros
    global contenedorComprarLibros

    # Se muestra el contenedor respectivo y se oculta el resto
    contenedorMostrarLibros.pack()
    contenedorGuardarLibros.pack_forget()
    contenedorComprarLibros.pack_forget()

    # Texto leido del archivo
    contenidoArchivo = archivo.LeerArchivo()

    # Se limpia el contenido de la matriz donde se almacena el contenido completo de los libros
    matrizLibros.clear()

    matrizLibros = ObtenerMatrizDesdeArchivo(contenidoArchivo)

    # Se imprime el contenido del archivo de texto en la pantalla como una tabla
    textoTablaLibros.delete('1.0', tk.END)

    # Se inserta el encabezado de la tabla en pantalla
    textoTablaLibros.insert(tk.END, "codigo | nombre | categoria | precio | cantidad |")
    textoTablaLibros.insert(tk.END, "\n")

    # Se recorre la matriz de libros para mostrarla en pantalla
    cont = 0
    for fila in matrizLibros:
        for columna in fila:
            textoTablaLibros.insert(tk.END, columna)
            textoTablaLibros.insert(tk.END, " | ")

        # Este comando nos permite pasar a la siguiente linea y no imprimir todo en la misma linea
        textoTablaLibros.insert(tk.END, "\n")


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

    # Se llama a la función que actualiza el catálogo de compra
    ActualizarCatalogoParaCompra()


# Esta función permite realizar una nueva venta poniendo la factura en 0
def FinalizarVenta():
    # Definición de variables que son definidas fuera de la función y que son globales
    global textoFacturaVenta
    global textoFacturaVentaImpuestos
    global usuarios
    global claveUsuarioActual

    # Se escriben las ventas totales realizadas por los clientes antes de ingresar uno nuevo
    mensajeVenta = MensajeVentasTotales(usuarios)
    textoVentasTotales.config(text=mensajeVenta)

    # Se pasa a otro usuario solo si el valor de venta es > 0.0
    if usuarios[claveUsuarioActual] > 0.0:
        claveUsuarioActual += 1
        usuarios[claveUsuarioActual] = 0.0
        textoFacturaVenta.config(text="Valor factura: " + str(usuarios.get(claveUsuarioActual)))
        textoFacturaVentaImpuestos.config(text="Valor factura: " + str(usuarios.get(claveUsuarioActual)))


# -----     Inicio del programa     -----#

# Se crea la interfaz gráfica

# Crear una nueva ventana
ventana = tk.Tk()

# Se establece el título de la ventana
ventana.title("Inventario de libros")

# Se establece la geometría de la ventana
ventana.geometry("670x580+20+20")

# Esta etiqueta define el mensaje del menú
etiquetaMensajeMenu = tk.Label(ventana, text="Menú de opciones")

# Pondremos este elemento en la primera fila
etiquetaMensajeMenu.pack()

# Creación de contenedor de botones del menú
contenedorBotonesMenu = tk.Frame(ventana)
contenedorBotonesMenu.pack()

# Se generan los elementos en la interfaz con la función GenerarElementosGuardarLibro y se retornan los
# elementos creados en una tupla para ser usados posteriormente en el programa
(contenedorGuardarLibros, categoriaLibro, botonRadio1, botonRadio2, ingresoNombre, ingresoPrecio, ingresoCantidad,
 botonGuardarArchivo) = GenerarElementosGuardarLibro(ventana)

# Se configura la función a ser llamada por el botón de guardar que se encuentra dentro de contenedorGuardarLibros
botonGuardarArchivo.config(command=GuardarDatosLibro)

# Se generan los elementos en la interfaz con la función GenerarElementosLeerLibros para el proceso de mostrar el inventario
#  y se retornan los elementos creados en una tupla para ser usados posteriormente en el programa
(contenedorMostrarLibros, textoTablaLibros) = GenerarElementosLeerLibros(ventana)

# Se generan los elementos en la interfaz con la función GenerarElementosComprarLibros para el proceso de compra
#  y se retornan los elementos creados en una tupla para ser usados posteriormente en el programa
(contenedorComprarLibros, catalogoLibros, textoFacturaVenta, textoFacturaVentaImpuestos, textoVentasTotales,
 botonComprar, botonFinalizarVenta) = GenerarElementosComprarLibros(ventana)

# Se configuran las funciones a ser llamadas al presionar los botones
botonComprar.config(command=ComprarLibro)
botonFinalizarVenta.config(command=FinalizarVenta)

# Creación de botones para realizar acciones sobre la interfaz
botonMostrarProcesoGuardar = tk.Button(contenedorBotonesMenu, text="Guardar Libros Inventario",
                                       command=MostrarInterfazGuardar)
botonMostrarProcesoLeer = tk.Button(contenedorBotonesMenu, text="Mostrar Libros Inventario", command=LeerArchivo)
botonMostrarProcesoComprar = tk.Button(contenedorBotonesMenu, text="Comprar Libros", command=MostrarInterfazComprar)
botonBorrarArchivo = tk.Button(contenedorBotonesMenu, text="Eliminar Archivo", command=BorrarArchivo)
botonSalir = tk.Button(contenedorBotonesMenu, text="Salir de la Aplicación", command=ventana.destroy)

# Se organizan los botones en la interfaz
botonMostrarProcesoGuardar.pack()
botonMostrarProcesoLeer.pack()
botonMostrarProcesoComprar.pack()
botonBorrarArchivo.pack()
botonSalir.pack()

# Se inicia el bucle principal de la interfaz
ventana.mainloop()
