import tkinter as tk

# Definición de funciones

# Función para tomar el evento cuando se presiona el botón Guardar
# e imprimir los datos ingresados
def ImprimirEntradas():
    codigo = ingresoCodigo.get()
    nombre = ingresoNombre.get()
    categoria = ingresoCategoria.get()
    precio = ingresoPrecio.get()
    print(codigo, nombre, categoria, precio)

# Inicio del programa

# Crear una nueva ventana
ventana = tk.Tk()

# Se establece el título de la ventana
ventana.title("Inventario de libros")

# Se establece la geometría de la ventana
ventana.geometry("270x150")

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

# Crear un botón para guardar los datos del libro en el archivo
botonGuardar = tk.Button(ventana, text="Guardar", command=ImprimirEntradas)

# Agregar el botón a la ventana
botonGuardar.grid(row=4, column=1)


# Se inicia el bucle principal
ventana.mainloop()