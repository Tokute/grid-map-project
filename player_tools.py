"""
player_tools.py

This module has player movements and check_next_index method.
"""

from entities import BlankSpace
import location_tools

movement_logic = {
        'w': (-1, 0),
        's': (1, 0),
        'd': (0, 1),
        'a': (0, -1)
    }

def spawn_player(grid_map, player):
    """
        Sets the player location on the middle of the grid_map

        Args:
            grid_map (object): map to scan
    """
    row = len(grid_map.get_map())
    column = len(grid_map.get_map()[0])
    grid_map.modify_map(row//2, column//2, player)
    print("spawn_player function ran")

def apply_movement(grid_map, player, move):
    last_row, last_col = location_tools.get_index(grid_map, player)
    if move == "w":
        grid_map.modify_map(last_row, last_col, BlankSpace())
        grid_map.modify_map(last_row - 1, last_col, player)
    elif move == "s":
        grid_map.modify_map(last_row, last_col, BlankSpace())
        grid_map.modify_map(last_row + 1, last_col, player)
    elif move == "a":
        grid_map.modify_map(last_row, last_col, BlankSpace())
        grid_map.modify_map(last_row, last_col - 1, player)
    elif move == "d":
        grid_map.modify_map(last_row, last_col,BlankSpace())
        grid_map.modify_map(last_row, last_col + 1, player)

def integer_of_next_index(grid_map, player, key_pressed):
    """
        This function checks the next index to get what integer the player is moving to.
    """
    row = len(grid_map.get_map())
    column = len(grid_map.get_map()[0])

    last_row, last_col = location_tools.get_index(grid_map, player)
    row_offset, col_offset = movement_logic[key_pressed]

    target_row = last_row + row_offset
    target_col = last_col + col_offset

    if not ((0 <= target_row <= row) and (0 <= target_col <= column)):
        raise IndexError("Error Index Out of Bounds")
        #grid_map[last_row][last_col] = 0
        #grid_map = location_tools.set_player_location(grid_map)  
    return grid_map.get_map()[target_row][target_col].entity_id
