from model import Prvenstva, Tekma, Igralec

# Funkcija za prikaz glavnega menija

def prikazi_meni():
    print("\nEVROPSKA PRVENSTVA V NOGOMETU")
    print("1. Prikaži seznam let")
    print("2. Prikaži tekme za določeno leto")
    print("3. Prikaži igralce določene države za določeno leto")
    print("4. Izhod")

# Funkcija za prikaz vseh let evropskih prvenstev

def prikazi_leta():
    prvenstva = Prvenstva.pridobi_vsa_prvenstva()
    print("\nDostopna leta evropskih prvenstev:")
    for prvenstvo in prvenstva:
        print(prvenstvo.leto)

# Funkcija za prikaz vseh tekem za določeno leto

def prikazi_tekme():
    leto = input("Vnesi leto prvenstva: ")
    try:
        leto = int(leto)
        tekme = Tekma.pridobi_tekme_za_prvenstvo(leto)
        if not tekme:
            print("Ni podatkov za izbrano leto.")
        else:
            print(f"\nTekme v letu {leto}:")
            for tekma in tekme:
                print(f"{tekma.datum}: {tekma.domaca_ekipa} {tekma.domaci_goli} - {tekma.gostujoci_goli} {tekma.gostujoca_ekipa} ({tekma.stadion}, {tekma.mesto}) - {tekma.del_prvenstva}")
    except ValueError:
        print("Napaka: vnesi pravilno številko leta.")

# Funkcija za prikaz igralcev določene države in leta

def prikazi_igralce():
    leto = input("Vnesi leto prvenstva: ")
    drzava = input("Vnesi ime države: ")
    try:
        leto = int(leto)
        igralci = Igralec.pridobi_igralce_za_drzavo_in_leto(drzava.strip(), leto)
        if not igralci:
            print("Ni podatkov za izbrano državo in leto.")
        else:
            print(f"\nIgralci {drzava} na EP {leto}:")
            for igralec in igralci:
                print(f"{igralec.ime_priimek} - {igralec.pozicija} (Rojen: {igralec.rojstni_datum})")
    except ValueError:
        print("Napaka: vnesi pravilno številko leta.")

# Glavna zanka programa, ki omogoča izbiro med funkcionalnostmi

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
            break
        else:
            print("Neveljavna izbira. Poskusi znova.")

# Če je datoteka zagnana neposredno, se sproži glavni program
if __name__ == "__main__":
    glavni_program()
