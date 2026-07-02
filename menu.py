from catalogo import cargar_pokedex, cargar_medallas, HashMap, medallasObtenidas
from gestion import equipo, PC, centroPokemon, transferidos
import random, os, time
import colores as c

lideres_gimnasio = None
Pokedex = None

def cargar():
    global Pokedex, lideres_gimnasio
    Pokedex = HashMap()

    cargar_pokedex("pokedex.json", Pokedex)

    lideres_gimnasio = cargar_medallas("medallas.json")

def menucito():
    seguir = True
    while seguir:
        os.system("cls")
        print(f"{c.rosa}⋆˙⟡♡ ๋࣭ ⭑ {c.bold}¡Pokemon Huergo!{c.reset}{c.rosa} ໒꒰ྀིっ˕ -｡꒱ྀི১ ₊˚⊹♡{c.reset} \n")
        print(f"{c.rosita}⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔ ꒰ ᧔ෆ݁݁᧓ ꒱⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔{c.reset}")
        print(f"{c.rosa}1-{c.reset} Ver Pokédex")
        print(f"{c.rosa}2-{c.reset} Ver Equipo Principal")
        print(f"{c.rosa}3-{c.reset} Ver PC")
        print(f"{c.rosa}4-{c.reset} Ver Medallas")
        print(f"{c.rosa}5-{c.reset} Capturar nuevo Pokémon")
        print(f"{c.rosa}6-{c.reset} Ordenar PC")
        print(f"{c.rosa}7-{c.reset} Buscar Pokémon en Equipo")
        print(f"{c.rosa}8-{c.reset} Enviar Pokémon al Centro Pokémon")
        print(f"{c.rosa}9-{c.reset} Transferir Pokémon al Profesor Oak")
        print(f"{c.rosa}10-{c.reset} Deshacer última transferencia")
        print(f"{c.rosa}11-{c.reset} Desafiar Líder de Gimnasio")
        print(f"{c.rosa}12-{c.reset} Cambiar el Equipo")
        print(f"{c.rosa}13-{c.reset} Salir del sistema")
        print(f"{c.rosita}───────────────୨ৎ───────────────{c.reset}\n")

        selec = input(f"{c.rosita}݁ ˖Ი𐑼⋆{c.reset} Seleccione una opción {c.rosita}݁ ˖Ი𐑼⋆  {c.reset}")
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
            os.system("cls")
            cambiar_equipo()
        elif selec == "13":
            seguir = False
        else:
            os.system("cls")
            print(f"{c.rosita}Opción no válida. {c.rosa}₍^. .^₎Ⳋ{c.reset}")
            input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def ver_pokedex():
    print(f"⋆｡‧˚ʚ{c.bold}{c.rosa} Pokedex {c.reset}ɞ˚‧｡⋆\n")
    for e in Pokedex.buckets:
        for key, pokemon in e:
            print(f"{c.rosita}{key}-{c.reset} {pokemon}")
    selec = input(f"\nʚɞ ⁺˖ ⸝⸝ ¿Querés buscar un pokemon en específico? (y/n): {c.rosita}")
    print(c.reset)
    if selec.lower() == "y":
        try:
            pok = int(input(f"{c.rosita} ׅ 𝄂𝄚𝅦𝄚𝄞𝅄{c.reset} Ingrese el ID: "))
        except ValueError:
            print(f"El ID debe ser un {c.rosa}número{c.reset}. ˚. ꉂ(˵˃ ᗜ ˂˵) ᵎᵎ")
            return
        resultado = busq_pokedex(pok)
        if resultado != -1:
            pokemoncito = Pokedex.buscar(pok)
            print(f"\n¡El pokemon {c.bold}{c.rosita}sí{c.reset} se encuentra en la Pokedex! ‧₊˚♪ 𝄞₊˚⊹ Es {c.rosa}{pokemoncito.nombre}{c.reset}. ♬⋆.˚")
        else:
            print(f"\nEl pokemon {c.bold}{c.rosita}no{c.reset} se encuentra en la Pokedex. (˶˃ ᵕ ˂˶) ᵎ!ᵎ")
    elif selec.lower() == "n":
        pass
    else:
        os.system('cls')
        print(f"{c.rosita}Opción no válida. {c.rosa}₍^. .^₎Ⳋ{c.reset}")
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

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
        print(f"No tienes pokemons en tu {c.rosita}equipo{c.reset} todavía. ૮◞ ‸ ◟ ა")
    else:
        print(f"{c.bold}{c.rosa}Equipo:{c.reset} ₍₍⚞(˶>ᗜ<˶)⚟⁾⁾\n")
        for e in equipo:
            print(e)
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def ver_pc():
    if PC.tamaño() > 0:
        print(f"{c.bold}{c.rosa}PC:{c.reset} (˶ᵔᗜᵔ˶)ﾉﾞ\n")
        PC.recorrer()
    else:
        print(f"No tienes pokemons en tu {c.rosita}PC{c.reset} todavía. ૮◞ ‸ ◟ ა")
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def capturar_pok():
    pok = Pokedex.elegir_random()
    print(f"Ha aparecido un {c.bold}{c.rosa}{pok.nombre}{c.reset} salvaje (PC: {pok.poder_combate}). (˶ˆᗜˆ˵).ᐟ\n")
    captura = random.getrandbits(1)
    if captura == 1:
        print(f". ݁₊ ⊹ . ݁˖ . ݁ {c.rosita}¡Captura exitosa!{c.reset} . ݁₊ ⊹ . ݁˖ . ݁")
        print(f"ദ്ദി◝ ⩊ ◜.ᐟ Equipo Principal: {c.rosa}{len(equipo)}/6{c.reset}")
        if len(equipo) < 6:
            equipo.append(pok)
            print(f"¡Pokemon {c.rosita}añadido{c.reset} al equipo! ({len(equipo)}/6) ꉂ(˵˃ ᗜ ˂˵)")
        else:
            print(f"Está {c.rosita}lleno{c.reset}. Derivando a almacenamiento de {c.rosa}PC{c.reset}... *ੈ✩‧₊˚")
            PC.agregar(pok)
            print(f"⤷ ゛ ˎˊ˗ Registro {c.rosita}añadido{c.reset} exitosamente. ₊˚⊹♡")
    else:
        print(f"⋆˚࿔ {c.rosita}Captura fallida{c.reset}... (˶°ㅁ°)!!")
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def ordenar_pc():
    print(f"{c.rosa}1-{c.reset} Ordenar alfabeticamente")
    print(f"{c.rosa}2-{c.reset} Ordenar por tipo")
    print(f"{c.rosa}3-{c.reset} Ordenar por poder de combate\n")
    
    selec = input(f"{c.rosita}݁ ˖Ი𐑼⋆{c.reset} Seleccione una opción {c.rosita}݁ ˖Ი𐑼⋆  {c.reset}")
    
    if PC.tamaño() > 0:
        if selec == "1":
            PC.orden_alfabetico()
        elif selec == "2":
            PC.orden_tipo()
        elif selec == "3":
            PC.orden_competitivo()
        else:
            print(f"{c.rosita}Opción no válida. {c.rosa}₍^. .^₎Ⳋ{c.reset}")
            input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")
            return
        print(f"⋆.˚ Se ordenó la PC. Seleccione {c.rosa}'Ver PC'{c.reset} en el {c.rosita}menu{c.reset} para ver los cambios. (˶ᵔ ᵕ ᵔ˶) <3")
    else:
        print(f"{c.rosita}No{c.reset} hay pokemons en la {c.rosa}PC{c.reset} todavía... “(ノ _ <,, )")
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def buscar_pok():
    if len(equipo) > 0:
        pok = input(f"✧˖°. Ingrese el {c.rosa}nombre{c.reset} de un {c.rosita}pokemon{c.reset}: ")
        for e in equipo:
            if e.nombre.lower() == pok.lower():
                print(f"El pokemon {c.rosita}sí{c.reset} se encuentra en el equipo. ૮ ྀིᴗ͈ . ᴗ͈ ྀིა")
                print(f"⋆ ˚｡⋆{c.rosita}୨୧{c.reset}˚ ¡Es un pokemon {c.rosita}tipo {c.rosa}{e.tipo}{c.reset} y su {c.rosita}poder de combate{c.reset} es {c.rosa}{e.poder_combate}{c.reset}! ٩(^ᗜ^ )و ´-")
                input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")
                return
        print(f"El pokemon {c.rosita}no{c.reset} se encuentra en el equipo. ૮꒰◞ ˕ ◟ ྀི꒱ა")
    else:
        print(f"♡⸝⸝ ¡El {c.rosita}equipo{c.reset} está {c.rosa}vacío{c.reset}! {c.rosita}₍ᐢ. .ᐢ₎ ₊˚⊹♡{c.reset}")
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def enviar_centropokemon():
    print(f"𝄞⨾💿✮˚.⋆ Ingresando {c.rosa}equipo{c.reset} a la {c.rosita}cola{c.reset}...\n")
    for pok in equipo:
        centroPokemon.enqueue(pok)
    
    while centroPokemon.head is not None:
        pok = centroPokemon.dequeue()
        print(f"⋆౨ৎ˚⟡˖ ࣪ {c.rosa}{pok.nombre}{c.reset} se está curando", end="", flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("")
        time.sleep(1)
    print(f"\n¡Todos los pokemons fueron {c.rosita}curados{c.reset}! ⸜(｡˃ ᵕ ˂ )⸝♡")
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def transferir_oak():
    temp = []
    actual = PC.head
    i = 1
    while actual:
        print(f"{c.rosa}{i}-{c.reset} {actual.dato.nombre}")
        temp.append(actual.dato)
        actual = actual.siguiente
        i += 1
    if PC.tamaño() == 0:
        print(f"⊹ ࣪ ˖ No tenes {c.rosita}pokemons{c.reset} para transferir. (,,>_<,,)")
    else:
        try:
            selec = int(input(f"\n꒰ྀི১ ໒꒱ིྀ ¿Qué {c.rosita}pokemon{c.reset} querés {c.rosa}transferir{c.reset}?: "))
        except ValueError:
            print(f"\nDebe ingresar un {c.rosita}número{c.reset}. ˚. ꉂ(˵˃ ᗜ ˂˵) ᵎᵎ")
            input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")
            return
        if selec > 0 and selec < i:
            os.system("cls")
            PC.eliminar(temp[selec-1])
            print(f"Transfiriendo {c.rosa}{temp[selec-1].nombre}{c.reset} al Profesor Oak... ˚ ༘ ೀ⋆｡˚")
            
            if transferidos.size() < 5:
                transferidos.push(temp[selec-1])
            else:
                actual = transferidos.lista.head
                while actual.siguiente.siguiente:
                    actual = actual.siguiente
                actual.siguiente = None
                
                transferidos.push(temp[selec-1])
            
            time.sleep(0.5)
            print(f"¡{c.rosita}Pokemon transferido{c.reset} con éxito! ༉‧₊˚.")
        else:
            print(f"{c.rosita}Opción no válida. {c.rosa}₍^. .^₎Ⳋ{c.reset}")
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def deshacer_transf():
    if transferidos.size() < 1:
        print(f"{c.rosita}No{c.reset} hay {c.rosita}pokemons{c.reset} que recuperar. (˶˃𐃷˂˶)")
    else:
        print(f"⋆｡‧˚ʚ ୨ৎ {c.rosa}Recuperando{c.reset} último pokemon...")
        pok = transferidos.pop()
        PC.agregar(pok)
        print(f"{c.rosita}{pok.nombre}{c.reset} ha vuelto a la PC. 𐔌՞ ܸ.ˬ.ܸ՞𐦯")
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def desafiar_lider(): #decorar Y PONER c EN LOS PRINTS DE LIDERES Y MEDALLAS.
    if len(equipo) < 1:
        print(f"¡Debes tener un {c.rosa}equipo{c.reset} para desafiar a un {c.rosita}líder{c.reset}! (˶ˆᗜˆ˵)!!")
    else:
        cont = 1
        for e, i in lideres_gimnasio.items():
            print(f"{c.rosa}{cont}-{c.reset} Líder {e} ({c.rosita}{i}{c.reset})")
            cont += 1
        
        try:
            selec = int(input(f"٩(ˊᗜˋ*)و ♡ ¿Contra qué {c.rosita}líder{c.reset} querés pelear?: "))
            ls_lideres = list(lideres_gimnasio.items())
            lider, med = ls_lideres[selec-1]
        except (IndexError, ValueError):
            print(f"{c.rosita}Opción no válida. {c.rosa}₍^. .^₎Ⳋ{c.reset}")
        else:
            print(f"Estás a punto de pelear contra {c.rosita}{lider}{c.reset} por la {c.rosa}{med}{c.reset}. ₍₍⚞(˶>ᗜ<˶)⚟⁾⁾")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print("")
            
            victoria = random.getrandbits(1)
            if victoria == 1:
                print (f"₊⊹ ¡{c.rosita}Ganaste{c.reset} la pelea! {c.rosa}٩(ˊᗜˋ*)و ♡{c.reset}")
                if med in medallasObtenidas:
                    print(f". ݁₊ ⊹ . ݁ Parece que {c.rosita}ya tienes{c.reset} está medalla.")
                    print(f"¡Felicidades por derrotar a {c.rosa}{lider}{c.reset} una vez más! ₍ᐢ. .ᐢ₎ ₊˚⊹♡")
                else:
                    print(f"♡⸝⸝ Obtuviste la {c.verde}{med}{c.reset}, {c.rosa}¡{c.rosita}Felicidades{c.rosa}!{c.reset} ₍₍⚞(˶>ᗜ<˶)⚟⁾⁾")
                    medallasObtenidas.append(med)
            else:
                print(f"༄.° {c.rosita}Perdiste{c.reset} la pelea... ( ˶°ㅁ°) !!")
                print(f"✶⋆.˚ ¡Mejor {c.rosa}suerte{c.reset} la próxima! ദ്ദി◝ ⩊ ◜.ᐟ")
    
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def ver_medallas():
    print(f">⩊< {c.bold}{c.rosa}Medallas Obtenidas:{c.reset} (๑ᵔ⤙ᵔ๑)")
    for e in medallasObtenidas:
        print(f"    {e}")
    print(f"\n>⩊< {c.bold}{c.rosa}Medallas No Obtenidas:{c.reset} (,,>_<,,)")
    for _, i in lideres_gimnasio.items():
        if i not in medallasObtenidas:
            print(f"    {c.rosita}{i}")
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")

def cambiar_equipo(): #decorar
    if len(equipo) < 1 or PC.tamaño() < 1:
        print(f"No tienes pokemons en tu {c.rosita}equipo{c.reset} o {c.rosita}PC{c.reset} todavía. ૮◞ ‸ ◟ ა")
    else:
        print(f"{c.bold}{c.rosa}Equipo:{c.reset} ₍₍⚞(˶>ᗜ<˶)⚟⁾⁾\n")
        cont = 1
        for e in equipo:
            print(f"{c.rosa}{cont}-{c.reset} {e.nombre}")
            cont += 1
        try:
            selec = int(input(f"\n(˵◝ ⩊  ◜˵マ ¿A qué {c.rosita}pokemon{c.reset} querés {c.rosa}cambiar{c.reset}?: ")) 
        except ValueError:
            print(f"{c.rosita}Opción no válida. {c.rosa}₍^. .^₎Ⳋ{c.reset}")
            input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")
            return
        if selec > 0 and selec <= len(equipo):
            sacar = selec-1
            
            os.system("cls")
            temp = []
            actual = PC.head
            i = 1
            while actual:
                print(f"{c.rosa}{i}-{c.reset} {actual.dato.nombre}")
                temp.append(actual.dato)
                actual = actual.siguiente
                i += 1
            try:
                selec_pc = int(input(f"\n✧˖°. (๑>◡<๑) ¿A qué {c.rosita}pokemon{c.reset} querés poner en tu {c.rosa}equipo{c.reset}?: "))
            except ValueError:
                print(f"{c.rosita}Opción no válida. {c.rosa}₍^. .^₎Ⳋ{c.reset}")
                input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")
                return
            if selec_pc > 0 and selec_pc <= PC.tamaño():
                PC.agregar(equipo[sacar])
                equipo.pop(sacar)
                equipo.append(temp[selec_pc-1])
                PC.eliminar(temp[selec_pc-1])
                print(f"₊˚⊹♡ ¡{c.rosita}Cambio{c.reset} realizado con {c.rosa}éxito{c.reset}! ◝(ᵔᗜᵔ)◜")
            else:
                print(f"{c.rosita}𝜗ৎ{c.reset} ¡Elección fuera de {c.rosa}rango{c.reset}!. ˚. ꉂ(˵˃ ᗜ ˂˵) ᵎᵎ")
        else:
            print(f"{c.rosita}𝜗ৎ{c.reset} ¡Elección fuera de {c.rosa}rango{c.reset}!. ˚. ꉂ(˵˃ ᗜ ˂˵) ᵎᵎ")
    input(f"\n{c.rosita}𓏵‧₊˚ ┊{c.reset} Presione {c.rosa}Enter{c.reset} para volver al menu.")