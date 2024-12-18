from tkinter import *

from shapely.predicates import within

day = 1

spreadsheet_link = open("spreadlink.txt").read()
resx = open("res.txt").read().split(" ")[0]
resy = open("res.txt").read().split(" ")[1]



def set_link():
    spreadsheet_link = spreadsheet_link_entry.get()
    print(spreadsheet_link)
    with open("spreadlink.txt", "w") as file:
        file.write(spreadsheet_link)
    current_spread.config(text="Current Spreadsheet: " + spreadsheet_link)

def set_resx():
    if resx_entry.get().isdigit():
        resx = resx_entry.get()
        with open("spreadlink.txt", "w") as file:
            file.write(resx + " " + resy)
        current_link.config(text="Current Resolution:" + resx + " x " + resy + "            Current Starting Day: " + str(day))

def set_resy():
    if resy_entry.get().isdigit():
        resy = resx_entry.get()
        with open("spreadlink.txt", "w") as file:
            file.write(resx + " " + resy)
        current_link.config(text="Current Resolution:" + resx + " x " + resy + "            Current Starting Day: " + str(day))

def set_day():
    if day_entry.get().isdigit():
        day = day_entry.get()
        current_link.config(text="Current Resolution:" + resx + " x " + resy + "            Current Starting Day: " + str(day))


title_font = ("VT323", 36, "bold")
label_font = ("VT323", 24)

red = "#fe5a46"

root = Tk()
root.title("LCScreenSucker")
root.geometry("710x350")
root.resizable(width=False, height=False)
root.configure(background="Black")


title = Label(root, text="LCScreenSucker", font=title_font, background="Black", fg=red)
title.pack()

frame1 = Frame(root)
frame1.pack(side="top", anchor="nw")

spreadsheet_link_label = Label(frame1, text="Spreadsheet Link: ", font=label_font, background="black", fg=red)
spreadsheet_link_label.pack(side="left")

spreadsheet_link_button = Button(frame1, width=2, anchor="center", command=set_link, bg="#00fd7d")
spreadsheet_link_button.pack(side="right")

spreadsheet_entry = StringVar()
spreadsheet_link_entry = Entry(frame1, font=("VT323", 18), textvariable=spreadsheet_entry)
spreadsheet_link_entry.pack(side="right")

frame2 = Frame(root)
frame2.pack(side="top", anchor="nw", pady=10)

resx_button = Button(frame2, width=2, anchor="center", command=set_resx, bg="#00fd7d")
resx_button.pack(side="right")

Label(frame2, text="Monitor Width:    ", font=label_font, background="black", fg=red).pack(side="left")
resx_entry = Entry(frame2, font=("VT323", 18))
resx_entry.pack(side="right")

frame3 = Frame(root)
frame3.pack(anchor="nw")

resy_button = Button(frame3, width=2, anchor="center", command=set_resy, bg="#00fd7d")
resy_button.pack(side="right")

Label(frame3, text="Monitor Height:   ", font=label_font, background="black", fg=red).pack(side="left")
resy_entry = Entry(frame3, font=("VT323", 18))
resy_entry.pack(side="right")

frame4 = Frame(root)
frame4.pack(anchor="nw", pady = 10)

day_label = Label(frame4, text="Starting Day:     ", font=label_font, background="black", fg=red)
day_label.pack(side="left")

day_button = Button(frame4, width=2, anchor="center", command=set_day, bg="#00fd7d")
day_button.pack(side="right")

day_entry = Entry(frame4, font=("VT323", 18))
day_entry.pack(side="right")

frame5 = Frame(root)
frame5.pack(anchor="nw")

current_link = Label(frame5, text="Current Resolution:" + resx + " x " + resy + "            Current Starting Day: " + str(day), font=("VT323", 10), background="black", fg=red)
current_link.pack()

frame6 = Frame(root)
frame6.pack(anchor="nw")

current_spread = Label(frame6, text="Current Spreadsheet: " + spreadsheet_link, font=("VT323", 10), background="black", fg=red)
current_spread.pack()

root.mainloop()