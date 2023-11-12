import csv
import json
import hledani


def load_json_elements(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        groups = json.load(file)
    return groups


def load_csv_elements(csv_file):
    elements = []
    with open(csv_file, 'r', encoding="utf-8") as file:
        csv_txt = csv.reader(file)
        for row in csv_txt:
            elements.append(row)
            csv_row = ",".join(row)
    return elements


def vyber():
    print("1: Vyhledavani prvku")
    print("2: Periodicka tabulka")
    print("3: Vypocet")
    print("4: Vypnout program")


def main():
    elements = load_csv_elements('elements.csv')
    groups = load_json_elements('groups.json')

    while True:
        vyber()
        volba = input("Zadej svou volbu: ")
        if volba == "1":
            prvek = input("Zadej prvek, který chceš vyhledat: ")
            vyskyt = hledani.hledani(elements, prvek)
            if vyskyt:
                hledani.vypis_samotneho_prvku(vyskyt, elements)
        elif volba == "2":
            print("neni dodelano")
        elif volba == "3":
            print("neni dodelano")
        elif volba == "4":
            break


main()
