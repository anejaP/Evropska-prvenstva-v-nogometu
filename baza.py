import sqlite3
import csv

PARAM_FMT = ":{}"  # za SQLite

class Tabela:
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
        podatki = {k: v for k, v in podatki.items() if v is not None}
        poizvedba = self.dodajanje(podatki.keys())
        self.conn.execute(poizvedba, podatki)

    def uvozi(self, encoding="UTF8"):
        if self.podatki is None:
            return None
        try:
            with open(self.podatki, encoding=encoding) as datoteka:
                podatki = csv.reader(datoteka, delimiter=';')
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
        sql = '''
        CREATE TABLE prvenstva (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            leto INTEGER NOT NULL UNIQUE,
            drzava_gostiteljica TEXT NOT NULL
        );
        '''
        self.conn.execute(sql)


class Tekma(Tabela):
    ime = 'tekme'
    podatki = 'tekme.csv'

    def ustvari(self):
        sql = '''
        CREATE TABLE tekme (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datum TEXT NOT NULL,
            domaca_ekipa TEXT NOT NULL,
            gostujoca_ekipa TEXT NOT NULL,
            domaci_goli INTEGER NOT NULL,
            gostujoci_goli INTEGER NOT NULL,
            del_prvenstva TEXT NOT NULL,
            stadion TEXT NOT NULL,
            mesto TEXT NOT NULL,
            stevilo_gledalcev INTEGER NOT NULL,
            leto INTEGER NOT NULL,
            FOREIGN KEY (leto) REFERENCES prvenstva(leto)
        );
        '''
        self.conn.execute(sql)


class Igralec(Tabela):
    ime = 'igralci'
    podatki = 'igralci.csv'

    def ustvari(self):
        sql = '''
        CREATE TABLE igralci (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ime_priimek TEXT NOT NULL,
            drzava TEXT NOT NULL,
            rojstni_datum TEXT,
            leto INTEGER NOT NULL,
            pozicija TEXT NOT NULL
        );
        '''
        self.conn.execute(sql)


def pripravi_bazo():
    conn = sqlite3.connect("baza.sqlite")
    tabele = [Prvenstva(conn), Tekma(conn), Igralec(conn)]
    for tabela in tabele:
        tabela.izbrisi()
        tabela.ustvari()
        if tabela.podatki:
            tabela.uvozi()

    conn.commit()
    conn.close()


if __name__ == "__main__":
    pripravi_bazo()
