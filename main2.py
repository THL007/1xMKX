from ast import Pass
import json
import os
import sys
from xmlrpc.client import Boolean
import requests as r
from time import sleep

url1 = "https://cm1xbet.com/LiveFeed/Get1x2_VZip?sports=103&champs=1252965&count=50&lng=en&mode=4&country=84&partner=55&getEmpty=true&noFilterBlockEvent=true"
url2 = lambda id : "https://cm1xbet.com/LiveFeed/GetGameZip?id=" +str(id)+ "&lng=en&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=55&marketType=1&isNewBuilder=true"


# TODO: I have to update these with un gar bien has done !!!


def load_cookies_header() -> dict:
    '''This function should load all  header's cookies from an external .txt file'''
    pass




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
            filename = os.getcwd() + r"/mkx_Rfinish.json" # On windows use reverse-slash please (\)

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


def bet(referal_link,summ,rodd,userid, gameid,param) -> Boolean:

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
                    "Cookie": "Cookie: lng=de; auid=LYd6cmMt/UuUNPNhBNnDAg==; _ga=GA1.2.1463082551.1663958356; _fbp=fb.1.1663958357262.347393914; _ym_uid=16639583591041611848; _ym_d=1663958359; sh.session=b176f08b-019d-4fc5-90af-b7195d285833; tzo=1; uhash=60e3eb7a4fc12c5ba40ae6f4dcf5bca0; cur=XAF; SESSION=40b9909ef519ee735a2c6c5f9788128c; widget-setting-lite-version=true; widget-show-game-number=1; _ya_t=1664445960; slot_key_access=89; coefview=0; _gid=GA1.2.1541947888.1664438562; proofOfAge=1; _ym_1664444502=_ud1467147; _ym_isad=2; _ym_visorc=b; ua=152159655; activeid=152159655; one_click=true; one_sum=90; base_bet_setting_XAF=5; custom_bet_setting_one_XAF=5; custom_bet_setting_two_XAF=10; custom_bet_setting_three_XAF=20; custom_bet_setting_four_XAF=30; custom_bet_setting_five_XAF=50; favorites_markets=%7B%22full%22%3A%5B%5D%2C%22short%22%3A%5B%5D%7D; when_change_coef=2; download_application_hide=1; _gat=1; num_games_in_live_55=147",
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
                    "Summ":	"90",       # amount to bet
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
                "Referer": "https://cm1xbet.mobi/de/live/",
                "Cookie": "Cookie: lng=de; auid=LYd6cmMt/UuUNPNhBNnDAg==; _ga=GA1.2.1463082551.1663958356; _fbp=fb.1.1663958357262.347393914; _ym_uid=16639583591041611848; _ym_d=1663958359; sh.session=b176f08b-019d-4fc5-90af-b7195d285833; tzo=1; uhash=60e3eb7a4fc12c5ba40ae6f4dcf5bca0; cur=XAF; SESSION=40b9909ef519ee735a2c6c5f9788128c; widget-setting-lite-version=true; widget-show-game-number=1; _ya_t=1664445960; slot_key_access=89; coefview=0; _gid=GA1.2.1541947888.1664438562; proofOfAge=1; _ym_1664444502=_ud1467147; _ym_isad=2; _ym_visorc=b; ua=152159655; activeid=152159655; one_click=true; one_sum=90; base_bet_setting_XAF=5; custom_bet_setting_one_XAF=5; custom_bet_setting_two_XAF=10; custom_bet_setting_three_XAF=20; custom_bet_setting_four_XAF=30; custom_bet_setting_five_XAF=50; favorites_markets=%7B%22full%22%3A%5B%5D%2C%22short%22%3A%5B%5D%7D; when_change_coef=2; download_application_hide=1; _gat=1; num_games_in_live_55=147",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Content-Length": "0",
                "TE": "trailers",
            })

        if (response.status_code == 200):
            flag = True

    return response.json()['balance'][0]['money']


def check_betting() -> Boolean:

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
                "Referer": "https://cm1xbet.mobi/de/live/",
                "Cookie": "lng=de; auid=LYd6cmMt/UuUNPNhBNnDAg==; _ga=GA1.2.1463082551.1663958356; _gid=GA1.2.657740254.1663958356; _fbp=fb.1.1663958357262.347393914; _ym_uid=16639583591041611848; _ym_d=1663958359; sh.session=b176f08b-019d-4fc5-90af-b7195d285833; SESSION=d97098c7d0e758f4df03402465c6a8ea; tzo=1; slot_key_access=104; coefview=0; proofOfAge=1; download_application_hide=1; _ym_1664014066=ya14op147; _ym_1664014193=_ud1467171; uhash=60e3eb7a4fc12c5ba40ae6f4dcf5bca0; cur=XAF; type1x2=1; typeBetNames=short; widget-setting-lite-version=true; widget-show-game-number=1; _ya_t=1664047430; _ym_isad=2; _ym_1664047430=ya167187; one_sum=90; base_bet_setting_JPY=5; custom_bet_setting_one_JPY=5; custom_bet_setting_two_JPY=10; custom_bet_setting_three_JPY=20; custom_bet_setting_four_JPY=30; custom_bet_setting_five_JPY=50; favorites_markets=%7B%22full%22%3A%5B%5D%2C%22short%22%3A%5B%5D%7D; when_change_coef=2; ua=152159655; one_click=true; activeid=152159655; base_bet_setting_XAF=5; custom_bet_setting_one_XAF=5; custom_bet_setting_two_XAF=10; custom_bet_setting_three_XAF=20; custom_bet_setting_four_XAF=30; custom_bet_setting_five_XAF=50; _gat=1",
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


def success() -> Boolean:

    if( check_balance() >= SUM):
        # was a success
        return True
    else:
        # Was a failure
        return False




def main():

    algos = load_json_file()

    ids = []


    while True:

        bet_sum = 90 #(14/100)*SUM

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

            r2 = r.get(url2(id))
            value2 = r2.json()['Value']
            rodd = value2['GE'][4]['E'][0][2]['C']
            P1 = players[value2['O1R'].replace(" ", "").replace("'", "").replace("-", "")]
            P2 = players[value2['O2R'].replace(" ", "").replace("'", "").replace("-", "")]
            link = "https://cm1xbet.mobi/en/live/Mortal-Kombat/"  + str(value2['LI']) + "-" +str(value2['LE']).replace(" ", "-") + "/" + str(value2['I']) + "-" + str(value2["O1E"]).replace("'","").replace(" ","-") + "-" + str(value2["O2E"]).replace("'","").replace(" ","-") + "/"
            param = get_param(value2)
            balance = check_balance()

            

            if (P1 in algos.keys()):
                if ( rodd >= 0 and rodd <= 10.2): # P2 in algos[P1] and   1.9 : 2.2
                    print(f"{P1} - {P2}  {rodd}")

                    if bet(link,bet_sum,rodd,0,id,param):     # TODO: Change Userid later on

                        while check_betting():
                            sleep(3)

                        if not success():

                            bet_sum = 90 # ((14/100)*SUM) * 1.2

                            results = json.loads(value2['SC']['S'][1]['Value'])

                            if results == []:
                                break
                            if (results[0]['DI']!="Regular" and value2['SC']['CP']==5): #if round1 has finished and was a loss 

                                print(f"{P1} - {P2}  {rodd}")

                                if bet(link,bet_sum,rodd,0,id,param):     # TODO: Change Userid later on

                                    while check_betting():
                                        sleep(3)
                
            if  (value2['SC']['CPS']=='3 round' or 
                value2['SC']['CPS']=='4 round' or 
                value2['SC']['CPS']=='5 round' or 
                value2['SC']['CPS']=='6 round' or 
                value2['SC']['CPS']=='7 round'
                ):ids.remove(id)

main()