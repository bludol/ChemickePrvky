def vypis_samotneho_prvku(vyskyt, elements):
    for element in vyskyt:
        for i in range(len(element)):
            print(f"{elements[0][i]}:{element[i]}")
#vypíšeme název a element, který si uživatel vybral

def vypis_skupin(VolbaSkupiny, groups):
    nalezen = []
    vsechny_skupiny = []
    for group in groups:
        aktualni_skupina = []
        en_jmeno = group.get("en", "N/A")
        aktualni_skupina.append(f'{en_jmeno}')

        cz_jmeno = group.get("cs", "N/A")
        aktualni_skupina.append(f'{cz_jmeno}')

        popisek = group.get("description", "N/A")
        aktualni_skupina.append(f'{popisek}')

        prvky = group.get("elements", [])
        aktualni_skupina.append(prvky)

        vsechny_skupiny.append(aktualni_skupina)

    for i in range(len(vsechny_skupiny)):
        if VolbaSkupiny.lower() == vsechny_skupiny[int(i)][0].lower() or VolbaSkupiny.lower() == vsechny_skupiny[int(i)][1].lower():
            nalezen = vsechny_skupiny[i]
    return nalezen
#Rozkládáme prvky obsažené v groups na menší části. abychom v nich mohli hledat názvy skupin a ty poté porovnáváme s vstupem uživatele. 

def hledani(elements, prvek):
    found = []
    for element in elements:
        if prvek == element[0] or prvek.lower() == element[1].lower() or prvek.lower() == element[2].lower():
            found.append(element)
    return found
# hledáme shodu prvku s prvkem, který si uživatel vybral 
