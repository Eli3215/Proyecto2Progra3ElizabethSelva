# Se importan las librerias
import tkinter as tk
from manejoArchivos import ManejoArchivo

#Variables y constantes
nombreArchivo = "datos_libros.txt"

# Definición de funciones

def LeerArchivo():

    mensaje = archivo.LeerArchivo()

    info_text.delete('1.0', tk.END)
    info_text.insert(tk.END, mensaje)
    print(mensaje)

def GuardarDatosLibro():

    codigo = ingresoCodigo.get()
    nombre = ingresoNombre.get()
    categoria = ingresoCategoria.get()
    precio = ingresoPrecio.get()

    mensaje = f"{codigo};{nombre};{categoria};{precio}"
    archivo.AnadirContenidoAlArchivo( mensaje )

# Inicio del programa

# Se crea un objeto de la clase ManejoArchivo
archivo = ManejoArchivo()

# Se crea el archivo donde se guardarán los datos de la librería
archivo.CrearArchivo(nombreArchivo)

# Crear una nueva ventana
ventana = tk.Tk()

# Se establece el título de la ventana
ventana.title("Inventario de libros")

# Se establece la geometría de la ventana
ventana.geometry("270x250")

# Se crean etiquetas para cada campo
etiquetaCodigo = tk.Label(ventana, text="Código:")
etiquetaNombre = tk.Label(ventana, text="Nombre:")
etiquetaCategoria = tk.Label(ventana, text="Categoría:")
etiquetaPrecio = tk.Label(ventana, text="Precio:")

# Se crean campos de entrada para cada característica
ingresoCodigo = tk.Entry(ventana)
ingresoNombre = tk.Entry(ventana)
ingresoCategoria = tk.Entry(ventana)
ingresoPrecio = tk.Entry(ventana)

# Se usa el componente grid para colocar las etiquetas y campos de entrada de forma ordenada
etiquetaCodigo.grid(row=0, column=0, sticky="E")
ingresoCodigo.grid(row=0, column=1)
etiquetaNombre.grid(row=1, column=0, sticky="E")
ingresoNombre.grid(row=1, column=1)
etiquetaCategoria.grid(row=2, column=0, sticky="E")
ingresoCategoria.grid(row=2, column=1)
etiquetaPrecio.grid(row=3, column=0, sticky="E")
ingresoPrecio.grid(row=3, column=1)

# Se crea un texto para mostrar la información del archivo
info_text = tk.Text(ventana, height=5, width=30)
info_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Crear un botón para guardar los datos del libro en el archivo
botonGuardar = tk.Button(ventana, text="Guardar", command=GuardarDatosLibro)
botonLeerArchivo = tk.Button(ventana, text="Leer", command=LeerArchivo)

# Agregar botones a la ventana
botonGuardar.grid(row=5, column=0)
botonLeerArchivo.grid(row=5, column=1)

# Se inicia el bucle principal
ventana.mainloop()