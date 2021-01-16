import json
import tkinter as tk
import requests
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import *
import RPi.GPIO as GPIO
import time
import sys


user = 76561198256031295

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

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

    for i in range(0, num1):
        Left[i] = lst[begin + i]

    for j in range(0, num2):
        Right[j] = lst[mid + 1 + j]

    i = 0
    j = 0
    k = begin

    while i < num1 and j < num2:
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


def mergeSort(lst, begin, end):
    if begin < end:
        mid = (begin + (end - 1)) // 2

        mergeSort(lst, begin, mid)
        mergeSort(lst, mid + 1, end)
        merge(lst, begin, mid, end)


def games_list():
    games_data = open_json()

    tup_list = []
    counter = 0
    for i in games_data:
        tup_list.append((games_data[counter]['name'], games_data[counter]['appid'], games_data[counter]['price']))
        counter += 1

    n = len(tup_list)
    mergeSort(tup_list, 0, n - 1)
    return tup_list

def playerSummary(steamid):
    api_player = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=9B2182C10BA7534CC1C7EC708C080A13&steamids={}'.format(steamid)

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


def ownedGamesByPlaytime(steamid):
    api_games = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=9B2182C10BA7534CC1C7EC708C080A13&steamid={}&format=json'.format(steamid)

    json_games = requests.get(api_games).json()
    owned_games = []
    counter = 0
    for i in json_games['response']['games']:
        owned_games.append((i['appid'], i['playtime_forever']))
        counter += 1
    owned_games.sort(key=lambda x: x[1], reverse=True)
    return owned_games


def mostPlayed(steamid):
    list_of_games = ownedGamesByPlaytime(steamid)
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

    return playtime


def accountValue(steamid):
    list_of_games = mostPlayed(steamid)
    total = 0
    for i in list_of_games:
        total += i[2]

    # print("Your account value is: {} euro's!".format(int(total)))
    return total


def friendList(steamid):
    api_friends = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=9B2182C10BA7534CC1C7EC708C080A13&steamid={}&relationship=friend'.format(steamid)
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
    return friends


def recentlyPlayed(steamid):
    api_recently = 'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=9B2182C10BA7534CC1C7EC708C080A13&steamid={}&format=json'.format(steamid)

    json_recently = requests.get(api_recently).json()
    recent_games = []
    for i in json_recently['response']['games']:
        try:
            recent_games.append((i['name'], round(i['playtime_2weeks'] / 60, 2)))
        except(KeyError):
            pass

    return recent_games

def pulse( pin, delay1, delay2 ):
   GPIO.output( pin, GPIO.HIGH )
   time.sleep( delay1 )
   GPIO.output( pin, GPIO.LOW )
   time.sleep( delay2 )

def spinServo():
    def servo_pulse( pin_nr, position ):
       def pulse( pin, delay1, delay2 ):
           GPIO.output( pin, GPIO.HIGH )
           time.sleep( delay1 )
           GPIO.output( pin, GPIO.LOW )
           time.sleep( delay2 )
       
       pos = (0.5/1000) + (position/50000)
       pulse(pin_nr, pos , 0.01)
       
    delay = 0.1
    delay_offset = 0.02 

    servo = 25
    GPIO.setup( servo, GPIO.OUT )
    for i in range( 0, 100, 1 ):
        servo_pulse( servo, i )
    time.sleep(delay - delay_offset)
    for i in range( 100, 0, -1 ):
        servo_pulse( servo, i )
    time.sleep(delay - delay_offset)

clock_pin = 19
f_data_pin = 26

GPIO.setup( clock_pin, GPIO.OUT )
GPIO.setup( f_data_pin, GPIO.OUT )

def apa102_send_bytes( clock_pin, f_data_pin, bytes ):
    for i in bytes:
        for x in range(0,8):
            if i % 2 == 0:
                GPIO.output(f_data_pin, GPIO.LOW)
            else:
                GPIO.output(f_data_pin, GPIO.HIGH)
        
            i = i // 2
            
            GPIO.output(clock_pin, GPIO.HIGH)
            GPIO.output(clock_pin, GPIO.LOW)

def apa102( clock_pin, f_data_pin, colors ):
    first = [0,0,0,0]
    last = [255,255,255,255]
    apa102_send_bytes(clock_pin, f_data_pin, first)
    for color_list in colors:
        kleur = [255]
        for color in color_list:
            kleur.append(color)
        apa102_send_bytes(clock_pin, f_data_pin, kleur)
    apa102_send_bytes(clock_pin, f_data_pin, last)

orange = [ 0, 165, 255 ]
green = [ 0, 255, 0 ]
red = [ 0, 0, 100 ]

def colors( x, n, on, off ):
   result = []
   for i in range( 0, n ):
      if i == x:
           result.append( on )
      else:
           result.append( off )
   return result           

def flag( clock_pin, f_data_pin, delay, n = 8 ):
    onlinestate = playerSummary(user)
    if onlinestate[0][1] == 'Offline':
        for x in range(0, n):
            apa102( clock_pin, f_data_pin, colors( x, n, red, red) )
            time.sleep( delay )
    elif onlinestate[0][1] == 'Online':
        for x in range(0, n):
            apa102( clock_pin, f_data_pin, colors( x, n, green, green) )
            time.sleep( delay )
    else:
        for x in range(0, n):
            apa102( clock_pin, f_data_pin, colors( x, n, orange, orange) )
            time.sleep( delay )

sr04_trig = 20
sr04_echo = 21

def sr04( trig_pin, echo_pin ): 
   GPIO.setup( sr04_trig, GPIO.OUT )
   GPIO.setup( sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
   while True:
      GPIO.output(trig_pin, GPIO.HIGH)
      time.sleep(0.2)
      GPIO.output(trig_pin, GPIO.LOW) 

      while GPIO.input(echo_pin) == 0:
         start_time = time.time()

      while GPIO.input(echo_pin) == 1:
         end_time = time.time()

      timedelta = end_time - start_time
      afstand = timedelta * 17150
      distance = "You are sitting {} cm away from your screen!".format(round(afstand, 2))
      return distance

shift_clock_pin = 5
latch_clock_pin = 6
data_pin = 13

GPIO.setup( shift_clock_pin, GPIO.OUT )
GPIO.setup( latch_clock_pin, GPIO.OUT )
GPIO.setup( data_pin, GPIO.OUT )

def hc595( shift_clock_pin, latch_clock_pin, data_pin, value, delay ):
   for x in range(0, 4):
      if value % 2 == 0:
         GPIO.output(data_pin, 0)
      else:
         GPIO.output(data_pin, 1)
         value = value / 2
   GPIO.output(shift_clock_pin, 1)
   time.sleep(delay)
   GPIO.output(shift_clock_pin, 0)
   time.sleep(delay)
   GPIO.output(latch_clock_pin, 1)
   time.sleep(delay)
   GPIO.output(latch_clock_pin, 0)

def walk():
    delay = 0.1
    hc595( shift_clock_pin, latch_clock_pin, data_pin,   1, delay )
    hc595( shift_clock_pin, latch_clock_pin, data_pin,   2, delay )
    hc595( shift_clock_pin, latch_clock_pin, data_pin,   4, delay )
    hc595( shift_clock_pin, latch_clock_pin, data_pin,   8, delay )

def terminate(channel):
    sys.exit()

playerSummary(user)
#recentlyPlayed(user)
spinServo()
flag( clock_pin, f_data_pin, 0.03)