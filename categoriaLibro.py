# Importación de librerías
from abc import ABC, abstractmethod


# Interfaz del Libro que declara las operaciones que todas las clases hijas deben implementar
class Libro(ABC):

    # Método para establecer el código del libro
    # Parámetros de ingreso: Código del libro
    # Retorna: No
    @abstractmethod
    def EstablecerCodigo(self, codigo):
        pass

    # Método para establecer el nombre del libro
    # Parámetros de ingreso: nombre del libro
    # Retorna: No
    @abstractmethod
    def EstablecerNombre(self, nombre):
        pass

    # Método para establecer el precio del libro
    # Parámetros de ingreso: Precio del libro
    # Retorna: No
    @abstractmethod
    def EstablecerPrecio(self, precio):
        pass

    # Método para establecer la cantidad de libros
    # Parámetros de ingreso: Cantidad del libros
    # Retorna: No
    @abstractmethod
    def EstablecerCantidad(self, cantidad):
        pass

    # Método para retornar el código del libro
    # Parámetros de ingreso: No
    # Retorna: Código del libro
    @abstractmethod
    def RetornarCodigo(self):
        pass

    # Método para retornar el nombre del libro
    # Parámetros de ingreso: No
    # Retorna: Nombre del libro
    @abstractmethod
    def RetornarNombre(self):
        pass

    # Método para retornar el precio del libro
    # Parámetros de ingreso: No
    # Retorna: Precio del libro
    @abstractmethod
    def RetornarPrecio(self):
        pass

    # Método para retornar la cantidad de libros
    # Parámetros de ingreso: No
    # Retorna: Cantidad de libros
    @abstractmethod
    def RetornarCantidad(self):
        pass

    # Método para retornar un mensaje con las caracteristicas del libro
    # Parámetros de ingreso: No
    # Retorna: Un mensaje con las caracteristicas del libro
    @abstractmethod
    def RetornarCaracteristicasLibro(self):
        pass


# Se implementan los métodos abstractos de la padre en la clase LibroCiencias
class LibroCiencias(Libro):

    # Método para establecer el código del libro
    # Parámetros de ingreso: Código del libro
    # Retorna: No
    def EstablecerCodigo(self, codigo):
        self.codigo = codigo

    # Método para establecer el nombre del libro
    # Parámetros de ingreso: nombre del libro
    # Retorna: No
    def EstablecerNombre(self, nombre):
        self.nombre = nombre

    # Método para establecer el precio del libro
    # Parámetros de ingreso: Precio del libro
    # Retorna: No
    def EstablecerPrecio(self, precio):
        self.precio = precio

    # Método para establecer la cantidad de libros
    # Parámetros de ingreso: Cantidad del libros
    # Retorna: No
    def EstablecerCantidad(self, cantidad):
        self.cantidad = cantidad

    # Método para retornar el código del libro
    # Parámetros de ingreso: No
    # Retorna: Código del libro
    def RetornarCodigo(self):
        return self.codigo

    # Método para retornar el nombre del libro
    # Parámetros de ingreso: No
    # Retorna: Nombre del libro
    def RetornarNombre(self):
        return self.nombre

    # Método para retornar el precio del libro
    # Parámetros de ingreso: No
    # Retorna: Precio del libro
    def RetornarPrecio(self):
        return self.precio

    # Método para retornar la cantidad de libros
    # Parámetros de ingreso: No
    # Retorna: Cantidad de libros
    def RetornarCantidad(self):
        return self.cantidad

    # Método para retornar un mensaje con las caracteristicas del libro
    # Parámetros de ingreso: No
    # Retorna: Un mensaje con las caracteristicas del libro
    def RetornarCaracteristicasLibro(self):
        mensaje = f"{self.codigo};{self.nombre};'Ciencias';{self.precio};{self.cantidad}"
        return mensaje


# Se implementan los métodos abstractos de la interfaz libro en la clase LibroHumanidades
class LibroHumanidades(Libro):

    # Método para establecer el código del libro
    # Parámetros de ingreso: Código del libro
    # Retorna: No
    def EstablecerCodigo(self, codigo):
        self.codigo = codigo

    # Método para establecer el nombre del libro
    # Parámetros de ingreso: nombre del libro
    # Retorna: No
    def EstablecerNombre(self, nombre):
        self.nombre = nombre

    # Método para establecer el precio del libro
    # Parámetros de ingreso: Precio del libro
    # Retorna: No
    def EstablecerPrecio(self, precio):
        self.precio = precio

    # Método para establecer la cantidad de libros
    # Parámetros de ingreso: Cantidad del libros
    # Retorna: No
    def EstablecerCantidad(self, cantidad):
        self.cantidad = cantidad

    # Método para retornar el código del libro
    # Parámetros de ingreso: No
    # Retorna: Código del libro
    def RetornarCodigo(self):
        return self.codigo

    # Método para retornar el nombre del libro
    # Parámetros de ingreso: No
    # Retorna: Nombre del libro
    def RetornarNombre(self):
        return self.nombre

    # Método para retornar el precio del libro
    # Parámetros de ingreso: No
    # Retorna: Precio del libro
    def RetornarPrecio(self):
        return self.precio

    # Método para retornar la cantidad de libros
    # Parámetros de ingreso: No
    # Retorna: Cantidad de libros
    def RetornarCantidad(self):
        return self.cantidad

    # Método para retornar un mensaje con las caracteristicas del libro
    # Parámetros de ingreso: No
    # Retorna: Un mensaje con las caracteristicas del libro
    def RetornarCaracteristicasLibro(self):
        mensaje = f"{self.codigo};{self.nombre};'Humanidades';{self.precio};{self.cantidad}"
        return mensaje


# Esta clase FabricaLibros declara el método factory (CrearLibro) que retornará un objeto ya sea de la clase LibroCiencias o LibroHumanidades
class FabricaLibros:


    # Este método permite returnar un objeto ya sea de la clase LibroCiencias o de la clase LibroHumanidades
    # Parámetros de ingreso: Tipo de libro a ser generado ('LibroCiencias' o 'LibroHumanidades')
    # Retorna: Instancia de la clase LibroCiencias() o de la clase LibroHumanidades()
    def CrearLibro(self, tipo):
        if tipo == 'LibroCiencias':
            return LibroCiencias()
        elif tipo == 'LibroHumanidades':
            return LibroHumanidades()
        else:
            None