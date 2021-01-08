import json
import tkinter as tk 
import requests
from tkinter import ttk 
from tkinter import * 


def open_json():
    with open("steam.json", "r") as steam:
        data = json.load(steam)
        return data

def first_game():
    games_data = open_json()
    print(games_data[0]['name'])

def merge(lst, begin, mid, end): 
    num1 = mid - begin + 1
    num2 = end - mid 
  
    Left = [0] * (num1) 
    Right = [0] * (num2) 
  
    for i in range(0 , num1): 
        Left[i] = lst[begin + i] 
  
    for j in range(0 , num2): 
        Right[j] = lst[mid + 1 + j] 
  
    i = 0
    j = 0 
    k = begin
  
    while i < num1 and j < num2 : 
        if Left[i] <= Right[j]: 
            lst[k] = Left[i] 
            i += 1
        else: 
            lst[k] = Right[j] 
            j += 1
        k += 1
  
    while i < num1: 
        lst[k] = Left[i] 
        i += 1
        k += 1
  
    while j < num2: 
        lst[k] = Right[j] 
        j += 1
        k += 1
  
def mergeSort(lst,begin,end): 
    if begin < end: 
        mid = (begin+(end-1))//2
  
        mergeSort(lst, begin, mid) 
        mergeSort(lst, mid+1, end) 
        merge(lst, begin, mid, end)

def games_list():
    games_data = open_json()

    tup_list = []
    counter = 0
    for i in games_data:
        tup_list.append((games_data[counter]['name'], games_data[counter]['appid'], games_data[counter]['price']))
        counter += 1

    n = len(tup_list)    
    mergeSort(tup_list, 0, n-1)
    return tup_list

def playerSummary(steamid):
    api_player = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=9B2182C10BA7534CC1C7EC708C080A13&steamids={}'.format(steamid)

    json_player = requests.get(api_player).json()
    online = json_player['response']['players'][0]['personastate']
    account_name = json_player['response']['players'][0]['personaname']
    if online == 0:
        online = "Offline"
    elif online == 1:
        online = "Online"
    elif online == 3:
        online = "Away"
    elif online == 4:
        online = "Snooze"

    welcome_message = "Welcome back {}. Your current status is: {}".format(account_name, online)
    playerinfo = [(account_name, online, welcome_message)]
    
    return playerinfo

    #print(welcome_message)

def ownedGamesByPlaytime():
    api_games = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=9B2182C10BA7534CC1C7EC708C080A13&steamid=76561198028494198&format=json'

    json_games = requests.get(api_games).json()
    owned_games = []
    counter = 0
    for i in json_games['response']['games']:
        owned_games.append((i['appid'], i['playtime_forever']))
        counter += 1
    owned_games.sort(key=lambda x:x[1], reverse=True)
    return owned_games

def mostPlayed():
    list_of_games = ownedGamesByPlaytime()
    all_games = games_list()
    playtime = []
    for i in list_of_games:
        counter = 0
        try:
            while i[0] != all_games[counter][1]:
                counter += 1
            else:
                playtime.append((all_games[counter][0], int((i[1] / 60)), all_games[counter][2]))
        except IndexError:
            pass
    nr_1 = playtime[0]
    nr_2 = playtime[1]
    nr_3 = playtime[2]
    nr_4 = playtime[3]
    nr_5 = playtime[4]

    #print("Your most played game is {} for {} hours".format(nr_1[0], nr_1[1]))
    #print("Your 2nd most played game is {} for {} hours".format(nr_2[0], nr_2[1]))
    #print("Your 3rd most played game is {} for {} hours".format(nr_3[0], nr_3[1]))
    #print("Your 4th most played game is {} for {} hours".format(nr_4[0], nr_4[1]))
    #print("Your 5th most played game is {} for {} hours".format(nr_5[0], nr_5[1]))
    return playtime

def accountValue():
    list_of_games = mostPlayed()
    total = 0
    for i in list_of_games:
        total += i[2]

    print("Your account value is: {} euro's!".format(int(total)))

def friendList():
    api_friends = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=9B2182C10BA7534CC1C7EC708C080A13&steamid=76561198028494198&relationship=friend'

    json_friends = requests.get(api_friends).json()
    friends = []
    for i in json_friends['friendslist']['friends']:
        steamid = i['steamid']
        playerinfo = playerSummary(steamid)
        friends.append((playerinfo[0][0], playerinfo[0][1]))
    
    friends.sort(key=lambda x:x[1], reverse=True)
    print(friends)

def recentlyPlayed():
    api_recently = 'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=9B2182C10BA7534CC1C7EC708C080A13&steamid=76561198028494198&format=json'

    json_recently = requests.get(api_recently).json()
    recent_games = []
    for i in json_recently['response']['games']:
        recent_games.append((i['name'], round(i['playtime_2weeks'] / 60, 2)))
    
    print(recent_games)

#def show_dashboard():
    gesorteerd = games_list('name')
    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('840x450')
    root.configure(background='#1B2838')
    root.title('Steam Dashboard')

    # This is the section of code which creates the gamelabel
    gamelabel = Label(root, text='Placeholder label', bg='#1B2838', fg='white', font=('arial', 12, 'normal'))
    gamelabel.place(x=338, y=210)
    updated_text = gesorteerd[0][0]
    gamelabel.configure(text = updated_text)

    root.mainloop()


playerSummary('76561198028494198')
#show_dashboard()