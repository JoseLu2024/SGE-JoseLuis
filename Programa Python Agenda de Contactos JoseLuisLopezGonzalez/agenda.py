class Persona:
    """Esta es la clase persona que contiene los atributos básicos."""
    def __init__(self, nombre, direccion, correo):
        self.nombre = nombre
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, Correo: {self.correo}"


class Contacto(Persona):
    """Esta clase es la que representa un contacto, que es heredado de la clase Persona."""
    def __init__(self, nombre, direccion, correo, telefono):
        super().__init__(nombre, direccion, correo)  
        self.telefono = telefono

    def __str__(self):
        return f"{super().__str__()}, Teléfono: {self.telefono}"


class Agenda:
    """Esta clase es la que permite gestionar los contactos."""
    def __init__(self):
        self.contactos = {}

    def alta_contacto(self):
        """Esta funcion sirve para agregar o registrar un nuevo contacto a la agenda solicitando todos los datos disponibles del usuario."""
        nombre = input("Ingrese el nombre del contacto: ")
        direccion = input("Ingrese la dirección del contacto: ")
        correo = input("Ingrese el correo del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        self.contactos[nombre] = Contacto(nombre, direccion, correo, telefono)
        print(f"Contacto {nombre} agregado a la agenda.")

    def baja_contacto(self):
        """Esta funcion baja contacto permite eliminar un contacto seleccionando su nombre."""
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto {nombre} eliminado de la agenda.")
        else:
            print(f"El contacto {nombre} no se encuentra en la agenda.")

    def modificar_contacto(self):
        """Esta funcion modificar contacto permite cambiar la informacion de un contacto que ya existe."""
        nombre = input("Ingrese el nombre del contacto a modificar: ")
        if nombre in self.contactos:
            print("Deje el campo en blanco para no modificarlo.")
            direccion = input(f"Dirección actual ({self.contactos[nombre].direccion}): ") or self.contactos[nombre].direccion
            correo = input(f"Correo actual ({self.contactos[nombre].correo}): ") or self.contactos[nombre].correo
            telefono = input(f"Teléfono actual ({self.contactos[nombre].telefono}): ") or self.contactos[nombre].telefono
            self.contactos[nombre] = Contacto(nombre, direccion, correo, telefono)
            print(f"Contacto {nombre} modificado.")
        else:
            print(f"El contacto {nombre} no se encuentra en la agenda.")

    def buscar_contacto(self):
        """Esta funcion nos permite buscar un contacto por su nombre y mostrar toda su información."""
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre in self.contactos:
            print(self.contactos[nombre])
        else:
            print(f"El contacto {nombre} no está disponible en la agenda.")

    def formato_html(func):
        """Funcion que permite mostrar la salida de un método en formato HTML."""
        def decorador(self, *args, **kwargs):
            print("<html><body>")
            func(self, *args, **kwargs)
            print("</body></html>")
        return decorador

    def listar_agenda(self):
        """Funcion que muestra una lista de todos los contactos en formato HTML utilizando el decorador."""
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("<h1>Listado Completo de la Agenda</h1>")
            for contacto in self.contactos.values():
                print(f"<p>{contacto}</p>")

    def menu(self):
        """Menú de Usuario que contiene un bucle que no se cierra hasta que se pone la opcion 6 de salida."""
        while True:
            print("\nMenú de opciones:")
            print("1. Dar el alta al contacto")
            print("2. Dar de Baja a contacto")
            print("3. Modificación de contacto")
            print("4. Listar contactos")
            print("5. Buscar un contacto")
            print("6. Salida de la agenda.")
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                self.alta_contacto()
            elif opcion == "2":
                self.baja_contacto()
            elif opcion == "3":
                self.modificar_contacto()
            elif opcion == "4":
                self.listar_agenda()
            elif opcion == "5":
                self.buscar_contacto()
            elif opcion == "6":
                print("Salida del programa,espere...")
                break
            else:
                print("Esta opción no es válida, por favor intente de nuevo.")

#Nos permite  ejecutar  la agenda.
if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()
