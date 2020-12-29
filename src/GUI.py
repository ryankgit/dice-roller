# .../dice-roller/src/GUI.py
# Creates tkinter GUI for getting user input and displaying results

import tkinter as tk
from collections import deque

# list of dice types
dice_list = deque([4, 6, 8, 10, 12, 20])


# ---------------------------------------------------------------------------------------------
# tk.Button commands
# ---------------------------------------------------------------------------------------------
def roll_click():
    dice = lbl_dice['text']
    roll_amount = lbl_roll_amount['text']
    print(dice)
    print(roll_amount)
    # send to function or file to calc results


def increase_dice():
    dice_list.rotate(-1)
    lbl_dice["text"] = f"{dice_list[0]}"


def decrease_dice():
    dice_list.rotate(1)
    lbl_dice["text"] = f"{dice_list[0]}"


def increase_roll_amount():
    value = int(lbl_roll_amount["text"])
    lbl_roll_amount["text"] = f"{value + 1}"


def decrease_roll_amount():
    if int(lbl_roll_amount["text"]) != 1:
        value = int(lbl_roll_amount["text"])
        lbl_roll_amount["text"] = f"{value - 1}"


# ---------------------------------------------------------------------------------------------
# tk setup and widgets
# ---------------------------------------------------------------------------------------------
window = tk.Tk()
# configure window grid layout
window.rowconfigure([0, 1, 2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# decrement dice type button
btn_dec_dice = tk.Button(master=window, text="-", command=decrease_dice)
btn_dec_dice.grid(row=0, column=0, sticky="nsew")

# dice type label
lbl_dice = tk.Label(master=window, text=dice_list[0])
lbl_dice.grid(row=0, column=1)

# increment dice type button
btn_inc_dice = tk.Button(master=window, text="+", command=increase_dice)
btn_inc_dice.grid(row=0, column=2, sticky="nsew")

# decrement amount of dice rolls button
btn_dec_roll_amount = tk.Button(master=window, text="-", command=decrease_roll_amount)
btn_dec_roll_amount.grid(row=1, column=0, sticky="nsew")

# amount of dice rolls label
lbl_roll_amount = tk.Label(master=window, text=1)
lbl_roll_amount.grid(row=1, column=1)

# increment amount of dice rolls button
btn_inc_roll_amount = tk.Button(master=window, text="+", command=increase_roll_amount)
btn_inc_roll_amount.grid(row=1, column=2, sticky="nsew")

# roll button
btn_roll = tk.Button(master=window, text='Roll', command=roll_click)
btn_roll.grid(row=2, column=1, sticky="nsew")

window.mainloop()
