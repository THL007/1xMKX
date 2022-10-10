import json
import os
from posixpath import split
from tkinter import W
from xmlrpc.client import Boolean
from helium import *
from time import sleep


url1 = "https://cm1xbet.com/LiveFeed/Get1x2_VZip?sports=103&champs=1252965&count=50&lng=en&mode=4&country=84&partner=55&getEmpty=true&noFilterBlockEvent=true"

url2 = lambda id : "https://cm1xbet.com/LiveFeed/GetGameZip?id=" +str(id)+ "&lng=en&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=55&marketType=1&isNewBuilder=true"

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


def load_json_file() -> dict:
    
    # This function loead the json file used to bet
    # This fucntion returns a dictionary 


    print("Laoding algos...", end="")
    filename = os.getcwd() + "\\mkx_Rfinish.json"

    with open(filename, 'r') as jsonf_obj:
        fights = json.load(jsonf_obj)

    algos = {}

    for fight in fights:
        fight = fight.split()
        algos[fight[0]] = []

    for fight in fights:
        fight = fight.split()
        algos[fight[0]].append(fight[2])

    

    print("Done!!")
    return algos


def load_credential() -> str: #
    # Reads credentials from a file and returns username and password

    filename = os.getcwd() + "\\credential.txt"
    

    with open(filename, "r") as f_obj:

        txt = f_obj.readline()

        f_obj.close()

    usr = txt.split(":")[0]
    pss = txt.split(":")[1]

    return usr,pss


def init_credential(usrname,passwrd) -> None:

    sleep(3)

    # d = start_firefox("https://cm1xbet.mobi/en/", headless=False)

    # click("Yes")

    wait_until(Text("Log in").exists)
    click("Log in")

    wait_until(TextField("EMAIL OR ID").exists)
    write(usrname, into='EMAIL OR ID')

    wait_until(TextField("PASSWORD").exists)
    write(passwrd, into='PASSWORD')

    wait_until(Text("LOG IN").exists)
    click("LOG IN")
    
   

    return None


def main():
    ## Main function 

    combats = []
    ids = []

    start_firefox("https://cm1xbet.mobi/en/", headless=False)

    sleep(30)
    print(wait_until(Text("Yes").exists))
    click("Yes")

    username, password = load_credential()

    init_credential(username,password)

    close_dialog(0)

    init_amount(0,90)
    switch(0)

    #find_match(0,399991226)
    lookup(0,'https://cm1xbet.mobi/en/live/Mortal-Kombat/1252965-Mortal-Kombat-X/400005467-Scorpion-Jacqueline-Briggs/')

    sleep(6)

    bet(0,1)

    print("HEllo")
    

def init_amount(driver,amt) -> int:

    sleep(6)

    wait_until(S(".one-click__ascent").exists)
    click(S(".one-click__ascent"))

    wait_until(S(".spinner__number > input:nth-child(2)").exists)
    write(str(amt), into=S(".spinner__number > input:nth-child(2)"))

    sleep(1)
    click("SAVE")
    sleep(1)
    click("OK")


def find_match(driver,match_id) -> int:

    #obsolete

    sleep(1)

    wait_until(S("div.main-nav__item > li:nth-child(2)").exists)
    click(S("div.main-nav__item > li:nth-child(2)"))

    wait_until(S("#search").exists)
    write(str(match_id), into=S("#search"))
    
    wait_until(S(".btn__ico_single").exists)
    click(S(".btn__ico_single"))
    
    wait_until(S("li.events__item_col:nth-child(1)").exists)
    click(S("li.events__item_col:nth-child(1)"))

def lookup(driver,link) -> str:

    sleep(1)
    go_to(str(link))


def close_dialog(drvier,) -> int:
    sleep(1)

    wait_until(S(".download-application__close").exists)
    click(S(".download-application__close"))


def switch(driver) -> int:

    sleep(1)

    wait_until(S(".one-click > div:nth-child(2) > label:nth-child(2)").exists)
    click(S(".one-click > div:nth-child(2) > label:nth-child(2)"))


def bet(driver, roound) ->  int:

    sleep(1)
    
    if round == 1:
        wait_until(Text("No Finish In 1 Round").exists)        
        click("No Finish In 1 Round")
    elif round == 2:
        wait_until(Text("No Finish In 2 Round").exists)
        click("No Finish In 2 Round")
    elif round == 3:
        wait_until(Text("No Finish In 3 Round").exists)
        click("No Finish In 3 Round")
    elif round == 4:
        wait_until(Text("No Finish In 4 Round").exists)
        click("No Finish In 4 Round")
    elif round == 5:
        wait_until(Text("No Finish In 5 Round").exists)
        click("No Finish In 5 Round")
    elif round == 6:
        wait_until(Text("No Finish In 6 Round").exists)
        click("No Finish In 6 Round")
    elif round == 7:
        wait_until(Text("No Finish In 7 Round").exists)
        click("No Finish In 7 Round")
    
    wait_until(Text("Bet accepted!").exists,30)
    click("OK")


def wait_for_end(driver) -> bool:


    sleep(1)

    wait_until(S(".header__link").exists)
    click(S(".header__link"))

    while(wait_until(S("div.balance__row:nth-child(4)").exists)):
        pass
    print("H")

    
    while True:
        sleep(60)

        #check balance if bigger than what was expected, kill the loop and return True


main()