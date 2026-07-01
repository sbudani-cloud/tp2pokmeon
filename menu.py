from catalogo import cargar_pokedex, HashMap, lideres_gimnasio, medallasObtenidas
from gestion import equipo, PC, centroPokemon, transferidos
import random, os, time

# AAAAAAA agregar algunos emojis en la deco
# solo falta lo q dice arriba y lo de los lideres y medallas siiiiiii
# ah y pasar cositas al main


Pokedex = HashMap()

cargar_pokedex("pokedex.json", Pokedex)

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
    selec = input("\nʚɞ ⁺˖ ⸝⸝ ¿Querés buscar un pokemon en específico? (y/n): ")
    if selec.lower() == "y":
        try:
            pok = int(input("\n ׅ 𝄂𝄚𝅦𝄚𝄞𝅄 Ingrese el ID: "))
        except ValueError:
            print("\nEl ID debe ser un número. ˚. ꉂ(˵˃ ᗜ ˂˵) ᵎᵎ")
            return
        resultado = busq_pokedex(pok)
        if resultado != -1:
            pokemoncito = Pokedex.buscar(pok)
            print(f"\n¡El pokemon sí se encuentra en la Pokedex! ‧₊˚♪ 𝄞₊˚⊹ Es {pokemoncito.nombre}. ♬⋆.˚") #quiero q su nmbre este en color. dps agrego colores
        else:
            print("\nEl pokemon no se encuentra en la Pokedex. (˶˃ ᵕ ˂˶) ᵎ!ᵎ")
    elif selec.lower() == "n":
        pass
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
    if len(equipo) == 0:
        print("No tienes pokemons en tu equipo todavía. ૮◞ ‸ ◟ ა")
    else:
        print("\033[1mEquipo:\033[0m ₍₍⚞(˶>ᗜ<˶)⚟⁾⁾\n") #negritas \033[1m \033[0m
        for e in equipo:
            print(e)
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def ver_pc():
    print("\033[1mPC:\033[0m (˶ᵔᗜᵔ˶)ﾉﾞ\n")
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
    pok = input("✧˖°. Ingrese el nombre de un pokemon: ")
    for e in equipo:
        if e.nombre.lower() == pok.lower():
            print("El pokemon se encuentra en el equipo. ૮ ྀིᴗ͈ . ᴗ͈ ྀིა")
            input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")
            return
    print("El pokemon no se encuentra en el equipo. ૮꒰◞ ˕ ◟ ྀི꒱ა")
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def enviar_centropokemon():
    print("𝄞⨾💿✮˚.⋆ Ingresando equipo a la cola...\n")
    for pok in equipo:
        centroPokemon.enqueue(pok)
    
    while centroPokemon.head is not None:
        pok = centroPokemon.dequeue()
        print(f"⋆౨ৎ˚⟡˖ ࣪ {pok.nombre} se está curando", end="", flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("")
        time.sleep(1)
    print("\n¡Todos los pokemons fueron curados! ⸜(｡˃ ᵕ ˂ )⸝♡")
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def transferir_oak():
    temp = []
    actual = PC.head
    i = 1
    while actual:
        print(f"{i} - {actual.dato.nombre}")
        temp.append(actual.dato)
        actual = actual.siguiente
        i += 1
    if PC.tamaño() == 0:
        print("⊹ ࣪ ˖ No tenes pokemons para transferir. (,,>_<,,)")
    else:
        try:
            selec = int(input("\n꒰ྀི১ ໒꒱ིྀ ¿Qué pokemon querés transferir?: "))
        except ValueError:
            print("\nDebe ingresar un número. ˚. ꉂ(˵˃ ᗜ ˂˵) ᵎᵎ")
            input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")
            return
        if selec > 0 and selec < i:
            os.system("cls")
            PC.eliminar(temp[selec-1])
            print(f"Transfiriendo {temp[selec-1].nombre} al Profesor Oak... ˚ ༘ ೀ⋆｡˚")
            
            if transferidos.size() < 5:
                transferidos.push(temp[selec-1])
            else:
                actual = transferidos.lista.head
                while actual.siguiente.siguiente:
                    actual = actual.siguiente
                actual.siguiente = None
                
                transferidos.push(temp[selec-1])
            
            time.sleep(0.5)
            print("¡Pokemon transferido con éxito! ༉‧₊˚.")
        else:
            print("Opción no válida. ₍^. .^₎Ⳋ")
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def deshacer_transf():
    if transferidos.size() < 1:
        print("No hay pokemons que recuperar. (˶˃𐃷˂˶)")
    else:
        print("⋆｡‧˚ʚ ୨ৎ Recuperando último pokemon...")
        pok = transferidos.pop()
        PC.agregar(pok)
        print(f"{pok.nombre} ha vuelto a la PC. 𐔌՞ ܸ.ˬ.ܸ՞𐦯")
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def desafiar_lider(): #decorar Y PONER COLORES EN LOS PRINTS DE LIDERES Y MEDALLAS.
    if len(equipo) < 1:
        print("¡Debes tener un equipo para desafiar a un líder! (˶ˆᗜˆ˵)!!")
    else:
        cont = 1
        for e, i in lideres_gimnasio.items():
            print(f"{cont}- Líder {e} ({i})") #aca
            cont += 1
        
        try:
            selec = int(input("¿Contra qué líder querés pelear?: "))
            ls_lideres = list(lideres_gimnasio.items())
            lider, med = ls_lideres[selec-1]
        except (IndexError, ValueError):
            print("Opción no válida. ₍^. .^₎Ⳋ")
        else:
            print(f"Estás a punto de pelear contra {lider} por la {med}.")
            
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print("")
            
            victoria = random.getrandbits(1)
            if victoria == 1: #mejorar textos
                print ("Ganaste la pelea!")
                if med in medallasObtenidas:
                    print("Ya tenes la medalla, asi q na")
                else:
                    print("Aaca tenes la medalla por tu esfuerzo")
                    medallasObtenidas.append(med)
            else:
                print("Perdiste la pelea...")
    
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

def ver_medallas():
    print(">⩊< \033[1mMedallas Obtenidas:\033[0m (๑ᵔ⤙ᵔ๑)")
    for e in medallasObtenidas:
        print(f"    {e}")
    print("\n>⩊< \033[1mMedallas No Obtenidas:\033[0m (,,>_<,,)")
    for _, i in lideres_gimnasio.items():
        if i not in medallasObtenidas:
            print(f"    {i}")
    input("\n𓏵‧₊˚ ┊ Presione Enter para volver al menu.")

menucito()