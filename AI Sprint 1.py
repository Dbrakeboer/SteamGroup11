import json
import tkinter as tk 
from tkinter import ttk 
from tkinter import * 

def open_json():
    with open("steam.json", "r") as steam:
        data = json.load(steam)
        return data

def first_game():
    games_data = open_json()
    print(games_data[0]['name'])

def games_list(input):
    games_data = open_json()
    games_sorted = []
    counter = 0
    for i in games_data:
        games_sorted.append(games_data[counter][input])
        counter += 1
        
    gesorteerd = sorted(games_sorted)
    return gesorteerd

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

def show_dashboard():
    gesorteerd = sorted_games()
    root = Tk() 

    # This is the section of code which creates the main window 
    root.geometry('840x450') 
    root.configure(background='#1B2838') 
    root.title('Steam Dashboard') 

    # This is the section of code which creates the gamelabel 
    gamelabel = Label(root, text='Placeholder label', bg='#1B2838', fg='white', font=('arial', 12, 'normal'))
    gamelabel.place(x=338, y=210)
    updated_text = gesorteerd[0]
    gamelabel.configure(text = updated_text)

    root.mainloop()

def sorted_games():
    list_of_games = games_list('name')
    n = len(list_of_games)
    mergeSort(list_of_games, 0, n-1)

    print(list_of_games[0])

    return list_of_games


show_dashboard()