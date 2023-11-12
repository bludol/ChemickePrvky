def vypis_samotneho_prvku(vyskyt, elements):
    for element in vyskyt:
        for i in range(len(element)):
            print(f"{elements[0][i]}:{element[i]}")


def hledani(elements, prvek):
    found = []
    for element in elements:
        if prvek == element[0] or prvek.lower() == element[1].lower() or prvek.lower() == element[2].lower():
            found.append(element)
    return found
