import json
import tkinter as tk
import requests
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import *


def open_json():
    with open("steam.json", "r") as steam:
        data = json.load(steam)
        return data


def playerSummary(steamid):
    api_player = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=9B2182C10BA7534CC1C7EC708C080A13&steamids={}'.format(
        steamid)

    json_player = requests.get(api_player).json()

    playerinfo = []

    for i in json_player['response']['players']:
        online = i['personastate']
        account_name = i['personaname']
        if online == 0:
            online = "Offline"
        elif online == 1:
            online = "Online"
        elif online == 3:
            online = "Away"
        elif online == 4:
            online = "Snooze"

        if len(json_player['response']['players']) == 1:
            welcome_message = "Welcome back {}. Your current status is: {}".format(account_name, online)
            playerinfo.append((account_name, online, welcome_message))
        else:
            playerinfo.append((account_name, online))

    return playerinfo

    # print(welcome_message)

def friendList():
    api_friends = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=9B2182C10BA7534CC1C7EC708C080A13&steamid=76561198028494198&relationship=friend'
    json_friends = requests.get(api_friends).json()
    players = []
    friends = []
    for i in json_friends['friendslist']['friends']:
        steamid = i['steamid']
        players.append(steamid)
    counter = 0
    my_string = ', '.join(players)
    playerinfo = playerSummary(my_string)

    for player in playerinfo:
        friends.append((playerinfo[counter][0], playerinfo[counter][1]))
        counter += 1

    friends.sort(key=lambda x: x[1], reverse=True)
    print(friends)
    return friends

friendList()
