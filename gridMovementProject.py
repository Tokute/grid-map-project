import keyboard
import time
import os

# grid_map is the map of the level or stage
# 0 = empty space, 1 = player, 2 = outer limit/kill zone, 3 = player meets outer limit
# TO DO: Try to learn about OOP or refactor the entire program before developing next ideas
# Also need more ideas to continue this project with:
"""
Ideas:
    Dynamic Map Shapes
        this will make each grid_map dynamic with different or combined shapes
        currently dont have any idea how can I do this, will need research

    Randomly Generated Structures/Objects
        this will generate random integers on the 0s, these integers will represent objects that the player will need
        or something

    Goal/Enter Room Condition
        Maybe set a random location or somewhere in the outer limits to maybe number 4. 4 basically means if the player
        manages to reach this index, they will advance to another room.
        (This project is gonna need more handling on more grid_maps)
"""
grid_map = []

def createMap(row, column):
    """
        Creates the map from two arguments(row, column)

        Args:
            row (int): num of rows
            column (int): num of columns

        Returns:
            grid_map (2d List): filled with zeros with rows and columns based on the args
    """
    grid_map = [[0 for _ in range(column)] for _ in range(row)]
    return grid_map

def setOuterLimit():
    """
        Sets the outer limit of the grid_map

        No args

        Returns:
            grid_map (2d List): grid_map with 2s on the edge
    """
    for i in range(row):
        for j in range(column):
            if (i == 0 or i == row-1):
                grid_map[i][j] = 2

            if (j == 0 or j == column-1):
                grid_map[i][j] = 2
    return grid_map

def showMap(render=False):
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
                    case 0:
                        print(chr(0x2B1B), end=" ")
                    case 1:
                        print(chr(0x2705), end=" ")
                    case 2:
                        print(chr(0x1F536), end=" ")
                    case 3:
                        print(chr(0x1F198), end=" ")
                    case _:
                        print(element, end=" ")
            print("")

def setPlayerLocation():
    """
        Sets the player location on the middle of the grid_map

        No Args

        Returns:
        grid_map (2d List): grid_map with a number 1 on the middle
    """
    grid_map[row//2][column//2] = 1

    return grid_map

def getPlayerLocation(): # returns 2 values: row, column
    """
        Loops through grid_map to find where the player (1) is located

        No Args

        Returns:
            foundRow (int): row index of player location
            foundColumn (int): row column of player location
    """
    playerFound = False
    for i in range(row):
        for j in range(column):
            if grid_map[i][j] == 1:
                playerFound = True
                foundRow, foundColumn = i, j
    
    if (playerFound):
        return foundRow, foundColumn
    else:
        return -1, -1
            
def isLocationValid(playerRow, playerCol):
    """
        Checks if the location of the player is not within the outer limits

        Args:
            playerRow (int)
            playerCol (int)

        Returns:
            True or False
    """
    if (((playerRow == 0) or (playerRow == row-1)) or ((playerCol == 0) or (playerCol == column-1))):
        return False
    else:
        return True

def moveUp(lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow-1][lastCol] = 1

def moveDown(lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow+1][lastCol] = 1

def moveRight(lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow][lastCol+1] = 1

def moveLeft(lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow][lastCol-1] = 1

# main program below

while True:
    row = int(input("What will be the number of rows for this map: "))
    column = int(input("What will be the number of columns for this map: "))

    if ((row >= 2) and (column >= 2)):
        break
    elif (row < 3):
        print("Error! row must be greater than 2.")
    elif (column < 3):
        print("Error! column must be greater than 2.")

grid_map = createMap(row, column)
grid_map = setOuterLimit()
grid_map = setPlayerLocation()
showMap(render=True)

playerRow, playerColumn = getPlayerLocation()
print(f"Player is at [{playerRow}][{playerColumn}]")

newRow, newCol = getPlayerLocation()
key_states = {"w": False, "a": False, "s": False, "d": False}

while True:
    lastRow, lastCol = getPlayerLocation()

    if not isLocationValid(lastRow, lastCol):
        os.system('cls' if os.name == 'nt' else 'clear')
        grid_map[lastRow][lastCol] = 3
        showMap(render=True)
        print("Player hit the grid. Player has died")
        break

    moved = False
    for key in key_states:
        if keyboard.is_pressed(key):
            if not key_states[key]:
                match key:
                    case 'w': moveUp(lastRow, lastCol)
                    case 's': moveDown(lastRow, lastCol)
                    case 'a': moveLeft(lastRow, lastCol)
                    case 'd': moveRight(lastRow, lastCol)

                moved = True
                key_states[key] = True
                break
        else:
            key_states[key] = False

    if moved:
        os.system('cls' if os.name == 'nt' else 'clear')
        showMap(render=True)
        #newRow, newCol = getPlayerLocation()

    if keyboard.is_pressed("esc"):
        break

    time.sleep(0.05)