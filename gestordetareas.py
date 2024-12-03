class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def __str__(self):
        estado = "✔" if self.completada else "✘"
        return f"{self.descripcion} [{estado}]"


class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        print("Tarea agregada exitosamente.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for idx, tarea in enumerate(self.tareas, start=1):
                print(f"{idx}. {tarea}")

    def marcar_completada(self, indice):
        if 0 < indice <= len(self.tareas):
            self.tareas[indice - 1].completada = True
            print("Tarea marcada como completada.")
        else:
            print("Índice inválido.")

    def eliminar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            self.tareas.pop(indice - 1)
            print("Tarea eliminada exitosamente.")
        else:
            print("Índice inválido.")


def menu():
    lista = ListaTareas()

    while True:
        print("\n--- Lista de Tareas ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            lista.agregar_tarea(descripcion)

        elif opcion == "2":
            lista.mostrar_tareas()

        elif opcion == "3":
            lista.mostrar_tareas()
            indice = int(input("Índice de la tarea a marcar como completada: "))
            lista.marcar_completada(indice)

        elif opcion == "4":
            lista.mostrar_tareas()
            indice = int(input("Índice de la tarea a eliminar: "))
            lista.eliminar_tarea(indice)

        elif opcion == "5":
            print("Saliendo del gestor de tareas...")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    menu()
