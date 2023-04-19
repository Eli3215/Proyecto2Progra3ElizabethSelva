import tkinter as tk


# Esta función permite encontrar el código más alto a partir de la matriz de libros ingresada
def BuscarCodigoMasAlto(matrizLibros):
    # Se crea el vector de códigos para evitar repetirlos
    listaCodigos = []

    for fila in matrizLibros:
        # Se genera una tupla para obtener cada caracterista de la fila
        (codigo, nombre, categoria, precio, cantidad) = fila

        # Se convierte el código a int porque se lee como un str
        codigo = int(codigo)

        # Esta variable booleana permite definir si ya existe el codigo en la lista
        yaExisteElCodigo = False

        codigoMasAlto = 0
        listaCodigos.append(codigo)

        for codigoLista in listaCodigos:

            # Se realiza la comparación para verificar si ya existe el código en la lista
            # y se busca el código más alto
            if codigo == codigoLista and codigo >= codigoLista:
                yaExisteElCodigo = True
                codigoMasAlto = codigo

                # Se suma 1 al código más alto encontrado en la lista para evitar repetir
        if yaExisteElCodigo == True:
            listaCodigos.append(codigoMasAlto + 1)

    # En esta parte se selecciona el último código de la lista ya que esta se encuentra ordenada
    # y el último es el más alto
    if len(listaCodigos) > 0:
        codigo = listaCodigos[-1]
    else:
        codigo = 1

    return codigo


# Esta función permite retornar un mensaje para generar las ventas totales
# del proceso de compra en la librería
def MensajeVentasTotales(usuarios):
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


# Esta función permite obtener la matriz de libros y caracteristicas desde el archivo
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


# Creación de la interfaz gráfica por medio de funciones

# Esta función permitirá definir los elementos que se crearán para el proceso de guardado de libros por parte del administrador,
# se recibirá la ventana y retorna una tupla con cada uno de los elementos creados para
# ser usados a través del programa principal por otras funciones
def GenerarElementosGuardarLibro(ventana):
    # Creación de contenedor que tendrá los elementos necesarios para el proceso de guardar
    contenedorElementos = tk.Frame(ventana)

    # Estas variables nos permitirán ubicar de forma ordenada los elementos en la interfaz
    numeroFila = 0
    columnaEtiquetas = 1
    columnaEntradasTexto = 2

    # Esta etiqueta define el encabezado en la primera sección donde el administrador ingresará los libros en el archivo
    etiquetaMensajeAdministrador = tk.Label(contenedorElementos, text="Espacio del administrador para ingresar libros")

    # Pondremos este elemento en la primera fila
    etiquetaMensajeAdministrador.grid(row=numeroFila, column=1, columnspan=2, sticky="E")

    # Se crean etiquetas para cada campo de ingreso
    # Esta variable permite leer la categoria del libro a ingresar
    categoriaLibro = tk.StringVar()

    # Se crean las etiquetas y botones de radio para seleccionar el tipo de libro a ingresar
    etiquetaCategoriaLibro1 = tk.Label(contenedorElementos, text="Categoria 1:")
    botonRadio1 = tk.Radiobutton(contenedorElementos, text="Ciencias", variable=categoriaLibro, value='LibroCiencias')
    botonRadio1.select()

    # Se ubica el elemento en la interfaz
    numeroFila = 1
    etiquetaCategoriaLibro1.grid(row=numeroFila, column=1, sticky="E")
    botonRadio1.grid(row=numeroFila, column=columnaEntradasTexto, sticky="W")

    etiquetaCategoriaLibro2 = tk.Label(contenedorElementos, text="Categoria 2:")
    botonRadio2 = tk.Radiobutton(contenedorElementos, text="Humanidades", variable=categoriaLibro,
                                 value='LibroHumanidades')

    # Se ubica el elemento en la interfaz
    numeroFila = numeroFila + 1
    etiquetaCategoriaLibro2.grid(row=numeroFila, column=1, sticky="E")
    botonRadio2.grid(row=numeroFila, column=columnaEntradasTexto, sticky="W")

    # Se crean etiquetas para ingresar nombre, precio y cantidad de libros
    etiquetaNombre = tk.Label(contenedorElementos, text="Nombre:")
    etiquetaPrecio = tk.Label(contenedorElementos, text="Precio:")
    etiquetaCantidad = tk.Label(contenedorElementos, text="Cantidad:")

    # Se crean campos de entrada para cada característica de los libros
    ingresoNombre = tk.Entry(contenedorElementos)
    ingresoPrecio = tk.Entry(contenedorElementos)
    ingresoCantidad = tk.Entry(contenedorElementos)

    # Se usa el componente grid para colocar las etiquetas y campos de entrada de forma ordenada
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
    botonGuardarArchivo = tk.Button(contenedorElementos, text="Guardar Libro")
    botonGuardarArchivo.grid(row=numeroFila, column=2)

    return (
    contenedorElementos, categoriaLibro, botonRadio1, botonRadio2, ingresoNombre, ingresoPrecio, ingresoCantidad,
    botonGuardarArchivo)


# Esta función permite crear los elementos necesarios para leer el inventario disponible en el archivo,
# se recibe la ventana principal y se retorna una tupla con los elementos a ser usados en el programa principal
def GenerarElementosLeerLibros(ventana):
    # Creación de contenedor que tendrá los elementos necesarios para mostrar el contenido del archivo
    contenedorElementos = tk.Frame(ventana)

    # Se crea un texto en la interfaz para mostrar la información del archivo
    textoTablaLibros = tk.Text(contenedorElementos, height=5)
    textoTablaLibros.insert(tk.END, "codigo | nombre | categoria | precio | cantidad |")

    textoTablaLibros.grid(row=0, column=0, columnspan=2)

    return (contenedorElementos, textoTablaLibros)


# Esta función permite crear los elementos necesarios para comprar libros desde el inventario disponible,
# se recibe la ventana principal y se retorna una tupla con los elementos a ser usados en el programa principal
def GenerarElementosComprarLibros(ventana):
    # Creación de contenedor que tendrá los elementos necesarios para comprar los libros
    contenedorElementos = tk.Frame(ventana)

    # Se agrega una etiqueta para definir la compra de libros por parte del cliente
    etiquetaParaComprarLibros = tk.Label(contenedorElementos,
                                         text="Espacio para comprar libros por parte del cliente,\nseleccione el código para comprar libros y oprimir en el botón de comprar")

    # Se presenta el catálogo de libros al cliente
    catalogoLibros = tk.Listbox(contenedorElementos, height=5)

    # Se crea un texto en la interfaz para mostrar el valor de la factura
    textoFacturaVenta = tk.Label(contenedorElementos, text="Valor factura:")
    textoFacturaVentaImpuestos = tk.Label(contenedorElementos, text="Valor factura con impuestos:")

    botonComprar = tk.Button(contenedorElementos, text="Comprar Libro")
    botonFinalizarVenta = tk.Button(contenedorElementos, text="Finalizar Venta Actual")

    # En esta sección ubicaremos los elementos en la interfaz de manera ordenada
    # Estas variables nos permitirán definir la fila y columna donde pondremos los elementos en la interfaz
    numeroFila = 0
    etiquetaParaComprarLibros.grid(row=numeroFila, column=0, columnspan=4, pady=5)

    numeroFila = numeroFila + 1
    botonComprar.grid(row=numeroFila, column=1)
    catalogoLibros.grid(row=numeroFila, column=2, pady=10)

    numeroFila = numeroFila + 1
    textoFacturaVenta.grid(row=numeroFila, column=1)

    numeroFila = numeroFila + 1
    textoFacturaVentaImpuestos.grid(row=numeroFila, column=1)

    botonFinalizarVenta.grid(row=numeroFila, column=2)

    return (contenedorElementos, catalogoLibros, textoFacturaVenta, textoFacturaVentaImpuestos, botonComprar,
            botonFinalizarVenta)


# Esta función permite crear los elementos necesarios para mostrar las ventas totales,
# se recibe la ventana principal y se retorna una tupla con los elementos a ser usados en el programa principal
def GenerarElementosMostrarVentasTotales(ventana):
    # Creación de contenedor que tendrá los elementos necesarios para mostrar las ventas totales
    contenedorElementos = tk.Frame(ventana)

    textoVentasTotales = tk.Label(contenedorElementos, text="Ventas Totales")

    textoVentasTotales.grid(row=0, column=0)

    return (contenedorElementos, textoVentasTotales)