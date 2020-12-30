# Creates tkinter GUI for getting user input and displaying results

import tkinter as tk
from collections import deque
from random import randrange


class Dice:
    # list of dice types
    dice_list = deque([4, 6, 8, 10, 12, 20])


def calc_roll_results(dice, roll_amount):
    result_list = []
    total = 0
    for x in range(roll_amount):
        rand_roll = randrange(1, dice + 1)
        result_list.append(str(rand_roll))
        total += rand_roll
    result_list.append(total)
    return result_list


def calc_roll_total(total):
    mod1 = int(lbl_mod1['text'])
    mod2 = int(lbl_mod2['text'])
    proficiency = int(lbl_proficiency['text'])

    new_total = total + mod1 + mod2 + proficiency
    result_formula = f'{total} + {mod1} + {mod2} + {proficiency} = {new_total}'
    return result_formula


# ---------------------------------------------------------------------------------------------
# tk.Button commands
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
#
# ---------------------------------------------------------------------------------------------



def main():
    window = tk.Tk()
    window.title('Grip it and rip it')
    # configure window grid layout
    window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=50, weight=1)
    window.columnconfigure([0, 1, 2, 3], minsize=75, weight=1)

    btn_dec_dice = Button(master=window, text='-', bg='#747cd6', command=Button.decrease_dice, row=0, column=0)
    window.mainloop()


class Button:
    def __init__(self, master, text, bg, command, row, column, relief=tk.RAISED, columnspan=1, bd=3, sticky='nsew'):
        self.master = master
        self.text = text
        self.bg = bg
        self.command = command
        self.row = row
        self.column = column
        self.relief = relief
        self.columnspan = columnspan
        self.bd = bd
        self.sticky = sticky

    def create_tk_button(self):
        button = tk.Button(master=self.master,
                           text=self.text,
                           bg=self.bg,
                           relief=self.relief,
                           command=self.command,
                           bd=self.bd)
        button.grid(row=self.row,
                    column=self.column,
                    columnspan=self.columnspan,
                    sticky=self.sticky)
        return button

    def roll_click(self):
        # calculate results
        results = calc_roll_results(int(lbl_dice['text']), int(lbl_roll_amount['text']))
        total_result = calc_roll_total(results.pop())
        # display results
        results_str = ', '.join(results)
        lbl_results['text'] = f'{results_str}'
        lbl_total['text'] = f'{total_result}'

    def reset_click(self):
        # set dice_list to proper order
        Dice.dice_list = deque([4, 6, 8, 10, 12, 20])
        # set all labels to defaults
        lbl_dice['text'] = f'{Dice.dice_list[0]}'
        lbl_roll_amount['text'] = f'{1}'
        lbl_mod1['text'] = f'{0}'
        lbl_mod2['text'] = f'{0}'
        lbl_proficiency['text'] = f'{0}'
        lbl_results['text'] = f'{""}'
        lbl_total['text'] = f'{""}'

    def roll_d20(self):
        results = calc_roll_results(20, 1)
        lbl_results['text'] = f'{results.pop()}'
        lbl_total['text'] = f'{""}'

    def increase_dice(self):
        Dice.dice_list.rotate(-1)
        lbl_dice['text'] = f'{Dice.dice_list[0]}'

    def decrease_dice(self):
        Dice.dice_list.rotate(1)
        lbl_dice['text'] = f'{Dice.dice_list[0]}'

    def increase_roll_amount(self):
        value = int(lbl_roll_amount['text'])
        lbl_roll_amount['text'] = f'{value + 1}'

    def decrease_roll_amount(self):
        if int(lbl_roll_amount['text']) != 1:
            value = int(lbl_roll_amount['text'])
            lbl_roll_amount['text'] = f'{value - 1}'

    def increase_mod1(self):
        value = int(lbl_mod1['text'])
        lbl_mod1['text'] = f'{value + 1}'

    def decrease_mod1(self):
        value = int(lbl_mod1['text'])
        lbl_mod1['text'] = f'{value - 1}'

    def increase_mod2(self):
        value = int(lbl_mod2['text'])
        lbl_mod2['text'] = f'{value + 1}'

    def decrease_mod2(self):
        value = int(lbl_mod2['text'])
        lbl_mod2['text'] = f'{value - 1}'

    def increase_proficiency(self):
        value = int(lbl_proficiency['text'])
        lbl_proficiency['text'] = f'{value + 1}'

    def decrease_proficiency(self):
        value = int(lbl_proficiency['text'])
        lbl_proficiency['text'] = f'{value - 1}'


# ---------------------------------------------------------------------------------------------
# tk setup and widgets
# ---------------------------------------------------------------------------------------------
window = tk.Tk()
window.title('Grip it and rip it')
# configure window grid layout
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=75, weight=1)

# row 0 widgets (Select Dice) -------------------------------------
lbl_dice_prompt = tk.Label(master=window, text='Dice', bg='#4f5bd5')
lbl_dice_prompt.grid(row=0, column=0, sticky='nsew')

# decrement dice type button
# btn_dec_dice = tk.Button(master=window, text='-', bg='#747cd6', relief=tk.RAISED, bd=3, command=decrease_dice)
# btn_dec_dice.grid(row=0, column=1, sticky='nsew')

# dice type label
lbl_dice = tk.Label(master=window, text=Dice.dice_list[0], bg='#747cd6')
lbl_dice.grid(row=0, column=2, sticky='nsew')

# increment dice type button
btn_inc_dice = tk.Button(master=window, text='+', bg='#747cd6', relief=tk.RAISED, bd=3, command=increase_dice)
btn_inc_dice.grid(row=0, column=3, sticky='nsew')

# row 1 widgets (Set amount of Dice to roll) ----------------------
lbl_roll_amount_prompt = tk.Label(master=window, text='Amount', bg='#962fbf')
lbl_roll_amount_prompt.grid(row=1, column=0, sticky='nsew')

# decrement amount of dice rolls button
btn_dec_roll_amount = tk.Button(master=window, text='-', bg='#a661c2', relief=tk.RAISED, bd=3,
                                command=decrease_roll_amount)
btn_dec_roll_amount.grid(row=1, column=1, sticky='nsew')

# amount of dice rolls label
lbl_roll_amount = tk.Label(master=window, text=1, bg='#a661c2')
lbl_roll_amount.grid(row=1, column=2, sticky='nsew')

# increment amount of dice rolls button
btn_inc_roll_amount = tk.Button(master=window, text='+', bg='#a661c2', relief=tk.RAISED, bd=3,
                                command=increase_roll_amount)
btn_inc_roll_amount.grid(row=1, column=3, sticky='nsew')

# row 2 widgets (Set Modifier 1) ---------------------------------
lbl_mod1_prompt = tk.Label(master=window, text='Modifier\n1', bg='#d62976')
lbl_mod1_prompt.grid(row=2, column=0, sticky='nsew')

# decrement modifier1 button
btn_dec_mod1 = tk.Button(master=window, text='-', bg='#d45d92', relief=tk.RAISED, bd=3, command=decrease_mod1)
btn_dec_mod1.grid(row=2, column=1, sticky='nsew')

# modifier1 label
lbl_mod1 = tk.Label(master=window, text='0', bg='#d45d92')
lbl_mod1.grid(row=2, column=2, sticky='nsew')

# increment modifier1 button
btn_inc_mod1 = tk.Button(master=window, text='+', bg='#d45d92', relief=tk.RAISED, bd=3, command=increase_mod1)
btn_inc_mod1.grid(row=2, column=3, sticky='nsew')

# row 3 widgets (Set Modifier 2) ---------------------------------
lbl_mod2_prompt = tk.Label(master=window, text='Modifier\n2', bg='#fa7e1e')
lbl_mod2_prompt.grid(row=3, column=0, sticky='nsew')

# decrement modifier2 button
btn_dec_mod2 = tk.Button(master=window, text='-', bg='#fca662', relief=tk.RAISED, bd=3, command=decrease_mod2)
btn_dec_mod2.grid(row=3, column=1, sticky='nsew')

# modifier2 label
lbl_mod2 = tk.Label(master=window, text='0', bg='#fca662')
lbl_mod2.grid(row=3, column=2, sticky='nsew')

# increment modifier2 button
btn_inc_mod2 = tk.Button(master=window, text='+', bg='#fca662', relief=tk.RAISED, bd=3, command=increase_mod2)
btn_inc_mod2.grid(row=3, column=3, sticky='nsew')

# row 4 widgets (Set Proficiency bonus) --------------------------
lbl_proficiency_prompt = tk.Label(master=window, text='Proficiency\nBonus', bg='#feda75')
lbl_proficiency_prompt.grid(row=4, column=0, sticky='nsew')

# decrement proficiency button
btn_dec_proficiency = tk.Button(master=window, text='-', bg='#ffe8a8', relief=tk.RAISED, bd=3,
                                command=decrease_proficiency)
btn_dec_proficiency.grid(row=4, column=1, sticky='nsew')

# proficiency label
lbl_proficiency = tk.Label(master=window, text='0', bg='#ffe8a8')
lbl_proficiency.grid(row=4, column=2, sticky='nsew')

# increment proficiency button
btn_inc_proficiency = tk.Button(master=window, text='+', bg='#ffe8a8', relief=tk.RAISED, bd=3,
                                command=increase_proficiency)
btn_inc_proficiency.grid(row=4, column=3, sticky='nsew')

# row 5 widgets (Roll d20, Reset, and Roll buttons) --------------
btn_reset = tk.Button(master=window, text='Reset\nAll', bg='#eb3b28', relief=tk.RAISED, bd=3, command=reset_click)
btn_reset.grid(row=5, column=0, sticky='nsew')

# roll d20 button
btn_roll_d20 = tk.Button(master=window, text='Roll\nd20', bg='#79db72', relief=tk.RAISED, bd=3, command=roll_d20)
btn_roll_d20.grid(row=5, column=1, sticky='nsew')

# roll button
btn_roll = tk.Button(master=window, text='Roll\nAll', bg='#24b519', relief=tk.RAISED, bd=3, command=roll_click)
btn_roll.grid(row=5, column=2, columnspan=2, sticky='nsew')

# row 6 widgets (Results of Dice roll(s)) -------------------------
lbl_results_prompt = tk.Label(master=window, text='Roll\nResults', bg='#d6d6d6')
lbl_results_prompt.grid(row=6, column=0, sticky='nsew')

lbl_results = tk.Label(master=window, text='', bg='#e3e3e3')
lbl_results.grid(row=6, column=1, columnspan=3, sticky='nsew')

# row 7 widgets (Total of Roll results) ---------------------------
lbl_total_prompt = tk.Label(master=window, text='Total\nResult', bg='#bdbdbd')
lbl_total_prompt.grid(row=7, column=0, sticky='nsew')

lbl_total = tk.Label(master=window, text='', bg='#d6d6d6')
lbl_total.grid(row=7, column=1, columnspan=3, sticky='nsew')

window.mainloop()

if __name__ == '__main__':
    main()
