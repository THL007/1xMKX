import json
import os

import requests as r
import sys
from time import sleep

url1 = "https://cm1xbet.mobi/LiveFeed/Get1x2_VZip?sports=103&champs=1252965&count=50&lng=en&mode=4&country=84&partner=55&getEmpty=true&noFilterBlockEvent=true"
url2 = lambda id : "https://cm1xbet.mobi/LiveFeed/GetGameZip?id=" +str(id)+ "&lng=en&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=55&marketType=1&isNewBuilder=true"


COOKIE = "SESSION=64cf1e4789d29a669574a4fe1399ddef; widget-setting-lite-version=true; widget-show-game-number=1; lng=en; _ya_t=1664531579; auid=LYd6cmM2pMqCN9ERCjcmAg==; tzo=1; slot_key_access=92; coefview=0; typeBetNames=short; proofOfAge=1; sh.session=4541cbe8-c2a4-48ae-8540-4ae709dd3314; _ym_1664531469=ml143131; uhash=60e3eb7a4fc12c5ba40ae6f4dcf5bca0; cur=XAF; ua=152159655; activeid=152159655; one_click=true; one_sum=90; base_bet_setting_XAF=5; custom_bet_setting_one_XAF=5; custom_bet_setting_two_XAF=10; custom_bet_setting_three_XAF=20; custom_bet_setting_four_XAF=30; custom_bet_setting_five_XAF=50; favorites_markets=%7B%22full%22%3A%5B%5D%2C%22short%22%3A%5B%5D%7D; when_change_coef=2; download_application_hide=1"
COOKIE = COOKIE.replace("lng=de", "lng=en")

def load_cookies_header(cookie:str , filename:str=None) -> dict:
    '''This function should load all  header's cookies from an external .txt file'''
    if filename is not None:
        with open(filename, r) as fileobj:
            cookie = fileobj.read()
            cookie = cookie.replace("Cookie: ", "").replace("lng=de", "lng=en")
    else:
        cookie = cookie.replace("Cookie: ", "").replace("lng=de", "lng=en")
    
    items = cookie.split(";")
    
    cles = []
    valeurs = []
    for item in items:
        cles.append(item.split("=", maxsplit=1)[0])
        valeurs.append(item.split("=", maxsplit=1)[1])
    
    Cookie = {}
    for i in range(0, len(cles)):
        Cookie[cles[i]] = valeurs[i]
    
    
    return Cookie


def payload(sum, rodd,UserId) -> dict:

    return {
        	
        "UserId": "152159655",      #
        "Events[0][GameId]": "400123117",
        "Events[0][Type]": "4059",
        "Events[0][Coef]": str(rodd),     #
        "Events[0][Param]":	"3",
        "Events[0][PlayerId]": "0",
        "Events[0][Kind]": "1",
        "Events[0][Expired]": "0",
        "Events[0][Price]":	"0",
        "Events[0][InstrumentId]": "0",
        "Events[0][Seconds]": "0",
        "partner": "55",
        "CfView": "0",
        "Summ":	"90",   #
        "Lng": "de",
        "Vid": "0",
        "hash":	"60e3eb7a4fc12c5ba40ae6f4dcf5bca0",
        "Source": "110",
        "CheckCf": "2",
        "Live":	"true",
        "notWait": "true"
    }


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


def load_json_file() -> dict:# try except checked
    
    # This function loead the json file used to bet
    # This fucntion returns a dictionary 


    print("Laoding algos...", end="")

    count = 0

    while True:

        try:
            #filename = os.getcwd() + r"/mkx_Rfinish.json" # On windows use reverse-slash please (\)
            filename = "C:/Users/Dell Latitude E7270/Documents/PYTHON Codes/MKX/MKX/mkx_Rfinish.json"

            with open(filename, 'r') as jsonf_obj:
                fights = json.load(jsonf_obj)

            algos = {}

            for fight in fights:
                fight = fight.split()
                algos[fight[0]] = []

            for fight in fights:
                fight = fight.split()
                algos[fight[0]].append(fight[2])
            
            break
        except:

            if count == 5:
                print("Has tried to load files more than 5 times now exiting")
                sys.exit(0)
            else:
                count += 1


    

    print("Done!!")
    return algos


def bet(referal_link,summ,rodd,userid, gameid,param) -> bool:

    url = "	https://cm1xbet.mobi/datalinelive/putbetscommon"

    count = 0
    while True:
        try:

            response = r.post(
                url,
                headers={

                    "Host": "cm1xbet.mobi",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Language": "en-US;q=0.7,en;q=0.3",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-Requested-With": "XMLHttpRequest",
                    "Content-Length": "512",
                    "Origin": "https://cm1xbet.mobi",
                    "Connection": "keep-alive",
                    "Referer": str(referal_link),
                    "Cookie": COOKIE,
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "TE": "trailers",
                }, 
                data={
            
                    "UserId" :	"152159655",
                    "Events[0][GameId]":	str(gameid),
                    "Events[0][Type]":	"4059",
                    "Events[0][Coef]":	str(rodd),
                    "Events[0][Param]":	str(param),        # Here is the round number
                    "Events[0][PlayerId]":	"0",
                    "Events[0][Kind]":	"1",
                    "Events[0][Expired]":	"0",
                    "Events[0][Price]":	"0",
                    "Events[0][InstrumentId]":	"0",
                    "Events[0][Seconds]":	"0",
                    "partner":	"55",
                    "CfView":	"0",
                    "Summ":	str(summ),       # amount to bet
                    "Lng":	"en",
                    "Vid":	"0",
                    "hash":	"60e3eb7a4fc12c5ba40ae6f4dcf5bca0",
                    "Source":	"110",
                    "CheckCf":	"2",
                    "Live":	"true",
                    "notWait":	"true",

                })

            print("Content:" ,response.json())

        except  r.JSONDecodeError as js:
            if check_betting():
                return True
            else:
                return False
        except:

            if count == 5:
                print("Has tried to bet without success; aborting the operation...")
                sys.exit(0) 
            else:
                print("Trying again to bet")
                sleep(1)
                count +=1


def get_param(value2) -> str:

    if('CP' in value2['SC'].keys()):
        fightround = int(value2['SC']['CP']) + 1
    else:
        fightround = 1

    return str(fightround)


def check_balance() -> float:

    url = "https://cm1xbet.mobi/user/balance/"

    

    while True:

        try:

            response = r.post(
                url,
                headers= {
                    "Host": "cm1xbet.mobi",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
                    "Accept-Encoding": "gzip, deflate, br",
                    "X-Requested-With": "XMLHttpRequest",
                    "Origin": "https://cm1xbet.mobi",
                    "Connection": "keep-alive",
                    "Referer": "https://cm1xbet.mobi/en/live/",
                    "Cookie": COOKIE,
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "Content-Length": "0",
                    "TE": "trailers",
                })
            if (response.status_code == 200):
                break

        except:
            if count == 5:
                print("Has tried more than 3 times without success, exiting the program ...")
                sys.exit(0)
            else:
                count +=1



        else:
            count += 1

    return response.json()['balance'][0]['money']


def check_betting() -> bool:

    sleep(1)

    url = "https://cm1xbet.mobi/user/balance/"

    flag = False

    while not flag:

        response = r.post(
            url,
            headers= {
                "Host": "cm1xbet.mobi",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://cm1xbet.mobi",
                "Connection": "keep-alive",
                "Referer": "https://cm1xbet.mobi/en/live/",
                "Cookie": COOKIE,
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Content-Length": "0",
                "TE": "trailers",
            }
            )

        if (response.status_code == 200):

            flag = True
    
    if response.json()['balance'][0]['summ_unplaced_bets'] == 0:
        return False     # Means it is finished
    else:
        return True    # Means it is not yet finished


SUM=check_balance()


def success() -> bool:

    if( check_balance() >= SUM):
        # was a success
        return True
    else:
        # Was a failure
        return False


# def roundup(x:int): ### Added this
#     if x % 100 == 0:
#         return x  
#     else:
#         return (x + 100) - (x % 100)



def main():

    algos = load_json_file()

    ids = []


    while True:

        first_bet_sum = 100 ### Changed this OK

        try:

            r1 = r.get(url1)
            value1 = r1.json()['Value']

            for i in range(len(value1)): ### removed something after this maybe ????
                flag = False
                try:
                    if (value1[i]['SC']['I']=="Pre-game betting" and value1[i]['SC']['TS']>20):  #if the fight has not yet begun and will begin in more than 30s
                        if not value1[i]['I'] in ids:
                            ids.append(value1[i]['I'])
                except:
                    print("I doesn't exist here")

            print(ids)

            for id in ids:
                global SUM ### Added this
                try:
                    SUM=check_balance() ### Added this
                except KeyError():
                    print("Cookie Expired !!!\n Login again to copy new cookie and paste in code")
                    sys.exit(0)
                
                print(f"Account Balance = {SUM}")
                r2 = r.get(url2(id))
                value2 = r2.json()['Value']
                rodd = value2['GE'][4]['E'][0][2]['C']
                P1 = players[value2['O1R'].replace(" ", "").replace("'", "").replace("-", "")]
                P2 = players[value2['O2R'].replace(" ", "").replace("'", "").replace("-", "")]
                link = "https://cm1xbet.mobi/en/live/Mortal-Kombat/"  + str(value2['LI']) + "-" +str(value2['LE']).replace(" ", "-") + "/" + str(value2['I']) + "-" + str(value2["O1E"]).replace("'","").replace(" ","-") + "-" + str(value2["O2E"]).replace("'","").replace(" ","-") + "/"
                param = get_param(value2)
                #balance = check_balance() ### Removed this this

                

                if (P1 in algos.keys()): ### Changed this
                    if(P2 in algos[P1]):
                        if ( rodd >= 1.9 and rodd <= 2.2): # P2 in algos[P1] and   1.9 : 2.2
                            print(f"{P1} - {P2}  {rodd} first round")

                            if bet(link,first_bet_sum,rodd,0,id,param):     # TODO: Change Userid later on

                                while check_betting():
                                    sleep(3)

                                if not success():

                                    # second_bet_sum = roundup(int(round(first_bet_sum + first_bet_sum*rodd/(rodd-1)))) ### Changed this

                                    second_bet_sum = int( first_bet_sum + first_bet_sum*rodd/(rodd-1))

                                    results = json.loads(value2['SC']['S'][1]['Value'])

                                    if results == []:
                                        break
                                    # if (results[0]['DI']!="Regular" and value2['SC']['CP']==2): ### Removed this

                                    print(f"{P1} - {P2}  {rodd} Second round")  ### Changed this

                                    if bet(link,second_bet_sum,rodd,0,id,param):  ### Changed this

                                        while check_betting():
                                            sleep(3)
                    else:
                        ids.remove(id)
                        sleep(20)
                else:
                    ids.remove(id)
                    sleep(20)
                
                if  (value2['SC']['CPS']=='3 round' or 
                    value2['SC']['CPS']=='4 round' or 
                    value2['SC']['CPS']=='5 round' or 
                    value2['SC']['CPS']=='6 round' or 
                    value2['SC']['CPS']=='7 round'
                    ):ids.remove(id)
        except KeyError as ke:
            print("Error occured -> ",ke," but chill the program will not exit")
        except Exception as e:
            print("Something wierd occured let's debug it")

main()