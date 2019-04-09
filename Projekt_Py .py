try:
    file = open('0953371S1.csv', 'r')
except:
    print('V mapi kjer je shranjen program ni datoteke z imenom "0953371S1.csv"')

for i, vr in enumerate(file):
    if i == 0: #prva vr, z nje preberemo naslov
        naslov = vr[:-1].strip(';') #tu je sedaj naslov v nizu
    elif i == 2: #tretja vr z letnicami
        letnice = ' '.join(vr.split(';')).split() #tabela letnic, dolžina tabele nam pove za koliko let imamo podatke
    if i == 3:
        break

D_tabela = [] #"bodoča" 4D tabela  1.indeks: leto, 2.indeks: regija, 3.indeks: področje izobraževanja, 4.indeks: vrsta izobraževanja

leto = 0 #indeks s katerim vodimo leto (po vrsti) beremo podatke leta: 0, 1, 2, ...
izobrazevanje = 0 #indeks s katerim vodimo področje izobraževanja
regija = 0 #indeks s katerim vodimo regije

for leto in range(len(letnice)):
    D_tabela.append([])
    if regija == 13: #ko začnemo brati podatke za drugo leto regijo nastavimo na 0
        regija = 0
    file = open('0953371S1.csv', 'r') #datoteko je potrebno na novo odpreti, če ne, zanka nadaljuje kjer je ostala pred breakom prejšnje zanke
    for vr in file:
        if vr == 'Vir: Statistični urad Republike Slovenije.;;;;;;;;;;;;;;;;;;;;;\n': #prišli smo do konca vrstic s podatki ki nas zanimajo
            break
        tab = vr.strip().split(';') #podatki so podani v tabeli, celice v tabeli so ločene z ';'
        if tab[0] != '' and tab[0] != naslov: #prišli smo do nove regije, dodamo novo podtabelo za ustrezno leto
            D_tabela[leto].append([])
        elif vr[:2] == ';{0}'.format(izobrazevanje): # za vsako področje izobraževanja v regijo dodamo eno podtabelo
            D_tabela[leto][regija].append(tab[3+leto*10:5+leto*10] + tab[6+leto*10:9+leto*10] + tab[10+leto*10:12+leto*10]) #pri vsakem letu moramo začeti brati podatke 10 mest bolj desno, začetni indeksi so za 1. leto (leto 0)
            izobrazevanje += 1
            if izobrazevanje == 9: #prišli smo na konec regije
                regija += 1
                izobrazevanje = 0

#tabele regij področij in vrst izobraževanja:
Tab_regij = ['SLOVENIJA','Pomurska','Podravska','Koroška','Savinjska','Zasavska','Posavska','Jugovzhodna Slovenija','Osrednjeslovenska','Gorenjska','Primorsko-notranjska','Goriška','Obalno-kraška']
Tab_podrocij = ['Splošne izobraževalne aktivnosti','Izobraževalne vede in izobraževanje učiteljev','Umetnost in humanistika','Družbene, poslovne, upravne in pravne vede','Naravoslovje, matematika in računalništvo','Tehnika, proizvodne tehnologije in gradbeništvo','Kmetijstvo, gozdarstvo, ribištvo, veterinarstvo','Zdravstvo in sociala','Storitve']
Tab_vrst = ['Nižje poklicno','Srednje poklicno','srednje tehniško in dr. strokovno','poklicno tehniško','poklicni tečaj','splošna in strokovna gimnazija','maturitetni tečaj',]

#spreminjnje podatkov iz nizov v števila
for i in range(len(letnice)):
    for j in range(len(Tab_regij)):
        for k in range(len(Tab_podrocij)):
            for m in range(len(Tab_vrst)):
                if D_tabela[i][j][k][m] == '-': #namesto ničel so podatki oblike '-'
                    D_tabela[i][j][k][m] = 0
                else:
                    D_tabela[i][j][k][m] = int(D_tabela[i][j][k][m])

#vnos področja in vrste izobraževanja
vnos = False
while not vnos: #uporabnika sprašujemo po vnosu dokler ne vnese pravilnega vnosa
    vnos_podrocja = input('Vnesi področje izobrazbe: ')
    vnos_vrste = input('Vnesi vrsto izobrzbe: ')
    if vnos_podrocja in Tab_podrocij and vnos_vrste in Tab_vrst: #dobili smo pravilen vnos
        vnos = True
    else:
        print('Nepravilen vnos področja in vrste izobrazbe.')

for i, podrocje in enumerate(Tab_podrocij): #v tabeli poiščemo področje, ki zanima uporabnika
    if vnos_podrocja == podrocje:
        indeks_podrocja = i

for i, vrsta in enumerate(Tab_vrst): #v tabeli poiščemo vrsto, ki zanima uporabnika
    if vnos_vrste == vrsta:
        indeks_vrste = i

vpis = [] #sem bomo shranili podatke, ki zanimajo uporabnika, (vsako leto v svojo podatabelo)
for i in range(len(letnice)):
    vpis.append([])
    for j in range(1, len(Tab_regij)): #regijo Slovenija izpustimo, ker so tam le vsi podatki sešteti skupaj
        vpis[i].append(D_tabela[i][j][indeks_podrocja][indeks_vrste]) #gremo čez vsa leta in regije, ter bzemamo podatke, ki zanimajo uporabnika

regije_z_vpisi = Tab_regij[1:]

max = 0
for i in range(len(letnice)):
    for j, el in enumerate(vpis[i]): #poiščemo kje in kdaj je bilo največ vpisanih in si zapomnimo kje in kdaj je to bilo
        if el > max:
            max = el
            ind_leta = i #leto z največ vpisi: letnice[ind_leta]
            ind_regije = j #regija z največ vpisi: regije_z_vpisi[ind_regije]

import matplotlib.pyplot as plt

if max != 0:
    print('V ta program se je največ dijakov vpisalo leta {0} v regiji {1}, in sicer {2}.'.format(letnice[ind_leta], regije_z_vpisi[ind_regije], max))
    for i in range(len(letnice)): #za vsako leto bomo naredili svoj graf
        tab_vpisov = vpis[i] #tab_vpisov sedaj hrani podatke o vpisih za eno leto
        tab_vpisov_graf = [] #tabela vpisov brez ničel
        regije_z_vpisi_graf = []#tabela brez regij z nič vpisi
        for ind, st_vpisov in enumerate(tab_vpisov): #odstranimo tiste regije, v katerih se ni na to področje in vrsto vpisal nihče
            if st_vpisov != 0:
                tab_vpisov_graf += [st_vpisov]
                if regije_z_vpisi[ind] == 'Jugovzhodna Slovenija': #določena imena regij moramo skrajšati
                    regije_z_vpisi_graf += ['JV SLO']
                elif regije_z_vpisi[ind] == 'Osrednjeslovenska': #določena imena regij moramo skrajšati
                    regije_z_vpisi_graf += ['Osred. SLO']
                elif regije_z_vpisi[ind] == 'Primorsko-notranjska': #določena imena regij moramo skrajšati
                    regije_z_vpisi_graf += ['Prim.-notr.']
                else:
                    regije_z_vpisi_graf += [regije_z_vpisi[ind]]
        plt.bar(regije_z_vpisi_graf, tab_vpisov_graf) #nariše graf št. vpisov v odvisnosti od regije
        plt.ylabel('Št. vpisov') #opis y osi
        plt.xlabel('Regije') #opis x osi
        plt.title('Število vpisanih dijakov na področju {0} v letu {1}.'.format(vnos_podrocja, letnice[i])) #naslov grafa
        plt.show()

else:
    print('V ta program se v letih s katerih so vzeti podatki ni vpisal nihče.')
