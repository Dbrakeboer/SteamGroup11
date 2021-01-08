from tkinter import *
from aisprint1 import *
from PIL import ImageTk, Image

test = playerSummary('76561198028494198')

splash_root = Tk()
splash_root.title('Steam Dashboard')

splash_width = 750
splash_height = 400

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = (screen_width/2) - (splash_width/2)
y = (screen_height/2) - (splash_height/2)

splash_root.geometry('%dx%d+%d+%d' % (splash_width, splash_height, x, y))
splash_root.overrideredirect(True)
splash_root.configure(bg='#1b2838')

splash_label = Label(splash_root, text=test[0][2], bg='#1b2838', fg='#c7d5e0', font='Arial 10 bold')
splash_label.place(x=220, y=250)

steam_dashboard_text_label = Label(splash_root, text='Steam Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 18 bold')
steam_dashboard_text_label.place(x=270, y=180)

steam_logo = ImageTk.PhotoImage(Image.open("images\steam_logo.png"))
steam_logo_label = Label(image=steam_logo, bg='#1b2838')
steam_logo_label.place(x=320, y=50)

def application():
    splash_root.destroy()

    def showMenuFrame():
        most_played_frame.pack_forget()
        friend_list_frame.pack_forget()
        main_menu_frame.pack(fill='both', expand=True)
        hideMenubar()

    def showMostPlayedFrame():
        main_menu_frame.pack_forget()
        friend_list_frame.pack_forget()
        most_played_frame.pack(fill='both', expand=True)
        showMenubarMostPlayedGames()

    def showFriendListFrame():
        main_menu_frame.pack_forget()
        most_played_frame.pack_forget()
        friend_list_frame.pack(fill='both', expand=True)
        showMenubarFriendList()

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
        menu_bar.add_command(label='Recently Played Games')

    def showMenubarFriendList():
        menu_bar = Menu(root)
        root.config(menu=menu_bar)

        menu_bar.add_command(label='Exit Dashboard', command=exitDashboard)
        menu_bar.add_command(label='Main Menu', command=showMenuFrame)
        menu_bar.add_command(label='Most Played Games', command=showMostPlayedFrame)
        menu_bar.add_command(label='Recently Played Games')

    def showMenubarRecentlyPlayedGames():
        menu_bar = Menu(root)
        root.config(menu=menu_bar)

        menu_bar.add_command(label='Exit Dashboard', command=exitDashboard)
        menu_bar.add_command(label='Main Menu', command=showMenuFrame)
        menu_bar.add_command(label='Most Played Games', command=showMostPlayedFrame)
        menu_bar.add_command(label='Friend List', command=showFriendListFrame)

    root = Tk()
    root.state('zoomed')
    root.title('Steam Dashboard')
    root.iconbitmap('images\steam_icon.ico')
    root.config(bg='#1b2838')
    root.after(0, hideMenubar)

    global steam_logo

    main_menu_frame = Frame(root, bg='#1b2838')
    main_menu_frame.pack(fill='both', expand=True)

    steam_logo = ImageTk.PhotoImage(Image.open("images\steam_logo.png"))
    steam_logo_label = Label(main_menu_frame, image=steam_logo, bg='#1b2838')
    steam_logo_label.pack(pady=(15,5))
    steam_dashboard_text_label = Label(main_menu_frame, text='Steam Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 18 bold')
    steam_dashboard_text_label.pack()
    steam_dashboard_menu_text_label = Label(main_menu_frame, text='Main Menu', bg='#1b2838', fg='#c7d5e0', font='Arial 10 bold', borderwidth=2, width=20, relief='ridge')
    steam_dashboard_menu_text_label.pack()
    menu_message = Label(main_menu_frame, text='Welcome to your personal Steam Dashboard,' + ' ' + test[0][0] + '.' + ' Use the menu buttons below to navigate to your desired statistics.', bg='#1b2838', fg='#c7d5e0', font='Arial 13 bold')
    menu_message.pack(pady=30)
    most_played_button = Button(main_menu_frame, text='Most Played Games', bg='#1b2838', fg='#c7d5e0', font='Arial 11 bold', width=20, activebackground='#66c0f4', activeforeground='#1b2838', command=showMostPlayedFrame)
    most_played_button.pack(pady=5, padx=150)
    friend_list_button = Button(main_menu_frame, text='Friend List', bg='#1b2838', fg='#c7d5e0', font='Arial 11 bold', width=20, activebackground='#66c0f4', activeforeground='#1b2838', command=showFriendListFrame)
    friend_list_button.pack(pady=5, padx=25)
    recently_played_button = Button(main_menu_frame, text='Recently Played Games', bg='#1b2838', fg='#c7d5e0', font='Arial 11 bold', width=20, activebackground='#66c0f4', activeforeground='#1b2838')
    recently_played_button.pack(pady=5, padx=30)
    exit_dashboard_button = Button(main_menu_frame, text='Exit Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 11 bold', width=20, activebackground='#66c0f4', activeforeground='#1b2838', command=exitDashboard)
    exit_dashboard_button.pack(pady=5, padx=30)
    recently_played_button.pack(pady=5, padx=30)
    status_label = Label(main_menu_frame, text=test[0][1], fg='#66c0f4', bg='#1b2838', font='Arial 11 bold')
    status_label.pack(pady=(30,0))

    most_played_frame = Frame(root, bg='#1b2838')
    steam_logo2 = ImageTk.PhotoImage(Image.open("images\steam_logo.png"))
    steam_logo_label2 = Label(most_played_frame, image=steam_logo, bg='#1b2838')
    steam_logo_label2.pack(pady=(15, 5))
    steam_dashboard_text_label2 = Label(most_played_frame, text='Steam Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 18 bold')
    steam_dashboard_text_label2.pack()
    steam_dashboard_menu_text_label2 = Label(most_played_frame, text='Most Played Games', bg='#1b2838', fg='#c7d5e0', font='Arial 10 bold', borderwidth=2, width=20, relief='ridge')
    steam_dashboard_menu_text_label2.pack()

    friend_list_frame = Frame(root, bg='#1b2838')
    steam_logo3 = ImageTk.PhotoImage(Image.open("images\steam_logo.png"))
    steam_logo_label3 = Label(friend_list_frame, image=steam_logo, bg='#1b2838')
    steam_logo_label3.pack(pady=(15, 5))
    steam_dashboard_text_label3 = Label(friend_list_frame, text='Steam Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 18 bold')
    steam_dashboard_text_label3.pack()
    steam_dashboard_menu_text_label3 = Label(friend_list_frame, text='Friend List', bg='#1b2838', fg='#c7d5e0',font='Arial 10 bold', borderwidth=2, width=20, relief='ridge')
    steam_dashboard_menu_text_label3.pack()

    recently_played_frame = Frame(root, bg='#1b2838')
    steam_logo4 = ImageTk.PhotoImage(Image.open("images\steam_logo.png"))
    steam_logo_label4 = Label(recently_played_frame, image=steam_logo, bg='#1b2838')
    steam_logo_label4.pack(pady=(15, 5))
    steam_dashboard_text_label4 = Label(recently_played_frame, text='Steam Dashboard', bg='#1b2838', fg='#c7d5e0', font='Arial 18 bold')
    steam_dashboard_text_label4.pack()
    steam_dashboard_menu_text_label4 = Label(recently_played_frame, text='Recently Played Games', bg='#1b2838', fg='#c7d5e0',font='Arial 10 bold', borderwidth=2, width=20, relief='ridge')
    steam_dashboard_menu_text_label4.pack()

splash_root.after(3000, application)
mainloop()
