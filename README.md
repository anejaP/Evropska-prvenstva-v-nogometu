# Evropska prvenstva v nogometu
Projektna naloga pri Podatkovnih bazah 1

### Opis baze:
1. Podatkovna tabela **Prvenstva** bo vsebovala podatke o vseh tekmah na prvenstvih. Atributi bodo *id*, *datum*, *domaca_ekipa*, *gostujoca_ekipa*, *domaci_goli*, *gostujoci_goli*, *del_prvenstva*, *dodatek*, *stadion*, *mesto*, *stevilo_gledalcev* in *leto*.
2. Podatkovna tabela **Igralci** bo vsebovala podatke o igralcih neke države na posameznih prvenstvih. Atributi bodo *id*, *ime_in_priimek*, *ekipa*, *rojstni_datum* in *pozicija*.
3. Vmesna tabela **Ekipe** bo povezovala tabeli **Prvenstva** in **Igralci**. Prvenstva so z ekipo povezana preko leta in imena (domaca_ekipa ali gostujoca_ekipa). Pravtako pa je ekipa z igralci povezana preko leta in imena ekipe. 

Tako lahko za vsako prvenstvo dostopamo do tekem in njihovih podatkov ter do igralcev ekip.

![ER diagram](static/images/ER%20diagram.jpg)

