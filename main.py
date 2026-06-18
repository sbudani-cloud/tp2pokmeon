from catalogo import cargar_medallas, cargar_pokedex, HashMap

Pokedex = HashMap()

cargar_pokedex("pokedex.json", Pokedex)
cargar_medallas("medallas.json")