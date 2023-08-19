#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase: Un constructor, donde los datos pueden estar vacíos. Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. mostrar(): Muestra los datos de la cuenta. ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.



#En esta implementación, la clase Cuenta tiene los atributos __titular y __cantidad con doble guión bajo al principio para hacerlos "privados". Esto significa que estos atributos no deben ser accedidos directamente desde fuera de la clase, en lugar de eso, se utilizan los métodos getter y setter para acceder y modificar estos atributos.El constructor __init__ crea una cuenta con el titular y la cantidad inicial proporcionados.Los métodos get_titular, set_titular, get_cantidad y set_cantidad permiten acceder y modificar los atributos __titular y __cantidad de manera controlada.El método mostrar muestra los datos de la cuenta en la consola.Los métodos ingresar y retirar agregan o restan una cantidad a la cuenta, respectivamente, solo si la cantidad es mayor que cero.El ejemplo de uso final crea una instancia de la clase Cuenta, muestra sus datos iniciales, realiza un depósito e un retiro, y luego muestra los datos actualizados de la cuenta.


class Cuenta():
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad

# Ejemplo de uso
cuenta1 = Cuenta("Juan Perez", 1000)
cuenta1.mostrar()

cuenta1.ingresar(500)
cuenta1.retirar(200)
cuenta1.mostrar()