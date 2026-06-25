from catalogo import cargar_medallas, cargar_pokedex, HashMap
from gestion import equipo, PC, CentroPokemon, Transferidos
import random, os

Pokedex = HashMap()

cargar_pokedex("pokedex.json", Pokedex)
cargar_medallas("medallas.json")

def menucito():
    seguir = True
    while seguir:
        os.system("cls")
        print("1 -Ver Pokédex")
        print("2- Ver Equipo Principal")
        print("3- Ver PC")
        print("4- Ver Medallas")
        print("5- Capturar nuevo Pokémon")
        print("6- Ordenar PC")
        print("7- Buscar Pokémon en Equipo")
        print("8- Enviar Pokémon al Centro Pokémon")
        print("9- Transferir Pokémon al Profesor Oak")
        print("10- Deshacer última transferencia")
        print("11- Desafiar Líder de Gimnasio")
        print("12- Salir del sistema\n")
        
        selec = input("Seleccione una opción: ")
        if selec == "1":
            os.system("cls")
            ver_pokedex()
        elif selec == "2":
            os.system("cls")
            ver_equipo()
        elif selec == "3":
            os.system("cls")
            ver_pc()
        elif selec == "4":
            os.system("cls")
            ver_medallas()
        elif selec == "5":
            os.system("cls")
            capturar_pok()
        elif selec == "6":
            os.system("cls")
            ordenar_pc()
        elif selec == "7":
            os.system("cls")
            buscar_pok()
        elif selec == "8":
            os.system("cls")
            enviar_centropokemon()
        elif selec == "9":
            os.system("cls")
            transferir_oak()
        elif selec == "10":
            os.system("cls")
            deshacer_transf()
        elif selec == "11":
            os.system("cls")
            desafiar_lider()
        elif selec == "12":
            seguir = False
        else:
            os.system("cls")
            print("Opción no válida.")
            input("\nPresione Enter para volver al menu.")

def ver_pokedex():
    pass

def ver_equipo():
    print("\033[1mEquipo:\033[0m") #negritas
    for e in equipo:
        print(e)
    input("\nPresione Enter para volver al menu.")

def ver_pc():
    print("\033[1mPC:\033[0m")
    PC.recorrer()
    input("\nPresione Enter para volver al menu.")

def capturar_pok():
    pok = Pokedex.elegir_random()
    print(f"Ha aparecido un {pok.nombre} salvaje (PC: {pok.poder_combate}).")
    captura = random.getrandbits(1)
    if captura == 1:
        print("¡Captura exitosa!")
        print(f"Equipo Principal: {len(equipo)}/6")
        if len(equipo) < 6:
            equipo.append(pok)
            print(f"¡Pokemon añadido al equipo! ({len(equipo)}/6)")
        else:
            print("Está lleno. Derivando a almacenamiento de PC...")
            PC.agregar(pok)
            print("Registro añadido exitosamente.")
    else:
        print("Captura fallida...")
    input("\nPresione Enter para volver al menu.")

def ordenar_pc():
    print("1- Ordenar alfabeticamente")
    print("2- Ordenar por tipo")
    print("3- Ordenar por poder de combate")
    
    selec = input ("Seleccione una opción: ")
    
    if selec == "1":
        PC.orden_alfabetico()
        print("Se ordenó la PC. Seleccione 'Ver PC' en el menu para ver los cambios.")
    elif selec == "2":
        PC.orden_tipo()
        print("Se ordenó la PC. Seleccione 'Ver PC' en el menu para ver los cambios.")
    elif selec == "3":
        PC.orden_competitivo()
        print("Se ordenó la PC. Seleccione 'Ver PC' en el menu para ver los cambios.")
    else:
        print("Opción no válida.")
    input("\nPresione Enter para volver al menu.")
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

def ver_medallas():
    pass

menucito()