class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertar(self, elemento):
        nuevo_nodo = Node(elemento)
        if not self.head or self.head.value.prioridad < elemento.prioridad:
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next and actual.next.value.prioridad >= elemento.prioridad:
                actual = actual.next
            nuevo_nodo.next = actual.next
            actual.next = nuevo_nodo
        self.size += 1

    def atender(self):
        if not self.head:
            raise Exception("No hay pacientes en la cola.")
        paciente_atendido = self.head.value
        self.head = self.head.next
        self.size -= 1
        return paciente_atendido

    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.value)
            actual = actual.next
