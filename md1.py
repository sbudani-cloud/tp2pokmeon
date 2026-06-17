import json

class Pokemon:
    def __init__(self, id, nombre, tipo, pc):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = pc

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

    def modificar(self, key, nuevo_valor):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, nuevo_valor)
                print(f"Valor de '{key}' modificado.")
                return

        print(f"Clave '{key}' no encontrada.")

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

Pokedex = HashMap()
cargar_pokedex("pokedex.json", Pokedex)