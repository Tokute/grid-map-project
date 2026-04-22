"""main.py is the main python file"""

import time
import os
import keyboard
import map_tools
import location_tools
import player_tools
import interaction_screen
# grid_map is the map of the level or stage
# TO DO: Try to learn about OOP or refactor the entire program before developing next ideas

def clear_terminal():
    """just clears terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def determine_event(index_value):
    """
        Determines what event depending on the integer passed onto this function.
    """
    event_integers = {
        0: "FREE",
        1: "PLAYER",
        2: "DEATH",
        3: "DEATH_LOC",
        4: "NEW_ROOM",
        5: "NPC"
    }

    if index_value in event_integers:
        #print(event_integers[index_value])
        return event_integers[index_value]
    else:
        return str(f"Unregistered or invalid event: {index_value}")

def apply_event(given_event):
    """
    Applies the event, complements determine_event(). This function needs to return True if player is is_alive.
    """
    global grid_map
    if given_event == "DEATH":
        return False

    if given_event == "NEW_ROOM":
        grid_map = map_tools.generate_map()
        grid_map = location_tools.set_player_location_middle(grid_map)
        return True

    if given_event == "NPC":
        npc_int = interaction_screen.npc_dialogue()
        print("1. Talk\n2. Leave")
        while True:
            check_input = keyboard.read_event()
            if check_input.event_type == keyboard.KEY_DOWN:
                if check_input.name == "2":
                    break
                if check_input.name == "1":
                    clear_terminal()
                    interaction_screen.npc_dialogue(interacted=True, npc_interacted=npc_int)
                    print("1. Talk\n2. Leave")

    return True

#grid_map = map_tools.create_map(row, column)a
grid_map = map_tools.generate_map()
grid_map = location_tools.set_player_location_middle(grid_map)
map_tools.show_map(grid_map)

player_row, player_column = location_tools.get_index_of_integer(grid_map, 1)
print(f"Player is at [{player_row}][{player_column}]")

key_states = {"w": False, "a": False, "s": False, "d": False}
is_alive = True
event = ""

while is_alive:
    last_row, last_col = location_tools.get_index_of_integer(grid_map, 1)
    #print(f"Last Row: {last_row}, Last Column: {last_col}")

    #is_alive = apply_event(event)

    moved = False
    for key, _ in key_states.items():
        if keyboard.is_pressed(key):
            if not key_states[key]:
                try:
                    event = determine_event(player_tools.integer_of_next_index(grid_map, key))
                    match key:
                        case 'w': player_tools.up(grid_map)
                        case 's': player_tools.down(grid_map)
                        case 'a': player_tools.left(grid_map)
                        case 'd': player_tools.right(grid_map)
                except IndexError as ie:
                    print("Error index invalid.")

                moved = True
                key_states[key] = True
                is_alive = apply_event(event)
                break
        else:
            key_states[key] = False

    if moved:
        clear_terminal()
        map_tools.show_map(grid_map)
        player_row, player_column = location_tools.get_index_of_integer(grid_map, 1)
        print(f"Player is at [{player_row}][{player_column}]")
        #new_row, new_col = getPlayerLocation()

    if keyboard.is_pressed("esc"):
        clear_terminal()
        print("Menu Screen")
        break

    time.sleep(0.05)

last_row, last_col = location_tools.get_index_of_integer(grid_map, 1)
clear_terminal()
grid_map[last_row][last_col] = 3
map_tools.show_map(grid_map)
print("Player hit the grid. Player has died")
