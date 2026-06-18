equipo = []

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
class ListaEnlazada:
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

PC = ListaEnlazada() #mochila

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, dato):
        nuevo = Nodo(dato)
        if self.head is None:
            self.head = nuevo
            self.tail = nuevo
            return
        self.tail.siguiente = nuevo
        self.tail = nuevo

    def dequeue(self):
        if self.head is None:
            return None
        dato = self.head.dato
        self.head = self.head.siguiente
        if self.head is None:
            self.tail = None
        return dato

CentroPokemon = Queue()

class Stack:
    def __init__(self):
        self.lista = ListaEnlazada()

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.lista.head
        self.lista.head = nuevo

    def pop(self):
        if self.lista.head is None:
            return None
        dato = self.lista.head.dato
        self.lista.head = self.lista.head.siguiente
        return dato

    def peek(self):
        if self.lista.head:
            return self.lista.head.dato
        return None

Transferidos = Stack()

lideres_gimnasio = {
    "Limon Agrio": "Medalla Limoncito",
    "Dulce Princesa": "Medalla Chicle",
    "Marceline": "Medalla Vampira",
    "Jake": "Medalla Perro",
    "Finn": "Medalla Humano",
    "Princesa Grumosa": "Medalla Grumos",
    "Rey Helado": "Medalla Hielo",
    "Prismo": "Medalla Prismatica"
}