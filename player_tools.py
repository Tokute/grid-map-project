"""
player_tools.py

This module has player movements and check_next_index method.
"""

import location_tools

movement_logic = {
        'w': (-1, 0),
        's': (1, 0),
        'd': (0, 1),
        'a': (0, -1)
    }

def up(grid_map):
    """Move player up by one row."""
    last_row, last_col = location_tools.get_player_location(grid_map)
    grid_map[last_row][last_col] = 0
    grid_map[last_row - 1][last_col] = 1

def down(grid_map):
    """Move player down by one row."""
    last_row, last_col = location_tools.get_player_location(grid_map)
    grid_map[last_row][last_col] = 0
    grid_map[last_row + 1][last_col] = 1

def right(grid_map):
    """Move player right by one column."""
    last_row, last_col = location_tools.get_player_location(grid_map)
    grid_map[last_row][last_col] = 0
    grid_map[last_row][last_col + 1] = 1

def left(grid_map):
    """Move player left by one column."""
    last_row, last_col = location_tools.get_player_location(grid_map)
    grid_map[last_row][last_col] = 0
    grid_map[last_row][last_col - 1] = 1

def check_next_index(grid_map, key_pressed):
    """
        This function checks the next index to get what integer the player is moving to.
    """
    row = len(grid_map)
    column = len(grid_map[0])
    last_row, last_col = location_tools.get_player_location(grid_map)
    row_offset, col_offset = movement_logic[key_pressed]
    target_row = last_row + row_offset
    target_col = last_col + col_offset

    if not ((0 <= target_row <= row) and (0 <= target_col <= column)):
        raise IndexError("Error Index Out of Bounds")
        #grid_map[last_row][last_col] = 0
        #grid_map = location_tools.set_player_location(grid_map)  
    return grid_map[target_row][target_col]
