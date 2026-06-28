"""main.py is the main python file"""

import time
import os
import keyboard
import map_tools
import location_tools
import player_tools
import interaction_screen
import entities
# grid_map is the map of the level or stage
# TO DO: Try to learn about OOP or refactor the entire program before developing next ideas

blank_space = entities.BlankSpace()
player = entities.Player()
kill_zone = entities.KillZone()

def clear_terminal():
    """just clears terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def determine_event(index_value):
    """
        Determines what event depending on the integer passed onto this function.
        OBJECT HAS TO PASS ITS ENTITY_ID
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

def apply_event(grid_map, given_event):
    """
    Applies the event, complements determine_event(). This function needs to return True if player is alive.
    """
    grid_map.get_map()
    if given_event == "DEATH":
        return False

    if given_event == "NEW_ROOM":
        grid_map.initialize_map()
        player_tools.spawn_player(grid_map, player)
        return True

    if given_event == "NPC":
        npc_int = interaction_screen.npc_dialogue()
        while True:
            check_input = keyboard.read_event()
            print("1. Talk\n2. Leave")
            if check_input.event_type == keyboard.KEY_DOWN:
                if check_input.name == "2":
                    break
                if check_input.name == "1":
                    clear_terminal()
                    interaction_screen.npc_dialogue(interacted=True, npc_interacted=npc_int)
                    continue
    return True

if __name__ == "__main__":

    player.name = input("What is your name: ")

    grid_map = map_tools.GridMap()
    #grid_map = map_tools.create_map(row, column)a
    grid_map.initialize_map()
    player_tools.spawn_player(grid_map, player)
    grid_map.print_map()

    player_row, player_column = location_tools.get_index(grid_map, player)
    print(f"Player is at [{player_row}][{player_column}]")

    key_states = {"w": False, "a": False, "s": False, "d": False}
    alive = True
    event = ""

    while alive:
        last_row, last_col = location_tools.get_index(grid_map, player)
        #print(f"Last Row: {last_row}, Last Column: {last_col}")

        moved = False
        for key, _ in key_states.items():
            if keyboard.is_pressed(key):
                if not key_states[key]:
                    try:
                        event = determine_event(player_tools.integer_of_next_index(grid_map, player, key))
                        match key:
                            case 'w': player_tools.apply_movement(grid_map, player, 'w')
                            case 's': player_tools.apply_movement(grid_map, player, 's')
                            case 'a': player_tools.apply_movement(grid_map, player, 'a')
                            case 'd': player_tools.apply_movement(grid_map, player, 'd')
                    except IndexError as ie:
                        print("Error index invalid.")

                    moved = True
                    key_states[key] = True
                    alive = apply_event(grid_map, event)
                    break
            else:
                key_states[key] = False

        if moved:
            clear_terminal()
            grid_map.print_map()
            player_row, player_column = location_tools.get_index(grid_map, player)
            print(f"Player is at [{player_row}][{player_column}]")
            #new_row, new_col = getPlayerLocation()

        if keyboard.is_pressed("esc"):
            clear_terminal()
            print("Menu Screen")
            break

        time.sleep(0.05)

    if not alive:
        last_row, last_col = location_tools.get_index(grid_map, player)
        clear_terminal()
        grid_map.modify_map(last_row, last_col, entities.PlayerDeath())
        grid_map.print_map()
        print(f"{player.name.title()} has died.")
