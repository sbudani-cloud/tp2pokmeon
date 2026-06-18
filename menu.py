from catalogo import cargar_medallas, cargar_pokedex, HashMap
from gestion import equipo, PC, CentroPokemon, Transferidos
import random

Pokedex = HashMap()

cargar_pokedex("pokedex.json", Pokedex)
cargar_medallas("medallas.json")

def menucito():
    seguir = True
    while seguir:
        print("1 -Ver Pokédex")
        print("2- Ver Equipo Principal")
        print("3- Ver PC")
        print("4- Capturar nuevo Pokémon")
        print("5- Ordenar PC (Submenú: Alfabético, Por Tipo, Por PC)")
        print("6- Buscar Pokémon en Equipo")
        print("7- Enviar Pokémon al Centro Pokémon")
        print("8- Transferir Pokémon al Profesor Oak")
        print("9- Deshacer última transferencia")
        print("10- Desafiar Líder de Gimnasio")
        print("11- Salir del sistema\n")
        
        selec = input("Seleccione una opción: ")
        if selec == "1":
            ver_pokedex()
        elif selec == "2":
            ver_equipo()
        elif selec == "3":
            ver_pc()
        elif selec == "4":
            capturar_pok()
        elif selec == "5":
            ordenar_pc()
        elif selec == "6":
            buscar_pok()
        elif selec == "7":
            enviar_centropokemon()
        elif selec == "8":
            transferir_oak()
        elif selec == "9":
            deshacer_transf()
        elif selec == "10":
            desafiar_lider()
        elif selec == "11":
            seguir = False
        else:
            print("naquever")

def ver_pokedex():
    pass

def ver_equipo():
    pass

def ver_pc():
    pass

def capturar_pok():
    pok = Pokedex.elegir_random()
    print(f"Ha aparecido un {pok.nombre} salvaje (PC: {pok.poder_combate}).")
    captura = random.getrandbits(1)
    if captura == 1:
        print("¡Captura exitosa!")
        print(f"Equipo Principal: {len(equipo)}/6")
        if len(equipo) < 6:
            print("Pokemon añadido al equipo!")
            equipo.append(pok)
        else:
            print("Está lleno. Derivando a almacenamiento de PC...")
            PC.agregar(pok)
            print("Registro añadido exitosamente.")
        input()
    else:
        print("Captura fallida...")
        input()

def ordenar_pc():
    pass

def buscar_pok():
    pass

def enviar_centropokemon():
    pass

def transferir_oak():
    pass

def deshacer_transf():
    pass

def desafiar_lider():
    pass

menucito()