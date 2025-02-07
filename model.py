import sqlite3

class Prvenstva:
    def __init__(self, id, datum, domaca_ekipa, gostujoca_ekipa, domaci_goli, gostujoci_goli, del_prvenstva, dodatek):
        self.id = id
        self.datum = datum
        self.domaca_ekipa = domaca_ekipa
        self.gostujoca_ekipa = gostujoca_ekipa
        self.domaci_goli = domaci_goli
        self.gostujoci_goli = gostujoci_goli
        self.del_prvenstva = del_prvenstva
        self.dodatek = dodatek

    def __str__(self):
        return f"{self.datum}, {self.domaca_ekipa} {self.domaci_goli} : {self.gostujoca_ekipa} {self.gostujoci_goli}, {self.del_prvenstva}, {self.dodatek}"

    @staticmethod
    def prvenstvo(prvenstvo):
        poizvedba = "SELECT * FROM prvenstva WHERE leto = ?"
        with sqlite3.connect('baza.sqlite') as conn:
            rezultat = conn.execute(poizvedba, (prvenstvo,))
            return [Prvenstva(*vrsta) for vrsta in rezultat.fetchall()]

class Igralec:
    def __init__(self, ime_priimek, pozicija):
        self.ime_priimek = ime_priimek
        self.pozicija = pozicija

    def __str__(self):
        return f"{self.ime_priimek} (Pozicija: {self.pozicija})"

def igralci_drzave_in_leto(drzava, leto):
    conn = sqlite3.connect("baza.sqlite")
    query = "SELECT ime_priimek, pozicija FROM igralec WHERE drzava = ? AND leto = ?"
    igralci = conn.execute(query, (drzava, leto)).fetchall()
    conn.close()
    return [Igralec(row[0], row[1]) for row in igralci]