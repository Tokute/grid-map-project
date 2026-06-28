"""
location_tools.py

This module has and get_index_of_integer methods.
"""

def get_index(grid_map, given_obj):
    """This function takes in grid_map (obj) and given_obj (obj) as its parameters.
    returns row, column of where the given_obj is, returns (-1, -1) (int) if not found."""

    row = len(grid_map.get_map())
    column = len(grid_map.get_map()[0])
    found_row, found_column = -1, -1

    for i in range(row):
        for j in range(column):
            if grid_map.get_map()[i][j] == given_obj:
                found_row, found_column = i, j
    
    return found_row, found_column