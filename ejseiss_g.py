
#Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase: Un constructor, donde los datos pueden estar vacíos. Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.mostrar(): Muestra los datos de la persona. Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():
    def __init__(self, nombre=None, edad=None, dni=None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if edad is not None and edad >= 0:
            self._edad = edad
        else:
            print("Edad no válida")

    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        if dni is None or len(dni) == 8:
            self._dni = dni
        else:
            print("DNI no válido")

    def mostrar(self):
        print("Nombre:", self._nombre)
        print("Edad:", self._edad)
        print("DNI:", self._dni)

    def es_mayor_de_edad(self):
        return self._edad >= 18 if self._edad is not None else False

# Crear una instancia de Persona
persona1 = Persona()
persona1.set_nombre("Ana")
persona1.set_edad(30)
persona1.set_dni("98765432")
persona1.mostrar()
print("Es mayor de edad:", persona1.es_mayor_de_edad())

print("\n")

# Crear otra instancia de Persona con datos
persona2 = Persona()
persona2.set_nombre("Juan")
persona2.set_edad(17)  # Prueba con una edad menor de edad
persona2.set_dni("12345678")
persona2.mostrar()
print("Es mayor de edad:", persona2.es_mayor_de_edad())
