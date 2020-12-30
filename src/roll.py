# .../dice-roller/src/roll.py
# Calculates results based on user input from GUI.py, returns results to GUI.py to be displayed

from random import randrange


def roll(dice, roll_amount):
    result_list = []
    for x in range(roll_amount):
        result_list.append(randrange(1, dice + 1))
    return result_list
