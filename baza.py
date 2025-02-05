import csv
import sqlite3

PARAM_FMT = ":{}"  # za SQLite

class Tabela:
    ''' ... '''
    ime = None
    podatki = None

    def __init__(self, conn):
        self.conn = conn
    
    def ustvari(self):
        raise NotImplementedError
    
    def izbrisi(self):
        self.conn.execute(f"DROP TABLE IF EXISTS {self.ime};")
    
    def dodajanje(self, stolpci=None):
        return f"""
            INSERT INTO {self.ime} ({", ".join(stolpci)})
            VALUES ({", ".join(PARAM_FMT.format(s) for s in stolpci)});
        """

    def dodaj_vrstico(self, **podatki):
        podatki = {kljuc: vrednost for kljuc, vrednost in podatki.items() if vrednost is not None}
        poizvedba = self.dodajanje(podatki.keys())
        cur = self.conn.execute(poizvedba, podatki)
        return cur.lastrowid

    def uvozi(self, encoding="UTF8"):
            if self.podatki is None:
                return None
            try:
                with open(self.podatki, encoding=encoding) as datoteka:
                    podatki = csv.reader(datoteka, delimiter=';')  # Pravilno ločilo
                    stolpci = next(podatki)
                    for vrstica in podatki:
                        podatek = {k: None if v == "" else v for k, v in zip(stolpci, vrstica)}
                        self.dodaj_vrstico(**podatek)
            except Exception as e:
                print(f"Napaka pri uvozu podatkov iz {self.podatki}: {e}")


class Prvenstva(Tabela):
    ime = 'prvenstva'
    podatki = 'prvenstva.csv'

    def ustvari(self):
        sql = """
            CREATE TABLE prvenstva (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                datum TEXT NOT NULL,
                domaca_ekipa TEXT NOT NULL,
                gostujoca_ekipa TEXT NOT NULL,
                domaci_goli INTEGER NOT NULL,
                gostujoci_goli INTEGER NOT NULL,
                del_prvenstva TEXT NOT NULL,
                dodatek TEXT,
                stadion TEXT NOT NULL,
                mesto TEXT NOT NULL,
                stevilo_gledalcev INTEGER,
                leto INTEGER NOT NULL
            );
        """
        self.conn.execute(sql)


class Igralci(Tabela):
    """
    Tabela za igralce. Vsebuje podatke o imenu, priimku, državi, rojstnem datumu, poziciji in letu prvenstva.
    """
    ime = 'igralec'
    podatki = 'igralci.csv'

    def ustvari(self):
        sql = """
            CREATE TABLE igralec (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ime_priimek TEXT NOT NULL,
                drzava TEXT,
                rojstni_datum TEXT,
                pozicija TEXT,
                leto INTEGER NOT NULL
            );
        """
        self.conn.execute(sql)


def pripravi_bazo():
    conn = sqlite3.connect("baza.sqlite")
    prvenstvo = Prvenstva(conn)
    igralec = Igralci(conn)
    prvenstvo.izbrisi()
    igralec.izbrisi()
    prvenstvo.ustvari()
    igralec.ustvari()
    prvenstvo.uvozi()
    igralec.uvozi()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    pripravi_bazo()
