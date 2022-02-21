import json

vardss = input('ievadiet vardu:')
uzvardss = input('ievadiet uzvardu:')
vecumss = int(input('ievadiet vecumu:'))
tell = int(input('ievadiet telefona numuru:'))

vardnica = {}
vardnica[vardss] = {
    'Uzvardss' :uzvardss,
    'Vecums' : vecumss,
    'Telefona Numurs:':tell
}

def dati(vards,uzvards,vecums,tell):
    with open('ievaktieDati.json','r',ecoding='utf-8') as file:
        ievaktieDati = json.load(file)
        print(vardnica)
        print(ievaktieDati)
    with open('ievaktieDati.json','w',encoding='utf-8') as file:
        json.dump(vardnica,file,indent=4,ensure_ascii=False)


dati(vardss,uzvardss,vecumss,tell)