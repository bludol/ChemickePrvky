grid = 162
blanks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 93, 126]
rows = [2, 10, 18, 36, 54, 86, 118]
blanks_block = "<td class='blank'></td>"


def tabulka(dict_list):
    html_tabulka = "<!DOCTYPE html> <html> <head> <title>Chemicka tabulka</title> <link rel='stylesheet' href='style.css' /> </head> <body> <h1 class='title'>Chemicka tabulka</h1> <table> <tr>"
    lan = "<td class='blank'></td> <td class='blank'></td>"
    akt = "<td class='blank'></td> <td class='blank'></td>"
    f = open("index.html", "w")
    index = 1

    for i in dict_list:
        if i[0] == "AtomicNumber":
            continue
        for j in blanks:
            if j == index:
                html_tabulka += blanks_block
                index += 1
        if 57 <= int(i[0]) <= 71:
            lan += "<td>"
            lan += f"<p class='nazev'>{i[1]}</p>"
            lan += f"<p class='pCislo'>{i[0]}</p>"
            lan += f"<p class='znacka'>{i[2]}</p>"
            lan += f"<p class='hmotnost'>{i[3]}</p>"
            lan += "</td>"
        elif 89 <= int(i[0]) <= 103:
            akt += "<td>"
            akt += f"<p class='nazev'>{i[1]}</p>"
            akt += f"<p class='pCislo'>{i[0]}</p>"
            akt += f"<p class='znacka'>{i[2]}</p>"
            akt += f"<p class='hmotnost'>{i[3]}</p>"
            akt += "</td>"
        else:
            html_tabulka += "<td>"
            html_tabulka += f"<p class='nazev'>{i[1]}</p>"
            html_tabulka += f"<p class='pCislo'>{i[0]}</p>"
            html_tabulka += f"<p class='znacka'>{i[2]}</p>"
            html_tabulka += f"<p class='hmotnost'>{i[3]}</p>"
            html_tabulka += "</td>"

        for j in rows:
            if j == int(i[0]):
                html_tabulka += "</tr> <tr>"

        index += 1
    html_tabulka += "</tr> <tr id=mezera> </tr>"
    html_tabulka += lan
    html_tabulka += "</tr>"
    html_tabulka += "<tr>"
    html_tabulka += akt
    html_tabulka += "</tr> </table> </body> </html>"
    f.write(html_tabulka)

