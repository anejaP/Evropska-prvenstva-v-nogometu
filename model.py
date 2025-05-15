import sqlite3
from datetime import datetime  # Uvoz knjižnice za delo z datumi

class Prvenstva:
    def __init__(self, id, leto, drzava_gostiteljica, st_tekem):
        self.id = id
        self.leto = leto
        self.drzava_gostiteljica = drzava_gostiteljica
        self.st_tekem = st_tekem

    @staticmethod
    def pridobi_vsa_prvenstva():
        conn = sqlite3.connect("baza.sqlite")
        poizvedba = '''
        SELECT p.id, p.leto, p.drzava_gostiteljica, COUNT(t.id) AS st_tekem
        FROM prvenstva p
        LEFT JOIN tekme t ON p.leto = t.leto
        GROUP BY p.id, p.leto, p.drzava_gostiteljica
        ORDER BY p.leto;
        '''
        prvenstva = [Prvenstva(*vrsta) for vrsta in conn.execute(poizvedba)]
        conn.close()
        return prvenstva

    @staticmethod
    def pridobi_prvenstvo(leto):
        conn = sqlite3.connect("baza.sqlite")
        poizvedba = '''
        SELECT p.id, p.leto, p.drzava_gostiteljica, COUNT(t.id) AS st_tekem
        FROM prvenstva p
        LEFT JOIN tekme t ON p.leto = t.leto
        WHERE p.leto = ?
        GROUP BY p.id, p.leto, p.drzava_gostiteljica
        ORDER BY p.leto;
        '''
        vrsta = conn.execute(poizvedba, (leto,)).fetchone()
        conn.close()
        return Prvenstva(*vrsta) if vrsta else None

    def __repr__(self):
        return f"Prvenstvo(id={self.id}, leto={self.leto}, drzava_gostiteljica='{self.drzava_gostiteljica}', st_tekem={self.st_tekem})"


class Tekma:
    def __init__(self, id, datum, domaca_ekipa, gostujoca_ekipa, domaci_goli, gostujoci_goli, del_prvenstva, stadion, mesto, stevilo_gledalcev, leto):
        self.id = id
        self.datum = datum
        self.domaca_ekipa = domaca_ekipa
        self.gostujoca_ekipa = gostujoca_ekipa
        self.domaci_goli = domaci_goli
        self.gostujoci_goli = gostujoci_goli
        self.del_prvenstva = del_prvenstva
        self.stadion = stadion
        self.mesto = mesto
        self.stevilo_gledalcev = stevilo_gledalcev
        self.leto = leto

    @staticmethod
    def pridobi_tekme_za_prvenstvo(leto):
        conn = sqlite3.connect("baza.sqlite")
        poizvedba = '''
        SELECT id, datum, domaca_ekipa, gostujoca_ekipa, domaci_goli, gostujoci_goli, del_prvenstva, stadion, mesto, stevilo_gledalcev, leto
        FROM tekme
        WHERE leto = ?
        ORDER BY datum;
        '''
        tekme = [Tekma(*vrsta) for vrsta in conn.execute(poizvedba, (leto,))]
        conn.close()
        return tekme

    def __repr__(self):
        return f"Tekma(id={self.id}, datum='{self.datum}', domaca_ekipa='{self.domaca_ekipa}', gostujoca_ekipa='{self.gostujoca_ekipa}', domaci_goli={self.domaci_goli}, gostujoci_goli={self.gostujoci_goli}, del_prvenstva='{self.del_prvenstva}', stadion='{self.stadion}', mesto='{self.mesto}', stevilo_gledalcev={self.stevilo_gledalcev}, leto={self.leto})"


class Igralec:
    def __init__(self, id, ime_priimek, drzava, leto, pozicija, rojstni_datum=None):
        self.id = id
        self.ime_priimek = ime_priimek
        self.drzava = drzava
        self.leto = leto
        self.pozicija = pozicija
        self.rojstni_datum = self.formatiraj_datum(rojstni_datum)

    @staticmethod
    def pridobi_igralce_za_drzavo_in_leto(drzava, leto):
        conn = sqlite3.connect("baza.sqlite")
        poizvedba = '''
        SELECT DISTINCT ime_priimek, pozicija, rojstni_datum
        FROM igralci
        WHERE drzava = ? AND leto = ?
        ORDER BY ime_priimek;
        '''
        igralci = []
        for row in conn.execute(poizvedba, (drzava, leto)):
            ime_priimek, pozicija, rojstni_datum = row
            igralci.append(Igralec(None, ime_priimek, drzava, leto, pozicija, rojstni_datum))
        conn.close()
        return igralci

    @staticmethod
    def formatiraj_datum(rojstni_datum):
        if rojstni_datum:
            try:
                # Formatiramo datum iz oblike DDMYYYY v DD.MM.YYYY
                return datetime.strptime(str(int(rojstni_datum)), "%d%m%Y").strftime("%d.%m.%Y")
            except ValueError:
                return "Neznan datum"
        return "Neznan datum"
