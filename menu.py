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
        print("⋆˙⟡♡ ๋࣭ ⭑ \033[1m¡Pokemon Huergo!\033[0m ໒꒰ྀིっ˕ -｡꒱ྀི১ ₊˚⊹♡ \n")
        print("⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔ ꒰ ᧔ෆ݁݁᧓ ꒱⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔")
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
        print("12- Salir del sistema")
        print("───────────────୨ৎ───────────────\n")
        
        selec = input("݁ ˖Ი𐑼⋆ Seleccione una opción ݁ ˖Ი𐑼⋆ ")
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
            print("Opción no válida. ₍^. .^₎Ⳋ")
            input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def ver_pokedex():
    for e in Pokedex.buckets:
        for key, pokemon in e:
            print(f"{key} - {pokemon}")
    selec = input("¿Querés buscar un pokemon en específico? (y/n): ")
    if selec.lower() == "y":
        pok = input("Ingrese el ID: ")
        resultado = busq_pokedex(pok)
        if resultado != -1:
            print("si esta jasd") #ACÁ
        else:
            print("no eesta") #ACÁ
    elif selec.lower() == "n":
        ("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")
    else:
        print("Opción no válida. ₍^. .^₎Ⳋ")
        input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def busq_pokedex(pok):
    lista = []
    for e in Pokedex.buckets:
        for key, pokemon in e:
            lista.append(key)
    left = 0
    right = len(lista) - 1
    while left <= right:
        mid = (left + right) // 2
        if lista[mid] == pok:
            return mid
        if lista[mid] < pok:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    input()

def ver_equipo():
    print("\033[1mEquipo:\033[0m ₍₍⚞(˶>ᗜ<˶)⚟⁾⁾") #negritas \033[1m \033[0m
    for e in equipo:
        print(e)
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def ver_pc():
    print("\033[1mPC:\033[0m (˶ᵔᗜᵔ˶)ﾉﾞ")
    PC.recorrer()
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def capturar_pok():
    pok = Pokedex.elegir_random()
    print(f"Ha aparecido un {pok.nombre} salvaje (PC: {pok.poder_combate}). (˶ˆᗜˆ˵).ᐟ\n")
    captura = random.getrandbits(1)
    if captura == 1:
        print(". ݁₊ ⊹ . ݁˖ . ݁ ¡Captura exitosa! . ݁₊ ⊹ . ݁˖ . ݁")
        print(f"ദ്ദി◝ ⩊ ◜.ᐟ Equipo Principal: {len(equipo)}/6")
        if len(equipo) < 6:
            equipo.append(pok)
            print(f"¡Pokemon añadido al equipo! ({len(equipo)}/6) ꉂ(˵˃ ᗜ ˂˵)")
        else:
            print("Está lleno. Derivando a almacenamiento de PC... *ੈ✩‧₊˚")
            PC.agregar(pok)
            print("⤷ ゛ ˎˊ˗ Registro añadido exitosamente. ₊˚⊹♡")
    else:
        print("⋆˚࿔ Captura fallida... (˶°ㅁ°)!!")
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def ordenar_pc():
    print("1- Ordenar alfabeticamente")
    print("2- Ordenar por tipo")
    print("3- Ordenar por poder de combate\n")
    
    selec = input ("݁ ˖Ი𐑼⋆ Seleccione una opción ݁ ˖Ი𐑼⋆ ")
    
    if selec == "1":
        PC.orden_alfabetico()
        print("Se ordenó la PC. Seleccione 'Ver PC' en el menu para ver los cambios. (˶ᵔ ᵕ ᵔ˶) <3")
    elif selec == "2":
        PC.orden_tipo()
        print("Se ordenó la PC. Seleccione 'Ver PC' en el menu para ver los cambios. (˶ᵔ ᵕ ᵔ˶) <3")
    elif selec == "3":
        PC.orden_competitivo()
        print("Se ordenó la PC. Seleccione 'Ver PC' en el menu para ver los cambios. (˶ᵔ ᵕ ᵔ˶) <3")
    else:
        print("Opción no válida. ₍^. .^₎Ⳋ")
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def buscar_pok(): #falta decorar
    pok = input("Ingrese el nombre de un pokemon: ")
    for e in equipo:
        if e.nombre.lower() == pok.lower():
            print("El pokemon se encuentra en el equipo.")
            input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")
            return
    print("El pokemon no se encuentra en el equipo.")
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

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