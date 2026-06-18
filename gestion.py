equipo = [None, None, None, None, None, None]

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.head is None:
            self.head = nuevo
            return
        actual = self.head
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def buscar(self, dato):
        actual = self.head
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, dato):
        if self.head is None:
            return
        if self.head.dato == dato:
            self.head = self.head.siguiente
            return
        actual = self.head
        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    def recorrer(self):
        actual = self.head
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def tamaño(self):
        contador = 0
        actual = self.head
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def ordenar(self):
        if self.head is None:
            return
        actual = self.head
        while actual:
            siguiente = actual.siguiente
            while siguiente:
                if actual.dato > siguiente.dato:
                    actual.dato, siguiente.dato = (
                        siguiente.dato,
                        actual.dato
                    )
                siguiente = siguiente.siguiente
            actual = actual.siguiente