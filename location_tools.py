"""
location_tools.py

This module has setplayerlocation and getplayerlocation methods.
"""

def set_player_location(grid_map):
    """
        Sets the player location on the middle of the grid_map

        Args:
            grid_map (2d List): map to scan

        Returns:
        grid_map (2d List): grid_map with a number 1 on the middle
    """
    row = len(grid_map)
    column = len (grid_map[0])
    grid_map[row//2][column//2] = 1

    return grid_map

def get_player_location(grid_map): # returns 2 values: row, column
    """
        Loops through grid_map to find where the player (1) is located

        Args:
            grid_map (2d List): grid_map it will scan

        Returns:
            found_row (int): row index of player location
            found_column (int): row column of player location
    """
    row = len(grid_map)
    column = len (grid_map[0])
    found_row, found_column = -1, -1

    for i in range(row):
        for j in range(column):
            if grid_map[i][j] == 1:
                found_row, found_column = i, j
    
    return found_row, found_column