import json

#Vardnica

vardnica = {
    'Vards':'Artjoms',
    'Izglitiba':'Videja',
    'Vecums':16
}

#Parveidot Python uz JSON
a = json.dumps(vardnica)

print(a, type(a))

#Parveidot JSON uz Python
b = json.loads(a)

print(b, type(b))

print(json.dumps(['banans','mandarins']))

#dict - object
#list - array
#tuple - array
#str - string
#int - number
#float - number
#true - true
#false - false
#none - null

py_data = {
    'Vards':'Vladlendik',
    'Vecums':1000,
    'Dzivs':True,
    'Nedzivs':False,
    'Berni':('Rozenmaiden','Shrinemaiden'),
    'Dzivnieki':None,
    'Masinas':[
        {'Modelis':'Corolla levin','Gads':1986},
        {'Modelis':'Cybertruck','Gads':2020}
    ]
}

print(json.dumps(py_data, indent=4, separators=(',',':')))

fails = open('jsonqwe.json','w',encoding='utf-8')
json.dump(py_data,fails,indent=4, ensure_ascii=False)
fails.close()

fails = open('jsonqwe.json','r',encoding='utf-8')
json_dati = json.load(fails)

#vardnicas garums
print(len(json_dati))

#Visas atslegas
print(json_dati.keys())

#Visas vertibas
print(json_dati.values())

#Parbaudi, vai dota atslega ir vardnica un izvadi tas vertibu
atslega = 'Dzivs'

for key in json_dati:
    if key == atslega:
        print(json_dati[key])

#Nodefinet funkciju, kura ka argumentus izmantos datnes nosaukumu un atslegas nosaukumu
#jaizvada atslegas vertiba
def funkcija(datnes_name,key_name):
    for key in datnes_name.keys():
        if key == key_name:
            print(datnes_name[key_name])
            return
        else:
            break
    print(f'Nav atslegas')

funkcija(json_dati,'Vards')