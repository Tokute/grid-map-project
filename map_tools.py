"""
map_tools.py

this file stores the functions needed for map creation, printing, and the like.
"""


import random
import entities

grid_map = []

class GridMap:
    def __init__(self):
        self.grid_map = []

    def initialize_map(self, outer_limit=True):
        row = random.randint(5, 10)
        column = random.randint(5, 10)
        self.grid_map = [[entities.BlankSpace() for _ in range(column)] for _ in range(row)]

        if outer_limit:
            row = len(self.grid_map)
            column = len(self.grid_map[0])
            for i in range(row):
                for j in range(column):
                    if ((i == 0 or i == row-1) or (j == 0 or j == column-1)):
                        self.grid_map[i][j] = entities.KillZone()

        self.grid_map[0][column//2] = entities.Door()
        self.grid_map[-1][column//2] = entities.Door()
        self.grid_map[row//2][0] = entities.Door()
        self.grid_map[row//2][-1] = entities.Door()

        # For random npcs:
        random_row = random.randint(1, row-2)
        random_col = random.randint(1, column-2)

        self.grid_map[random_row][random_col] = entities.NPC()

    def print_map(self, render=True):
        if not render:
            for row in self.grid_map:
                for element in row:
                    print(element, end=" ")
                print()
        else:
            for row in self.grid_map:
                for element in row:
                    try:
                        print(element.unicode, end=" ")
                    except AttributeError as ae:
                        print(element)
                        print(ae)
                print("")
    
    def get_map(self):
        return self.grid_map

    def create_map(self, row, column):
        self.grid_map = [[0 for _ in range(column)] for _ in range(row)]

    def modify_map(self, row, column, new_val):
        self.grid_map[row][column] = new_val

