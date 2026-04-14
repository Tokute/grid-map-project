import keyboard
import time
import os
import playerMovement as move
import mapTools
import locationTools


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
while True:
    row = int(input("What will be the number of rows for this map: "))
    column = int(input("What will be the number of columns for this map: "))

    if ((row >= 2) and (column >= 2)):
        break
    elif (row < 3):
        print("Error! row must be greater than 2.")
    elif (column < 3):
        print("Error! column must be greater than 2.")

grid_map = mapTools.createMap(row, column)
grid_map = mapTools.setOuterLimit(grid_map)
grid_map = locationTools.setPlayerLocation(grid_map)
mapTools.showMap(grid_map, render=True)

playerRow, playerColumn = locationTools.getPlayerLocation(grid_map)
print(f"Player is at [{playerRow}][{playerColumn}]")

newRow, newCol = locationTools.getPlayerLocation(grid_map)
key_states = {"w": False, "a": False, "s": False, "d": False}

while True:
    lastRow, lastCol = locationTools.getPlayerLocation(grid_map)
    #print(f"Last Row: {lastRow}, Last Column: {lastCol}")

    if not locationTools.isLocationValid(grid_map, lastRow, lastCol):
        os.system('cls' if os.name == 'nt' else 'clear')
        grid_map[lastRow][lastCol] = 3
        mapTools.showMap(grid_map, render=True)
        print("Player hit the grid. Player has died")
        break

    moved = False
    for key in key_states:
        if keyboard.is_pressed(key):
            if not key_states[key]:
                match key:
                    case 'w': move.up(grid_map, lastRow, lastCol)
                    case 's': move.down(grid_map, lastRow, lastCol)
                    case 'a': move.left(grid_map, lastRow, lastCol)
                    case 'd': move.right(grid_map, lastRow, lastCol)

                moved = True
                key_states[key] = True
                break
        else:
            key_states[key] = False

    if moved:
        os.system('cls' if os.name == 'nt' else 'clear')
        mapTools.showMap(grid_map, render=True)
        #newRow, newCol = getPlayerLocation()

    if keyboard.is_pressed("esc"):
        
        break

    time.sleep(0.05)