<<<<<<< HEAD
import sqlite3  # Uvoz knjižnice za delo z SQLite bazo podatkov

# Funkcija za prikaz glavnega menija

def prikazi_meni():
    print("\nEVROPSKA PRVENSTVA V NOGOMETU")
    print("1. Prikaži seznam let")  # Prikaz vseh let, ko so potekala prvenstva
    print("2. Prikaži tekme za določeno leto")  # Izpis vseh tekem za izbrano leto
    print("3. Prikaži igralce določene države za določeno leto")  # Izpis igralcev določene države
    print("4. Izhod")  # Zaključi program

# Funkcija za pridobitev vseh let evropskih prvenstev iz baze

def pridobi_leta():
    conn = sqlite3.connect("baza.sqlite")  # Povezava z bazo podatkov
    cursor = conn.execute("SELECT DISTINCT leto FROM prvenstva ORDER BY leto")  # SQL poizvedba za vsa leta
    leta = [row[0] for row in cursor.fetchall()]  # Shrani rezultate v seznam
    conn.close()  # Zapre povezavo z bazo
    return leta

# Funkcija za prikaz vseh let prvenstev v terminalu

=======
# tekstovni_vmesnik.py
import sqlite3

def prikazi_meni():
    print("\nEVROPSKA PRVENSTVA V NOGOMETU")
    print("1. Prikaži seznam let")
    print("2. Prikaži tekme za določeno leto")
    print("3. Prikaži igralce določene države za določeno leto")
    print("4. Izhod")

def pridobi_leta():
    conn = sqlite3.connect("baza.sqlite")
    cursor = conn.execute("SELECT DISTINCT leto FROM prvenstva ORDER BY leto")
    leta = [row[0] for row in cursor.fetchall()]
    conn.close()
    return leta

>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
def prikazi_leta():
    leta = pridobi_leta()
    print("\nDostopna leta evropskih prvenstev:")
    for leto in leta:
<<<<<<< HEAD
        print(leto)  # Izpis posameznega leta

# Funkcija za pridobitev vseh tekem za določeno leto

def pridobi_tekme(leto):
    conn = sqlite3.connect("baza.sqlite")  # Povezava z bazo
=======
        print(leto)

def pridobi_tekme(leto):
    conn = sqlite3.connect("baza.sqlite")
>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
    tekme_query = """
    SELECT datum, domaca_ekipa, domaci_goli, gostujoca_ekipa, gostujoci_goli, stadion, mesto, del_prvenstva, dodatek
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
            "del_prvenstva": row[7],
            "dodatek": row[8],
        } for row in conn.execute(tekme_query, (leto,))
    ]
    conn.close()
    return tekme

<<<<<<< HEAD
# Funkcija za prikaz tekem za določeno leto v terminalu

def prikazi_tekme():
    leto = input("Vnesi leto prvenstva: ")  # Uporabnik vnese leto
    try:
        leto = int(leto)  # Pretvorba vnosa v celo število
=======
def prikazi_tekme():
    leto = input("Vnesi leto prvenstva: ")
    try:
        leto = int(leto)
>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
        tekme = pridobi_tekme(leto)
        if not tekme:
            print("Ni podatkov za izbrano leto.")
        else:
            print(f"\nTekme v letu {leto}:")
            for tekma in tekme:
                print(f"{tekma['datum']}: {tekma['domaca_ekipa']} {tekma['domaci_goli']} - {tekma['gostujoci_goli']} {tekma['gostujoca_ekipa']} ({tekma['stadion']}, {tekma['mesto']}) - {tekma['del_prvenstva']} {tekma['dodatek']}")
    except ValueError:
        print("Napaka: vnesi pravilno številko leta.")

<<<<<<< HEAD
# Funkcija za pridobitev igralcev določene države in leta iz baze

def pridobi_igralce(leto, drzava):
    conn = sqlite3.connect("baza.sqlite")  # Povezava z bazo
=======
def pridobi_igralce(leto, drzava):
    conn = sqlite3.connect("baza.sqlite")
>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
    igralci_query = """
    SELECT DISTINCT ime_priimek, pozicija, rojstni_datum FROM igralec WHERE leto = ? AND drzava = ?
    """
    igralci = [
        {
            "ime_priimek": row[0],
            "pozicija": row[1],
            "rojstni_datum": row[2] if row[2] else "Neznan datum",
        } for row in conn.execute(igralci_query, (leto, drzava))
    ]
    conn.close()
    return igralci

<<<<<<< HEAD
# Funkcija za prikaz igralcev določene države na prvenstvu

=======
>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
def prikazi_igralce():
    leto = input("Vnesi leto prvenstva: ")
    drzava = input("Vnesi ime države: ")
    try:
<<<<<<< HEAD
        leto = int(leto)  # Pretvorba vnosa v število
=======
        leto = int(leto)
>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
        igralci = pridobi_igralce(leto, drzava)
        if not igralci:
            print("Ni podatkov za izbrano državo in leto.")
        else:
            print(f"\nIgralci {drzava} na EP {leto}:")
            for igralec in igralci:
                print(f"{igralec['ime_priimek']} - {igralec['pozicija']} (Rojen: {igralec['rojstni_datum']})")
    except ValueError:
        print("Napaka: vnesi pravilno številko leta.")

<<<<<<< HEAD
# Glavna zanka programa, ki omogoča izbiro med funkcionalnostmi

=======
>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
def glavni_program():
    while True:
        prikazi_meni()
        izbira = input("Izberi možnost: ")
        if izbira == "1":
            prikazi_leta()
        elif izbira == "2":
            prikazi_tekme()
        elif izbira == "3":
            prikazi_igralce()
        elif izbira == "4":
            print("Izhod iz programa.")
<<<<<<< HEAD
            break  # Prekine izvajanje programa
        else:
            print("Neveljavna izbira. Poskusi znova.")

# Če je datoteka zagnana neposredno, se sproži glavni program
=======
            break
        else:
            print("Neveljavna izbira. Poskusi znova.")

>>>>>>> b2541e538c3cc1f5b8777b495d470598d16d8f0a
if __name__ == "__main__":
    glavni_program()
