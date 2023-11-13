import csv
import json
import hledani
from os import remove
import os.path
import webbrowser
import tabulka


def load_json_elements(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        groups = json.load(file)
    return groups
#nacteni dat ze souboru groups.json

def load_csv_elements(csv_file):
    elements = []
    with open(csv_file, 'r', encoding="utf-8") as file:
        csv_txt = csv.reader(file)
        for row in csv_txt:
            elements.append(row)
            csv_row = ",".join(row)
    return elements
#nacteni dat ze souboru elements.csv


def vyber():
    print("1: Vyhledavani prvku")
    print("2: Periodicka tabulka")
    print("3: Vypis skupiny prvku")
    print("4: Vypnout program")
#funkce na vypsání vývběru

def main():
    elements = load_csv_elements('elements.csv')
    groups = load_json_elements('groups.json')
#vyvolani funkci k načtení dat
    while True:
        vyber()
#vypis vyběru
        volba = input("Zadej svou volbu: ")
#uživatelský vstup
        if volba == "1":
            prvek = input("Zadej protonové číslo, název nebo značku prvku, který chceš vyhledat: ")
            vyskyt = hledani.hledani(elements, prvek)
#Pokud je vybrána volba "1". Vyžádáme si vsatup pro hledání který pošleme do fuknce hledani s parametry elements a prvek.
            if vyskyt:
                hledani.vypis_samotneho_prvku(vyskyt, elements)
#Pokud je prvek nalezen, vypíše se pomocí funkce vypis_samostatneho_prvku s parametry vyskyt, elements.
        elif volba == "2":
            tabulka.tabulka(elements)
            path = os.path.abspath("index.html")
            url = "file://" + path
            webbrowser.open(url)
#Pokud je volba "2" Vytvoři se peridoická soustava prvků v tabulce a uloží se do souboru index.html.
        elif volba == "3":
            VolbaSkupiny = input("zadej nazev skupiny: ")
            vyskyt = hledani.vypis_skupin(VolbaSkupiny, groups)
            if vyskyt:
                print(vyskyt)
#Pokud je volba "3" Vyžádáme si vstup skupiny, kterou chceme hledat. vstup se pošle dofunkce vypis_skupin s parametry VolbaSkupiny, V případě nálezu se vypíše skupina.
        elif volba == "4":
            remove("index.html")
            break
#Při volbě "4" se vymaže index.html a ukončí se program.


main()
