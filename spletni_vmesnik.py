import bottle
import sqlite3
import os

# Nastavimo pot do predlog na isti direktorij kot datoteka spletni_vmesnik.py
bottle.TEMPLATE_PATH.insert(0, os.path.dirname(__file__))

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
            "datum": row[0],
            "domaca_ekipa": row[1],
            "domaci_goli": row[2],
            "gostujoca_ekipa": row[3],
            "gostujoci_goli": row[4],
            "stadion": row[5],
            "mesto": row[6],
            "stevilo_gledalcev": row[7],
            "del_prvenstva": row[8],
            "dodatek": row[9]
        }
        for row in conn.execute(tekme_query, (leto,))
    ]

    conn.close()
    return bottle.template("prvenstvo.html", leto=leto, tekme=tekme)

@bottle.get("/igralci/<leto:int>/<drzava>")
def igralci_drzave(leto, drzava):
    conn = sqlite3.connect("baza.sqlite")

    igralci_query = """
    SELECT ime_priimek, drzava, pozicija 
    FROM igralec WHERE leto = ? AND drzava = ?
    """
    igralci = [
        {
            "ime_priimek": row[0],
            "pozicija": row[2]
        }
        for row in conn.execute(igralci_query, (leto, drzava))
    ]

    conn.close()
    return bottle.template("igralci.html", drzava=drzava, igralci=igralci, leto=leto)

if __name__ == "__main__":
    bottle.run(host="localhost", port=8080, debug=True, reloader=True)
