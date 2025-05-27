import bottle
from model import Prvenstva, Tekma, Igralec

# Strezemo statične datoteke (slike, CSS, JavaScript)
@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='./static')

# Prikaz osnovne strani
@bottle.get('/')
def index():
    prvenstva = Prvenstva.pridobi_vsa_prvenstva()
    return bottle.template('index.html', prvenstva=prvenstva)

# Prikaz vseh let evropskih prvenstev
@bottle.get('/leta')
def leta():
    leta = [{"leto": p.leto, "drzava_gostiteljica": p.drzava_gostiteljica, "st_tekem": p.st_tekem} for p in Prvenstva.pridobi_vsa_prvenstva()]
    return bottle.json_dumps(leta)

# Prikaz tekem za določeno leto
@bottle.get('/prvenstvo/<leto:int>')
def prvenstvo(leto):
    prvenstvo = Prvenstva.pridobi_prvenstvo(leto)
    tekme = Tekma.pridobi_tekme_za_prvenstvo(leto)
    return bottle.template('prvenstvo.html', prvenstvo=prvenstvo, tekme=tekme)

# Prikaz igralcev določene ekipe na prvenstvu
@bottle.get("/igralci/<leto:int>/<drzava>")
def igralci_drzave(leto, drzava):
    drzava = drzava.strip()
    igralci = Igralec.pridobi_igralce_za_drzavo_in_leto(drzava, leto)
    return bottle.template("igralci.html", drzava=drzava, igralci=igralci, leto=leto)

# Zagon strežnika
if __name__ == "__main__":
    bottle.run(host="localhost", port=8080, debug=True, reloader=True)
