import json
import requests as r
from time import sleep


players = {
    "КэссиКейдж" : "CassieCage",
    "ЭрронБлэк" : "ErronBlack",
    "СабЗиро" : "SubZero",
    "Саб-Зиро" : "SubZero",
    "ДжейсонВурхиз" : "JasonVoorhees",
    "Милина" : "Mileena",
    "ДиВора" : "DiVorah",
    "Горо" : "Goro",
    "Шиннок" : "Shinnok",
    "Тремор" : "Tremor",
    "Кенши" : "Kenshi",
    "Китана" : "Kitana",
    "Эрмак" : "Ermac",
    "Чужой" : "Alien",
    "ТакедаТакахаши" : "TakedaTakahashi",
    "ДжонниКейдж" : "JohnnyCage",
    "Триборг" : "Triborg",
    "ФерраиТорр" : "FerraTorr",
    "Рептилия" : "Reptile",
    "ДжэкиБриггс" : "JacquiBriggs",
    "Таня" : "Tanya",
    "КунгДжин" : "KungJin",
    "СоняБлейд" : "SonyaBlade",
    "Скорпион" : "Scorpion",
    "КотальКан" : "KotalKahn",
    "ЛюКенг" : "LiuKang",
    "КуанЧи" : "QuanChi",
    "КунгЛао" : "KungLao",
    "Джакс" : "Jax",
    "Райдэн" : "Raiden",
    "Хищник" : "Predator",
    "Кано" : "Kano",
    "БоРайЧо" : "BoRaiCho",
    "Кожаноелицо" : "Leatherface",
    "Ди'Вора" : "DiVorah"
    }

filename = 'mkx_Rfinish.json' #Fights we are looking in order to bet
with open(filename, 'r') as f_obj:
    fights = json.load(f_obj)

algos = {}
for fight in fights:
    fight = fight.split()
    algos[fight[0]] = [] # create P1s as keys

for fight in fights:
    fight = fight.split()
    algos[fight[0]].append(fight[2]) #create P2s as values of P1s

url1 = "https://cm1xbet.com/LiveFeed/Get1x2_VZip?sports=103&champs=1252965&count=50&lng=en&mode=4&country=84&partner=55&getEmpty=true&noFilterBlockEvent=true"
url2 = lambda id : "https://cm1xbet.com/LiveFeed/GetGameZip?id=" +str(id)+ "&lng=en&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=55&marketType=1&isNewBuilder=true"

combats = []

ids = []

while True:

    

    r1 = r.get(url1)
    value1 = r1.json()['Value']
    
    for i in range(len(value1)):

        flag = False

        try:
            if (value1[i]['SC']['I']=="Pre-game betting" and value1[i]['SC']['TS']>30):  #if the fight has not yet begun and will begin in more than 30s
                if not value1[i]['I'] in ids:
                    ids.append(value1[i]['I'])
        except:
            print("I doesn't exist here")

    print(ids)

    for id in ids:

        # https://cm1xbet.mobi/en/live/Mortal-Kombat/1252965-Mortal-Kombat-X/399991226-DVorah-Reptile/
        # https://cm1xbet.mobi/en/live/Mortal-Kombat/1252965-Mortal-Kombat-X/399996375-Erron-Black-Sonya-Blade/
        # link = "https://cm1xbet.mobi/en/live/Mortal-Kombat/"  + str(value2['LI']) + str(value['LE']).replace(" ", "-") + "/" + str(value2['I']) + "-" + str(value1["O1E"]).replace("'","").replace(" ", ""),replace("-","") + "-" + str(value1["O2E"]).replace("'","").replace(" ", ""),replace("-","") + "/"

        r2 = r.get(url2(id))
        value2 = r2.json()['Value']
        rodd = value2['GE'][4]['E'][0][2]['C']
        P1 = players[value2['O1R'].replace(" ", "").replace("'", "").replace("-", "")]
        P2 = players[value2['O2R'].replace(" ", "").replace("'", "").replace("-", "")]
        link = "https://cm1xbet.mobi/en/live/Mortal-Kombat/"  + str(value2['LI']) + "-" +str(value2['LE']).replace(" ", "-") + "/" + str(value2['I']) + "-" + str(value2["O1E"]).replace("'","").replace(" ","-") + "-" + str(value2["O2E"]).replace("'","").replace(" ","-") + "/"

        if (P1 in algos.keys()):
            if ( P2 in algos[P1] and rodd >= 0 and rodd <= 10.2): #1.9 : 2.2
                print(f"{P1} - {P2}  {rodd}")

                ##TODO place_bet on first round Multiply the payroll by factor of odd
            results = json.loads(value2['SC']['S'][1]['Value'])
            if results == []:
                break
            if (results[0]['DI']!="Regular" and value2['SC']['CP']==5): #if round1 has finished and was a loss 

                ##TODO place a bet on second round multiply the [payroll] by the odd but must multiply by something else first dunno
                print(f"{P1} - {P2}  {rodd}")
            #end
        if  (value2['SC']['CPS']=='3 round' or 
             value2['SC']['CPS']=='4 round' or 
             value2['SC']['CPS']=='5 round' or 
             value2['SC']['CPS']=='6 round' or 
             value2['SC']['CPS']=='7 round'
            ):ids.remove(id)