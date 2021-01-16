from aisprint1 import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

start = playerSummary(user)

splash_root = Tk()
splash_root.title('Steam Dashboard')

splash_width = 750
splash_height = 400

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = (screen_width / 2) - (splash_width / 2)
y = (screen_height / 2) - (splash_height / 2)

splash_root.geometry('%dx%d+%d+%d' % (splash_width, splash_height, x, y))
splash_root.overrideredirect(True)
splash_root.configure(bg='#1b2838')

steam_logo = ImageTk.PhotoImage(Image.open("./images/steam_logo.png"))
steam_logo_label = Label(image=steam_logo, bg='#1b2838')
steam_logo_label.pack(padx=(25, 0), pady=(50, 0))

steam_dashboard_text_label = Label(splash_root, text='Steam Dashboard', bg='#1b2838', fg='#c7d5e0',
                                   font='Arial 18 bold')
steam_dashboard_text_label.pack(padx=(25, 0), pady=(15, 0))

splash_label = Label(splash_root, text=start[0][2], bg='#1b2838', fg='#c7d5e0', font='Arial 10 bold')
splash_label.pack(padx=(25, 0), pady=(25, 0))

def application():
    splash_root.destroy()

    def showMenuFrame():
        most_played_frame.pack_forget()
        friend_list_frame.pack_forget()
        recently_played_frame.pack_forget()
        main_menu_frame.pack(fill='both', expand=True)
        hideMenubar()
        walk()
        
    def showMostPlayedFrame():
        main_menu_frame.pack_forget()
        friend_list_frame.pack_forget()
        recently_played_frame.pack_forget()
        most_played_frame.pack(fill='both', expand=True)
        histoPlayed()
        showMenubarMostPlayedGames()
        walk()

    def showFriendListFrame():
        main_menu_frame.pack_forget()
        most_played_frame.pack_forget()
        recently_played_frame.pack_forget()
        friend_list_frame.pack(fill='both', expand=True)
        insertFriendList()
        friendChart()
        showMenubarFriendList()
        walk()

    def showRecentlyPlayedGamesFrame():
        main_menu_frame.pack_forget()
        most_played_frame.pack_forget()
        friend_list_frame.pack_forget()
        recently_played_frame.pack(fill='both', expand=True)
        insertRecentlyPlayedList()
        showMenubarRecentlyPlayedGames()
        walk()

    def hideMenubar():
        emptyMenu = Menu(root)
        root.config(menu=emptyMenu)

    def exitDashboard():
        root.destroy()

    def showMenubarMostPlayedGames():
        menu_bar = Menu(root)
        root.config(menu=menu_bar)

        menu_bar.add_command(label='Exit Dashboard', command=exitDashboard)
        menu_bar.add_command(label='Main Menu', command=showMenuFrame)
        menu_bar.add_command(label='Friend List', command=showFriendListFrame)
        menu_bar.add_command(label='Recently Played Games', command=showRecentlyPlayedGamesFrame)

    def showMenubarFriendList():
        menu_bar = Menu(root)
        root.config(menu=menu_bar)

        menu_bar.add_command(label='Exit Dashboard', command=exitDashboard)
        menu_bar.add_command(label='Main Menu', command=showMenuFrame)
        menu_bar.add_command(label='Most Played Games', command=showMostPlayedFrame)
        menu_bar.add_command(label='Recently Played Games', command=showRecentlyPlayedGamesFrame)

    def showMenubarRecentlyPlayedGames():
        menu_bar = Menu(root)
        root.config(menu=menu_bar)

        menu_bar.add_command(label='Exit Dashboard', command=exitDashboard)
        menu_bar.add_command(label='Main Menu', command=showMenuFrame)
        menu_bar.add_command(label='Most Played Games', command=showMostPlayedFrame)
        menu_bar.add_command(label='Friend List', command=showFriendListFrame)

    def insertFriendList():
        friendlistlst = friendList(user)
        friend_list_listbox.delete(0, 'end')
        teller = 0
        for row in friendlistlst:
            teller = teller + 1
            friend_list_listbox.insert(END, f"{row[0]} - {row[1]}", )

        if teller == 0 :
            friend_list_listbox.insert(1, 'Your friend list is empty.')

        friend_list_listbox.pack(side=LEFT, pady=(15, 30), padx=(30, 0))
        del friendlistlst
    
    def friendChart():
        activities = ['Online', 'Offline', 'Away', 'Snooze']

        online = 0
        offline = 0
        away = 0
        snooze = 0

        friends = friendList(user)

        for i in friends:
            if i[1] == 'Online':
                online += 1
            elif i[1] == 'Offline':
                offline += 1
            elif i[1] == 'Away':
                away += 1
            else:
                snooze += 1

        piechartfig = plt.figure(figsize=(6, 6), dpi=100)
        piechartfig.set_size_inches(8, 6)

        slices = [online, offline, away, snooze]
        colors = ['green', 'red', 'orange', 'blue']
        plt.pie(slices, labels=activities, pctdistance=0.9, colors=colors, startangle=90, shadow=False, explode=(0.1, 0, 0, 0), radius=1.2, autopct='%1.1f%%', textprops={'color':"w"})
        plt.legend(bbox_to_anchor=(0.8, 0.65))
        piechartfig.set_facecolor('#1b2838')
        canvas_piechart = FigureCanvasTkAgg(piechartfig, friend_list_frame)
        canvas_piechart.draw()
        canvas_piechart.get_tk_widget().pack(side=RIGHT, pady=(0, 25))

    def histoPlayed():
        hours = []
        games_list = mostPlayed(user)

        for i in games_list:
            hours.append(i[1])

        histogramfig = plt.figure(figsize=(6, 6), dpi=100)
        range = (1, 500)
        bins = 50

        plt.hist(hours, bins, range, color='#66c0f4', histtype='bar', rwidth=0.8)
        plt.xlabel('Hours played')
        plt.ylabel('No. of games')
        plt.title('Playtime')
        histogramfig.subplots_adjust(bottom=0.2)
        histogramfig.patch.set_facecolor('#1b2838')

        ax = plt.gca()
        ax.set_facecolor('#2a475e')
        ax.set_xlabel('Hours played')
        ax.set_ylabel('No. of games')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        canvas_histogram = FigureCanvasTkAgg(histogramfig, most_played_frame)
        canvas_histogram.draw()
        canvas_histogram.get_tk_widget().pack(pady=(1, 0))

    def insertRecentlyPlayedList():
        recentlistlst = recentlyPlayed(user)
        recent_games_listbox.delete(0, 'end')
        teller = 0
        for row in recentlistlst:
            teller = teller + 1
            recent_games_listbox.insert(END, f"{row[0]} - {row[1]} hours", )

        if teller == 0 :
            recent_games_listbox.insert(1, 'No games played within the last 2 weeks.')

        del recentlistlst
        recent_games_listbox.pack(pady=(50, 50))

    root = Tk()
    root.attributes('-fullscreen', True)
    root.title('Steam Dashboard | ' + start[0][0])
    root.config(bg='#1b2838')
    root.after(0, hideMenubar)
    root.update()

    global steam_logo

    main_menu_frame = Frame(root, bg='#1b2838')
    main_menu_frame.pack(fill='both', expand=True)

    steam_logo = ImageTk.PhotoImage(Image.open("./images/steam_logo.png"))
    steam_logo_label = Label(main_menu_frame, image=steam_logo, bg='#1b2838')
    steam_logo_label.pack(pady=(15, 5))
    steam_dashboard_text_label = Label(main_menu_frame, text='Steam Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 18 bold')
    steam_dashboard_text_label.pack()
    steam_dashboard_menu_text_label = Label(main_menu_frame, text='Main Menu', bg='#1b2838', fg='#c7d5e0', font='Arial 10 bold', borderwidth=2, width=20, relief='ridge')
    steam_dashboard_menu_text_label.pack()
    menu_message = Label(main_menu_frame, text='Welcome to your personal Steam Dashboard,' + ' ' + start[0][0] + '.\n'+ ' Use the menu buttons below to navigate to your desired statistics.', bg='#1b2838', fg='#c7d5e0', font='Arial 13 bold')
    menu_message.pack(pady=30)
    most_played_button = Button(main_menu_frame, text='Most Played Games', bg='#1b2838', fg='#c7d5e0', font='Arial 11 bold', width=20, activebackground='#66c0f4', activeforeground='#1b2838', command=showMostPlayedFrame)
    most_played_button.pack(pady=5, padx=150)
    friend_list_button = Button(main_menu_frame, text='Friend List', bg='#1b2838', fg='#c7d5e0', font='Arial 11 bold', width=20, activebackground='#66c0f4', activeforeground='#1b2838', command=showFriendListFrame)
    friend_list_button.pack(pady=5, padx=25)
    recently_played_button = Button(main_menu_frame, text='Recently Played Games', bg='#1b2838', fg='#c7d5e0', font='Arial 11 bold', width=20, activebackground='#66c0f4', activeforeground='#1b2838', command=showRecentlyPlayedGamesFrame)
    recently_played_button.pack(pady=5, padx=30)
    exit_dashboard_button = Button(main_menu_frame, text='Exit Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 11 bold', width=20, activebackground='#66c0f4', activeforeground='#1b2838', command=exitDashboard)
    exit_dashboard_button.pack(pady=5, padx=30)
    recently_played_button.pack(pady=5, padx=30)
    status_label = Label(main_menu_frame, text=start[0][1], fg='#66c0f4', bg='#1b2838', font='Arial 11 bold')
    status_label.pack(pady=(30, 0))
    
    distance = sr04(sr04_trig, sr04_echo)
    sr04_label = Label(main_menu_frame, text=distance, fg='#66c0f4', bg='#1b2838', font='Arial 11 bold')
    sr04_label.pack()
    
    root.update()

    most_played_frame = Frame(root, bg='#1b2838')
    steam_logo2 = ImageTk.PhotoImage(Image.open("./images/steam_logo.png"))
    steam_logo_label2 = Label(most_played_frame, image=steam_logo, bg='#1b2838')
    steam_logo_label2.pack(pady=(15, 5))
    steam_dashboard_text_label2 = Label(most_played_frame, text='Steam Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 18 bold')
    steam_dashboard_text_label2.pack()
    steam_dashboard_menu_text_label2 = Label(most_played_frame, text='Most Played Games', bg='#1b2838', fg='#c7d5e0', font='Arial 10 bold', borderwidth=2, width=20, relief='ridge')
    steam_dashboard_menu_text_label2.pack()

    top5_text_label = Label(most_played_frame, text='MY TOP 5', bg='#1b2838', fg='#66c0f4', font='Arial 15 bold')
    top5_text_label.pack(pady=(20, 0))

    playtime = mostPlayed(user)

    top5_games_text_label = Label(most_played_frame, justify=LEFT, bg='#1b2838', fg='#c7d5e0', font='Arial 10 bold',
                                  text='#1 {} | {} hours'.format(playtime[0][0], playtime[0][1])
                                       + '\n' + '#2 {} | {} hours'.format(playtime[1][0], playtime[1][1])
                                       + '\n' + '#3 {} | {} hours'.format(playtime[2][0], playtime[2][1])
                                       + '\n' + '#4 {} | {} hours'.format(playtime[3][0], playtime[3][1])
                                       + '\n' + '#5 {} | {} hours'.format(playtime[4][0], playtime[4][1]))
    top5_games_text_label.pack()

    funfact_text_label = Label(most_played_frame, text='FUN FACT', bg='#1b2838', fg='#66c0f4', font='Arial 15 bold')
    funfact_text_label.pack(pady=(20, 0))

    total = accountValue(user)

    funfact_accountvalue_text_label = Label(most_played_frame, justify=RIGHT, bg='#1b2838', fg='#c7d5e0', font='Arial 10 bold', text="Your account value is €{}!".format(int(total)))
    funfact_accountvalue_text_label.pack(pady=(1, 0))

    friend_list_frame = Frame(root, bg='#1b2838')
    steam_logo3 = ImageTk.PhotoImage(Image.open("./images/steam_logo.png"))
    steam_logo_label3 = Label(friend_list_frame, image=steam_logo, bg='#1b2838')
    steam_logo_label3.pack(pady=(15, 5))
    steam_dashboard_text_label3 = Label(friend_list_frame, text='Steam Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 18 bold')
    steam_dashboard_text_label3.pack()
    steam_dashboard_menu_text_label3 = Label(friend_list_frame, text='Friend List', bg='#1b2838', fg='#c7d5e0', font='Arial 10 bold', borderwidth=2, width=20, relief='ridge')
    steam_dashboard_menu_text_label3.pack()
    friend_list_listbox = Listbox(friend_list_frame, fg='#c7d5e0', bg='#2a475e', width=40, height=200, font=("Arial 15"))

    recently_played_frame = Frame(root, bg='#1b2838')
    steam_logo4 = ImageTk.PhotoImage(Image.open("./images/steam_logo.png"))
    steam_logo_label4 = Label(recently_played_frame, image=steam_logo, bg='#1b2838')
    steam_logo_label4.pack(pady=(15, 5))
    steam_dashboard_text_label4 = Label(recently_played_frame, text='Steam Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 18 bold')
    steam_dashboard_text_label4.pack()
    steam_dashboard_menu_text_label4 = Label(recently_played_frame, text='Recently Played Games', bg='#1b2838', fg='#c7d5e0', font='Arial 10 bold', borderwidth=2, width=20, relief='ridge')
    steam_dashboard_menu_text_label4.pack()
    recently_played_info_label = Label(recently_played_frame, text='Below you can find all your games played within the last 2 weeks with their matching playtime.', bg='#1b2838', fg='#c7d5e0', font='Arial 13 bold')
    recently_played_info_label.pack(pady=(50, 0))
    recent_games_listbox = Listbox(recently_played_frame, fg='#c7d5e0', bg='#2a475e', width=40, height=60, font=("Arial 15"))
    
    switch = 23
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(switch, GPIO.RISING, callback=terminate)

def boot():
    application()
    flag( clock_pin, data_pin, 0.03)

splash_root.after(3000, boot)
mainloop()

