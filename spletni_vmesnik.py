import bottle
import sqlite3
import os
from datetime import datetime

# Funkcija za odstranitev oklepajev in odvečnih presledkov
def odstrani_odvecne_znake(tekst):
    if tekst:
        return tekst.split('(')[0]
    return tekst

# Nastavimo pot do predlog na isti direktorij kot datoteka spletni_vmesnik.py
bottle.TEMPLATE_PATH.insert(0, os.path.dirname(__file__))

# Dovolimo dostop do statičnih datotek
@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='./static')

@bottle.get("/")
def index():
    return bottle.template("index.html")

@bottle.get("/leta")
def leta():
    conn = sqlite3.connect("baza.sqlite")
    cursor = conn.execute("SELECT DISTINCT leto FROM prvenstva ORDER BY leto")
    leta = [row[0] for row in cursor.fetchall()]
    conn.close()
    bottle.response.content_type = 'application/json'
    return bottle.json_dumps(leta)

@bottle.get("/prvenstvo/<leto:int>")
def prvenstvo(leto):
    conn = sqlite3.connect("baza.sqlite")
    tekme_query = """
    SELECT datum, domaca_ekipa, domaci_goli, gostujoca_ekipa, gostujoci_goli, 
           stadion, mesto, stevilo_gledalcev, del_prvenstva, dodatek 
    FROM prvenstva WHERE leto = ?
    """
    tekme = [
        {
            "datum": odstrani_odvecne_znake(row[0]),
            "domaca_ekipa": odstrani_odvecne_znake(row[1]),
            "domaci_goli": row[2],
            "gostujoca_ekipa": odstrani_odvecne_znake(row[3]),
            "gostujoci_goli": row[4],
            "stadion": odstrani_odvecne_znake(row[5]),
            "mesto": odstrani_odvecne_znake(row[6]),
            "stevilo_gledalcev": row[7],
            "del_prvenstva": odstrani_odvecne_znake(row[8]),
            "dodatek": odstrani_odvecne_znake(row[9])
        } for row in conn.execute(tekme_query, (leto,))
    ]
    conn.close()
    return bottle.template("prvenstvo.html", leto=leto, tekme=tekme)

@bottle.get("/igralci/<leto:int>/<drzava>")
def igralci_drzave(leto, drzava):
    conn = sqlite3.connect("baza.sqlite")
    drzava = drzava.strip()  # Odstranimo odvečne presledke

    igralci_query = """
    SELECT DISTINCT ime_priimek, pozicija, rojstni_datum 
    FROM igralec 
    WHERE leto = ? AND drzava = ?
    """

    igralci = []
    for row in conn.execute(igralci_query, (leto, drzava)):
        ime_priimek, pozicija, rojstni_datum = row
        if rojstni_datum:
            try:
                rojstni_datum = datetime.strptime(str(int(rojstni_datum)), "%d%m%Y").strftime("%d.%m.%Y")
            except ValueError:
                rojstni_datum = "Neznan datum"
        else:
            rojstni_datum = "Neznan datum"
        igralci.append({"ime_priimek": ime_priimek, "pozicija": pozicija, "rojstni_datum": rojstni_datum})

    conn.close()
    return bottle.template("igralci.html", drzava=drzava, igralci=igralci, leto=leto)

if __name__ == "__main__":
    bottle.run(host="localhost", port=8080, debug=True, reloader=True)