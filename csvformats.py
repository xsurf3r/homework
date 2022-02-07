import csv

file = open("csv_meg.csv",'r',encoding='utf-8')

print(type(file))

lasit_csv = csv.reader(file)

print(lasit_csv)

header = []
header = next(lasit_csv)
print(header)

saturs = []
for rinda in  lasit_csv:
    saturs.append(rinda)

print (saturs)
print(type(saturs))

file.close()

kolonnuNosaukumi = ['Vārs', '1.atzīme', '2.atzīme']
dati = [['Pēteris', 6,8], ['Annika',7,5], ['Viesturis',8,9]]

with open ('skolenu_dati.csv', 'w',encoding="utf-8") as fails:
    csvwrite = csv.writer(fails)
    csvwrite.writerow(kolonnuNosaukumi)
    csvwrite.writerows(dati)