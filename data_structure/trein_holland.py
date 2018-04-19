import csv
import sys

# lijst van trajecten in gebruik
spoorgebruik_1 = [['Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Zaandam', 'Hoorn', 38],
                ['Zaandam', 'Beverwijk', 'Castricum', 'Alkmaar', 'Den Helder', 37],
                ['Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag Centraal', 38],
                ['Gouda', 'Alphen a/d Rijn', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid', 'Amsterdam Amstel', 'Amsterdam Centraal', 72],
                ['Rotterdam Alexander', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag Centraal', 33],
                ['Dordrecht', 'Rotterdam Centraal', 17]]

spoorgebruik = [['Den Helder', 'Alkmaar', 'Hoorn', 'Zaandam', 'Castricum', 'Alkmaar', 107],
                ['Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 38],
                ['Den Haag Centraal', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Centraal', 36],
                ['Gouda', 'Alphen a/d Rijn', 'Leiden Centraal', 'Den Haag Centraal', 45],
                ['Haarlem', 'Beverwijk', 'Zaandam', 'Hoorn', 67],
                ['Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag Centraal', 54],
                ['Zaandam', 'Amsterdam Sloterdijk', 8]]
                

kritieke_sporen = []
kritieke_lijnen = []
alle_lijnen = []

# open lijst van alle stations en voeg de kritieke toe in een lijst
with open('StationsHolland.csv') as csvfile:
    stationsinfo = csv.reader(csvfile, delimiter=',')
    for station in stationsinfo:
        if station[-1] == 'Kritiek':
            kritieke_sporen.append(station[0])

# open de lijst alle sporen en voeg de kritieke toe in een lijst
with open('ConnectiesHolland.csv') as csvfile:
    stationsverbindingen = csv.reader(csvfile, delimiter=',')
    for lijn in stationsverbindingen:
        alle_lijnen.append([lijn[0],lijn[1]])
        if (lijn[0] in kritieke_sporen or lijn[1] in kritieke_sporen):
            kritieke_lijnen.append([lijn[0], lijn[1]])            

# bepaal totaal aantal kritieke sporen
tot_kr_sporen = len(kritieke_lijnen)

gebr_kr_sporen = 0

# itereer over trajecten
for i in range(len(spoorgebruik)):

    # itereer over sporen
    for j in range(len(spoorgebruik[i]) - 2):
        
        # check of tussensporen in de lijst met alle sporen zit
        if ([spoorgebruik[i][j], spoorgebruik[i][j+1]] not in alle_lijnen
            and [spoorgebruik[i][j+1], spoorgebruik[i][j]] not in alle_lijnen):
                # zo niet return error
                sys.exit("Error: opgegeven lijnen niet in gebruik!")

# itereer over al je trajecten
for lijn in spoorgebruik:

    if lijn[0] in kritieke_sporen:
        gebr_kr_sporen += 1

    if lijn[-1] in kritieke_sporen:
        gebr_kr_sporen += 1
    
    # itereer over al je stations
    for i in range(len(lijn) - 2):

        # tel alle kritieke stations
        if lijn[i + 1] in kritieke_sporen:
            if (lijn[i] not in kritieke_sporen and lijn[i + 2] not in kritieke_sporen):
                gebr_kr_sporen += 2
            else:
                gebr_kr_sporen += 1
                
    # als de laatste twee stations in je traject kritiek zijn heb je er een teveel geteld
    if (lijn[-2] in kritieke_sporen and lijn[-3] in kritieke_sporen):
        gebr_kr_sporen -= 1

# bepaal variabelen
p = gebr_kr_sporen / len(kritieke_lijnen)
t = len(spoorgebruik)
minutes = 0

# itereer over alle trajecten
for spoor in spoorgebruik:

    # check of traject niet te lang duurt
    if spoor[-1] > 120:
        sys.exit('Error: traject duurt te lang!')

    # tel de minuten van het traject bij het totaal aantal minuten op
    minutes += spoor[-1]

print(p)
# bepaal S
print('S =', p * 10000 - (t * 20 + minutes / 10))
    






