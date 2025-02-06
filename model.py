import sqlite3

conn = sqlite3.connect('baza.sqlite')

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
    
    def __repr__(self):
        return f"Prvenstva({self.id}, {self.datum}, {self.domaca_ekipa}, {self.gostujoca_ekipa}, {self.domaci_goli}, {self.gostujoci_goli}, {self.del_prvenstva}, {self.dodatek})"
    
    @staticmethod
    def prvenstvo(prvenstvo):
        poizvedba = """SELECT * FROM prvenstva WHERE leto = ?"""
        for row in conn.execute(poizvedba, [prvenstvo.leto]):
            yield Prvenstva(*row)

class Igralci:
    def __init__(self, id, ime_priimek, drzava, rojstni_datum, pozicija):
        self.id = id
        self.ime_priimek = ime_priimek
        self.drzava = drzava
        self.rojstni_datum = rojstni_datum
        self.pozicija = pozicija

    def __str__(self):
        return f"{self.ime_priimek}, {self.drzava}, {self.rojstni_datum}, {self.pozicija}"
    
    def __repr__(self):
        return f"Igralci({self.id}, {self.ime_priimek}, {self.drzava}, {self.rojstni_datum}, {self.pozicija})"
    
    @staticmethod
    def igralec(igralec):
        poizvedba = """SELECT * FROM igralec WHERE leto = ?"""
        for row in conn.execute(poizvedba, [igralec.leto]):
            yield Igralci(*row)