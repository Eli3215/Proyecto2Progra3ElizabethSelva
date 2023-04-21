import tkinter as tk


# Esta función permite encontrar el código más alto a partir de la matriz de libros ingresada
def BuscarCodigoMasAlto(matrizLibros):
    # Se crea el vector de códigos para evitar repetirlos
    listaCodigos = []

    # Se pasa sobre cada fila de la matriz con este ciclo
    for fila in matrizLibros:

        # Se genera una tupla para obtener cada caracterista del libro
        (codigo, nombre, categoria, precio, cantidad) = fila

        # Se convierte el código a int para hacer la comparación de los códigos como entero
        codigo = int(codigo)

        # Esta variable booleana permite definir si ya existe el codigo en la lista
        yaExisteElCodigo = False

        # Esta variable entera permite definir el código más alto encontrado en el inventario
        codigoMasAlto = 0

        # Se agrega el código leido desde la fila actual en la lista de códigos
        listaCodigos.append(codigo)

        # Se obtiene cada uno de los códigos almacenados en la lista listaCodigos para posteriormente comparar
        for codigoLista in listaCodigos:

            # Se realiza la comparación para verificar si ya existe el código en la lista
            # y se busca el código más alto para almacenarlo en la variable codigoMasAlto
            if codigo == codigoLista and codigo >= codigoLista:
                yaExisteElCodigo = True
                codigoMasAlto = codigo

                # Se suma 1 al código más alto encontrado en la lista para evitar repetir y se guarda en la lista listaCodigos
        if yaExisteElCodigo == True:
            listaCodigos.append(codigoMasAlto + 1)

    # En esta parte se selecciona el último código de la lista ya que esta se encuentra ordenada
    # y el último es el más alto, si no hay elementos en la lista se asigna el código 1 por defecto
    if len(listaCodigos) > 0:
        codigo = listaCodigos[-1]
    else:
        codigo = 1

    # Se retorna el código
    return codigo


# Esta función permite retornar un mensaje para generar las ventas totales
# del proceso de compra en la librería
def MensajeVentasTotales(usuarios):
    # Variable float para calcular el valor total de libros vendidos
    totalVendido = 0.0

    # Se genera el mensaje a mostrar en la etiqueta
    mensaje = "Ventas Totales\n"

    # Se lee todo el diccionario de usuarios
    for usuario, valorFactura in usuarios.items():
        # Se obtiene el valor de factura con impuestos
        valorFacturaConImpuesto = valorFactura + ((valorFactura * 5.0) / 100.0)

        # Se genera el mensaje
        mensaje += f"{usuario}: {valorFacturaConImpuesto}\n"

        # Se calcula el total vendido
        totalVendido += valorFacturaConImpuesto

    # Se pone al final del mensaje el total vendido
    mensaje += f"Total: {totalVendido}"

    # Se retorna el mensaje con las ventas realizadas a cada usuario y con el total vendido
    return mensaje


# Esta función permite obtener la matriz de libros y caracteristicas desde un texto que fue leido previamente desde el archivo
def ObtenerMatrizDesdeArchivo(texto):
    # Esta variable permite tener una lista con los libros que se encuentran almacenados en el archivo
    listaLibros = []

    # Esta variable permite almacenar los libros del archivo teniendo como filas cada libro
    # y como columnas cada caracteristica: código, nombre, categoria, precio, cantidad
    matriz = []

    # En esta instrucción obtenemos una lista con el texto de cada libro, ya que separamos por salto de linea
    listaLibros = texto.split("\n")

    # En este ciclo queremos separar de la listaLibros cada caracteristica por separado para formar la matriz
    for libro in listaLibros:

        # Usamos nuevamente el método split para buscar cada parámetro del libro
        # que esté separado por ; y lo almacenamos en la lista
        listaCaracteristicasLibro = libro.split(";")

        # Evaluamos si hay una lista de caracteristicas valida para evitar errores
        if len(listaCaracteristicasLibro) > 1:
            # Agregamos la fila a la matriz, cada fila tendrá código, nombre, categoria, precio y cantidad
            matriz.append(listaCaracteristicasLibro)

    # Se retorna la matriz extraida
    return matriz


# Esta función permite retornar un mensaje que actualizará todos los registros de libros en el archivo
# a partir de la matriz ingresada a la función
def ObtenerMensajeDesdeMatriz(matriz):
    # Variable que contendrá el mensaje a ser retornado
    mensaje = ""

    # Se recorre la matriz para generar el mensaje que tendrá cada libro separado por lineas
    for fila in matriz:
        # Se genera una tupla a partir del vector fila
        (codigo, nombre, categora, precio, cantidad) = fila

        # Se genera el mensaje con las caracteristicas de cada libro
        mensaje += f"{codigo};{nombre};{categora};{precio};{cantidad}\n"

    # Se retorna el texto a ser ingresado en el archivo
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

    # Pondremos este elemento en la primera fila, columna 1, abarcando 2 columnas usando la propiedad columnspan
    etiquetaMensajeAdministrador.grid(row=numeroFila, column=1, columnspan=2)

    # Esta variable permite leer la categoria del libro a ingresar
    categoriaLibro = tk.StringVar()

    # Se crean las etiquetas y botones de radio para seleccionar el tipo de libro a ingresar
    etiquetaCategoriaLibro1 = tk.Label(contenedorElementos, text="Categoria 1:")
    botonRadio1 = tk.Radiobutton(contenedorElementos, text="Ciencias", variable=categoriaLibro, value='LibroCiencias')
    botonRadio1.select()

    # Se ubican los elementos en la interfaz
    numeroFila = 1
    etiquetaCategoriaLibro1.grid(row=numeroFila, column=1, sticky="E")
    botonRadio1.grid(row=numeroFila, column=columnaEntradasTexto, sticky="W")

    # Se crean las etiquetas y botones de radio para seleccionar el tipo de libro a ingresar
    etiquetaCategoriaLibro2 = tk.Label(contenedorElementos, text="Categoria 2:")
    botonRadio2 = tk.Radiobutton(contenedorElementos, text="Humanidades", variable=categoriaLibro,
                                 value='LibroHumanidades')

    # Se ubican los elementos en la interfaz
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

    # Se retorna la tupla solo con los elementos que realmente se utilizan en el programa principal
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

    # Se organiza el elemento en el contenedor usando la propiedad grid
    textoTablaLibros.grid(row=0, column=0, columnspan=2)

    # Se retorna la tupla solo con los elementos que realmente se utilizan en el programa principal
    return (contenedorElementos, textoTablaLibros)


# Esta función permite crear los elementos necesarios para comprar libros desde el inventario disponible,
# se recibe la ventana principal y se retorna una tupla con los elementos a ser usados en el programa principal
def GenerarElementosComprarLibros(ventana):
    # Creación de contenedor que tendrá los elementos necesarios para comprar los libros
    contenedorElementos = tk.Frame(ventana)

    # Se agrega una etiqueta para definir la compra de libros por parte del cliente
    etiquetaParaComprarLibros = tk.Label(contenedorElementos,
                                         text="Espacio para comprar libros por parte del cliente,\nseleccione el código para comprar libros y oprimir en el botón de Comprar Libro")

    # Se presenta el catálogo de libros al cliente
    catalogoLibros = tk.Listbox(contenedorElementos, height=5)

    # Se crean dos textos en la interfaz para mostrar el valor de la factura con y sin impuestos
    textoFacturaVenta = tk.Label(contenedorElementos, text="Valor factura:")
    textoFacturaVentaImpuestos = tk.Label(contenedorElementos, text="Valor factura con impuestos:")

    # Se crean 2 botones para Comprar Libro y para Finalizar venta del cliente actual
    botonComprar = tk.Button(contenedorElementos, text="Comprar Libro")
    botonFinalizarVenta = tk.Button(contenedorElementos, text="Finalizar Venta Actual")

    # En esta sección ubicaremos los elementos en la interfaz de manera ordenada

    # Estaa variable nos permitirá ubicar de manera ordenada los elementos en la interfaz
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

    # Se retorna la tupla solo con los elementos que realmente se utilizan en el programa principal
    return (contenedorElementos, catalogoLibros, textoFacturaVenta, textoFacturaVentaImpuestos, botonComprar,
            botonFinalizarVenta)


# Esta función permite crear los elementos necesarios para mostrar las ventas totales,
# se recibe la ventana principal y se retorna una tupla con los elementos a ser usados en el programa principal
def GenerarElementosMostrarVentasTotales(ventana):
    # Creación de contenedor que tendrá los elementos necesarios para mostrar las ventas totales
    contenedorElementos = tk.Frame(ventana)

    # Se crea la etiquita donde mostraremos las ventas totales
    textoVentasTotales = tk.Label(contenedorElementos, text="Ventas Totales")

    # Se agrega el elemento a la interfaz de manera ordenada usando la propiedad grid
    textoVentasTotales.grid(row=0, column=0)

    # Se retorna la tupla solo con los elementos que realmente se utilizan en el programa principal
    return (contenedorElementos, textoVentasTotales)