import keyboard
import time
import os

# grid_map is the map of the level or stage
# TO DO: Try to learn about OOP or refactor the entire program before developing next ideas
# Also need more ideas to continue this project with:
"""
Ideas:
    mapRenderer() function: this function will render 0s, 1s, 2s to unicode (maybe)
        will probably do this by creating another copy of grid_map, or just make an decision structure
        that loops through the whole grid_map to convert numericals into unicode

    Dynamic Map Shapes
        this will make each grid_map dynamic with different or combined shapes
        currently dont have any idea how can I do this, will need research

    Randomly Generated Structures/Objects
        this will generate random integers on the 0s, these integers will represent objects that the player will need
        or something
"""
grid_map = []

def createMap(row, column):
    grid_map = [[0 for _ in range(column)] for _ in range(row)]
    return grid_map

def setOuterLimit():
    for i in range(row):
        for j in range(column):
            if (i == 0 or i == row-1):
                grid_map[i][j] = 2

            if (j == 0 or j == column-1):
                grid_map[i][j] = 2
    return grid_map

def showMap():
    for row in grid_map:
        for element in row:
            print(element, end=" ")
        print("")

def setPlayerLocation():
    grid_map[row//2][column//2] = 1

    return grid_map

def getPlayerLocation(): # returns 2 values: row, column
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
showMap()

playerRow, playerColumn = getPlayerLocation()
print(f"Player is at [{playerRow}][{playerColumn}]")

newRow, newCol = getPlayerLocation()
key_states = {"w": False, "a": False, "s": False, "d": False}

while True:
    lastRow, lastCol = getPlayerLocation()

    if not isLocationValid(lastRow, lastCol):
        os.system('cls' if os.name == 'nt' else 'clear')
        grid_map[lastRow][lastCol] = 3
        showMap()
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
        showMap()
        #newRow, newCol = getPlayerLocation()

    if keyboard.is_pressed("esc"):
        break

    time.sleep(0.05)