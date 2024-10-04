from ListaEnlazada import Node
from ListaEnlazada import LinkedList


class ColaPrioridad:
    def __init__(self):
        self.lista_pacientes = LinkedList()

    def enqueue(self, paciente):
        self.lista_pacientes.insertar(paciente)

    def dequeue(self):
        return self.lista_pacientes.atender()

    def fisrt(self):
        self.lista_pacientes.mostrar()


class Paciente:
    def __init__(self, nombre: str, descripcion_consulta: str):
        self.nombre: str = nombre
        self.descripcion_consulta: str = descripcion_consulta
        self.prioridad: int = self.calcular_prioridad()

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



cola = ColaPrioridad()

paciente1 = Paciente("juan", "fiebre alta y tos")
paciente2 = Paciente("maria", "dolor agudo en el pecho")
paciente3 = Paciente("carlos", "revisión de rutina")
paciente4 = Paciente("ana", "fractura en el brazo")
paciente5 = Paciente("ximena", "corazon roto en busca de control")


cola.enqueue(paciente1)
cola.enqueue(paciente2)
cola.enqueue(paciente3)
cola.enqueue(paciente4)
cola.enqueue(paciente5)

print("Cola de pacientes:")
cola.fisrt()

print("\nAtendiendo paciente:")
print(cola.dequeue())

print("\nCola de pacientes después de atender uno:")
cola.fisrt()

print("\nAtendiendo paciente:")
print(cola.dequeue())

print("\nAtendiendo paciente:")
print(cola.dequeue())

print("\nAtendiendo paciente:")
print(cola.dequeue())

print("\nAtendiendo paciente:")
print(cola.dequeue())

print("\nCola de pacientes:")
cola.fisrt()
