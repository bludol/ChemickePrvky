# Seznam indexů prvků v periodické tabulce, které mají být prázdné (blanks)
blanks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 93, 126]

# Seznam indexů řádků, kde mají být vloženy prázdné buňky mezi prvky (rows)
rows = [2, 10, 18, 36, 54, 86, 118]

# Řetězec reprezentující HTML kód prázdné buňky v tabulce
blanks_block = "<td class='blank'></td>"

# Funkce pro vytvoření HTML tabulky z poskytnutého seznamu slovníků (dict_list)
def tabulka(dict_list):
    # Začátek HTML dokumentu
    html_tabulka = "<!DOCTYPE html> <html> <head> <title>Chemicka tabulka</title> <link rel='stylesheet' href='style.css' /> </head> <body> <h1 class='title'>Chemicka tabulka</h1> <table> <tr>"
    
    # Inicializace řetězců pro zvláštní řádky lanthanoidů (lan) a aktinoidů (akt)
    lan = "<td class='blank'></td> <td class='blank'></td>"
    akt = "<td class='blank'></td> <td class='blank'></td>"
    
    # Otevření souboru index.html pro zápis
    f = open("index.html", "w")
    index = 1  # Inicializace indexu prvku v tabulce
    
    # Procházení seznamu slovníků a vytváření HTML kódu pro každý prvek
    for i in dict_list:
        # Ignorování prvku s názvem "AtomicNumber"
        if i[0] == "AtomicNumber":
            continue
        
        # Vložení prázdných buněk podle seznamu blanks
        for j in blanks:
            if j == index:
                html_tabulka += blanks_block
                index += 1
        
        # Vytvoření HTML kódu pro prvky lanthanoidů
        if 57 <= int(i[0]) <= 71:
            lan += "<td>"
            lan += f"<p class='nazev'>{i[1]}</p>"
            lan += f"<p class='pCislo'>{i[0]}</p>"
            lan += f"<p class='znacka'>{i[2]}</p>"
            lan += f"<p class='hmotnost'>{i[3]}</p>"
            lan += "</td>"
        # Vytvoření HTML kódu pro prvky aktinoidů
        elif 89 <= int(i[0]) <= 103:
            akt += "<td>"
            akt += f"<p class='nazev'>{i[1]}</p>"
            akt += f"<p class='pCislo'>{i[0]}</p>"
            akt += f"<p class='znacka'>{i[2]}</p>"
            akt += f"<p class='hmotnost'>{i[3]}</p>"
            akt += "</td>"
        # Vytvoření HTML kódu pro ostatní prvky
        else:
            html_tabulka += "<td>"
            html_tabulka += f"<p class='nazev'>{i[1]}</p>"
            html_tabulka += f"<p class='pCislo'>{i[0]}</p>"
            html_tabulka += f"<p class='znacka'>{i[2]}</p>"
            html_tabulka += f"<p class='hmotnost'>{i[3]}</p>"
            html_tabulka += "</td>"
        
        # Vložení prázdného řádku mezi prvky podle seznamu rows
        for j in rows:
            if j == int(i[0]):
                html_tabulka += "</tr> <tr>"
        
        index += 1  # Inkrementace indexu prvku
    
    # Zakončení HTML kódu
    html_tabulka += "</tr> <tr id=mezera> </tr>"
    html_tabulka += lan
    html_tabulka += "</tr>"
    html_tabulka += "<tr>"
    html_tabulka += akt
    html_tabulka += "</tr> </table> </body> </html>"
    
    # Zápis vytvořeného HTML kódu do souboru index.html
    f.write(html_tabulka)
    
