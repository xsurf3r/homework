#try_flask


from flask import Flask
import json
import datetime

app = Flask(__name__)
app.config["JSON_AS_ASCII"]=False

@app.route('/')
def index():
    return 'nothing is here'

@app.route('/hello')
def hello():
    return '<h1>Hello, World</h1>'

@app.route('/sutit/<vards>/<zina>')
def send(vards,zina):
    now=datetime.datetime.now()
    time=now.strftime("%Y/%m/%d, %H:%M:%S")

    print(vards,zina,time)

    rinda = {
        'zina':zina,
        'vards':vards,
        'time':time
    }

    with open('C:/Users/veing/Downloads/homework/CSV/PYTHON 2022/FlaskServer/chats.json','r',encoding='utf-8') as file:
        oldzinas = file.read()
        oldJson = json.loads(oldzinas)

    oldJson.append(rinda)

    with open('C:/Users/veing/Downloads/homework/CSV/PYTHON 2022/FlaskServer/chats.json','w',encoding='utf-8') as f:
        f.write(json.dumps(oldJson,indent=2,ensure_ascii=False))
        
    return 'ok'

@app.route('/date')
def datums():
    return (f'<hi>Today is {datetime.datetime.now()}</hi>')



@app.route('/user/<vards>/<vecums>')
def lietotajs(vards,vecums):
    dati = {vards:vecums}
    dati_json = json.dumps(dati)

    with open("lietotaji.json","w",encoding="utf-8") as fails:
        json.dump(dati_json,fails,indent=2,ensure_ascii=False)

app.run(host='0.0.0.0',port=81)