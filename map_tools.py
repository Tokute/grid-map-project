"""
map_tools.py

this module stores the functions needed for map creation, printing, and the like.
"""

import random
grid_map = []

def create_map(row, column, set_outer_limit=True):
    """
        Creates the map from two arguments(row, column)

        Args:
            row (int): num of rows
            column (int): num of columns

        Returns:
            grid_map (2d List): filled with zeros with rows and columns based on the args
    """
    grid_map = [[0 for _ in range(column)] for _ in range(row)]

    if set_outer_limit:
        set_grid_limit(grid_map)

    return grid_map

def generate_map(set_outer_limit=True):
    """
        generate_map basically generates a 2d List randomly. Args: set_outer_limit is True, Returns grid_map (2d List)
    """
    row = random.randint(5, 10)
    column = random.randint(5, 10)

    grid_map = [[0 for _ in range(column)] for _ in range(row)]

    if set_outer_limit:
        set_grid_limit(grid_map)

    grid_map[0][column//2] = 4
    grid_map[-1][column//2] = 4
    grid_map[row//2][0] = 4
    grid_map[row//2][-1] = 4

    return grid_map

def set_grid_limit(grid_map):
    """
        Sets the outer limit of the grid_map

        No args

        Returns:
            grid_map (2d List): grid_map with 2s on the edge
    """
    row = len(grid_map)
    column = len(grid_map[0])
    for i in range(row):
        for j in range(column):
            if (i == 0 or i == row-1):
                grid_map[i][j] = 2

            if (j == 0 or j == column-1):
                grid_map[i][j] = 2
    return grid_map

def show_map(grid_map, render=True):
    """
        Prints out the grid_map
        
        Args:
            render (bool): determines if the function will print pure integers or unicode

        No Returns
    """

    if not render:
        for row in grid_map:
            for element in row:
                print(element, end=" ")
            print("")
    else:
        for row in grid_map:
            for element in row:
                match (element):
                    case 0: # Free space (black square emoji)
                        print(chr(0x2B1B), end=" ")
                    case 1: # Player space (checkmark emoji)
                        print(chr(0x2705), end=" ")
                    case 2: # Outer/Killzone space (red diamond emoji)
                        print(chr(0x1F536), end=" ")
                    case 3: # Death space (SOS emoji)
                        print(chr(0x1F198), end=" ")
                    case 4: # Door emoji "NEW_ROOM"
                        print(chr(0x1F6AA), end=" ")
                    case _: # if unknown/unassigned integer, print integer itself
                        print(element, end=" ")
            print("")
