import tkinter as tk
from collections import deque
from random import randrange
from functools import partial


# ---------------------------------------------------------------------------------------------
# classes
# ---------------------------------------------------------------------------------------------
class Dice:
    # list of dice types
    dice_list = deque([4, 6, 8, 10, 12, 20])


class Widgets:
    # dictionary of widgets
    # key: widget name, value: tk widget
    dict = {}


class Root:
    window = tk.Tk()
    window.title('Grip it and rip it ¯\\_(ツ)_/¯')
    # configure window grid layout
    window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=50, weight=1)
    window.columnconfigure([0, 1, 2, 3], minsize=75, weight=1)


class Button:
    def __init__(self, name, text, bg, command, row, column, master=Root.window, relief=tk.RAISED, columnspan=1, bd=3,
                 sticky='nsew'):
        self.name = name
        self.text = text
        self.bg = bg
        self.command = command
        self.row = row
        self.column = column
        self.master = master
        self.relief = relief
        self.columnspan = columnspan
        self.bd = bd
        self.sticky = sticky

        # create tk.Button
        btn = tk.Button(master=self.master, text=self.text, bg=self.bg, relief=self.relief, command=self.command,
                        bd=self.bd)
        # add tk.Button to grid
        btn.grid(row=self.row, column=self.column, columnspan=self.columnspan, sticky=self.sticky)
        # add tk.Button to dict (key: unique name, value: tk.Button)
        Widgets.dict.update({name: btn})


class Label:
    def __init__(self, name, text, bg, row, column, master=Root.window, columnspan=1, sticky='nsew'):
        self.name = name
        self.text = text
        self.bg = bg
        self.row = row
        self.column = column
        self.master = master
        self.columnspan = columnspan
        self.sticky = sticky

        # create tk.Label
        lbl = tk.Label(master=self.master, text=self.text, bg=self.bg)
        # add tk.Label to grid
        lbl.grid(row=self.row, column=self.column, columnspan=self.columnspan, sticky=self.sticky)
        # add tk.Label to dict (key: unique name, value: tk.Label)
        Widgets.dict.update({name: lbl})


# ---------------------------------------------------------------------------------------------
# tk.Button commands
# ---------------------------------------------------------------------------------------------
def roll_all():
    # calculate results
    results = calc_roll_results(int(Widgets.dict.get('lbl_dice_type')['text']),
                                int(Widgets.dict.get('lbl_roll_amount')['text']))
    total_result = calc_roll_total(results.pop())
    # display results
    results_str = ', '.join(results)
    Widgets.dict.get('lbl_results')['text'] = f'{results_str}'
    Widgets.dict.get('lbl_total')['text'] = f'{total_result}'


def reset_all():
    # set dice_list to proper order
    Dice.dice_list = deque([4, 6, 8, 10, 12, 20])
    # set all labels to defaults
    Widgets.dict.get('lbl_dice_type')['text'] = f'{Dice.dice_list[0]}'
    Widgets.dict.get('lbl_roll_amount')['text'] = f'{1}'
    Widgets.dict.get('lbl_mod1')['text'] = f'{0}'
    Widgets.dict.get('lbl_mod2')['text'] = f'{0}'
    Widgets.dict.get('lbl_proficiency')['text'] = f'{0}'
    Widgets.dict.get('lbl_results')['text'] = f'{""}'
    Widgets.dict.get('lbl_total')['text'] = f'{""}'


def roll_d20():
    results = calc_roll_results(20, 1)
    Widgets.dict.get('lbl_results')['text'] = f'{results.pop()}'
    Widgets.dict.get('lbl_total')['text'] = f'{""}'


def update_label(lbl_name, action):
    # get current value from label as int
    value = int(Widgets.dict.get(lbl_name)['text'])

    if action == '+':
        Widgets.dict.get(lbl_name)['text'] = f'{value + 1}'
    elif action == '-':
        if lbl_name == 'lbl_roll_amount' and value == 1:
            pass
        else:
            Widgets.dict.get(lbl_name)['text'] = f'{value - 1}'
    else:
        if action == '++':
            Dice.dice_list.rotate(-1)
        elif action == '--':
            Dice.dice_list.rotate(1)
        Widgets.dict.get(lbl_name)['text'] = f'{Dice.dice_list[0]}'


# ---------------------------------------------------------------------------------------------
# functions
# ---------------------------------------------------------------------------------------------
def main():
    create_tk_widgets()
    Root.window.mainloop()


def create_tk_widgets():
    Label(name='lbl_dice_prompt', text='Dice', bg='#4f5bd5', row=0, column=0)
    Button(name='btn_dec_dice', text='-', bg='#747cd6', command=partial(update_label, 'lbl_dice_type', '--'), row=0,
           column=1),
    Label(name='lbl_dice_type', text=Dice.dice_list[0], bg='#747cd6', row=0, column=2)
    Button(name='btn_inc_dice', text='+', bg='#747cd6', bd=3, command=partial(update_label, 'lbl_dice_type', '++'),
           row=0, column=3),
    Label(name='lbl_roll_amount_prompt', text='Amount', bg='#962fbf', row=1, column=0)
    Button(name='btn_dec_roll_amount', text='-', bg='#a661c2', bd=3,
           command=partial(update_label, 'lbl_roll_amount', '-'), row=1, column=1)
    Label(name='lbl_roll_amount', text=1, bg='#a661c2', row=1, column=2)
    Button(name='btn_inc_roll_amount', text='+', bg='#a661c2', bd=3,
           command=partial(update_label, 'lbl_roll_amount', '+'), row=1, column=3)
    Label(name='lbl_mod1_prompt', text='Modifier\n1', bg='#d62976', row=2, column=0)
    Button(name='btn_dec_mod1', text='-', bg='#d45d92', bd=3, command=partial(update_label, 'lbl_mod1', '-'), row=2,
           column=1),
    Label(name='lbl_mod1', text='0', bg='#d45d92', row=2, column=2)
    Button(name='btn_inc_mod1', text='+', bg='#d45d92', bd=3, command=partial(update_label, 'lbl_mod1', '+'), row=2,
           column=3),
    Label(name='lbl_mod2_prompt', text='Modifier\n2', bg='#fa7e1e', row=3, column=0)
    Button(name='btn_dec_mod2', text='-', bg='#fca662', bd=3, command=partial(update_label, 'lbl_mod2', '-'), row=3,
           column=1),
    Label(name='lbl_mod2', text='0', bg='#fca662', row=3, column=2)
    Button(name='btn_inc_mod2', text='+', bg='#fca662', bd=3, command=partial(update_label, 'lbl_mod2', '+'), row=3,
           column=3),
    Label(name='lbl_proficiency_prompt', text='Proficiency\nBonus', bg='#feda75', row=4, column=0)
    Button(name='btn_dec_proficiency', text='-', bg='#ffe8a8', bd=3,
           command=partial(update_label, 'lbl_proficiency', '-'), row=4, column=1)
    Label(name='lbl_proficiency', text='0', bg='#ffe8a8', row=4, column=2)
    Button(name='btn_inc_proficiency', text='+', bg='#ffe8a8', bd=3,
           command=partial(update_label, 'lbl_proficiency', '+'), row=4, column=3)
    Button(name='btn_reset', text='Reset\nAll', bg='#eb3b28', bd=3, command=reset_all, row=5, column=0)
    Button(name='btn_roll_d20', text='Roll\nd20', bg='#79db72', bd=3, command=roll_d20, row=5, column=1)
    Button(name='btn_roll', text='Roll\nAll', bg='#24b519', bd=3, command=roll_all, row=5, column=2, columnspan=2)
    Label(name='lbl_results_prompt', text='Roll\nResults', bg='#d6d6d6', row=6, column=0)
    Label(name='lbl_results', text='', bg='#e3e3e3', row=6, column=1, columnspan=3)
    Label(name='lbl_total_prompt', text='Total\nResult', bg='#bdbdbd', row=7, column=0)
    Label(name='lbl_total', text='', bg='#d6d6d6', row=7, column=1, columnspan=3)


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
    mod1 = int(Widgets.dict.get('lbl_mod1')['text'])
    mod2 = int(Widgets.dict.get('lbl_mod2')['text'])
    proficiency = int(Widgets.dict.get('lbl_proficiency')['text'])

    new_total = total + mod1 + mod2 + proficiency
    result_formula = f'{total} + {mod1} + {mod2} + {proficiency} = {new_total}'
    return result_formula


if __name__ == '__main__':
    main()