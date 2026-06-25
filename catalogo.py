import json, random

#clases
class Pokemon:
    def __init__(self, id, nombre, tipo, pc):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = pc
    
    def __str__(self):
        return f"{self.nombre} / {self.tipo} / {self.poder_combate}" #cambiar a que se vea mas lindo
    
    def __repr__(self):
        return f"{self.nombre}"

class HashMap:
    def __init__(self):
        self.capacidad = 50
        self.buckets = [[] for _ in range(self.capacidad)]

    def _hash(self, key):
        return hash(key) % self.capacidad

    def agregar(self, key, value):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        # Si la clave ya existe, actualiza el valor
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                print(f"Valor de '{key}' actualizado.")
                return

        # Si no existe, la agrega
        bucket.append((key, value))

    def eliminar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                print(f"Clave '{key}' eliminada.")
                return

        print(f"Clave '{key}' no encontrada.")

    def buscar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def elegir_random(self):
        pokemones = []

        for bucket in self.buckets:
            for key, pokemon in bucket:
                pokemones.append(pokemon)
        if not pokemones:
            return None

        return random.choice(pokemones)
    

    def modificar(self, key, nuevo_valor):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, nuevo_valor)
                print(f"Valor de '{key}' modificado.")
                return

        print(f"Clave '{key}' no encontrada.")

class HashSet:
    def __init__(self):
        self.capacidad = 10
        self.buckets = [[] for _ in range(self.capacidad)]

    def _hash(self, key):
        return hash(key) % self.capacidad

    def agregar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        if key not in bucket:
            bucket.append(key)
            print(f"Elemento '{key}' agregado.")
        else:
            print(f"El elemento '{key}' ya existe.")

    def eliminar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        if key in bucket:
            bucket.remove(key)
            print(f"Elemento '{key}' eliminado.")
        else:
            print(f"Elemento '{key}' no encontrado.")

    def buscar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        return key in bucket

    def modificar(self, key_vieja, key_nueva):
        if not self.buscar(key_vieja):
            print(f"El elemento '{key_vieja}' no existe.")
            return

        if self.buscar(key_nueva):
            print(f"El elemento '{key_nueva}' ya existe.")
            return

        self.eliminar(key_vieja)
        self.agregar(key_nueva)
        print(f"Elemento '{key_vieja}' modificado a '{key_nueva}'.")

#____cargar__
def cargar_pokedex(ruta_archivo, pokedex):
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        datos = json.load(file)

    for p in datos:
        pokemon = Pokemon(
            p["id"],
            p["nombre"],
            p["tipo"],
            p["pc"]
        )

        pokedex.agregar(pokemon.id, pokemon)

def cargar_medallas(ruta_archivo):
    medallasObtenidas = []
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        datos = json.load(file)

    medallasObtenidas.append(datos[0])
    medallasObtenidas.append(datos[1])