<<<<<<< HEAD
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
=======
import bottle  # Uvoz knjižnice Bottle za spletni strežnik
import sqlite3  # Uvoz SQLite3 za delo z bazo podatkov
import os  # Uvoz knjižnice OS za delo s potmi do datotek
from datetime import datetime  # Uvoz knjižnice za delo z datumi

# Funkcija za odstranitev oklepajev in odvečnih presledkov iz podatkov
# Ta funkcija se uporablja pri podatkih iz baze, da odstranimo morebitne nepotrebne znake

def odstrani_odvecne_znake(tekst):
    if tekst:
        return tekst.split('(')[0]  # Odstrani vse od prvega oklepaja naprej
    return tekst  # Če je tekst prazen, vrne nespremenjen tekst

# Nastavimo pot do predlog HTML datotek na isto lokacijo, kjer je ta datoteka
bottle.TEMPLATE_PATH.insert(0, os.path.dirname(__file__))

# Nastavimo dostop do statičnih datotek (npr. slike)
@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='./static')  # Datoteke se strežejo iz mape static/

# Domača stran spletne aplikacije
@bottle.get("/")
def index():
    return bottle.template("index.html")  # Prikaže index.html

# API točka, ki vrne seznam vseh let, v katerih so bila evropska prvenstva
@bottle.get("/leta")
def leta():
    conn = sqlite3.connect("baza.sqlite")  # Povezava z bazo
    cursor = conn.execute("SELECT DISTINCT leto FROM prvenstva ORDER BY leto")
    leta = [row[0] for row in cursor.fetchall()]  # Seznam vseh let iz baze
    conn.close()
    bottle.response.content_type = 'application/json'
    return bottle.json_dumps(leta)  # Vrnemo podatke v JSON formatu

# Prikaz tekem za določeno leto
@bottle.get("/prvenstvo/<leto:int>")
def prvenstvo(leto):
    conn = sqlite3.connect("baza.sqlite")  # Povezava z bazo
>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
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
<<<<<<< HEAD
    return bottle.template("prvenstvo.html", leto=leto, tekme=tekme)

@bottle.get("/igralci/<leto:int>/<drzava>")
def igralci_drzave(leto, drzava):
    conn = sqlite3.connect("baza.sqlite")
    drzava = drzava.strip()  # Odstranimo odvečne presledke
=======
    return bottle.template("prvenstvo.html", leto=leto, tekme=tekme)  # Prikaže HTML predlogo prvenstva

# Prikaz igralcev določene države na prvenstvu v določenem letu
@bottle.get("/igralci/<leto:int>/<drzava>")
def igralci_drzave(leto, drzava):
    conn = sqlite3.connect("baza.sqlite")  # Povezava z bazo
    drzava = drzava.strip()  # Odstranimo odvečne presledke iz imena države
>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a

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
<<<<<<< HEAD
                rojstni_datum = datetime.strptime(str(int(rojstni_datum)), "%d%m%Y").strftime("%d.%m.%Y")
            except ValueError:
                rojstni_datum = "Neznan datum"
=======
                # Formatiramo datum iz oblike DDMYYYY v DD.MM.YYYY
                rojstni_datum = datetime.strptime(str(int(rojstni_datum)), "%d%m%Y").strftime("%d.%m.%Y")
            except ValueError:
                rojstni_datum = "Neznan datum"  # Če datum ni pravilne oblike, zapišemo "Neznan datum"
>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
        else:
            rojstni_datum = "Neznan datum"
        igralci.append({"ime_priimek": ime_priimek, "pozicija": pozicija, "rojstni_datum": rojstni_datum})

    conn.close()
<<<<<<< HEAD
    return bottle.template("igralci.html", drzava=drzava, igralci=igralci, leto=leto)

if __name__ == "__main__":
    bottle.run(host="localhost", port=8080, debug=True, reloader=True)
=======
    return bottle.template("igralci.html", drzava=drzava, igralci=igralci, leto=leto)  # Prikaže HTML predlogo igralcev

# Zagon Bottle spletnega strežnika
if __name__ == "__main__":
    bottle.run(host="localhost", port=8080, debug=True, reloader=True)  # Strežnik teče na localhost:8080
>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
