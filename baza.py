import csv

PARAM_FMT = ":{}" # za SQLite

class Tabela:
    """
    Razred, ki predstavlja tabelo v bazi.

    Polja razreda:
    - ime: ime tabele
    - podatki: ime datoteke s podatki ali None
    """
    ime = None
    podatki = None

    def __init__(self, conn):
        self.conn = conn
    
    def ustvari(self):
        """Ustvari tabelo v bazi.

        Podrazredi morajo povoziti to metodo.
        """
        raise NotImplementedError
    
    def izbrisi(self):
        """Izbriše tabelo."""
        self.conn.execute(f"DROP TABLE IF EXISTS {self.ime};")
    
    def dodajanje(self, stolpci=None):
        """
        Metoda za gradnjo poizvedbe.

        Argumenti:
        - stolpci: seznam stolpcev
        """
        return f"""
            INSERT INTO {self.ime} ({", ".join(stolpci)})
            VALUES ({", ".join(PARAM_FMT.format(s) for s in stolpci)});
        """

    def dodaj_vrstico(self, **podatki):
        """
        Metoda za dodajanje vrstice.

        Argumenti:
        - poimenovani parametri: vrednosti v ustreznih stolpcih
        """
        podatki = {kljuc: vrednost for kljuc, vrednost in podatki.items()
                   if vrednost is not None}
        poizvedba = self.dodajanje(podatki.keys())
        cur = self.conn.execute(poizvedba, podatki)
        return cur.lastrowid

    def uvozi(self, encoding="UTF8"):
        if self.podatki is None:
            return None
        with open(self.podatki, encoding=encoding) as datoteka:
            podatki = csv.reader(datoteka)
            stolpci = next(podatki)
            for vrstica in podatki:
                podatek = {k: None if v == "" else v for k, v in zip(stolpci, vrstica)}
                self.dodaj_vrstico(**podatek)

class Prvenstva(Tabela):
    ime = 'prvenstva'
    podatki = 'prvenstva.csv'

    def ustvari(self):
        sql = """
            CREATE TABLE prvenstva (
                datum TEXT NOT NULL,
                domaca_ekipa TEXT NOT NULL,
                gostujoca_ekipa TEXT NOT NULL,
                domaci_goli INTEGER NOT NULL,
                gostujoci_goli INTEGER NOT NULL,
                del_prvenstva TEXT NOT NULL,
                dodatek TEXT NOT NULL,
                stadion TEXT NOT NULL,
                mesto TEXT NOT NULL,
                stevilo_gledalcev INTEGER NOT NULL,
                leto INTEGER NOT NULL
            );
        """
        self.conn.execute(sql)


class Igralci(Tabela):
    """"""
    ime = 'igralec'
    podatki = 'igralci.csv'

    def ustvari(self):
        sql="""
            CREATE TABLE igralec (
                ime TEXT NOT NULL,
                priimek TEXT NOT NULL,
                drzava TEXT NOT NULL,
                rojstni_datum TEXT NOT NULL,
                pozicija TEXT NOT NULL,
                leto_prvenstva INTEGER NOT NULL
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
    import sqlite3
    pripravi_bazo()
