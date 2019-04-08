# Python projekt

## Opis programa

Namen programa je da uporabniku, ki ve v katero področje in vrsto izobrazbe bi se rad vpisal v srednji šoli, pove v katerih regijah v Sloveniji je vpis možen in kje je bilo v preteklosti vpisanih največ dijakov v izbrane programe. Rezultate njegove poizvedbe mu predstavimo grafično in tekstovno. Na grafu je prikazano v kateri regiji je bilo vpisanih koliko študentov, regije v katerih se na področje ni vpisal nihče so izpuščene, za vsako leto s katerega so vzeti podatki naredi nov graf, program pa tudi izpiše v kateri regiji je bilo vpisanih največ študentov.

Program podatke vzame z excelove tabele, ki je vzeta s spletne strani OPSI. Podatke s tabele prepišemo v 4D tabelo, v kateri s 1. indeksom dostopamo do leta z 2. do regije, s 3. do področja in s 4. do vrste izobrazbe. Program podatke prebere pravilno tudi, če v tabelo dodamo podatke za več let, vendar če bi katero izmed regij, področij ali pa vrst razcepili na več le teh, ali pa bi dodali nove, program ne bi več deloval pravilno in bi ga bilo potrebno popraviti.

Ko uporabnik vnese področje in vrsto izobraževanja, program iz 4d tabele vzame podatke za vsa leta in regije, in samo za izbrano področje in vrsto. Nato iz teh podatkov naredi grafe in izpiše leto in regijo z maksimalnim št. vpisov.

## Navodila za uporabo

V mapi kjer je datoteka Projekt_Py.py mora biti tudi datoteka, ki vsebuje excelovo tabelo (format csv), ime datoteke mora biti: '0953371S1.csv'. V primeru spreminjanja/dodajanja podatkov v datoteki mora uporabnik upoštevati vzorec po katerem so podatki že vpisani, če ne program morda ne bo deloval pravilno.

Prvi vnos mora biti niz iz tabele:
```py
Tab_podrocij = ['Splošne izobraževalne aktivnosti','Izobraževalne vede in izobraževanje učiteljev','Umetnost in humanistika','Družbene, poslovne, upravne in pravne vede','Naravoslovje, matematika in računalništvo','Tehnika, proizvodne tehnologije in gradbeništvo','Kmetijstvo, gozdarstvo, ribištvo, veterinarstvo','Zdravstvo in sociala','Storitve']
```

Drugi vnos mora biti niz iz tabele:
```py
Tab_vrst = ['Nižje poklicno','Srednje poklicno','srednje tehniško in dr. strokovno','poklicno tehniško','poklicni tečaj','splošna in strokovna gimnazija','maturitetni tečaj',]
```

Če se v program izbranega področja in vrste v letih s katerih so pridobljeni podatki ni vpisal nihče, bo program izpisal:
```py
'V ta program se v letih s katerih so vzeti podatki ni vpisal nihče.'
```

V nasprotnem primeru pa se bo izpisalo leto v katerem je bil dosežen maksimalni vpis in št. dijakov ki so se takrat vpisali. Prav tako se bo odprlo novo okence (po potrebi okence raztegnemo za bolši pregled) na katerem bo izrisan graf, kjer lahko vidimo št. vpisanih dijakov v posamezni regiji. Za vsako leto se bo odprlo novo okence z grafom, da se odpre naslednje okence je potrebno prejšnjega zapreti.
