# Evropska prvenstva v nogometu
Projektna naloga pri Podatkovnih bazah 1

Spletna stran omogoča pregled nad vsemu evropskimi prvenstvi. Dostopamo lahko do vseh tekem vsakega leta. Tam je pregled informacij za posamezno tekmo (npr. faza tekmovanja, število gledalcev itd.). Preko tekem pa lahko za vsako državo dostopamo do njenih igralcev in njihovih podatkov.

### Opis baze:
1. Podatkovna tabela **Prvenstva** bo vsebovala leta in gostiteljice prvenstev. Atributi bodo *id*, *leto*, *drzava_gostiteljica*.
2. Podatkovna tabela **Tekme** bo vsebovala podatke o vseh tekmah na prvenstvih. Atributi bodo *id*, *datum*, *domaca_ekipa*, *gostujoca_ekipa*, *domaci_goli*, *gostujoci_goli*, *del_prvenstva*, *stadion*, *mesto*, *stevilo_gledalcev* in *leto*.
3. Podatkovna tabela **Igralci** bo vsebovala podatke o igralcih neke države na posameznih prvenstvih. Atributi bodo *id*, *ime_in_priimek*, *drzava*, *rojstni_datum* in *pozicija*.


Tako lahko za vsako prvenstvo dostopamo do tekem in njihovih podatkov ter do igralcev ekip.

![ER diagram](static/images/ER%20diagram.jpg)

