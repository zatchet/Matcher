import tkinter as tk
import random

root = tk.Tk()
root.title('Happy Birthday babe')
root.geometry("1000x1200")

myLabel = tk.Label(root, text = ' ')
myLabel.pack(pady=20)

global winner
winner = 0

# images
icon1 = tk.PhotoImage(file='res/pic1.gif')
icon2 = tk.PhotoImage(file='res/pic2.gif')
icon3 = tk.PhotoImage(file='res/pic3.gif')
icon4 = tk.PhotoImage(file='res/pic4.gif')
icon5 = tk.PhotoImage(file='res/pic5.gif')
icon6 = tk.PhotoImage(file='res/pic6.gif')
icon7 = tk.PhotoImage(file='res/pic7.gif')
icon8 = tk.PhotoImage(file='res/pic8.gif')

baseicon = tk.PhotoImage(file='res/gray.gif')
winicon = tk.PhotoImage(file='res/pink.gif')

matches = [icon1,icon1,icon2,icon2,icon3,icon3,icon4,icon4,icon5,icon5,icon6,icon6,icon7,icon7,icon8,icon8]

random.shuffle(matches)
print(matches)

my_frame = tk.Frame(root)
my_frame.pack(pady = 10)

count = 0
answer_list = []
answer_dict = {}

def reset():
    global matches, winner
    winner = 0
    matches = [icon1, icon1, icon2, icon2, icon3, icon3, icon4, icon4, icon5, icon5, icon6, icon6, icon7, icon7, icon8,
               icon8]
    random.shuffle(matches)

    myLabel.config(text="")

    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15]
    for button in button_list:
        button.config(text = " ", image=baseicon, state="normal")


def win():
    myLabel.config(text = "WOOOOOOOOO")
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]
    for button in button_list:
        button.config(image = winicon)


def button_click(b, n):
    global count, answer_list, answer_dict, winner

    if b["text"] == ' ' and count < 2:
        b["image"] = matches[n]
        answer_list.append(n)
        answer_dict[b] = matches[n]
        #b["state"] == "disabled"
        count += 1

    if len(answer_list) == 2:
        #time.sleep(2)
        if matches[answer_list[0]] == matches[answer_list[1]]:
            myLabel.config(text='wooooooooo')
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dict = {}
            #inc win counter
            winner += 1
            if winner == 8:
                win()
        else:
            myLabel.config(text='u suck homo')
            #time.sleep(1)
            count = 0
            answer_list = []

            for key in answer_dict:
                key["image"] = baseicon
                key["text"] = ' '

            answer_dict = {}




# buttons
b0 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b0, 0))
b1 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b1, 1))
b2 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b2, 2))
b3 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b3, 3))
b4 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b4, 4))
b5 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b5, 5))
b6 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b6, 6))
b7 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b7, 7))
b8 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b8, 8))
b9 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b9, 9))
b10 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b10, 10))
b11 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b11, 11))
b12 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b12, 12))
b13 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b13, 13))
b14 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b14, 14))
b15 = tk.Button(my_frame, text = ' ', image = baseicon, command = lambda: button_click(b15, 15))


my_Menu = tk.Menu(root)
root.config(menu=my_Menu)

option_menu = tk.Menu(my_Menu, tearoff=False)
my_Menu.add_cascade(label = "options", menu = option_menu)
option_menu.add_command(label = "reset game (this is fun zach)", command = reset)
option_menu.add_command(label = "quit (i suck)", command = root.quit)

# grid
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

b12.grid(row=3,column=0)
b13.grid(row=3,column=1)
b14.grid(row=3,column=2)
b15.grid(row=3,column=3)



root.mainloop()