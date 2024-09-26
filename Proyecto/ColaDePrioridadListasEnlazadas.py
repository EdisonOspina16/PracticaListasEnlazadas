from ListaEnlazada import Node
from ListaEnlazada import LinkedList


class ColaPrioridad:
    def __init__(self):
        self.lista_pacientes = LinkedList()

    def insertar(self, paciente):
        """Inserta un paciente en la cola de prioridad."""
        self.lista_pacientes.insertar(paciente)

    def atender(self):
        """Atiende al paciente con mayor prioridad."""
        return self.lista_pacientes.atender()

    def mostrar(self):
        """Muestra todos los pacientes en la cola."""
        self.lista_pacientes.mostrar()


class Paciente:
    def __init__(self, nombre: str, descripcion_consulta: str):
        self.nombre = nombre
        self.descripcion_consulta = descripcion_consulta
        self.prioridad = self.calcular_prioridad()

    def calcular_prioridad(self) -> int:
        descripcion = self.descripcion_consulta.lower()
        if any(palabra in descripcion for palabra in ["dolor agudo", "fractura", "ataque"]):
            return 5
        elif any(palabra in descripcion for palabra in ["fiebre", "tos"]):
            return 3
        elif any(palabra in descripcion for palabra in ["revisión", "control"]):
            return 1
        raise Exception("Los sintomas no son validos....Ingrese uno correcto.")

    def __str__(self) -> str:
        return f"Paciente: {self.nombre}, Prioridad: {self.prioridad}, Motivo: {self.descripcion_consulta}"


# Ejemplo de uso:
cola = ColaPrioridad()


paciente1 = Paciente("Juan", "fiebre alta y tos")
paciente2 = Paciente("María", "dolor agudo en el pecho")
paciente3 = Paciente("Carlos", "revisión de rutina")
paciente4 = Paciente("Ana", "fractura en el brazo")


cola.insertar(paciente2)
cola.insertar(paciente3)
cola.insertar(paciente4)

print("Cola de pacientes:")
cola.mostrar()

print("\nAtendiendo paciente:")
print(cola.atender())

print("\nCola de pacientes después de atender uno:")
cola.mostrar()
