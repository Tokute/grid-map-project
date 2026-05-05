"""
map_tools.py

this file stores the functions needed for map creation, printing, and the like.
"""

import random
grid_map = []

class GridMap:
    def __init__(self):
        self.grid_map = []

    def initialize_map(self, outer_limit=True):
        row = random.randint(5, 10)
        column = random.randint(5, 10)
        self.grid_map = [[0 for _ in range(column)] for _ in range(row)]

    def print_map(self, render=False):
        if not render:
            for row in self.grid_map:
                for element in row:
                    print(element, end=" ")
                print()

    def create_map(self, row, column):
        self.grid_map = [[0 for _ in range(column)] for _ in range(row)]



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
                    case 5: # NPC emoji "NPC"
                        print(chr(0x1F64B), end=" ")
                    case _: # if unknown/unassigned integer, print integer itself
                        print(element, end=" ")
            print("")