"""this module is responsible for printing out and processing menu changes."""
import os
import random

def random_number(max_num):
    """receives max_num (int) for generating random integer value."""
    return random.randint(0, max_num)

def center_print(given_str, char='='):
    """
    receives given_str (string) and char (char) variables.
    char would determine the what char to use when
    filling empty spaces
    """
    return print(given_str.center(75, char))

def npc_dialogue(interacted=False, npc_interacted=0):
    """
    arguments: interacted (bool), npc_interacted (int)
    interacted is for the dialogue loop
    npc_interacted is to replicate the npc_name if player is still interacting.
    clears the command line, puts npc dialogue in the screen. Returns npc name.

    RETURNS: last npc interacted (int)
    """
    npc_names = ["Klye", "John", "Edward", "Aileen", "Mathilda"]
    npc_index = random_number(len(npc_names) - 1)

    dialogues = [
        "What a wonderful day it is.",
        "sick seven sick seven",
        "Let's larp.",
        "Computer Science in 2026? You gotta be kidding me fam.",
        "Goodluck on your journey player!",
        "Great loot ahead.",
        "Let me solo her."
    ]
    if not interacted:
        header = f"[You are talking to {npc_names[npc_index]}]"
    else:
        header = f"[You are talking to {npc_names[npc_interacted]}]"


    # Printing below
    os.system('cls' if os.name == 'nt' else 'clear')
    center_print(header)
    center_print(dialogues[random_number(len(dialogues) - 1)], char=' ')
    center_print("")

    return npc_index